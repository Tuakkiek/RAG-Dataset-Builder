from pathlib import Path
from transformers import AutoTokenizer

FILE_PATH = Path("../data/mineru/02_giao-trinh/vi/VI_TX_011_Machine Learning co ban/VI_TX_011_Machine Learning co ban.md")

TOKENIZER_NAME = "Qwen/Qwen3-Embedding-0.6B"

CHUNK_SIZE = 512
OVERLAP = 50


def load_text(file_path):
    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as f:
        return f.read()


def count_tokens(
    text,
    tokenizer
):
    token_ids = tokenizer.encode(
        text,
        add_special_tokens=False
    )

    return len(token_ids)


def split_by_tokens(
    text,
    tokenizer,
    chunk_size,
    overlap
):
    if chunk_size <= 0:
        raise ValueError(
            "chunk_size phải > 0"
        )

    if overlap < 0:
        raise ValueError(
            "overlap phải >= 0"
        )

    if overlap >= chunk_size:
        raise ValueError(
            "overlap phải nhỏ hơn chunk_size"
        )

    token_ids = tokenizer.encode(
        text,
        add_special_tokens=False
    )

    chunks = []

    step = chunk_size - overlap

    for start in range(
        0,
        len(token_ids),
        step
    ):
        end = start + chunk_size

        chunk_ids = token_ids[start:end]

        chunk_text = tokenizer.decode(
            chunk_ids,
            skip_special_tokens=True
        )

        chunks.append(chunk_text)

    return chunks


def show_chunk_stats(
    chunks,
    tokenizer
):
    if not chunks:
        print("Không có chunk.")
        return

    token_counts = []

    for chunk in chunks:
        count = count_tokens(
            chunk,
            tokenizer
        )

        token_counts.append(count)

    average = (
        sum(token_counts)
        / len(token_counts)
    )

    print("\nChunk statistics")
    print("-" * 40)

    print(
        "Number of chunks:",
        len(chunks)
    )

    print(
        "Min tokens:",
        min(token_counts)
    )

    print(
        "Max tokens:",
        max(token_counts)
    )

    print(
        "Average tokens:",
        round(average, 2)
    )


def print_first_chunks(
    chunks,
    tokenizer,
    n=3
):
    for index, chunk in enumerate(
        chunks[:n],
        start=1
    ):
        print("\n" + "=" * 80)

        print(
            f"CHUNK_{index:04d}"
        )

        print("=" * 80)

        print(
            "Token count:",
            count_tokens(
                chunk,
                tokenizer
            )
        )

        print()

        print(chunk)


def main():
    if not FILE_PATH.exists():
        print("Không tìm thấy file:")
        print(FILE_PATH)
        return

    print("Đang load tokenizer...")

    tokenizer = AutoTokenizer.from_pretrained(
        TOKENIZER_NAME
    )

    text = load_text(
        FILE_PATH
    )

    total_tokens = count_tokens(
        text,
        tokenizer
    )

    print(
        "Total tokens:",
        total_tokens
    )

    print(
        "Chunk size:",
        CHUNK_SIZE
    )

    print(
        "Overlap:",
        OVERLAP
    )

    print(
        "Step:",
        CHUNK_SIZE - OVERLAP
    )

    chunks = split_by_tokens(
        text,
        tokenizer,
        CHUNK_SIZE,
        OVERLAP
    )

    show_chunk_stats(
        chunks,
        tokenizer
    )

    print_first_chunks(
        chunks,
        tokenizer,
        n=3
    )


if __name__ == "__main__":
    main()