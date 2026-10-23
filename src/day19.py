import json
from pathlib import Path
from statistics import mean

BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_PATH = BASE_DIR / "data" / "processed" / "day18.json"

OUTPUT_DIR = BASE_DIR / "data" / "chunked"

CHILD_OUTPUT_PATH = OUTPUT_DIR / "chunks.jsonl"
PARENT_OUTPUT_PATH = OUTPUT_DIR / "parents.jsonl"
STATS_OUTPUT_PATH = OUTPUT_DIR / "chunk_stats.json"
ERROR_OUTPUT_PATH = OUTPUT_DIR / "errors.jsonl"

DOC_ID = "VI_TX_010_Machine_Learning_co_ban"

CHILD_MAX_TOKENS = 500
PARENT_MAX_TOKENS = 1500

try:
    import tiktoken

    ENCODING = tiktoken.get_encoding("cl100k_base")

except ImportError as error:
    raise ImportError(
        "Missing tiktoken library. "
        "Install using: pip install tiktoken"
    ) from error

def load_json(input_path):
    with input_path.open("r", encoding="utf-8") as file:
        return json.load(file)

def count_tokens(text):
    return len(ENCODING.encode(text))

def get_text(record):
    text = record.get("text", "")

    if not isinstance(text, str):
        return ""

    return text.strip()

def get_section_path(record):
    path = record.get("section_path", [])

    if not isinstance(path, list):
        return []

    return [
        str(title).strip()
        for title in path
        if str(title).strip()
    ]

def unique_dicts(items, key_fields):
    result = []
    seen = set()

    for item in items:
        if not isinstance(item, dict):
            continue

        key = tuple(item.get(field) for field in key_fields)

        if key not in seen:
            seen.add(key)
            result.append(dict(item))

    return result

def get_page_bounds(children):
    pages = []

    for child in children:
        for field in ("page_start", "page_end"):
            page = child.get(field)

            if isinstance(page, int) and not isinstance(page, bool):
                pages.append(page)

        for source in child.get("source_blocks", []):
            if not isinstance(source, dict):
                continue

            page = source.get("page_idx")

            if isinstance(page, int) and not isinstance(page, bool):
                pages.append(page)

    if not pages:
        return None, None

    return min(pages), max(pages)

def combine_text(records):
    texts = [
        get_text(record)
        for record in records
        if get_text(record)
    ]

    return "\n\n".join(texts)

def normalize_child_records(
    records,
    max_tokens,
):
    normalized = []

    for index, record in enumerate(records):
        if not isinstance(record, dict):
            raise ValueError(
                f"Record at position {index} is not a dictionary."
            )

        text = get_text(record)
        actual_tokens = count_tokens(text)

        if actual_tokens > max_tokens:
            raise ValueError(
                f"Source chunk {record.get('chunk_id', index)} "
                f"has {actual_tokens} tokens, exceeding child limit "
                f"{max_tokens}. Please check Day 18 output."
            )

        child = dict(record)

        child["_source_chunk_id"] = record.get("chunk_id")

        child["text"] = text
        child["section_path"] = get_section_path(record)
        child["token_count"] = actual_tokens

        normalized.append(child)

    return normalized

def group_children_into_parents(
    children,
    parent_max_tokens,
):
    if parent_max_tokens <= 0:
        raise ValueError(
            "parent_max_tokens must be greater than 0."
        )

    groups = []
    current_group = []
    current_section_path = None

    for child in children:
        section_path = child["section_path"]

        if (
            current_group
            and section_path != current_section_path
        ):
            groups.append(current_group)
            current_group = []

        if not current_group:
            current_section_path = section_path

        candidate_text = combine_text(
            current_group + [child]
        )

        if (
            current_group
            and count_tokens(candidate_text) > parent_max_tokens
        ):
            groups.append(current_group)
            current_group = []
            current_section_path = section_path

        if count_tokens(get_text(child)) > parent_max_tokens:
            raise ValueError(
                "A child exceeds the parent limit."
            )

        current_group.append(child)

    if current_group:
        groups.append(current_group)

    return groups

def build_parent_child_dataset(
    records,
    child_max_tokens=CHILD_MAX_TOKENS,
    parent_max_tokens=PARENT_MAX_TOKENS,
):
    normalized = normalize_child_records(
        records,
        child_max_tokens,
    )

    groups = group_children_into_parents(
        normalized,
        parent_max_tokens,
    )

    children_output = []
    parents_output = []

    child_counter = 0

    for parent_index, group in enumerate(groups, start=1):
        parent_id = f"parent_{parent_index:06d}"

        children_of_parent = []

        for source_child in group:
            child_counter += 1

            child = dict(source_child)

            source_chunk_id = child.pop(
                "_source_chunk_id",
                None,
            )

            child_id = f"child_{child_counter:06d}"

            child["chunk_id"] = child_id
            child["parent_id"] = parent_id
            child["doc_id"] = DOC_ID
            child["source_chunk_id"] = source_chunk_id
            child["source_file"] = INPUT_PATH.name

            child["section_path"] = list(
                source_child["section_path"]
            )

            child["text"] = get_text(source_child)
            child["token_count"] = count_tokens(child["text"])

            children_of_parent.append(child)
            children_output.append(child)

        parent_text = combine_text(children_of_parent)

        if count_tokens(parent_text) > parent_max_tokens:
            raise ValueError(
                f"{parent_id} exceeds parent token limit."
            )

        page_start, page_end = get_page_bounds(
            children_of_parent
        )

        block_types = []

        for child in children_of_parent:
            for block_type in child.get("block_types", []):
                if block_type not in block_types:
                    block_types.append(block_type)

        all_source_blocks = []

        for child in children_of_parent:
            all_source_blocks.extend(
                child.get("source_blocks", [])
            )

        all_images = []

        for child in children_of_parent:
            all_images.extend(
                child.get("images", [])
            )

        all_table_sources = []

        for child in children_of_parent:
            all_table_sources.extend(
                child.get("table_sources", [])
            )

        source_blocks = unique_dicts(
            all_source_blocks,
            ("page_idx", "source_index", "type"),
        )

        images = unique_dicts(
            all_images,
            ("page_idx", "source_index", "path"),
        )

        table_sources = unique_dicts(
            all_table_sources,
            (
                "page_idx",
                "source_index",
                "part_index",
            ),
        )

        has_table = any(
            child.get("has_table", False)
            for child in children_of_parent
        )

        has_equation = any(
            child.get("has_equation", False)
            for child in children_of_parent
        )

        has_image = any(
            child.get("has_image", False)
            or child.get("images")
            for child in children_of_parent
        )

        parent = {
            "parent_id": parent_id,
            "doc_id": DOC_ID,
            "section_path": list(
                children_of_parent[0]["section_path"]
            ),
            "page_start": page_start,
            "page_end": page_end,
            "text": parent_text,
            "token_count": count_tokens(parent_text),
            "child_ids": [
                child["chunk_id"]
                for child in children_of_parent
            ],
            "child_count": len(children_of_parent),
            "block_types": block_types,
            "has_table": has_table,
            "has_equation": has_equation,
            "has_image": has_image,
            "images": images,
            "table_sources": table_sources,
            "source_blocks": source_blocks,
            "source_file": INPUT_PATH.name,
        }

        parents_output.append(parent)

    return children_output, parents_output

def validate_dataset(
    children,
    parents,
    child_max_tokens,
    parent_max_tokens,
):
    child_ids = set()
    parent_ids = set()

    for parent in parents:
        parent_id = parent["parent_id"]

        if parent_id in parent_ids:
            raise ValueError(
                f"Duplicate parent ID: {parent_id}"
            )

        parent_ids.add(parent_id)

        if count_tokens(parent["text"]) > parent_max_tokens:
            raise ValueError(
                f"{parent_id} exceeds token limit."
            )

    for child in children:
        child_id = child["chunk_id"]

        if child_id in child_ids:
            raise ValueError(
                f"Duplicate child ID: {child_id}"
            )

        child_ids.add(child_id)

        if child["parent_id"] not in parent_ids:
            raise ValueError(
                f"{child_id} references a non-existent parent."
            )

        actual_tokens = count_tokens(child["text"])

        if actual_tokens > child_max_tokens:
            raise ValueError(
                f"{child_id} exceeds child token limit."
            )

        if actual_tokens != child["token_count"]:
            raise ValueError(
                f"token_count mismatch: {child_id}"
            )

    child_to_parent = {
        child["chunk_id"]: child["parent_id"]
        for child in children
    }

    for parent in parents:
        for child_id in parent["child_ids"]:
            if child_to_parent.get(child_id) != parent["parent_id"]:
                raise ValueError(
                    f"Parent-child link mismatch: {child_id}"
                )

        if parent["child_count"] != len(parent["child_ids"]):
            raise ValueError(
                f"child_count mismatch: {parent['parent_id']}"
            )

        if count_tokens(parent["text"]) != parent["token_count"]:
            raise ValueError(
                f"token_count mismatch: {parent['parent_id']}"
            )

def write_jsonl(data, output_path):
    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with output_path.open("w", encoding="utf-8") as file:
        for record in data:
            file.write(
                json.dumps(
                    record,
                    ensure_ascii=False,
                )
                + "\n"
            )

def write_json(data, output_path):
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

def build_stats(
    children,
    parents,
):
    child_tokens = [
        child["token_count"]
        for child in children
    ]

    parent_tokens = [
        parent["token_count"]
        for parent in parents
    ]

    cross_page_children = sum(
        1
        for child in children
        if (
            child.get("page_start") is not None
            and child.get("page_end") is not None
            and child["page_start"] != child["page_end"]
        )
    )

    cross_page_parents = sum(
        1
        for parent in parents
        if (
            parent.get("page_start") is not None
            and parent.get("page_end") is not None
            and parent["page_start"] != parent["page_end"]
        )
    )

    return {
        "doc_id": DOC_ID,
        "input_file": INPUT_PATH.name,
        "child_max_tokens": CHILD_MAX_TOKENS,
        "parent_max_tokens": PARENT_MAX_TOKENS,
        "total_children": len(children),
        "total_parents": len(parents),
        "average_child_tokens": (
            round(mean(child_tokens), 2)
            if child_tokens else 0
        ),
        "min_child_tokens": (
            min(child_tokens) if child_tokens else 0
        ),
        "max_child_tokens": (
            max(child_tokens) if child_tokens else 0
        ),
        "average_parent_tokens": (
            round(mean(parent_tokens), 2)
            if parent_tokens else 0
        ),
        "min_parent_tokens": (
            min(parent_tokens) if parent_tokens else 0
        ),
        "max_parent_tokens": (
            max(parent_tokens) if parent_tokens else 0
        ),
        "children_spanning_multiple_pages": cross_page_children,
        "parents_spanning_multiple_pages": cross_page_parents,
        "children_with_images": sum(
            bool(child.get("has_image"))
            for child in children
        ),
        "children_with_tables": sum(
            bool(child.get("has_table"))
            for child in children
        ),
        "children_with_equations": sum(
            bool(child.get("has_equation"))
            for child in children
        ),
    }

def main():
    if not INPUT_PATH.exists():
        print(f"File not found: {INPUT_PATH}")
        return

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    try:
        records = load_json(INPUT_PATH)

        if not isinstance(records, list):
            raise ValueError(
                "day18.json must contain a list of chunks."
            )

        print(f"Input: {INPUT_PATH}")
        print(f"Input records: {len(records)}")

        children, parents = build_parent_child_dataset(
            records,
            child_max_tokens=CHILD_MAX_TOKENS,
            parent_max_tokens=PARENT_MAX_TOKENS,
        )

        validate_dataset(
            children,
            parents,
            child_max_tokens=CHILD_MAX_TOKENS,
            parent_max_tokens=PARENT_MAX_TOKENS,
        )

        write_jsonl(
            children,
            CHILD_OUTPUT_PATH,
        )

        write_jsonl(
            parents,
            PARENT_OUTPUT_PATH,
        )

        stats = build_stats(children, parents)

        write_json(
            stats,
            STATS_OUTPUT_PATH,
        )

        write_jsonl(
            [],
            ERROR_OUTPUT_PATH,
        )

        print(f"Total children: {len(children)}")
        print(f"Total parents: {len(parents)}")

        print(
            "Average child tokens: "
            f"{stats['average_child_tokens']}"
        )

        print(
            "Average parent tokens: "
            f"{stats['average_parent_tokens']}"
        )

        print(
            "Max child tokens: "
            f"{stats['max_child_tokens']}"
        )

        print(
            "Max parent tokens: "
            f"{stats['max_parent_tokens']}"
        )

        print(f"\nChildren: {CHILD_OUTPUT_PATH}")
        print(f"Parents: {PARENT_OUTPUT_PATH}")
        print(f"Statistics: {STATS_OUTPUT_PATH}")
        print(f"Errors: {ERROR_OUTPUT_PATH}")

        print("\nFirst 3 child records:")

        for child in children[:3]:
            print({
                "chunk_id": child["chunk_id"],
                "parent_id": child["parent_id"],
                "section_path": child["section_path"],
                "token_count": child["token_count"],
            })

        print("\nFirst 3 parent records:")

        for parent in parents[:3]:
            print({
                "parent_id": parent["parent_id"],
                "child_count": parent["child_count"],
                "child_ids": parent["child_ids"],
                "token_count": parent["token_count"],
            })

        print("\nValidation passed.")

    except (
        OSError,
        json.JSONDecodeError,
        ValueError,
    ) as error:
        print(f"Error: {error}")

        write_jsonl(
            [{
                "stage": "day19",
                "error": str(error),
            }],
            ERROR_OUTPUT_PATH,
        )

if __name__ == "__main__":
    main()