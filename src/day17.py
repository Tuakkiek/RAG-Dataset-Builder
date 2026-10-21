import json
import re
from pathlib import Path

import tiktoken

BASE_DIR = Path(__file__).resolve().parent.parent

STRUCTURED_PATH = (
    BASE_DIR
    / "data"
    / "mineru"
    / "02_giao-trinh"
    / "vi"
    / "VI_TX_010_Machine Learning co ban"
    / "structured_content.json"
)

NORMALIZED_PATH = BASE_DIR / "data" / "processed" / "day13.json"
OUTPUT_PATH = BASE_DIR / "data" / "processed" / "day17.json"

MAX_TOKENS = 500

ENCODING = tiktoken.get_encoding("cl100k_base")

IMAGE_TYPE = "image"

IGNORE_TYPES = {
    "header",
    "footer",
    "page_number",
}

def count_tokens(text):
    return len(ENCODING.encode(text))

def load_json(input_path):
    with input_path.open("r", encoding="utf-8") as file:
        return json.load(file)

def index_raw_blocks(data):
    pages = data.get("pages", [])

    if not isinstance(pages, list):
        raise ValueError(
            "structured_content.json does not contain a valid pages list."
        )

    block_index = {}

    for page in pages:
        page_idx = page.get("page_idx")
        blocks = page.get("blocks", [])

        for source_index, block in enumerate(blocks):
            if not isinstance(block, dict):
                continue

            key = (page_idx, source_index)
            block_index[key] = block

    return block_index

def enrich_records(
    records,
    raw_block_index,
):
    enriched = []

    for record in records:
        if not isinstance(record, dict):
            continue

        result = dict(record)

        key = (
            record.get("page_idx"),
            record.get("source_index"),
        )

        raw_block = raw_block_index.get(key)

        if raw_block is not None:
            for field in (
                "image_source",
                "captions",
                "footnotes",
            ):
                if field in raw_block:
                    result[field] = raw_block[field]

        enriched.append(result)

    return enriched

def get_content(record):
    content = record.get("content", "")

    if not isinstance(content, str):
        return ""

    return content.strip()

def get_section_path(record):
    path = record.get("section_path", [])

    if not isinstance(path, list):
        return []

    return [
        str(title).strip()
        for title in path
        if str(title).strip()
    ]

def should_keep_record(record):
    block_type = record.get("type", "")

    if block_type in IGNORE_TYPES:
        return False

    if block_type == IMAGE_TYPE:
        return True

    return bool(get_content(record))

def get_source_info(record):
    return {
        "page_idx": record.get("page_idx"),
        "source_index": record.get("source_index"),
        "type": record.get("type", "unknown"),
    }

def extract_caption(record):
    captions = record.get("captions", [])

    if isinstance(captions, str):
        return captions.strip()

    if not isinstance(captions, list):
        return ""

    caption_texts = []

    for caption in captions:
        if isinstance(caption, str):
            content = caption.strip()

        elif isinstance(caption, dict):
            content = str(
                caption.get("content", "")
            ).strip()

        else:
            continue

        if content and content not in caption_texts:
            caption_texts.append(content)

    return " ".join(caption_texts)

def get_image_ref(record):
    raw_path = record.get("image_source")

    if isinstance(raw_path, str):
        raw_path = raw_path.strip()
    else:
        raw_path = None

    return {
        "path": raw_path or None,
        "caption": extract_caption(record),
        "page_idx": record.get("page_idx"),
        "source_index": record.get("source_index"),
    }

def split_long_word(word, max_tokens):
    pieces = []
    current = ""

    for char in word:
        candidate = current + char

        if current and count_tokens(candidate) > max_tokens:
            pieces.append(current)
            current = char
        else:
            current = candidate

    if current:
        pieces.append(current)

    if any(count_tokens(piece) > max_tokens for piece in pieces):
        raise ValueError(
            "Unable to split string to meet token limit."
        )

    return pieces

def split_by_words(text, max_tokens):
    chunks = []
    current_words = []

    for word in text.split():
        if count_tokens(word) > max_tokens:
            if current_words:
                chunks.append(" ".join(current_words))
                current_words = []

            chunks.extend(
                split_long_word(word, max_tokens)
            )
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

def create_empty_chunk(section_path):
    return {
        "section_path": list(section_path),
        "texts": [],
        "pages": [],
        "block_types": [],
        "source_blocks": [],
        "images": [],
    }

def add_source_metadata(
    current,
    record,
):
    current["pages"].append(record.get("page_idx"))

    current["block_types"].append(
        record.get("type", "unknown")
    )

    current["source_blocks"].append(
        get_source_info(record)
    )

def attach_image(
    current,
    record,
):
    image_ref = get_image_ref(record)

    key = (
        image_ref["page_idx"],
        image_ref["source_index"],
        image_ref["path"],
    )

    existing_keys = {
        (
            image.get("page_idx"),
            image.get("source_index"),
            image.get("path"),
        )
        for image in current["images"]
    }

    if key not in existing_keys:
        current["images"].append(image_ref)
        add_source_metadata(current, record)

def finalize_chunk(current, chunks):
    if current is None:
        return

    if not current["texts"] and not current["images"]:
        return

    text = "\n\n".join(current["texts"]).strip()

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

    block_types = list(dict.fromkeys(
        current["block_types"]
    ))

    images = list(current["images"])

    chunks.append({
        "chunk_id": f"day17_chunk_{len(chunks) + 1:06d}",
        "section_path": list(current["section_path"]),
        "page_start": min(pages) if pages else None,
        "page_end": max(pages) if pages else None,
        "text": text,
        "token_count": count_tokens(text),
        "block_types": block_types,
        "has_image": bool(images),
        "image_count": len(images),
        "images": images,
        "has_table": "table" in block_types,
        "has_equation": "equation" in block_types,
        "source_blocks": source_blocks,
    })

def build_section_chunks(
    records,
    section_path,
    chunks,
    max_tokens,
):
    current = None
    pending_images = []

    for record in records:
        block_type = record.get("type", "")

        if block_type == IMAGE_TYPE:
            if current is not None and current["texts"]:
                attach_image(current, record)
            else:
                pending_images.append(record)

            continue

        content = get_content(record)

        if not content:
            continue

        pieces = split_text_to_fit(content, max_tokens)

        for piece in pieces:
            if current is None:
                current = create_empty_chunk(section_path)

                for image_record in pending_images:
                    attach_image(current, image_record)

                pending_images = []

            candidate = "\n\n".join(
                current["texts"] + [piece]
            )

            if (
                current["texts"]
                and count_tokens(candidate) > max_tokens
            ):
                finalize_chunk(current, chunks)

                current = create_empty_chunk(section_path)

            current["texts"].append(piece)

            add_source_metadata(current, record)

    if current is not None:
        finalize_chunk(current, chunks)

    if pending_images:
        image_only_chunk = create_empty_chunk(section_path)

        for image_record in pending_images:
            attach_image(image_only_chunk, image_record)

        finalize_chunk(image_only_chunk, chunks)

def build_image_aware_chunks(
    records,
    max_tokens=MAX_TOKENS,
):
    if max_tokens <= 0:
        raise ValueError("max_tokens must be greater than 0.")

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
            build_section_chunks(
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
        build_section_chunks(
            section_records,
            current_section_path,
            chunks,
            max_tokens,
        )

    return chunks

def validate_chunks(
    chunks,
    max_tokens=MAX_TOKENS,
):
    seen_ids = set()

    for chunk in chunks:
        chunk_id = chunk["chunk_id"]

        if chunk_id in seen_ids:
            raise ValueError(
                f"Duplicate chunk ID: {chunk_id}"
            )

        seen_ids.add(chunk_id)

        text = chunk["text"]
        images = chunk["images"]

        if not text.strip() and not images:
            raise ValueError(
                f"Chunk has no text or images: {chunk_id}"
            )

        actual_tokens = count_tokens(text)

        if actual_tokens > max_tokens:
            raise ValueError(
                f"{chunk_id} exceeds MAX_TOKENS: "
                f"{actual_tokens} > {max_tokens}"
            )

        if actual_tokens != chunk["token_count"]:
            raise ValueError(
                f"token_count mismatch: {chunk_id}"
            )

        if chunk["has_image"] != bool(images):
            raise ValueError(
                f"has_image metadata mismatch: {chunk_id}"
            )

        if chunk["image_count"] != len(images):
            raise ValueError(
                f"image_count mismatch: {chunk_id}"
            )

        page_start = chunk["page_start"]
        page_end = chunk["page_end"]

        if (
            page_start is not None
            and page_end is not None
            and page_start > page_end
        ):
            raise ValueError(
                f"Invalid page range: {chunk_id}"
            )

def save_data(data, output_path):
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
    for path in (NORMALIZED_PATH, STRUCTURED_PATH):
        if not path.exists():
            print(f"File not found: {path}")
            return

    try:
        records = load_json(NORMALIZED_PATH)

        if not isinstance(records, list):
            raise ValueError(
                "day13.json must contain a list of records."
            )

        raw_data = load_json(STRUCTURED_PATH)

        if not isinstance(raw_data, dict):
            raise ValueError(
                "structured_content.json must be a JSON object."
            )

        raw_block_index = index_raw_blocks(raw_data)

        records = enrich_records(
            records,
            raw_block_index,
        )

        print(f"Normalized input: {NORMALIZED_PATH}")
        print(f"Original input: {STRUCTURED_PATH}")
        print(f"Total input records: {len(records)}")

        image_blocks = [
            record for record in records
            if record.get("type") == IMAGE_TYPE
        ]

        print(f"Image blocks found: {len(image_blocks)}")

        chunks = build_image_aware_chunks(
            records,
            max_tokens=MAX_TOKENS,
        )

        validate_chunks(
            chunks,
            max_tokens=MAX_TOKENS,
        )

        save_data(chunks, OUTPUT_PATH)

        chunks_with_images = [
            chunk for chunk in chunks
            if chunk["has_image"]
        ]

        image_refs = [
            image
            for chunk in chunks
            for image in chunk["images"]
        ]

        missing_paths = [
            image for image in image_refs
            if not image["path"]
        ]

        missing_captions = [
            image for image in image_refs
            if not image["caption"]
        ]

        token_counts = [
            chunk["token_count"]
            for chunk in chunks
        ]

        print(f"\nTotal chunks: {len(chunks)}")
        print(f"Chunks with images: {len(chunks_with_images)}")
        print(f"Total image references: {len(image_refs)}")
        print(f"Images missing paths: {len(missing_paths)}")
        print(f"Images missing captions: {len(missing_captions)}")
        print(f"MAX_TOKENS: {MAX_TOKENS}")

        if token_counts:
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
                "has_image": chunk["has_image"],
                "image_count": chunk["image_count"],
            })

        print("\nValidation passed.")
        print(f"Result saved at: {OUTPUT_PATH}")

    except (
        OSError,
        json.JSONDecodeError,
        ValueError,
    ) as error:
        print(f"Error: {error}")

if __name__ == "__main__":
    main()