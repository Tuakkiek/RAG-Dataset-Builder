import json
from pathlib import Path


FILE_PATH = Path("../data/mineru/02_giao-trinh/vi/VI_TX_010_Machine Learning co ban/structured_content.json")


KEEP_TYPES = {
    "text",
    "paragraph_title",
    "doc_title",
    "code"
}


DROP_TYPES = {
    "header",
    "footer",
    "page_number"
}


SPECIAL_TYPES = {
    "index",
    "page_footnote",
    "image",
    "ref_text",
    "table",
    "equation",
    "chart"
}


def load_json(
    file_path
):
    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as f:
        return json.load(f)


def classify_block(
    block_type
):
    if block_type in DROP_TYPES:
        return "drop"

    if block_type in KEEP_TYPES:
        return "keep"

    if block_type in SPECIAL_TYPES:
        return "special"

    return "unknown"


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

    category = classify_block(
        block_type
    )

    return {
        "page_index": page_index,
        "block_index": block_index,
        "type": block_type,
        "category": category,
        "text": text,
        "bbox": bbox,
        "raw_block": block
    }


def normalize_pages(
    pages
):
    normalized_blocks = []

    for fallback_index, page in enumerate(
        pages
    ):

        page_index = page.get(
            "page_idx",
            fallback_index
        )

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


def filter_blocks(
    blocks
):
    clean_blocks = []

    for block in blocks:

        if block["category"] == "drop":
            continue

        clean_blocks.append(
            block
        )

    return clean_blocks


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


def count_categories(
    blocks
):
    counts = {}

    for block in blocks:

        category = block.get(
            "category",
            "unknown"
        )

        if category not in counts:
            counts[category] = 0

        counts[category] += 1

    return counts


def find_unknown_types(
    blocks
):
    unknown_types = set()

    for block in blocks:

        if block["category"] == "unknown":

            unknown_types.add(
                block["type"]
            )

    return unknown_types


def main():

    if not FILE_PATH.exists():

        print(
            "Không tìm thấy file:"
        )

        print(
            FILE_PATH
        )

        return

    data = load_json(
        FILE_PATH
    )

    pages = data.get(
        "pages",
        []
    )

    normalized_blocks = normalize_pages(
        pages
    )

    print(
        "Total pages:",
        len(pages)
    )

    print(
        "Blocks before filtering:",
        len(normalized_blocks)
    )

    print(
        "\nBlock types before filtering:"
    )

    block_counts = count_block_types(
        normalized_blocks
    )

    for block_type, count in block_counts.items():

        print(
            f"{block_type:<25} {count}"
        )

    category_counts = count_categories(
        normalized_blocks
    )

    print(
        "\nCategories:"
    )

    for category, count in category_counts.items():

        print(
            f"{category:<25} {count}"
        )

    unknown_types = find_unknown_types(
        normalized_blocks
    )

    print(
        "\nUnknown block types:"
    )

    print(
        unknown_types
    )

    clean_blocks = filter_blocks(
        normalized_blocks
    )

    print(
        "\nBlocks after filtering:",
        len(clean_blocks)
    )

    removed_count = (
        len(normalized_blocks)
        - len(clean_blocks)
    )

    print(
        "Removed blocks:",
        removed_count
    )

    if normalized_blocks:

        removed_ratio = (
            removed_count
            / len(normalized_blocks)
        )

        print(
            "Removed ratio:",
            round(
                removed_ratio * 100,
                2
            ),
            "%"
        )

    print(
        "\nBlock types after filtering:"
    )

    clean_counts = count_block_types(
        clean_blocks
    )

    for block_type, count in clean_counts.items():

        print(
            f"{block_type:<25} {count}"
        )


if __name__ == "__main__":
    main()