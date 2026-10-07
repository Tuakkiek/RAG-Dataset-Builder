from pathlib import Path


FILE_PATH = Path("../data/mineru/02_giao-trinh/vi/VI_TX_011_Machine Learning co ban/VI_TX_011_Machine Learning co ban.md")


CHUNK_SIZE = 200


def load_text(file_path):
    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as f:
        return f.read()


def split_by_words(text, chunk_size):
    words = text.split()

    chunks = []

    for start in range(
        0,
        len(words),
        chunk_size
    ):
        end = start + chunk_size

        chunk_words = words[start:end]

        chunk = " ".join(
            chunk_words
        )

        chunks.append(chunk)

    return chunks


def show_chunk_stats(chunks):
    if not chunks:
        print("Không có chunk.")
        return

    word_counts = []

    for chunk in chunks:
        count = len(
            chunk.split()
        )

        word_counts.append(count)

    average = (
        sum(word_counts)
        / len(word_counts)
    )

    print("\nChunk statistics")
    print("-" * 40)

    print(
        "Number of chunks:",
        len(chunks)
    )

    print(
        "Min words:",
        min(word_counts)
    )

    print(
        "Max words:",
        max(word_counts)
    )

    print(
        "Average words:",
        round(average, 2)
    )


def print_first_chunks(
    chunks,
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

        print(chunk)


def main():
    if not FILE_PATH.exists():
        print(
            "Không tìm thấy file:"
        )

        print(FILE_PATH)

        return

    text = load_text(
        FILE_PATH
    )

    words = text.split()

    print(
        "Total characters:",
        len(text)
    )

    print(
        "Total words:",
        len(words)
    )

    chunks = split_by_words(
        text,
        CHUNK_SIZE
    )

    print(
        "Chunk size:",
        CHUNK_SIZE,
        "words"
    )

    show_chunk_stats(
        chunks
    )

    print_first_chunks(
        chunks,
        n=3
    )


if __name__ == "__main__":
    main()