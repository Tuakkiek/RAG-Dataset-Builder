from __future__ import annotations

import json
import logging
import math
import statistics
from copy import deepcopy
from pathlib import Path
from typing import Any, Iterable

import tiktoken

"""Day 20 - Adaptive Chunk Size.

Input : data/processed/day18.json
Output: data/processed/day20.json
        data/processed/day20_stats.json
        data/processed/day20_errors.jsonl
"""

MIN_TOKENS = 200
TARGET_TOKENS = 500
MAX_TOKENS = 800
ENCODING_NAME = "cl100k_base"

BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_PATH = BASE_DIR / "data" / "processed" / "day18.json"
OUTPUT_PATH = BASE_DIR / "data" / "processed" / "day20.json"
STATS_PATH = BASE_DIR / "data" / "processed" / "day20_stats.json"
ERRORS_PATH = BASE_DIR / "data" / "processed" / "day20_errors.jsonl"

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
LOGGER = logging.getLogger("adaptive_chunker")
ENCODING = tiktoken.get_encoding(ENCODING_NAME)


def count_tokens(
    text: str,
) -> int:
    return len(ENCODING.encode(text or ""))


def get_text(
    record: dict[str, Any],
) -> str:
    value = record.get("text")
    if value is None:
        value = record.get("content", "")
    if isinstance(value, str):
        return value.strip()
    if value is None:
        return ""
    return str(value).strip()


def stable_key(
    value: Any,
) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, default=str)


def section_key(
    record: dict[str, Any],
) -> str | None:
    section = record.get("section_path")
    if section in (None, "", [], {}):
        return None
    return stable_key(section)


def unique_values(
    values: Iterable[Any],
) -> list[Any]:
    output: list[Any] = []
    seen: set[str] = set()
    for value in values:
        key = stable_key(value)
        if key not in seen:
            seen.add(key)
            output.append(value)
    return output


def unique_from_records(
    records: list[dict[str, Any]],
    field: str,
) -> list[Any]:
    values: list[Any] = []
    for record in records:
        value = record.get(field)
        if isinstance(value, list):
            values.extend(value)
        elif value is not None:
            values.append(value)
    return unique_values(values)


def as_int(
    value: Any,
) -> int | None:
    try:
        if value is None or isinstance(value, bool):
            return None
        return int(value)
    except (TypeError, ValueError):
        return None


def record_source_ids(
    record: dict[str, Any],
) -> list[str]:
    existing = record.get("source_chunk_ids") or record.get("_source_chunk_ids")
    if isinstance(existing, list) and existing:
        return [str(x) for x in existing]
    original_id = record.get("chunk_id", record.get("id"))
    if original_id is not None:
        return [str(original_id)]
    return []


def largest_prefix_under_limit(
    text: str,
    start: int,
    max_tokens: int,
) -> int:
    low = start + 1
    high = len(text)
    best = start

    while low <= high:
        mid = (low + high) // 2
        token_count = count_tokens(text[start:mid])
        if token_count <= max_tokens:
            best = mid
            low = mid + 1
        else:
            high = mid - 1

    if best <= start:
        # Extremely defensive fallback. A single character should fit.
        return min(start + 1, len(text))

    return best


def choose_natural_boundary(
    text: str,
    start: int,
    max_end: int,
) -> int:
    if max_end >= len(text):
        return max_end

    # Search the final 25% of the candidate window so the resulting piece
    # remains reasonably close to MAX_TOKENS.
    lower = start + max(1, int((max_end - start) * 0.75))
    candidates = [
        text.rfind("\n\n", lower, max_end),
        text.rfind("\n", lower, max_end),
        text.rfind(". ", lower, max_end),
        text.rfind("! ", lower, max_end),
        text.rfind("? ", lower, max_end),
        text.rfind("; ", lower, max_end),
        text.rfind(" ", lower, max_end),
    ]
    valid = [p for p in candidates if p > start]
    if not valid:
        return max_end

    boundary = max(valid)
    
    if text[boundary:boundary + 2] in {". ", "! ", "? ", "; ", "\n\n"}:
        boundary += 1 if text[boundary:boundary + 2] != "\n\n" else 2
    else:
        boundary += 1
    return min(boundary, max_end)


def split_text_by_tokens(
    text: str,
    max_tokens: int,
) -> list[str]:
    text = text.strip()
    if not text:
        return [""]
    if count_tokens(text) <= max_tokens:
        return [text]

    pieces: list[str] = []
    start = 0
    while start < len(text):
        
        while start < len(text) and text[start].isspace():
            start += 1
        if start >= len(text):
            break

        max_end = largest_prefix_under_limit(text, start, max_tokens)
        end = choose_natural_boundary(text, start, max_end)
        piece = text[start:end].strip()

        while piece and count_tokens(piece) > max_tokens and end > start + 1:
            end -= 1
            piece = text[start:end].strip()

        if not piece:
            end = max(start + 1, end)
            piece = text[start:end].strip()

        pieces.append(piece)
        start = end

    result: list[str] = []
    for piece in pieces:
        if piece and count_tokens(piece) > max_tokens and len(piece) > 1:
            midpoint = len(piece) // 2
            result.extend(split_text_by_tokens(piece[:midpoint], max_tokens))
            result.extend(split_text_by_tokens(piece[midpoint:], max_tokens))
        else:
            result.append(piece)
    return [piece for piece in result if piece or not text]


def split_oversized_record(
    record: dict[str, Any],
) -> tuple[list[dict[str, Any]], int]:
    
    text = get_text(record)
    if count_tokens(text) <= MAX_TOKENS:
        copied = deepcopy(record)
        copied["text"] = text
        copied["_source_chunk_ids"] = record_source_ids(record)
        copied["token_count"] = count_tokens(text)
        return [copied], 0

    total_tokens = count_tokens(text)
    part_count = max(2, math.ceil(total_tokens / MAX_TOKENS))
    per_piece_limit = min(MAX_TOKENS, math.ceil(total_tokens / part_count))
    pieces = split_text_by_tokens(text, per_piece_limit)
    source_ids = record_source_ids(record)
    output: list[dict[str, Any]] = []
    for index, piece in enumerate(pieces, start=1):
        item = deepcopy(record)
        item["text"] = piece
        item["token_count"] = count_tokens(piece)
        item["_source_chunk_ids"] = source_ids
        item["split_part"] = index
        item["split_total"] = len(pieces)
        item["split_reason"] = f"source_chunk_exceeded_{MAX_TOKENS}_tokens"
        output.append(item)
    return output, 1


def merge_records(
    left: dict[str, Any],
    right: dict[str, Any],
) -> dict[str, Any]:

    merged = deepcopy(left)
    merged_texts = [get_text(left), get_text(right)]
    merged["text"] = "\n\n".join(text for text in merged_texts if text)
    merged["token_count"] = count_tokens(merged["text"])

    for field in ("split_part", "split_total"):
        merged.pop(field, None)
    if left.get("split_reason") or right.get("split_reason"):
        merged["split_reason"] = "merged_after_oversize_split"

    merged["_source_chunk_ids"] = unique_values(
        record_source_ids(left) + record_source_ids(right)
    )

    for field in ("images", "source_blocks", "block_types", "tables", "equations"):
        values = unique_from_records([left, right], field)
        if values:
            merged[field] = values

    page_starts = [as_int(r.get("page_start")) for r in (left, right)]
    page_starts = [n for n in page_starts if n is not None]
    page_ends = [as_int(r.get("page_end")) for r in (left, right)]
    page_ends = [n for n in page_ends if n is not None]
    if page_starts:
        merged["page_start"] = min(page_starts)
    if page_ends:
        merged["page_end"] = max(page_ends)

    for field in ("has_image", "has_table", "has_equation"):
        merged[field] = any(bool(r.get(field)) for r in (left, right))
    if merged.get("images"):
        merged["has_image"] = True
        merged["image_count"] = len(merged["images"])

    merged["section_path"] = deepcopy(left.get("section_path"))
    return merged


def can_merge(
    left: dict[str, Any],
    right: dict[str, Any],
) -> bool:
    left_section = section_key(left)
    right_section = section_key(right)
    if left_section is None or right_section is None:
        return False
    if left_section != right_section:
        return False
    combined_text = "\n\n".join(
        t for t in (get_text(left), get_text(right)) if t
    )
    return count_tokens(combined_text) <= MAX_TOKENS


def adaptive_pack(
    records: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], int]:

    packed: list[dict[str, Any]] = []
    current: dict[str, Any] | None = None
    merge_operations = 0

    for record in records:
        if current is None:
            current = deepcopy(record)
            continue

        current_tokens = count_tokens(get_text(current))
        if current_tokens < TARGET_TOKENS and can_merge(current, record):
            candidate = merge_records(current, record)
            candidate_tokens = count_tokens(get_text(candidate))
            if candidate_tokens <= MAX_TOKENS:
                current = candidate
                merge_operations += 1
                continue

        packed.append(current)
        current = deepcopy(record)

    if current is not None:
        packed.append(current)

    if len(packed) >= 2:
        previous, trailing = packed[-2], packed[-1]
        if (
            count_tokens(get_text(trailing)) < MIN_TOKENS
            and can_merge(previous, trailing)
        ):
            candidate = merge_records(previous, trailing)
            if count_tokens(get_text(candidate)) <= MAX_TOKENS:
                packed[-2:] = [candidate]
                merge_operations += 1

    return packed, merge_operations


def load_records(
    path: Path,
) -> list[Any]:
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    if isinstance(data, list):
        return data
    if isinstance(data, dict):
        for key in ("chunks", "records", "items", "data"):
            value = data.get(key)
            if isinstance(value, list):
                return value
    raise ValueError(
        "Input JSON phải là list record hoặc object chứa list trong key "
        "'chunks', 'records', 'items' hoặc 'data'."
    )


def write_jsonl(
    path: Path,
    records: list[dict[str, Any]],
) -> None:
    with path.open("w", encoding="utf-8") as f:
        for record in records:
            f.write(json.dumps(record, ensure_ascii=False, default=str) + "\n")


def validate_output(
    records: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    issues: list[dict[str, Any]] = []
    seen_ids: set[str] = set()

    for index, record in enumerate(records, start=1):
        chunk_id = str(record.get("chunk_id", ""))
        tokens = count_tokens(get_text(record))
        if not chunk_id:
            issues.append({"type": "missing_chunk_id", "index": index})
        elif chunk_id in seen_ids:
            issues.append({"type": "duplicate_chunk_id", "chunk_id": chunk_id})
        seen_ids.add(chunk_id)

        if tokens != record.get("token_count"):
            issues.append({
                "type": "token_count_mismatch",
                "chunk_id": chunk_id,
                "stored": record.get("token_count"),
                "actual": tokens,
            })
        if tokens > MAX_TOKENS:
            issues.append({"type": "over_max_tokens", "chunk_id": chunk_id, "tokens": tokens})
        if section_key(record) is None and tokens < MIN_TOKENS:
            issues.append({
                "type": "under_min_without_section",
                "chunk_id": chunk_id,
                "tokens": tokens,
            })
    return issues


def build_stats(
    input_count: int,
    records: list[dict[str, Any]],
    split_count: int,
    merge_operations: int,
    errors: list[dict[str, Any]],
    validation_issues: list[dict[str, Any]],
) -> dict[str, Any]:
    token_counts = [count_tokens(get_text(r)) for r in records]
    below_min = sum(n < MIN_TOKENS for n in token_counts)
    within_range = sum(MIN_TOKENS <= n <= MAX_TOKENS for n in token_counts)
    above_max = sum(n > MAX_TOKENS for n in token_counts)

    return {
        "input_file": str(INPUT_PATH.relative_to(BASE_DIR)),
        "output_file": str(OUTPUT_PATH.relative_to(BASE_DIR)),
        "encoding": ENCODING_NAME,
        "config": {
            "min_tokens": MIN_TOKENS,
            "target_tokens": TARGET_TOKENS,
            "max_tokens": MAX_TOKENS,
        },
        "input_chunks": input_count,
        "output_chunks": len(records),
        "chunks_split": split_count,
        "merge_operations": merge_operations,
        "chunks_merged_from_multiple_sources": sum(
            len(record.get("source_chunk_ids", [])) > 1 for record in records
        ),
        "token_count": {
            "min": min(token_counts) if token_counts else 0,
            "max": max(token_counts) if token_counts else 0,
            "average": round(statistics.mean(token_counts), 2) if token_counts else 0,
            "below_min": below_min,
            "within_min_max": within_range,
            "above_max": above_max,
        },
        "input_errors": len(errors),
        "validation_issues": len(validation_issues),
        "notes": [
            "TARGET_TOKENS là mục tiêu, không phải giới hạn cứng.",
            "Chunk dưới MIN có thể vẫn tồn tại nếu không có chunk cùng section để ghép an toàn.",
            "Khi tách một chunk lớn, metadata như images được sao chép sang từng phần vì không thể suy ra vị trí tương ứng chỉ từ text đã ghép.",
        ],
    }


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    ERRORS_PATH.parent.mkdir(parents=True, exist_ok=True)

    if not INPUT_PATH.exists():
        raise FileNotFoundError(
            f"Không tìm thấy đầu vào: {INPUT_PATH}\n"
            "Hãy chạy Day 18 trước hoặc sửa INPUT_PATH ở đầu file."
        )

    raw_records = load_records(INPUT_PATH)
    errors: list[dict[str, Any]] = []
    normalized: list[dict[str, Any]] = []
    split_count = 0

    for index, raw in enumerate(raw_records):
        if not isinstance(raw, dict):
            errors.append({
                "record_index": index,
                "error": "record_not_object",
                "value_type": type(raw).__name__,
            })
            continue

        record = deepcopy(raw)
        record["text"] = get_text(record)
        if not record["text"] and not any(
            record.get(field) for field in ("images", "tables", "equations", "has_image", "has_table", "has_equation")
        ):
            errors.append({
                "record_index": index,
                "error": "empty_text_and_no_multimodal_metadata",
                "chunk_id": record.get("chunk_id", record.get("id")),
            })
            continue

        try:
            split_records, was_split = split_oversized_record(record)
            normalized.extend(split_records)
            split_count += was_split
        except Exception as exc:  # keep processing other records
            errors.append({
                "record_index": index,
                "error": "record_normalization_failed",
                "chunk_id": record.get("chunk_id", record.get("id")),
                "message": str(exc),
            })

    adaptive_records, merge_operations = adaptive_pack(normalized)

    final_records: list[dict[str, Any]] = []
    for index, record in enumerate(adaptive_records, start=1):
        final_record = deepcopy(record)
        final_record.pop("_source_chunk_ids", None)
        final_record["chunk_id"] = f"adaptive_{index:06d}"
        final_record["source_chunk_ids"] = record_source_ids(record)
        final_record["token_count"] = count_tokens(get_text(final_record))
        tokens = final_record["token_count"]
        if tokens < MIN_TOKENS:
            final_record["adaptive_status"] = "below_min_unmergeable_or_section_boundary"
        elif tokens < TARGET_TOKENS:
            final_record["adaptive_status"] = "valid_below_target"
        elif tokens <= MAX_TOKENS:
            final_record["adaptive_status"] = "valid_at_or_above_target"
        else:
            final_record["adaptive_status"] = "over_max_check_error"
        final_records.append(final_record)

    validation_issues = validate_output(final_records)
    stats = build_stats(
        input_count=len(raw_records),
        records=final_records,
        split_count=split_count,
        merge_operations=merge_operations,
        errors=errors,
        validation_issues=validation_issues,
    )

    with OUTPUT_PATH.open("w", encoding="utf-8") as f:
        json.dump(final_records, f, ensure_ascii=False, indent=2, default=str)
    with STATS_PATH.open("w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)
    write_jsonl(ERRORS_PATH, errors + validation_issues)

    LOGGER.info("Day 20 adaptive chunking hoàn tất")
    LOGGER.info("Input chunks : %s", len(raw_records))
    LOGGER.info("Output chunks: %s", len(final_records))
    LOGGER.info("Merged ops   : %s", merge_operations)
    LOGGER.info("Split chunks : %s", split_count)
    LOGGER.info("Token stats  : %s", stats["token_count"])
    LOGGER.info("Output       : %s", OUTPUT_PATH)
    LOGGER.info("Stats        : %s", STATS_PATH)
    LOGGER.info("Errors       : %s", ERRORS_PATH)


if __name__ == "__main__":
    main()
