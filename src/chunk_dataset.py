from __future__ import annotations

import argparse
import json
import logging
import math
import re
import statistics
from copy import deepcopy
from pathlib import Path
from typing import Any, Iterable

try:
    import tiktoken
except ImportError as exc:  # pragma: no cover - exercised on user machines
    raise SystemExit(
        "Thiếu thư viện tiktoken. Cài bằng lệnh: python -m pip install tiktoken"
    ) from exc


# =====================================================================
# 1. CONFIGURATION
# =====================================================================
BASE_DIR = Path(__file__).resolve().parent.parent
DEFAULT_INPUT = (
    BASE_DIR
    / "data"
    / "mineru"
    / "02_giao-trinh"
    / "vi"
    / "VI_TX_010_Machine Learning co ban"
    / "structured_content.json"
)
DEFAULT_OUTPUT_DIR = BASE_DIR / "data" / "chunked"

ENCODING_NAME = "cl100k_base"
MIN_TOKENS = 200
TARGET_TOKENS = 500
MAX_TOKENS = 800
PARENT_MAX_TOKENS = 1500

# These are page furniture / navigational elements, not retrieval content.
EXCLUDED_TYPES = {"header", "footer", "page_number", "index"}
HEADING_TYPES = {"doc_title", "paragraph_title"}
TEXT_TYPES = {"text", "ref_text", "page_footnote", "code"}
SPECIAL_TYPES = {"image", "chart", "table", "equation"}

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%H:%M:%S",
)
LOGGER = logging.getLogger("chunk_dataset")
ENCODING = tiktoken.get_encoding(ENCODING_NAME)


# =====================================================================
# 2. SMALL UTILITIES
# =====================================================================
def count_tokens(text: str) -> int:
    """Count tokens using the configured tokenizer."""
    return len(ENCODING.encode(text or ""))


def json_key(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, default=str)


def unique_items(items: Iterable[Any]) -> list[Any]:
    """Deduplicate JSON-compatible objects without changing their order."""
    result: list[Any] = []
    seen: set[str] = set()
    for item in items:
        key = json_key(item)
        if key not in seen:
            seen.add(key)
            result.append(item)
    return result


def as_int(value: Any) -> int | None:
    if value is None or isinstance(value, bool):
        return None
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def clean_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value.strip()
    return str(value).strip()


def get_captions(block: dict[str, Any]) -> list[str]:
    captions: list[str] = []
    raw = block.get("captions", [])
    if isinstance(raw, list):
        for item in raw:
            if isinstance(item, dict):
                value = clean_text(item.get("content"))
            else:
                value = clean_text(item)
            if value:
                captions.append(value)
    elif raw:
        value = clean_text(raw)
        if value:
            captions.append(value)
    return captions


def get_footnotes(block: dict[str, Any]) -> list[str]:
    footnotes: list[str] = []
    raw = block.get("footnotes", [])
    if isinstance(raw, list):
        for item in raw:
            if isinstance(item, dict):
                value = clean_text(item.get("content"))
            else:
                value = clean_text(item)
            if value:
                footnotes.append(value)
    return footnotes


def safe_relative_path(value: Any) -> str | None:
    value = clean_text(value)
    if not value:
        return None
    # Keep MinerU's relative path as-is; don't turn it into an absolute path.
    return value.replace("\\", "/")


# =====================================================================
# 3. LOADING
# =====================================================================
def load_structured_content(path: Path) -> dict[str, Any]:
    """Load a MinerU structured_content.json document."""
    if not path.exists():
        raise FileNotFoundError(
            f"Không tìm thấy structured_content.json: {path}\n"
            "Hãy kiểm tra INPUT_PATH hoặc truyền --input."
        )
    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, dict) or not isinstance(data.get("pages"), list):
        raise ValueError(
            "JSON đầu vào không đúng cấu trúc MinerU: cần object có key 'pages' dạng list."
        )
    return data


def flatten_pages(document: dict[str, Any]) -> list[dict[str, Any]]:
    """Flatten pages into blocks while preserving page and source order."""
    flattened: list[dict[str, Any]] = []
    for page in document.get("pages", []):
        if not isinstance(page, dict):
            continue
        page_idx = as_int(page.get("page_idx"))
        if page_idx is None:
            page_idx = len(flattened)
        blocks = page.get("blocks", [])
        if not isinstance(blocks, list):
            continue
        for source_index, block in enumerate(blocks):
            if not isinstance(block, dict):
                flattened.append({
                    "_invalid_value": block,
                    "page_idx": page_idx,
                    "source_index": source_index,
                })
                continue
            copied = deepcopy(block)
            copied["page_idx"] = page_idx
            copied["source_index"] = source_index
            flattened.append(copied)
    return flattened


# =====================================================================
# 4. SPECIAL BLOCKS: TABLE / EQUATION / IMAGE
# =====================================================================
def handle_table(block: dict[str, Any]) -> dict[str, Any]:
    """Convert a MinerU table to searchable markdown plus table metadata."""
    content = clean_text(block.get("content"))
    captions = get_captions(block)
    footnotes = get_footnotes(block)
    parts: list[str] = []
    if captions:
        parts.append("Table caption: " + " ".join(captions))
    if content:
        parts.append(content)
    if footnotes:
        parts.append("Table notes: " + " ".join(footnotes))

    image_path = safe_relative_path(block.get("image_source"))
    table_meta = {
        "page_idx": block.get("page_idx"),
        "source_index": block.get("source_index"),
        "caption": " ".join(captions) if captions else None,
        "row_count": (
            len(re.findall(r"<tr\b", content, flags=re.IGNORECASE))
            if re.search(r"<tr\b", content, flags=re.IGNORECASE)
            else sum(1 for line in content.splitlines() if "|" in line)
        ),
        "image_path": image_path,
    }
    return {
        "text": "\n\n".join(part for part in parts if part).strip(),
        "tables": [table_meta],
        "images": ([{
            "path": image_path,
            "caption": " ".join(captions),
            "kind": "table_render",
            "page_idx": block.get("page_idx"),
            "source_index": block.get("source_index"),
        }] if image_path else []),
    }


def handle_equation(block: dict[str, Any]) -> dict[str, Any]:
    """Keep the equation as LaTeX text; retain its optional rendered image ref."""
    latex = clean_text(block.get("content"))
    if latex:
        # Delimiters make the equation boundary explicit to downstream readers.
        text = "\\[\n" + latex + "\n\\]"
    else:
        text = ""
    image_path = safe_relative_path(block.get("image_source"))
    equation_meta = {
        "page_idx": block.get("page_idx"),
        "source_index": block.get("source_index"),
        "image_path": image_path,
    }
    return {"text": text, "equations": [equation_meta], "images": []}


def handle_image(block: dict[str, Any]) -> dict[str, Any]:
    """Keep image/chart captions in text and the image path in metadata only."""
    captions = get_captions(block)
    footnotes = get_footnotes(block)
    parts: list[str] = []
    if captions:
        parts.append("Image caption: " + " ".join(captions))
    if footnotes:
        parts.append("Image notes: " + " ".join(footnotes))
    image_path = safe_relative_path(block.get("image_source"))
    image_meta = {
        "path": image_path,
        "caption": " ".join(captions) if captions else "",
        "kind": clean_text(block.get("type")) or "image",
        "page_idx": block.get("page_idx"),
        "source_index": block.get("source_index"),
    }
    images = [image_meta] if image_path else []
    return {"text": "\n\n".join(parts).strip(), "images": images}


# =====================================================================
# 5. NORMALIZATION AND FILTERING
# =====================================================================
def normalize_block(block: dict[str, Any], section_path: list[str]) -> dict[str, Any] | None:
    """Map one raw MinerU block to a common internal block representation."""
    block_type = clean_text(block.get("type")).lower()
    if not block_type:
        return None

    page_idx = as_int(block.get("page_idx"))
    source_index = as_int(block.get("source_index"))
    bbox = block.get("bbox") if isinstance(block.get("bbox"), list) else None

    if block_type == "table":
        special = handle_table(block)
        text = special["text"]
        tables = special.get("tables", [])
        images = special.get("images", [])
        equations: list[dict[str, Any]] = []
    elif block_type == "equation":
        special = handle_equation(block)
        text = special["text"]
        tables = []
        images = special.get("images", [])
        equations = special.get("equations", [])
    elif block_type in {"image", "chart"}:
        special = handle_image(block)
        text = special["text"]
        tables = []
        images = special.get("images", [])
        equations = []
    else:
        text = clean_text(block.get("content"))
        tables = []
        images = []
        equations = []

    # Preserve code formatting exactly as supplied by MinerU.
    if block_type == "code" and text and not text.startswith("```"):
        text = "```\n" + text + "\n```"

    source_ref = {
        "page_idx": page_idx,
        "source_index": source_index,
        "type": block_type,
    }
    if bbox is not None:
        source_ref["bbox"] = bbox

    # Image/chart without caption still carries metadata. It will be attached
    # to an adjacent text-bearing chunk rather than exported as empty text.
    if not text and not (images or tables or equations):
        return None

    heading_level = as_int(block.get("level"))
    if heading_level is None and block_type in HEADING_TYPES:
        heading_level = 1 if block_type == "doc_title" else 2

    return {
        "type": block_type,
        "text": text,
        "page_idx": page_idx,
        "source_index": source_index,
        "section_path": list(section_path) if section_path else ["__root__"],
        "heading_level": heading_level,
        "continues_prev": bool(block.get("continues_prev", False)),
        "source_blocks": [source_ref],
        "block_types": [block_type],
        "images": images,
        "tables": tables,
        "equations": equations,
        "has_image": bool(images),
        "has_table": bool(tables) or block_type == "table",
        "has_equation": bool(equations) or block_type == "equation",
    }


def filter_blocks(
    blocks: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], dict[str, int], list[dict[str, Any]]]:
    """Remove page furniture and collect counts / malformed block errors."""
    kept: list[dict[str, Any]] = []
    filtered_counts: dict[str, int] = {}
    errors: list[dict[str, Any]] = []

    for block in blocks:
        if "_invalid_value" in block:
            errors.append({
                "stage": "filter",
                "error": "block_not_object",
                "page_idx": block.get("page_idx"),
                "source_index": block.get("source_index"),
                "value_type": type(block["_invalid_value"]).__name__,
            })
            continue
        block_type = clean_text(block.get("type")).lower()
        if block_type in EXCLUDED_TYPES:
            filtered_counts[block_type] = filtered_counts.get(block_type, 0) + 1
            continue
        if not block_type:
            errors.append({
                "stage": "filter",
                "error": "missing_block_type",
                "page_idx": block.get("page_idx"),
                "source_index": block.get("source_index"),
            })
            continue
        kept.append(block)
    return kept, filtered_counts, errors


# =====================================================================
# 6. HEADING HIERARCHY
# =====================================================================
def infer_heading_level(block: dict[str, Any]) -> int:
    level = as_int(block.get("level"))
    if level is not None and level > 0:
        return min(level, 12)
    content = clean_text(block.get("content"))
    match = re.match(r"^\s*(\d+(?:\.\d+)*)\b", content)
    if match:
        return min(match.group(1).count(".") + 1, 12)
    return 1 if block.get("type") == "doc_title" else 2


def update_heading_stack(
    heading_stack: list[dict[str, Any]], block: dict[str, Any]
) -> list[str]:
    """Update hierarchical path when a MinerU title block is encountered."""
    block_type = clean_text(block.get("type")).lower()
    if block_type in HEADING_TYPES:
        title = clean_text(block.get("content"))
        if title:
            level = infer_heading_level(block)
            while heading_stack and heading_stack[-1]["level"] >= level:
                heading_stack.pop()
            heading_stack.append({"level": level, "title": title})
    return [item["title"] for item in heading_stack] or ["__root__"]


# =====================================================================
# 7. TOKEN-AWARE TEXT SPLITTING
# =====================================================================
def _largest_char_prefix(text: str, start: int, max_tokens: int) -> int:
    low, high = start + 1, len(text)
    best = start
    while low <= high:
        mid = (low + high) // 2
        if count_tokens(text[start:mid]) <= max_tokens:
            best = mid
            low = mid + 1
        else:
            high = mid - 1
    return best if best > start else min(start + 1, len(text))


def _natural_boundary(text: str, start: int, max_end: int) -> int:
    if max_end >= len(text):
        return max_end
    lower = start + max(1, int((max_end - start) * 0.72))
    candidates = [
        text.rfind("\n\n", lower, max_end),
        text.rfind("\n", lower, max_end),
        text.rfind(". ", lower, max_end),
        text.rfind("! ", lower, max_end),
        text.rfind("? ", lower, max_end),
        text.rfind("; ", lower, max_end),
        text.rfind(" ", lower, max_end),
    ]
    valid = [pos for pos in candidates if pos > start]
    if not valid:
        return max_end
    pos = max(valid)
    if text[pos:pos + 2] == "\n\n":
        return min(pos + 2, max_end)
    return min(pos + (2 if text[pos:pos + 2] in {". ", "! ", "? ", "; "} else 1), max_end)


def split_text_by_tokens(text: str, max_tokens: int) -> list[str]:
    """Split oversized text, preferring paragraph/sentence/word boundaries."""
    text = text.strip()
    if not text:
        return []
    if count_tokens(text) <= max_tokens:
        return [text]

    pieces: list[str] = []
    start = 0
    while start < len(text):
        while start < len(text) and text[start].isspace():
            start += 1
        if start >= len(text):
            break
        max_end = _largest_char_prefix(text, start, max_tokens)
        end = _natural_boundary(text, start, max_end)
        piece = text[start:end].strip()
        while piece and count_tokens(piece) > max_tokens and end > start + 1:
            end -= 1
            piece = text[start:end].strip()
        if not piece:
            end = max(start + 1, end)
            piece = text[start:end].strip()
        pieces.append(piece)
        start = end

    # Defensive postcondition: every non-empty piece must fit the configured max.
    result: list[str] = []
    for piece in pieces:
        if count_tokens(piece) > max_tokens and len(piece) > 1:
            mid = len(piece) // 2
            result.extend(split_text_by_tokens(piece[:mid], max_tokens))
            result.extend(split_text_by_tokens(piece[mid:], max_tokens))
        else:
            result.append(piece)
    return [piece for piece in result if piece]


def split_table_content(text: str, max_tokens: int) -> list[str]:
    """Split Markdown or HTML tables by rows and repeat the header row."""
    # MinerU may serialize tables as HTML (including embedded <img> tags).
    html_match = re.search(r"(<table\b[^>]*>)(.*?)(</table>)", text, flags=re.IGNORECASE | re.DOTALL)
    if html_match:
        prefix = text[:html_match.start()].strip()
        opening, body, closing = html_match.group(1), html_match.group(2), html_match.group(3)
        rows = re.findall(r"<tr\b[^>]*>.*?</tr>", body, flags=re.IGNORECASE | re.DOTALL)
        if rows:
            header = rows[0]
            data_rows = rows[1:]
            pieces: list[str] = []
            current_rows: list[str] = []
            for row in data_rows:
                candidate_rows = current_rows + [row]
                candidate_table = opening + header + "".join(candidate_rows) + closing
                candidate = (prefix + "\n\n" if prefix else "") + candidate_table
                if current_rows and count_tokens(candidate) > max_tokens:
                    table_html = opening + header + "".join(current_rows) + closing
                    pieces.append((prefix + "\n\n" if prefix and not pieces else "") + table_html)
                    current_rows = [row]
                else:
                    current_rows.append(row)
            if current_rows:
                table_html = opening + header + "".join(current_rows) + closing
                pieces.append((prefix + "\n\n" if prefix and not pieces else "") + table_html)
            final: list[str] = []
            for piece in pieces:
                if count_tokens(piece) <= max_tokens:
                    final.append(piece)
                else:
                    # A single oversized row/cell is an exceptional fallback.
                    final.extend(split_text_by_tokens(piece, max_tokens))
            return final or split_text_by_tokens(text, max_tokens)

    # Markdown table fallback.
    lines = [line.rstrip() for line in text.splitlines() if line.strip()]
    table_start = next((i for i, line in enumerate(lines) if "|" in line), None)
    if table_start is None or table_start + 1 >= len(lines) or "|" not in lines[table_start + 1]:
        return split_text_by_tokens(text, max_tokens)

    prefix = "\n".join(lines[:table_start]).strip()
    header = lines[table_start]
    separator = lines[table_start + 1]
    rows = lines[table_start + 2:]
    header_text = "\n".join([header, separator])

    pieces = []
    current_rows: list[str] = []
    for row in rows:
        candidate_rows = current_rows + [row]
        candidate = "\n".join(([prefix] if prefix else []) + [header_text] + candidate_rows)
        if current_rows and count_tokens(candidate) > max_tokens:
            piece = "\n".join(([prefix] if prefix and not pieces else []) + [header_text] + current_rows)
            pieces.append(piece)
            current_rows = [row]
        else:
            current_rows.append(row)

    if current_rows:
        piece = "\n".join(([prefix] if prefix and not pieces else []) + [header_text] + current_rows)
        pieces.append(piece)

    final = []
    for piece in pieces:
        if count_tokens(piece) <= max_tokens:
            final.append(piece)
        else:
            final.extend(split_text_by_tokens(piece, max_tokens))
    return final or split_text_by_tokens(text, max_tokens)


# =====================================================================
# 8. SEMANTIC GROUPING AND CHUNK SPLITTING
# =====================================================================
def group_blocks(blocks: list[dict[str, Any]]) -> list[list[dict[str, Any]]]:
    """Group sequential blocks by section path; page changes are not boundaries."""
    groups: list[list[dict[str, Any]]] = []
    current: list[dict[str, Any]] = []
    current_key: str | None = None

    for block in blocks:
        key = json_key(block.get("section_path") or ["__root__"])
        if current and key != current_key:
            groups.append(current)
            current = []
        current.append(block)
        current_key = key

    if current:
        groups.append(current)
    return groups


def _metadata_only_unit(unit: dict[str, Any]) -> bool:
    return not clean_text(unit.get("text")) and bool(
        unit.get("images") or unit.get("tables") or unit.get("equations")
    )


def _split_unit(unit: dict[str, Any], errors: list[dict[str, Any]]) -> list[dict[str, Any]]:
    text = clean_text(unit.get("text"))
    if not text or count_tokens(text) <= MAX_TOKENS:
        copied = deepcopy(unit)
        copied["text"] = text
        copied["token_count"] = count_tokens(text)
        return [copied]

    if unit.get("type") == "table":
        pieces = split_table_content(text, MAX_TOKENS)
    else:
        pieces = split_text_by_tokens(text, MAX_TOKENS)

    errors.append({
        "stage": "split_group",
        "severity": "warning",
        "warning": "oversized_source_block_split",
        "page_idx": unit.get("page_idx"),
        "source_index": unit.get("source_index"),
        "block_type": unit.get("type"),
        "original_tokens": count_tokens(text),
        "piece_count": len(pieces),
        "note": "Metadata của block được gắn vào các phần tách để không mất tham chiếu; có thể lặp image/table ref.",
    })

    output: list[dict[str, Any]] = []
    for index, piece in enumerate(pieces, start=1):
        copied = deepcopy(unit)
        copied["text"] = piece
        copied["token_count"] = count_tokens(piece)
        copied["split_part"] = index
        copied["split_total"] = len(pieces)
        output.append(copied)
    return output


def _empty_chunk(section_path: list[str]) -> dict[str, Any]:
    return {
        "text": "",
        "section_path": deepcopy(section_path),
        "page_indices": [],
        "block_types": [],
        "images": [],
        "tables": [],
        "equations": [],
        "source_blocks": [],
        "has_image": False,
        "has_table": False,
        "has_equation": False,
    }


def _add_unit_to_chunk(chunk: dict[str, Any], unit: dict[str, Any]) -> None:
    unit_text = clean_text(unit.get("text"))
    if unit_text:
        if chunk["text"]:
            separator = " " if unit.get("continues_prev") else "\n\n"
            chunk["text"] += separator + unit_text
        else:
            chunk["text"] = unit_text

    if unit.get("page_idx") is not None:
        chunk["page_indices"].append(unit["page_idx"])
    chunk["block_types"].extend(unit.get("block_types", []))
    chunk["source_blocks"].extend(unit.get("source_blocks", []))
    chunk["images"].extend(unit.get("images", []))
    chunk["tables"].extend(unit.get("tables", []))
    chunk["equations"].extend(unit.get("equations", []))
    chunk["has_image"] = chunk["has_image"] or bool(unit.get("has_image"))
    chunk["has_table"] = chunk["has_table"] or bool(unit.get("has_table"))
    chunk["has_equation"] = chunk["has_equation"] or bool(unit.get("has_equation"))


def _finalize_chunk(chunk: dict[str, Any]) -> dict[str, Any] | None:
    text = clean_text(chunk.get("text"))
    if not text:
        return None
    pages = [as_int(value) for value in chunk.get("page_indices", [])]
    pages = [value for value in pages if value is not None]
    output = deepcopy(chunk)
    output["text"] = text
    output["page_start"] = min(pages) if pages else None
    output["page_end"] = max(pages) if pages else None
    output["token_count"] = count_tokens(text)
    output["block_types"] = list(output.get("block_types", []))
    output["images"] = unique_items(output.get("images", []))
    output["tables"] = unique_items(output.get("tables", []))
    output["equations"] = unique_items(output.get("equations", []))
    output["source_blocks"] = unique_items(output.get("source_blocks", []))
    output["has_image"] = bool(output["images"]) or bool(output.get("has_image"))
    output["has_table"] = bool(output["tables"]) or bool(output.get("has_table"))
    output["has_equation"] = bool(output["equations"]) or bool(output.get("has_equation"))
    output["image_count"] = len(output["images"])
    output.pop("page_indices", None)
    return output


def _merge_chunk_drafts(left: dict[str, Any], right: dict[str, Any]) -> dict[str, Any]:
    merged = deepcopy(left)
    merged["text"] = "\n\n".join(
        value for value in (clean_text(left.get("text")), clean_text(right.get("text"))) if value
    )
    for field in ("page_indices", "block_types", "images", "tables", "equations", "source_blocks"):
        merged[field] = list(left.get(field, [])) + list(right.get(field, []))
    for field in ("has_image", "has_table", "has_equation"):
        merged[field] = bool(left.get(field)) or bool(right.get(field))
    return merged


def split_group(
    group: list[dict[str, Any]], errors: list[dict[str, Any]], counters: dict[str, int]
) -> list[dict[str, Any]]:
    """Adaptive chunking within one section, preserving block order."""
    if not group:
        return []
    section_path = group[0].get("section_path") or ["__root__"]

    units: list[dict[str, Any]] = []
    for unit in group:
        units.extend(_split_unit(unit, errors))

    drafts: list[dict[str, Any]] = []
    current = _empty_chunk(section_path)
    pending_metadata: list[dict[str, Any]] = []

    for unit in units:
        if _metadata_only_unit(unit):
            if current["text"]:
                _add_unit_to_chunk(current, unit)
            else:
                pending_metadata.append(unit)
            continue

        unit_text = clean_text(unit.get("text"))
        if not unit_text:
            continue

        if not current["text"]:
            for pending in pending_metadata:
                _add_unit_to_chunk(current, pending)
            pending_metadata.clear()
            _add_unit_to_chunk(current, unit)
            continue

        candidate_text = current["text"] + (" " if unit.get("continues_prev") else "\n\n") + unit_text
        candidate_tokens = count_tokens(candidate_text)
        current_tokens = count_tokens(current["text"])

        should_append = candidate_tokens <= TARGET_TOKENS
        # If current is still too short, grow it toward MIN/TARGET as long as
        # the hard maximum is respected.
        if current_tokens < MIN_TOKENS and candidate_tokens <= MAX_TOKENS:
            should_append = True

        if should_append and candidate_tokens <= MAX_TOKENS:
            _add_unit_to_chunk(current, unit)
        else:
            finalized = _finalize_chunk(current)
            if finalized:
                drafts.append(finalized)
            current = _empty_chunk(section_path)
            for pending in pending_metadata:
                _add_unit_to_chunk(current, pending)
            pending_metadata.clear()
            _add_unit_to_chunk(current, unit)

    finalized = _finalize_chunk(current)
    if finalized:
        drafts.append(finalized)

    # Metadata-only blocks at the tail attach to the nearest preceding chunk.
    if pending_metadata:
        if drafts:
            draft = drafts[-1]
            for pending in pending_metadata:
                draft["images"] = unique_items(draft.get("images", []) + pending.get("images", []))
                draft["tables"] = unique_items(draft.get("tables", []) + pending.get("tables", []))
                draft["equations"] = unique_items(draft.get("equations", []) + pending.get("equations", []))
                draft["source_blocks"] = unique_items(draft.get("source_blocks", []) + pending.get("source_blocks", []))
                if pending.get("page_idx") is not None:
                    pages = [p for p in (draft.get("page_start"), draft.get("page_end"), pending.get("page_idx")) if p is not None]
                    draft["page_start"], draft["page_end"] = min(pages), max(pages)
                draft["has_image"] = bool(draft.get("images")) or bool(draft.get("has_image"))
                draft["has_table"] = bool(draft.get("tables")) or bool(draft.get("has_table"))
                draft["has_equation"] = bool(draft.get("equations")) or bool(draft.get("has_equation"))
                draft["image_count"] = len(draft.get("images", []))
        else:
            for pending in pending_metadata:
                errors.append({
                    "stage": "split_group",
                    "severity": "warning",
                    "warning": "metadata_only_block_without_text_neighbor",
                    "page_idx": pending.get("page_idx"),
                    "source_index": pending.get("source_index"),
                    "block_type": pending.get("type"),
                })

    # Repair a small tail by merging backward, but never cross section/MAX.
    if len(drafts) >= 2:
        previous, trailing = drafts[-2], drafts[-1]
        combined = previous["text"] + "\n\n" + trailing["text"]
        if (
            trailing["token_count"] < MIN_TOKENS
            and previous["section_path"] == trailing["section_path"]
            and count_tokens(combined) <= MAX_TOKENS
        ):
            left_draft = {
                **previous,
                "page_indices": [previous.get("page_start"), previous.get("page_end")],
            }
            right_draft = {
                **trailing,
                "page_indices": [trailing.get("page_start"), trailing.get("page_end")],
            }
            merged = _merge_chunk_drafts(left_draft, right_draft)
            finalized_merged = _finalize_chunk(merged)
            if finalized_merged:
                drafts[-2:] = [finalized_merged]
                counters["merge_operations"] += 1

    counters["split_groups"] += 1
    return drafts


# =====================================================================
# 9. ADAPTIVE CHILD CHUNKS -> PARENT CHUNKS
# =====================================================================
def _section_key(record: dict[str, Any]) -> str:
    return json_key(record.get("section_path") or ["__root__"])


def _new_parent_draft(section_path: list[str]) -> dict[str, Any]:
    return {
        "text": "",
        "section_path": deepcopy(section_path),
        "child_ids": [],
        "child_count": 0,
        "page_starts": [],
        "page_ends": [],
        "block_types": [],
        "images": [],
        "tables": [],
        "equations": [],
        "source_blocks": [],
        "has_image": False,
        "has_table": False,
        "has_equation": False,
    }


def build_parent_child(
    child_drafts: list[dict[str, Any]],
    doc_id: str,
    document_title: str,
    source_file: str,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Assign child IDs and group adjacent children into <=1500-token parents."""
    children: list[dict[str, Any]] = []
    for index, draft in enumerate(child_drafts, start=1):
        child = deepcopy(draft)
        child["chunk_id"] = f"{doc_id}_C{index:06d}"
        child["parent_id"] = None  # filled when parent membership is known
        child["doc_id"] = doc_id
        child["document_title"] = document_title
        child["source_file"] = source_file
        child["token_count"] = count_tokens(child["text"])
        child["adaptive_status"] = (
            "below_min_unmergeable_or_section_boundary"
            if child["token_count"] < MIN_TOKENS
            else "valid_below_target"
            if child["token_count"] < TARGET_TOKENS
            else "valid_at_or_above_target"
        )
        children.append(child)

    parent_drafts: list[dict[str, Any]] = []
    current: dict[str, Any] | None = None
    for child in children:
        child_tokens = count_tokens(child["text"])
        if current is None:
            current = _new_parent_draft(child["section_path"])
        candidate_text = (current["text"] + "\n\n" + child["text"]).strip() if current["text"] else child["text"]
        same_section = _section_key({"section_path": current["section_path"]}) == _section_key(child)
        if current["text"] and (not same_section or count_tokens(candidate_text) > PARENT_MAX_TOKENS):
            parent_drafts.append(current)
            current = _new_parent_draft(child["section_path"])

        current["text"] = (current["text"] + "\n\n" + child["text"]).strip() if current["text"] else child["text"]
        current["child_ids"].append(child["chunk_id"])
        current["child_count"] += 1
        if child.get("page_start") is not None:
            current["page_starts"].append(child["page_start"])
        if child.get("page_end") is not None:
            current["page_ends"].append(child["page_end"])
        current["block_types"].extend(child.get("block_types", []))
        current["images"].extend(child.get("images", []))
        current["tables"].extend(child.get("tables", []))
        current["equations"].extend(child.get("equations", []))
        current["source_blocks"].extend(child.get("source_blocks", []))
        for flag in ("has_image", "has_table", "has_equation"):
            current[flag] = bool(current.get(flag)) or bool(child.get(flag))

        # A single child should already be <= MAX_TOKENS (< parent max).
        if child_tokens > PARENT_MAX_TOKENS:
            raise ValueError(f"Child {child['chunk_id']} vượt giới hạn Parent.")

    if current is not None and current["child_ids"]:
        parent_drafts.append(current)

    parents: list[dict[str, Any]] = []
    child_to_parent: dict[str, str] = {}
    for index, draft in enumerate(parent_drafts, start=1):
        parent_id = f"{doc_id}_P{index:06d}"
        for child_id in draft["child_ids"]:
            child_to_parent[child_id] = parent_id
        pages_start = draft["page_starts"]
        pages_end = draft["page_ends"]
        parent = {
            "parent_id": parent_id,
            "doc_id": doc_id,
            "document_title": document_title,
            "section_path": draft["section_path"],
            "page_start": min(pages_start) if pages_start else None,
            "page_end": max(pages_end) if pages_end else None,
            "text": draft["text"],
            "token_count": count_tokens(draft["text"]),
            "child_ids": draft["child_ids"],
            "child_count": draft["child_count"],
            "block_types": draft["block_types"],
            "images": unique_items(draft["images"]),
            "tables": unique_items(draft["tables"]),
            "equations": unique_items(draft["equations"]),
            "source_blocks": unique_items(draft["source_blocks"]),
            "has_image": bool(draft["images"]) or draft["has_image"],
            "has_table": bool(draft["tables"]) or draft["has_table"],
            "has_equation": bool(draft["equations"]) or draft["has_equation"],
            "source_file": source_file,
        }
        parents.append(parent)

    for child in children:
        child["parent_id"] = child_to_parent[child["chunk_id"]]
    return children, parents


# =====================================================================
# 10. VALIDATION
# =====================================================================
def validate_chunk(
    chunks: list[dict[str, Any]],
    parents: list[dict[str, Any]],
    input_dir: Path,
) -> list[dict[str, Any]]:
    """Validate required chunk fields and Parent/Child referential integrity."""
    issues: list[dict[str, Any]] = []
    chunk_ids: set[str] = set()
    parent_ids = {str(parent.get("parent_id")) for parent in parents}

    for chunk in chunks:
        chunk_id = str(chunk.get("chunk_id", ""))
        text = clean_text(chunk.get("text"))
        actual_tokens = count_tokens(text)
        if not text:
            issues.append({"severity": "error", "error": "empty_text", "chunk_id": chunk_id})
        if not chunk_id:
            issues.append({"severity": "error", "error": "missing_chunk_id"})
        elif chunk_id in chunk_ids:
            issues.append({"severity": "error", "error": "duplicate_chunk_id", "chunk_id": chunk_id})
        chunk_ids.add(chunk_id)
        if not chunk.get("doc_id"):
            issues.append({"severity": "error", "error": "missing_doc_id", "chunk_id": chunk_id})
        if actual_tokens != chunk.get("token_count"):
            issues.append({
                "severity": "error", "error": "token_count_mismatch", "chunk_id": chunk_id,
                "stored": chunk.get("token_count"), "actual": actual_tokens,
            })
        if actual_tokens > MAX_TOKENS:
            issues.append({"severity": "error", "error": "over_max_tokens", "chunk_id": chunk_id, "tokens": actual_tokens})
        if not isinstance(chunk.get("section_path"), list) or not chunk.get("section_path"):
            issues.append({"severity": "warning", "warning": "missing_section_path", "chunk_id": chunk_id})
        page_start, page_end = as_int(chunk.get("page_start")), as_int(chunk.get("page_end"))
        if page_start is not None and page_end is not None and page_start > page_end:
            issues.append({"severity": "error", "error": "invalid_page_range", "chunk_id": chunk_id})
        if chunk.get("parent_id") not in parent_ids:
            issues.append({"severity": "error", "error": "orphan_child", "chunk_id": chunk_id, "parent_id": chunk.get("parent_id")})

        # The actual image path is relative to the folder containing structured_content.json.
        for image_meta in chunk.get("images", []):
            image_path = clean_text(image_meta.get("path")) if isinstance(image_meta, dict) else ""
            if image_path and not (input_dir / Path(image_path)).exists():
                issues.append({
                    "severity": "warning", "warning": "image_path_not_found",
                    "chunk_id": chunk_id, "image_path": image_path,
                })

        # Check table content only when MinerU extracted rows as text.
        # A table may instead be represented by an image ref and have row_count=0.
        table_row_count = max(
            [as_int(item.get("row_count")) or 0 for item in chunk.get("tables", []) if isinstance(item, dict)]
            or [0]
        )
        if table_row_count > 0 and not (
            "|" in text or re.search(r"<table\b|<tr\b", text, flags=re.IGNORECASE)
        ):
            issues.append({"severity": "warning", "warning": "table_header_not_detected", "chunk_id": chunk_id})

    for parent in parents:
        parent_id = str(parent.get("parent_id", ""))
        if count_tokens(parent.get("text", "")) > PARENT_MAX_TOKENS:
            issues.append({"severity": "error", "error": "parent_over_max_tokens", "parent_id": parent_id})
        for child_id in parent.get("child_ids", []):
            if child_id not in chunk_ids:
                issues.append({"severity": "error", "error": "parent_references_missing_child", "parent_id": parent_id, "child_id": child_id})

    return issues


# =====================================================================
# 11. EXPORT
# =====================================================================
def write_jsonl(path: Path, records: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8") as file:
        for record in records:
            file.write(json.dumps(record, ensure_ascii=False, default=str) + "\n")


def write_json(path: Path, payload: dict[str, Any]) -> None:
    with path.open("w", encoding="utf-8") as file:
        json.dump(payload, file, ensure_ascii=False, indent=2, default=str)


def build_stats(
    input_path: Path,
    raw_block_count: int,
    kept_block_count: int,
    filtered_counts: dict[str, int],
    chunks: list[dict[str, Any]],
    parents: list[dict[str, Any]],
    errors: list[dict[str, Any]],
    counters: dict[str, int],
) -> dict[str, Any]:
    token_counts = [int(chunk.get("token_count", 0)) for chunk in chunks]
    parent_counts = [int(parent.get("token_count", 0)) for parent in parents]
    return {
        "pipeline": "chunk_dataset.py",
        "source_file": input_path.name,
        "encoding": ENCODING_NAME,
        "config": {
            "min_tokens": MIN_TOKENS,
            "target_tokens": TARGET_TOKENS,
            "max_tokens": MAX_TOKENS,
            "parent_max_tokens": PARENT_MAX_TOKENS,
            "excluded_types": sorted(EXCLUDED_TYPES),
        },
        "blocks": {
            "raw": raw_block_count,
            "kept_after_filter": kept_block_count,
            "filtered_by_type": filtered_counts,
        },
        "chunks": {
            "child_count": len(chunks),
            "parent_count": len(parents),
            "split_groups": counters.get("split_groups", 0),
            "merge_operations": counters.get("merge_operations", 0),
            "token_count": {
                "min": min(token_counts) if token_counts else 0,
                "max": max(token_counts) if token_counts else 0,
                "average": round(statistics.mean(token_counts), 2) if token_counts else 0,
                "below_min": sum(value < MIN_TOKENS for value in token_counts),
                "within_min_max": sum(MIN_TOKENS <= value <= MAX_TOKENS for value in token_counts),
                "above_max": sum(value > MAX_TOKENS for value in token_counts),
            },
            "parent_token_count": {
                "min": min(parent_counts) if parent_counts else 0,
                "max": max(parent_counts) if parent_counts else 0,
                "average": round(statistics.mean(parent_counts), 2) if parent_counts else 0,
            },
            "with_image": sum(bool(chunk.get("has_image")) for chunk in chunks),
            "with_table": sum(bool(chunk.get("has_table")) for chunk in chunks),
            "with_equation": sum(bool(chunk.get("has_equation")) for chunk in chunks),
        },
        "errors_and_warnings": len(errors),
        "notes": [
            "TARGET_TOKENS là mục tiêu, không phải kích thước bắt buộc.",
            "Chunk dưới MIN_TOKENS có thể được giữ lại nếu không thể ghép mà không vượt section hoặc MAX_TOKENS.",
            "Page boundary không tự động kết thúc chunk; section boundary thì có.",
            "Image path được lưu trong metadata, không chèn đường dẫn ảnh vào text embedding.",
            "Table được giữ dạng Markdown; khi tách bảng lớn, header được lặp lại theo từng phần nếu nhận diện được cấu trúc Markdown.",
        ],
    }


# =====================================================================
# 12. MAIN PIPELINE
# =====================================================================
def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build MinerU RAG chunks with a unified pipeline.")
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT, help="Path to MinerU structured_content.json")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR, help="Directory for JSONL and stats outputs")
    parser.add_argument("--doc-id", default="VI_TX_010", help="Stable document identifier")
    parser.add_argument("--doc-title", default=None, help="Override title stored in structured_content metadata")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    input_path: Path = args.input.expanduser().resolve()
    output_dir: Path = args.output_dir.expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    chunks_path = output_dir / "chunks.jsonl"
    parents_path = output_dir / "parents.jsonl"
    stats_path = output_dir / "chunk_stats.json"
    errors_path = output_dir / "errors.jsonl"

    LOGGER.info("Loading MinerU document: %s", input_path)
    document = load_structured_content(input_path)
    raw_blocks = flatten_pages(document)
    filtered_blocks, filtered_counts, errors = filter_blocks(raw_blocks)

    metadata = document.get("metadata", {})
    doc_metadata = metadata.get("document", {}) if isinstance(metadata, dict) else {}
    document_title = args.doc_title or clean_text(doc_metadata.get("title")) or input_path.parent.name
    doc_id = re.sub(r"[^A-Za-z0-9_-]+", "_", clean_text(args.doc_id)) or "DOC"
    source_file = input_path.name

    LOGGER.info("Blocks: raw=%d, after filter=%d", len(raw_blocks), len(filtered_blocks))

    # Build heading hierarchy before converting each block to internal form.
    heading_stack: list[dict[str, Any]] = []
    normalized_blocks: list[dict[str, Any]] = []
    for block in filtered_blocks:
        section_path = update_heading_stack(heading_stack, block)
        try:
            normalized = normalize_block(block, section_path)
            if normalized is not None:
                normalized_blocks.append(normalized)
        except Exception as exc:
            errors.append({
                "stage": "normalization",
                "error": "block_normalization_failed",
                "page_idx": block.get("page_idx"),
                "source_index": block.get("source_index"),
                "block_type": block.get("type"),
                "message": str(exc),
            })

    LOGGER.info("Normalized blocks: %d", len(normalized_blocks))

    groups = group_blocks(normalized_blocks)
    counters = {"split_groups": 0, "merge_operations": 0}
    child_drafts: list[dict[str, Any]] = []
    for group in groups:
        try:
            child_drafts.extend(split_group(group, errors, counters))
        except Exception as exc:
            errors.append({
                "stage": "chunking",
                "error": "section_group_failed",
                "section_path": group[0].get("section_path") if group else None,
                "message": str(exc),
            })

    children, parents = build_parent_child(
        child_drafts=child_drafts,
        doc_id=doc_id,
        document_title=document_title,
        source_file=source_file,
    )

    validation_issues = validate_chunk(children, parents, input_path.parent)
    errors.extend(validation_issues)

    write_jsonl(chunks_path, children)
    write_jsonl(parents_path, parents)
    write_jsonl(errors_path, errors)

    stats = build_stats(
        input_path=input_path,
        raw_block_count=len(raw_blocks),
        kept_block_count=len(filtered_blocks),
        filtered_counts=filtered_counts,
        chunks=children,
        parents=parents,
        errors=errors,
        counters=counters,
    )
    stats["document"] = {"doc_id": doc_id, "document_title": document_title}
    stats["output_files"] = {
        "chunks": str(chunks_path),
        "parents": str(parents_path),
        "stats": str(stats_path),
        "errors": str(errors_path),
    }
    write_json(stats_path, stats)

    error_count = sum(1 for item in errors if item.get("severity") == "error" or "error" in item)
    warning_count = len(errors) - error_count
    LOGGER.info("Pipeline completed")
    LOGGER.info("Child chunks : %d", len(children))
    LOGGER.info("Parent chunks: %d", len(parents))
    LOGGER.info("Token range  : %s", stats["chunks"]["token_count"])
    LOGGER.info("Errors       : %d | Warnings: %d", error_count, warning_count)
    LOGGER.info("Chunks       : %s", chunks_path)
    LOGGER.info("Parents      : %s", parents_path)
    LOGGER.info("Stats        : %s", stats_path)
    LOGGER.info("Errors       : %s", errors_path)


if __name__ == "__main__":
    main()
