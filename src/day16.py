import json
import re
from pathlib import Path

import tiktoken

BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_PATH = BASE_DIR / "data" / "processed" / "day13.json"
OUTPUT_PATH = BASE_DIR / "data" / "processed" / "day16.json"

MAX_TOKENS = 500

ENCODING = tiktoken.get_encoding("cl100k_base")

IGNORE_TYPES = {
    "header",
    "footer",
    "page_number",
}

TABLE_TYPE = "table"

EQUATION_TYPE = "equation"

EXPLANATION_TYPES = {"text"}

TABLE_CAPTION_RE = re.compile(
    r"^\s*(?:bảng|table)\s+\d+(?:[.-]\d+)*(?:\s|[.:])",
    re.IGNORECASE,
)

def count_tokens(text):
    return len(ENCODING.encode(text))

def load_json(input_path):

    with input_path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, list):
        raise ValueError(
            "day13.json phải chứa một danh sách record."
        )

    return data


def get_content(record):
    content = record.get("content", "")

    if not isinstance(content, str):
        return ""

    return content.strip()


def should_keep_record(record):

    if record.get("type", "") in IGNORE_TYPES:
        return False

    content = get_content(record)

    if record.get("type") == TABLE_TYPE:
        return True

    return bool(content)


def unique_records(records):
    result = []
    seen = set()

    for record in records:
        key = (
            record.get("page_idx"),
            record.get("source_index"),
            record.get("type"),
        )

        if key not in seen:
            seen.add(key)
            result.append(record)

    return result

def get_source_info(record):

    return {
        "page_idx": record.get("page_idx"),
        "source_index": record.get("source_index"),
        "type": record.get("type", "unknown"),
    }

def make_item(
    text,
    records,
    section_path,
    *,
    table_sources: list | None = None,
):
    source_records = unique_records(records)

    return {
        "text": text.strip(),
        "section_path": list(section_path),
        "pages": [
            record.get("page_idx")
            for record in source_records
        ],
        "block_types": [
            record.get("type", "unknown")
            for record in source_records
        ],
        "source_blocks": [
            get_source_info(record)
            for record in source_records
        ],
        "table_sources": list(table_sources or []),
    }


def split_markdown_cells(line):

    line = line.strip()

    if line.startswith("|"):
        line = line[1:]

    if line.endswith("|"):
        line = line[:-1]

    return [cell.strip() for cell in line.split("|")]

def is_separator_row(line):

    cells = split_markdown_cells(line)

    if not cells:
        return False

    return all(
        re.fullmatch(r":?-{3,}:?", cell.replace(" ", ""))
        for cell in cells
    )

def parse_markdown_table(content):

    lines = [
        line.rstrip()
        for line in content.splitlines()
        if line.strip()
    ]

    pipe_indices = [
        i for i, line in enumerate(lines)
        if "|" in line
    ]

    if len(pipe_indices) < 2:
        return None

    first = pipe_indices[0]
    last = pipe_indices[-1]

    table_lines = lines[first:last + 1]

    if not all("|" in line for line in table_lines):
        return None

    if (
        len(table_lines) < 2
        or not is_separator_row(table_lines[1])
    ):
        return None

    header_line = table_lines[0]
    separator_line = table_lines[1]

    data_lines = [
        line
        for line in table_lines[2:]
        if not is_separator_row(line)
    ]

    return {
        "prefix": lines[:first],
        "header": header_line,
        "separator": separator_line,
        "rows": data_lines,
        "suffix": lines[last + 1:],
    }


def render_table_part(
    caption_lines,
    prefix_lines,
    header_line,
    separator_line,
    rows,
    suffix_lines: list | None = None,
):

    lines = []

    for line in caption_lines + prefix_lines:
        if line and line not in lines:
            lines.append(line)

    lines.extend([header_line, separator_line])
    lines.extend(rows)
    lines.extend(suffix_lines or [])

    return "\n".join(lines).strip()

def split_large_markdown_table(
    record,
    caption_lines,
    caption_records,
    parsed,
    max_tokens,
):

    rows = parsed["rows"]
    prefix_lines = parsed["prefix"]
    suffix_lines = parsed["suffix"]

    header = parsed["header"]
    separator = parsed["separator"]

    context = caption_lines + prefix_lines

    if not rows:
        text = render_table_part(
            context,
            [],
            header,
            separator,
            [],
            suffix_lines,
        )

        if count_tokens(text) > max_tokens:
            raise ValueError(
                "Caption/header của bảng vượt MAX_TOKENS. "
                f"page_idx={record.get('page_idx')}"
            )

        groups = [[]]

    else:
        groups = []
        current_rows = []

        for row in rows:
            candidate_rows = current_rows + [row]

            candidate_text = render_table_part(
                context,
                [],
                header,
                separator,
                candidate_rows,
                suffix_lines,
            )

            if count_tokens(candidate_text) <= max_tokens:
                current_rows.append(row)
                continue

            if not current_rows:
                raise ValueError(
                    f"page_idx={record.get('page_idx')}, "
                    f"source_index={record.get('source_index')}. "
                )

            groups.append(current_rows)
            current_rows = [row]

            single_row_text = render_table_part(
                context,
                [],
                header,
                separator,
                current_rows,
                suffix_lines,
            )

            if count_tokens(single_row_text) > max_tokens:
                raise ValueError(
                    f"page_idx={record.get('page_idx')}"
                )

        if current_rows:
            groups.append(current_rows)

    table_source = get_source_info(record)
    items = []
    total_parts = len(groups)

    for part_index, group_rows in enumerate(groups, start=1):
        part_suffix = (
            suffix_lines
            if part_index == total_parts
            else []
        )

        text = render_table_part(
            context,
            [],
            header,
            separator,
            group_rows,
            part_suffix,
        )

        if count_tokens(text) > max_tokens:
            raise ValueError(
                "Một phần bảng vẫn vượt MAX_TOKENS sau khi chia. "
                f"page_idx={record.get('page_idx')}"
            )

        items.append(
            make_item(
                text,
                caption_records + [record],
                get_section_path(record),
                table_sources=[{
                    **table_source,
                    "part_index": part_index,
                    "part_count": total_parts,
                }],
            )
        )

    return items


def extract_embedded_captions(record):

    captions = record.get("captions", [])

    if isinstance(captions, str):
        captions = [captions]

    if not isinstance(captions, list):
        return []

    result = []

    for caption in captions:
        if isinstance(caption, str):
            content = caption.strip()

        elif isinstance(caption, dict):
            content = str(
                caption.get("content", "")
            ).strip()

        else:
            continue

        if content and content not in result:
            result.append(content)

    return result

def build_table_items(
    record,
    max_tokens,
    caption_record: dict | None = None,
):

    table_content = get_content(record)

    caption_records = []
    caption_lines = []

    if caption_record is not None:
        caption = get_content(caption_record)

        if caption:
            caption_lines.append(caption)

        caption_records.append(caption_record)

    for caption in extract_embedded_captions(record):
        if caption not in caption_lines:
            caption_lines.append(caption)

    if not table_content:
        if not caption_lines:
            return []

        text = "\n".join(caption_lines)

        return [
            make_item(
                text,
                caption_records + [record],
                get_section_path(record),
            )
        ]

    caption_text = "\n".join(caption_lines)

    full_text_parts = []

    if caption_text:
        full_text_parts.append(caption_text)

    full_text_parts.append(table_content)

    full_text = "\n\n".join(full_text_parts)

    table_source = get_source_info(record)

    if count_tokens(full_text) <= max_tokens:
        return [
            make_item(
                full_text,
                caption_records + [record],
                get_section_path(record),
                table_sources=[{
                    **table_source, # Dictionary Unpacking (**)
                    "part_index": 1,
                    "part_count": 1,
                }],
            )
        ]

    parsed = parse_markdown_table(table_content)

    if parsed is None:
        raise ValueError(
            f"page_idx={record.get('page_idx')}, "
            f"source_index={record.get('source_index')}. "
        )

    return split_large_markdown_table(
        record,
        caption_lines,
        caption_records,
        parsed,
        max_tokens,
    )

def get_section_path(record):
    
    path = record.get("section_path", [])

    if not isinstance(path, list):
        return []

    return [
        str(title).strip()
        for title in path
        if str(title).strip()
    ]


def split_by_words(
    text, 
    max_tokens
):
    chunks = []
    current_words = []

    for word in text.split():
        if count_tokens(word) > max_tokens:
            if current_words:
                chunks.append(" ".join(current_words))
                current_words = []

            chunks.extend(split_long_word(word, max_tokens))
            continue

        candidate = " ".join(current_words + [word])

        if (
            current_words
            and count_tokens(candidate) > max_tokens
        ):
            chunks.append(" ".join(current_words))
            current_words = [word]
        else:
            current_words.append(word)

    if current_words:
        chunks.append(" ".join(current_words))

    return chunks

def split_text_to_fit(text, max_tokens):

    text = text.strip()

    if not text:
        return []

    if count_tokens(text) <= max_tokens:
        return [text]

    sentences = re.split(
        r"(?<=[.!?。！？])\s+|\n+",
        text,
    )

    chunks = []
    current = ""

    for sentence in sentences:
        sentence = sentence.strip()

        if not sentence:
            continue

        if count_tokens(sentence) > max_tokens:
            if current:
                chunks.append(current)
                current = ""

            chunks.extend(
                split_by_words(sentence, max_tokens)
            )
            continue

        candidate = (
            f"{current}\n{sentence}"
            if current
            else sentence
        )

        if (
            current
            and count_tokens(candidate) > max_tokens
        ):
            chunks.append(current)
            current = sentence
        else:
            current = candidate

    if current:
        chunks.append(current)

    return chunks

def build_regular_items(
    records,
    max_tokens,
):

    items = []
    i = 0

    while i < len(records):
        record = records[i]
        block_type = record.get("type", "")
        section_path = get_section_path(record)

        unit = [record]
        i += 1

        if (
            block_type == EQUATION_TYPE
            and i < len(records)
            and records[i].get("type") in EXPLANATION_TYPES
            and get_section_path(records[i]) == section_path
        ):
            unit.append(records[i])
            i += 1

        elif (
            block_type in EXPLANATION_TYPES
            and i < len(records)
            and records[i].get("type") == EQUATION_TYPE
            and get_section_path(records[i]) == section_path
        ):
            unit.append(records[i])
            i += 1

            if (
                i < len(records)
                and records[i].get("type") in EXPLANATION_TYPES
                and get_section_path(records[i]) == section_path
            ):
                unit.append(records[i])
                i += 1

        unit_text = "\n\n".join(
            get_content(item)
            for item in unit
            if get_content(item)
        ).strip()

        if not unit_text:
            continue

        if count_tokens(unit_text) <= max_tokens:
            items.append(
                make_item(
                    unit_text,
                    unit,
                    section_path,
                )
            )
            continue

        for item_record in unit:
            content = get_content(item_record)

            for piece in split_text_to_fit(content, max_tokens):
                items.append(
                    make_item(
                        piece,
                        [item_record],
                        get_section_path(item_record),
                    )
                )

    return items


def is_table_caption(record):
    content = get_content(record)

    return bool(
        TABLE_CAPTION_RE.match(content)
    )

def build_items(
    records, 
    max_tokens
):

    valid_records = [
        record
        for record in records
        if isinstance(record, dict)
        and should_keep_record(record)
    ]

    items = []
    i = 0

    while i < len(valid_records):
        record = valid_records[i]
        block_type = record.get("type", "")

        if (
            is_table_caption(record)
            and i + 1 < len(valid_records)
            and valid_records[i + 1].get("type") == TABLE_TYPE
        ):
            table_record = valid_records[i + 1]

            items.extend(
                build_table_items(
                    table_record,
                    max_tokens,
                    caption_record=record,
                )
            )

            i += 2
            continue

        if block_type == TABLE_TYPE:
            items.extend(
                build_table_items(
                    record,
                    max_tokens,
                )
            )

            i += 1
            continue

        regular_records = []
        start_path = get_section_path(record)

        while i < len(valid_records):
            candidate = valid_records[i]

            if candidate.get("type") == TABLE_TYPE:
                break

            if (
                is_table_caption(candidate)
                and i + 1 < len(valid_records)
                and valid_records[i + 1].get("type") == TABLE_TYPE
            ):
                break

            if (
                regular_records
                and get_section_path(candidate) != start_path
            ):
                break

            regular_records.append(candidate)
            i += 1

        items.extend(
            build_regular_items(
                regular_records,
                max_tokens,
            )
        )

    return items


def finalize_chunk(
    current, 
    chunks
):

    if current is None or not current["texts"]:
        return

    text = "\n\n".join(current["texts"]).strip()

    if not text:
        return

    pages = [
        page
        for page in current["pages"]
        if isinstance(page, int)
        and not isinstance(page, bool)
    ]

    source_blocks = []
    seen_sources = set()

    for source in current["source_blocks"]:
        key = (
            source["page_idx"],
            source["source_index"],
            source["type"],
        )

        if key not in seen_sources:
            seen_sources.add(key)
            source_blocks.append(source)

    table_sources = []
    seen_table_parts = set()

    for source in current["table_sources"]:
        key = (
            source["page_idx"],
            source["source_index"],
            source["part_index"],
        )

        if key not in seen_table_parts:
            seen_table_parts.add(key)
            table_sources.append(source)

    unique_tables = {
        (source["page_idx"], source["source_index"])
        for source in table_sources
    }

    block_types = list(dict.fromkeys(current["block_types"]))

    chunks.append({
        "chunk_id": f"day16_chunk_{len(chunks) + 1:06d}",
        "section_path": list(current["section_path"]),
        "page_start": min(pages) if pages else None,
        "page_end": max(pages) if pages else None,
        "text": text,
        "token_count": count_tokens(text),
        "block_types": block_types,
        "has_table": bool(unique_tables),
        "table_count": len(unique_tables),
        "table_sources": table_sources,
        "has_equation": EQUATION_TYPE in block_types,
        "source_blocks": source_blocks,
    })


def create_empty_chunk(section_path):

    return {
        "section_path": list(section_path),
        "texts": [],
        "pages": [],
        "block_types": [],
        "source_blocks": [],
        "table_sources": [],
    }

def build_table_aware_chunks(
    records,
    max_tokens
):
    if max_tokens <= 0:
        raise ValueError("max_tokens must be greater than 0.")

    items = build_items(records, max_tokens)

    chunks = []
    current = None

    for item in items:
        text = item["text"]
        section_path = item["section_path"]

        if not text:
            continue

        item_tokens = count_tokens(text)

        if item_tokens > max_tokens:
            raise ValueError(
                f"{item_tokens} > {max_tokens}"
            )

        if (
            current is not None
            and current["section_path"] != section_path
        ):
            finalize_chunk(current, chunks)
            current = None

        if current is None:
            current = create_empty_chunk(section_path)

        candidate = "\n\n".join(
            current["texts"] + [text]
        )

        if (
            current["texts"]
            and count_tokens(candidate) > max_tokens
        ):
            finalize_chunk(current, chunks)
            current = create_empty_chunk(section_path)

        current["texts"].append(text)
        current["pages"].extend(item["pages"])
        current["block_types"].extend(item["block_types"])
        current["source_blocks"].extend(item["source_blocks"])
        current["table_sources"].extend(item["table_sources"])

    if current is not None:
        finalize_chunk(current, chunks)

    return chunks


def validate_chunks(
    chunks,
    max_tokens,
):

    seen_ids = set()

    for chunk in chunks:
        chunk_id = chunk["chunk_id"]

        if chunk_id in seen_ids:
            raise ValueError(
                f"Duplicate chunk ID: {chunk_id}"
            )

        seen_ids.add(chunk_id)

        if not chunk["text"].strip():
            raise ValueError(
                f"Empty chunk: {chunk_id}"
            )

        actual_tokens = count_tokens(chunk["text"])

        if actual_tokens > max_tokens:
            raise ValueError(
                f"{chunk_id} exceeds MAX_TOKENS: "
                f"{actual_tokens} > {max_tokens}"
            )

        if actual_tokens != chunk["token_count"]:
            raise ValueError(
                f"token_count dose not match: {chunk_id}"
            )

        if chunk["has_table"] != (chunk["table_count"] > 0):
            raise ValueError(
                f"Table metadata inconsistent: {chunk_id}"
            )

        start = chunk["page_start"]
        end = chunk["page_end"]

        if (
            start is not None
            and end is not None
            and start > end
        ):
            raise ValueError(
                f"Invalid page range: {chunk_id}"
            )


def save_data(
    data, 
    output_path
):
    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with output_path.open("w", encoding="utf-8") as file:
        json.dump(
            data,
            file,
            ensure_ascii=False,
            indent=2,
        )

def main(): 
    if not INPUT_PATH.exists():
        print(f"File not found: {INPUT_PATH}")
        return

    records = load_json(INPUT_PATH)

    print(f"Input: {INPUT_PATH}")
    print(f"Total input records: {len(records)}")

    chunks = build_table_aware_chunks(
        records,
        max_tokens=MAX_TOKENS,
    )

    validate_chunks(
        chunks,
        max_tokens=MAX_TOKENS,
    )
    save_data(chunks, OUTPUT_PATH)
    chunks_with_tables = [
        chunk for chunk in chunks
        if chunk["has_table"]
    ]
    chunks_with_equations = [
        chunk for chunk in chunks
        if chunk["has_equation"]
    ]
    print(f"Total chunks: {len(chunks)}")
    print(f"Chunks with tables: {len(chunks_with_tables)}")
    print(f"Chunks with equations: {len(chunks_with_equations)}")
    print(f"MAX_TOKENS: {MAX_TOKENS}")
    print(f"Output: {OUTPUT_PATH}")
    if chunks:
        token_counts = [
            chunk["token_count"]
            for chunk in chunks
        ]
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
                "has_table": chunk["has_table"],
                "table_count": chunk["table_count"],
            })
    print("\nValidation passed.")
    print(f"Result saved at: {OUTPUT_PATH}")


if __name__ == "__main__":
    main() 
