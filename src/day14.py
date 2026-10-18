import re
import json 
from pathlib import Path 

import tiktoken

BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_PATH = BASE_DIR / "data" / "processed" / "day13.json"

OUTPUT_PATH = BASE_DIR / "data" / "processed" / "day14.json"

MAX_TOKENS = 500

ENCODING = tiktoken.get_encoding("cl100k_base")

IGNORE_TYPES = {
    "header", 
    "footer", 
    "page_number"
}

def token_count(
    text
): 
    return len(ENCODING.encode(text))

def load_json(
    input_path
): 
    with open(input_path, "r", encoding="utf-8") as f: 
        return json.load(f)

def shoud_keep_record(
    record
): 
    block_type = record.get("type", "")
    content = record.get("content", "")

    if block_type in IGNORE_TYPES: 
        return False 

    if not isinstance(content, str): 
        return False 

    return bool(content.strip())

def count_tokens(text):
    return len(ENCODING.encode(text))

def get_section_path(
    record
): 
    path = record.get("section_path", [])

    if not isinstance(path, list): 
        return [] 

    return [
        str(title).strip()
        for title in path
        if str(title).strip()
    ]

def split_by_words(text: str, max_tokens: int) -> list:

    chunks = []
    current_words = []

    for word in text.split():
        if count_tokens(word) > max_tokens:
            if current_words:
                chunks.append(" ".join(current_words))
                current_words = []

            chunks.extend(split_long_word(word, max_tokens))
            continue

        candidate_words = current_words + [word]
        candidate_text = " ".join(candidate_words)

        if (
            current_words
            and count_tokens(candidate_text) > max_tokens
        ):
            chunks.append(" ".join(current_words))
            current_words = [word]
        else:
            current_words.append(word)

    if current_words:
        chunks.append(" ".join(current_words))

    return chunks



def split_text_to_fit(
    text, 
    max_tokens
):

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

        if current and count_tokens(candidate) > max_tokens:
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
    }

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

    unique_sources = [] 
    seen_sources = set() 

    for source in current["source_blocks"]: 
        key = (source["page_idx"], source["source_index"])

        if key not in seen_sources: 
            seen_sources.add(key)
            unique_sources.append(source)

    chunks.append({
        "chunk_id": f"day14_chunk_{len(chunks) + 1:06d}",
        "section_path": current["section_path"],
        "page_start": min(pages) if pages else None,
        "page_end": max(pages) if pages else None,
        "text": text,
        "token_count": count_tokens(text),
        "block_types": list(dict.fromkeys(
            current["block_types"]
        )),
        "source_blocks": unique_sources,
    })


def build_section_chunks(
    records, 
    max_tokens
): 
    chunks = [] 
    current = None 

    for record in records: 
        if not shoud_keep_record(record): 
            continue

        content = record.get("content").strip()
        section_path = get_section_path(record)

        if (
            current is not None
            and current["section_path"] != section_path
        ): 
            finalize_chunk(current, chunks)
            current = None

        pieces = split_text_to_fit(content, max_tokens)

        for piece in pieces:
            if current is None:
                current = create_empty_chunk(section_path)

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
            current["pages"].append(record.get("page_idx"))
            current["block_types"].append(
                record.get("type", "unknown")
            )
            current["source_blocks"].append({
                "page_idx": record.get("page_idx"),
                "source_index": record.get("source_index"),
            })

    if current is not None:
        finalize_chunk(current, chunks)

    return chunks

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
        print("File not found")
        print(INPUT_PATH)
        return 

    records = load_json(INPUT_PATH)

    print(records[0])

    print("Total input records: ", len(records))

    chunks = build_section_chunks(
        records, 
        max_tokens = MAX_TOKENS,
    )

    save_data(chunks, OUTPUT_PATH)

    print(f"Total number of chunks: {len(chunks)}")
    print(f"Max token: {MAX_TOKENS}")
    print(f"Output path: {OUTPUT_PATH}")

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
                })

    print(f"Result saved at: {OUTPUT_PATH}")

if __name__ == "__main__": 
    main()

