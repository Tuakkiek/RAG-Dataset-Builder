import json
import sys
from pathlib import Path

import tiktoken


BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_PATH = BASE_DIR / "data" / "processed" / "day13.json"
OUTPUT_PATH = BASE_DIR / "data" / "processed" / "day15.json"

MAX_TOKENS = 500
ENCODING = tiktoken.get_encoding("cl100k_base")

IGNORE_TYPES = {
    "header",
    "footer",
    "page_number",
}

EQUATION_TYPE = "equation"
EXPLANATION_TYPES = {"text"}


def count_tokens(text):
    return len(ENCODING.encode(text))


def load_json(input_path):
    with input_path.open("r", encoding="utf-8") as file:
        return json.load(file)


def should_keep_record(record):
    if not isinstance(record, dict):
        return False

    block_type = record.get("type", "")
    content = record.get("content", "")

    if block_type in IGNORE_TYPES:
        return False

    return isinstance(content, str) and bool(content.strip())


# Keep the old misspelled name as a compatibility alias.
shoud_keep_record = should_keep_record


def get_section_path(record):
    if not isinstance(record, dict):
        return []

    path = record.get("section_path", [])
    if not isinstance(path, list):
        return []

    return [
        str(title).strip()
        for title in path
        if str(title).strip()
    ]


def get_content(record):
    if not isinstance(record, dict):
        return ""

    content = record.get("content", "")
    return content.strip() if isinstance(content, str) else ""


def is_explanation_record(record):
    return (
        isinstance(record, dict)
        and record.get("type", "") in EXPLANATION_TYPES
        and bool(get_content(record))
    )


def build_equation_units(records):
    """Group equations with immediately adjacent explanation text."""
    units = []
    index = 0

    while index < len(records):
        record = records[index]

        if not isinstance(record, dict):
            index += 1
            continue

        block_type = record.get("type", "")

        if block_type == EQUATION_TYPE:
            unit = [record]
            index += 1

            if (
                index < len(records)
                and is_explanation_record(records[index])
            ):
                unit.append(records[index])
                index += 1

            units.append(unit)
            continue

        if (
            block_type in EXPLANATION_TYPES
            and index + 1 < len(records)
            and isinstance(records[index + 1], dict)
            and records[index + 1].get("type") == EQUATION_TYPE
        ):
            unit = [record, records[index + 1]]
            index += 2

            if (
                index < len(records)
                and is_explanation_record(records[index])
            ):
                unit.append(records[index])
                index += 1

            units.append(unit)
            continue

        units.append([record])
        index += 1

    return units


def create_empty_chunk(section_path):
    return {
        "section_path": list(section_path or []),
        "texts": [],
        "pages": [],
        "block_types": [],
        "source_blocks": [],
        "records": [],
    }


def get_unit_text(unit):
    return "\n\n".join(
        content
        for content in (get_content(record) for record in unit)
        if content
    )


def split_text_to_fit(text, max_tokens):
    """Split text into pieces that each fit the token limit."""
    text = text.strip()
    if not text:
        return []

    if count_tokens(text) <= max_tokens:
        return [text]

    pieces = []
    current_words = []

    for word in text.split():
        if count_tokens(word) > max_tokens:
            if current_words:
                pieces.append(" ".join(current_words))
                current_words = []

            token_ids = ENCODING.encode(word)
            pieces.extend(
                ENCODING.decode(token_ids[start:start + max_tokens])
                for start in range(0, len(token_ids), max_tokens)
            )
            continue

        candidate_words = current_words + [word]
        candidate = " ".join(candidate_words)

        if current_words and count_tokens(candidate) > max_tokens:
            pieces.append(" ".join(current_words))
            current_words = [word]
        else:
            current_words = candidate_words

    if current_words:
        pieces.append(" ".join(current_words))

    return pieces


def _split_record(record, max_tokens):
    pieces = split_text_to_fit(get_content(record), max_tokens)
    return [{**record, "content": piece} for piece in pieces]


def expand_oversized_unit(unit, max_tokens):
    """Split an oversized equation unit into individually safe units."""
    if max_tokens <= 0:
        raise ValueError("max_tokens must be greater than zero")

    if count_tokens(get_unit_text(unit)) <= max_tokens:
        return [unit]

    expanded = []
    for record in unit:
        expanded.extend(
            [[piece] for piece in _split_record(record, max_tokens)]
        )
    return expanded


def finalize_chunk(current, chunks):
    if current is None or not current["texts"]:
        return

    text = "\n\n".join(current["texts"]).strip()
    if not text:
        return

    pages = [
        page
        for page in current["pages"]
        if isinstance(page, int) and not isinstance(page, bool)
    ]

    unique_sources = []
    seen_sources = set()
    for source in current["source_blocks"]:
        key = (source.get("page_idx"), source.get("source_index"))
        if key not in seen_sources:
            seen_sources.add(key)
            unique_sources.append(source)

    equation_sources = {
        (record.get("page_idx"), record.get("source_index"))
        for record in current["records"]
        if record.get("type") == EQUATION_TYPE
    }

    chunks.append({
        "chunk_id": f"day15_chunk_{len(chunks) + 1:06d}",
        "section_path": list(current["section_path"]),
        "page_start": min(pages) if pages else None,
        "page_end": max(pages) if pages else None,
        "text": text,
        "token_count": count_tokens(text),
        "block_types": list(dict.fromkeys(current["block_types"])),
        "has_equation": bool(equation_sources),
        "equation_count": len(equation_sources),
        "source_blocks": unique_sources,
    })


def pack_section(records, section_path, chunks, max_tokens):
    units = build_equation_units(records)
    current = create_empty_chunk(section_path)

    for unit in units:
        safe_units = expand_oversized_unit(unit, max_tokens)

        for safe_unit in safe_units:
            unit_text = get_unit_text(safe_unit)
            if not unit_text:
                continue

            candidate = "\n\n".join(
                current["texts"] + [unit_text]
            )

            if (
                current["texts"]
                and count_tokens(candidate) > max_tokens
            ):
                finalize_chunk(current, chunks)
                current = create_empty_chunk(section_path)

            if count_tokens(unit_text) > max_tokens:
                raise ValueError(
                    "An expanded unit still exceeds max_tokens"
                )

            current["texts"].append(unit_text)
            for record in safe_unit:
                current["records"].append(record)
                current["pages"].append(record.get("page_idx"))
                current["block_types"].append(
                    record.get("type", "unknown")
                )
                current["source_blocks"].append({
                    "page_idx": record.get("page_idx"),
                    "source_index": record.get("source_index"),
                })

    finalize_chunk(current, chunks)


def build_equation_aware_chunks(records, max_tokens):
    if max_tokens <= 0:
        raise ValueError("max_tokens must be greater than zero")

    chunks = []
    section_records = []
    current_section_path = None

    for record in records:
        if not should_keep_record(record):
            continue

        section_path = get_section_path(record)

        if (
            section_records
            and section_path != current_section_path
        ):
            pack_section(
                section_records,
                current_section_path,
                chunks,
                max_tokens,
            )
            section_records = []

        if not section_records:
            current_section_path = section_path

        section_records.append(record)

    if section_records:
        pack_section(
            section_records,
            current_section_path,
            chunks,
            max_tokens,
        )

    return chunks


def validate_chunks(chunks, max_tokens):
    seen_ids = set()

    for chunk in chunks:
        chunk_id = chunk["chunk_id"]

        if chunk_id in seen_ids:
            raise ValueError(f"Duplicate chunk ID: {chunk_id}")
        seen_ids.add(chunk_id)

        if not chunk["text"].strip():
            raise ValueError(f"Empty chunk: {chunk_id}")

        actual_tokens = count_tokens(chunk["text"])
        if actual_tokens > max_tokens:
            raise ValueError(
                f"{chunk_id} Exceed the limit token: "
                f"{actual_tokens} > {max_tokens}"
            )

        if actual_tokens != chunk["token_count"]:
            raise ValueError("token_count does not match")

        if chunk["has_equation"] != (chunk["equation_count"] > 0):
            raise ValueError(
                f"Metadata equation inconsistent: {chunk_id}"
            )

        if chunk["has_equation"] != (
            EQUATION_TYPE in chunk["block_types"]
        ):
            raise ValueError(
                f"block_types does not match equation: {chunk_id}"
            )

        start = chunk["page_start"]
        end = chunk["page_end"]
        if (
            start is not None
            and end is not None
            and start > end
        ):
            raise ValueError(f"Invalid page range: {chunk_id}")


def save_data(data, output_path):
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    if not INPUT_PATH.exists():
        print("File not found")
        print(INPUT_PATH)
        return

    records = load_json(INPUT_PATH)
    print(f"Total number of records: {len(records)}")

    chunks = build_equation_aware_chunks(
        records,
        max_tokens=MAX_TOKENS,
    )
    validate_chunks(chunks, max_tokens=MAX_TOKENS)
    save_data(chunks, OUTPUT_PATH)

    equation_chunks = [chunk for chunk in chunks if chunk["has_equation"]]
    print(f"Total chunks: {len(chunks)}")
    print(f"Chunks containing equations: {len(equation_chunks)}")
    print(f"Max tokens: {MAX_TOKENS}")
    print(f"Output: {OUTPUT_PATH}")

    if chunks:
        token_counts = [chunk["token_count"] for chunk in chunks]
        print(f"Min tokens: {min(token_counts)}")
        print(f"Max actual tokens: {max(token_counts)}")
        print(
            "Average tokens: "
            f"{sum(token_counts) / len(token_counts):.2f}"
        )
        print("\nFirst 3 chunks:")
        for chunk in chunks[:3]:
            print({
                "chunk_id": chunk["chunk_id"],
                "section_path": chunk["section_path"],
                "page_start": chunk["page_start"],
                "page_end": chunk["page_end"],
                "token_count": chunk["token_count"],
                "has_equation": chunk["has_equation"],
                "equation_count": chunk["equation_count"],
            })

    print("\nValidation passed.")
    print(f"Result saved at: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
