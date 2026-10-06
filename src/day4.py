from pathlib import Path


FILE_PATH = Path("../data/mineru/02_giao-trinh/vi/VI_TX_011_Machine Learning co ban/VI_TX_011_Machine Learning co ban.md")


CHUNK_SIZE = 1000


def load_text(file_path):

    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def split_by_characters(text, chunk_size):

    chunks = []

    for start in range(
        0,
        len(text),
        chunk_size
    ):

        end = start + chunk_size

        chunk = text[start:end]

        chunks.append(chunk)

    return chunks


def show_chunk_stats(chunks):

    if not chunks:
        print("Không có chunk.")
        return

    lengths = []

    for chunk in chunks:
        lengths.append(len(chunk))

    print("\nChunk statistics")
    print("-" * 40)

    print("Number of chunks:", len(chunks))
    print("Min length:", min(lengths))
    print("Max length:", max(lengths))

    average = sum(lengths) / len(lengths)

    print("Average length:", round(average, 2))


def print_first_chunks(chunks, n=3):

    print("\nFirst chunks")

    for i in range(
        min(n, len(chunks))
    ):

        print("\n" + "=" * 80)
        print(f"CHUNK {i + 1}")
        print("=" * 80)

        print(chunks[i])


def main():

    if not FILE_PATH.exists():
        print("Không tìm thấy file:")
        print(FILE_PATH)
        return

    text = load_text(FILE_PATH)

    print("Total characters:")
    print(len(text))

    chunks = split_by_characters(
        text,
        CHUNK_SIZE
    )

    show_chunk_stats(chunks)

    print_first_chunks(
        chunks,
        n=3
    )


if __name__ == "__main__":
    main()