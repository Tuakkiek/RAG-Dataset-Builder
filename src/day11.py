import json
from pathlib import Path


FILE_PATH = Path("../data/mineru/02_giao-trinh/vi/VI_TX_010_Machine Learning co ban/structured_content.json")



def load_json(
    file_path
):
    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as f:
        return json.load(f)


def normalize_block(
    block,
    page_index,
    block_index
):
    block_type = block.get(
        "type",
        "unknown"
    )

    text = block.get(
        "text",
        ""
    )

    bbox = block.get(
        "bbox"
    )

    normalized_block = {
        "page_index": page_index,
        "block_index": block_index,
        "type": block_type,
        "text": text,
        "bbox": bbox,
        "raw_block": block
    }

    return normalized_block


def normalize_pages(
    pages
):
    normalized_blocks = []

    for page_index, page in enumerate(
        pages
    ):

        blocks = page.get(
            "blocks",
            []
        )

        for block_index, block in enumerate(
            blocks
        ):

            normalized_block = normalize_block(
                block,
                page_index,
                block_index
            )

            normalized_blocks.append(
                normalized_block
            )

    return normalized_blocks


def count_block_types(
    blocks
):
    counts = {}

    for block in blocks:

        block_type = block.get(
            "type",
            "unknown"
        )

        if block_type not in counts:
            counts[block_type] = 0

        counts[block_type] += 1

    return counts


def print_first_blocks(
    blocks,
    n=5
):
    for block in blocks[:n]:

        print(
            "\n"
            + "=" * 80
        )

        print(
            "Page index:",
            block["page_index"]
        )

        print(
            "Block index:",
            block["block_index"]
        )

        print(
            "Type:",
            block["type"]
        )

        print(
            "BBox:",
            block["bbox"]
        )

        print(
            "Text:"
        )

        print(
            block["text"]
        )


def main():

    if not FILE_PATH.exists():

        print(
            "File not found:"
        )

        print(
            FILE_PATH
        )

        return

    data = load_json(
        FILE_PATH
    )

    print(
        "Root type:",
        type(data)
    )

    print(
        "Root keys:",
        data.keys()
    )

    pages = data.get(
        "pages",
        []
    )

    print(
        "\nTotal pages:",
        len(pages)
    )

    if not pages:

        print(
            "There are no pages at all."
        )

        return

    print(
        "\nFirst page keys:"
    )

    print(
        pages[0].keys()
    )

    normalized_blocks = normalize_pages(
        pages
    )

    print(
        "\nTotal normalized blocks:",
        len(normalized_blocks)
    )

    block_counts = count_block_types(
        normalized_blocks
    )

    print(
        "\nBlock types:"
    )

    for block_type, count in block_counts.items():

        print(
            f"{block_type:<25} {count}"
        )

    print_first_blocks(
        normalized_blocks,
        n=10
    )


if __name__ == "__main__":
    main()