from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


# ============================================================
# CHỈ CẦN THAY ĐỔI 2 BIẾN NÀY
# ============================================================

INPUT_DIR = Path(
    r"D:\RAG-Dataset-Builder\data\02_parsed\scientific-papers\TiengViet"
)

OUTPUT_DIR = Path(
    r"D:\RAG-Dataset-Builder\data\03_chunked\scientific-papers\TiengViet"
)


# ============================================================
# CẤU HÌNH CHUNK
# ============================================================

# Baseline ban đầu.
# Đây là số từ gần đúng, chưa phải tokenizer token thực.
CHUNK_SIZE = 500

# Có giữ lại nội dung heading trong chunk hay không.
INCLUDE_HEADINGS = True


# ============================================================
# REGEX
# ============================================================

HEADING_RE = re.compile(
    r"^(#{1,6})\s+(.+?)\s*$"
)

PAGE_RE = re.compile(
    r"^(?:<!--\s*page\s*:\s*([1-9]\d*)\s*-->)"
    r"|(?:\[\s*page\s*:\s*([1-9]\d*)\s*\])$",
    re.IGNORECASE,
)

UNORDERED_LIST_RE = re.compile(
    r"^\s*[-*+]\s+(.+?)\s*$"
)

ORDERED_LIST_RE = re.compile(
    r"^\s*\d+[.)]\s+(.+?)\s*$"
)

TABLE_SEPARATOR_RE = re.compile(
    r"^\s*\|?\s*:?-+:?\s*(\|\s*:?-+:?\s*)+\|?\s*$"
)


# ============================================================
# PUBLIC FUNCTION
# ============================================================

def process_directory(
    input_dir: Path,
    output_dir: Path,
) -> None:
    """
    Parse và chunk tất cả file Markdown trong input_dir.

    Mỗi file .md sẽ tạo ra một file .jsonl tương ứng.

    Ví dụ:

        abc.md
        ->
        abc.jsonl
    """

    if not input_dir.exists():
        raise FileNotFoundError(
            f"Input directory không tồn tại:\n{input_dir}"
        )

    if not input_dir.is_dir():
        raise NotADirectoryError(
            f"Input path không phải thư mục:\n{input_dir}"
        )

    output_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    markdown_files = sorted(
        input_dir.rglob("*.md")
    )

    if not markdown_files:
        print(
            f"Không tìm thấy file Markdown trong:\n{input_dir}"
        )
        return

    print("=" * 70)
    print("MARKDOWN -> STRUCTURED CHUNKS")
    print("=" * 70)
    print(f"Input : {input_dir}")
    print(f"Output: {output_dir}")
    print(f"Files : {len(markdown_files)}")
    print()

    success_count = 0
    error_count = 0

    for md_file in markdown_files:
        try:
            print(f"[PROCESS] {md_file.name}")

            document = parse_markdown(
                md_file
            )

            chunks = build_chunks(
                document
            )

            json_file = (
                output_dir
                / f"{md_file.stem}.json"
            )

            jsonl_file = (
                output_dir
                / f"{md_file.stem}.jsonl"
            )

            save_json(
                chunks,
                json_file,
            )

            save_jsonl(
                chunks,
                jsonl_file,
            )

            print(
                f"          -> {len(chunks)} chunks"
            )

            print(
                f"          -> {json_file.name}"
            )

            print(
                f"          -> {jsonl_file.name}"
            )
            print()

            success_count += 1

        except Exception as exc:
            error_count += 1

            print(
                f"[ERROR] {md_file.name}"
            )
            print(
                f"        {type(exc).__name__}: {exc}"
            )
            print()

    print("=" * 70)
    print("DONE")
    print("=" * 70)
    print(f"Success: {success_count}")
    print(f"Errors : {error_count}")
    print(f"Output : {output_dir}")


# ============================================================
# MARKDOWN PARSER
# ============================================================

def parse_markdown(
    path: Path,
) -> dict[str, Any]:

    text = path.read_text(
        encoding="utf-8"
    )

    return parse_markdown_text(
        text=text,
        document_name=path.name,
        document_id=make_document_id(path),
    )


def parse_markdown_text(
    text: str,
    document_name: str,
    document_id: str,
) -> dict[str, Any]:

    lines = (
        text
        .replace("\r\n", "\n")
        .replace("\r", "\n")
        .split("\n")
    )

    elements: list[dict[str, Any]] = []

    current_page: int | None = None

    current_chapter: str | None = None
    current_section: str | None = None
    current_subsection: str | None = None

    paragraph_buffer: list[str] = []

    i = 0

    while i < len(lines):

        line = lines[i]

        # ------------------------------------------------------
        # EMPTY LINE
        # ------------------------------------------------------

        if not line.strip():

            flush_paragraph(
                elements,
                paragraph_buffer,
                current_page,
                current_chapter,
                current_section,
                current_subsection,
            )

            i += 1
            continue

        # ------------------------------------------------------
        # PAGE MARKER
        # ------------------------------------------------------

        page = parse_page_marker(line)

        if page is not None:

            flush_paragraph(
                elements,
                paragraph_buffer,
                current_page,
                current_chapter,
                current_section,
                current_subsection,
            )

            current_page = page

            i += 1
            continue

        # ------------------------------------------------------
        # HEADING
        # ------------------------------------------------------

        heading_match = HEADING_RE.match(line)

        if heading_match:

            flush_paragraph(
                elements,
                paragraph_buffer,
                current_page,
                current_chapter,
                current_section,
                current_subsection,
            )

            level = len(
                heading_match.group(1)
            )

            heading_text = clean_inline_markdown(
                heading_match.group(2).strip()
            )

            (
                current_chapter,
                current_section,
                current_subsection,
            ) = update_hierarchy(
                level,
                heading_text,
                current_chapter,
                current_section,
                current_subsection,
            )

            elements.append(
                {
                    "type": "heading",
                    "text": heading_text,
                    "level": level,
                    "page": current_page,
                    "chapter": current_chapter,
                    "section": current_section,
                    "subsection": current_subsection,
                }
            )

            i += 1
            continue

        # ------------------------------------------------------
        # TABLE
        # ------------------------------------------------------

        if is_table_start(lines, i):

            flush_paragraph(
                elements,
                paragraph_buffer,
                current_page,
                current_chapter,
                current_section,
                current_subsection,
            )

            table, next_index = parse_table(
                lines,
                i,
            )

            elements.append(
                {
                    "type": "table",
                    "rows": table,
                    "page": current_page,
                    "chapter": current_chapter,
                    "section": current_section,
                    "subsection": current_subsection,
                }
            )

            i = next_index
            continue

        # ------------------------------------------------------
        # LIST
        # ------------------------------------------------------

        if is_list_item(line):

            flush_paragraph(
                elements,
                paragraph_buffer,
                current_page,
                current_chapter,
                current_section,
                current_subsection,
            )

            items: list[dict[str, Any]] = []

            while i < len(lines):

                item_line = lines[i]

                match = (
                    UNORDERED_LIST_RE.match(item_line)
                    or ORDERED_LIST_RE.match(item_line)
                )

                if not match:
                    break

                item_text = clean_inline_markdown(
                    match.group(1).strip()
                )

                items.append(
                    {
                        "type": "list_item",
                        "text": item_text,
                        "page": current_page,
                        "chapter": current_chapter,
                        "section": current_section,
                        "subsection": current_subsection,
                    }
                )

                i += 1

            elements.append(
                {
                    "type": "list",
                    "items": items,
                    "page": current_page,
                    "chapter": current_chapter,
                    "section": current_section,
                    "subsection": current_subsection,
                }
            )

            continue

        # ------------------------------------------------------
        # HTML COMMENT
        # ------------------------------------------------------

        if (
            line.strip().startswith("<!--")
            and line.strip().endswith("-->")
        ):
            i += 1
            continue

        # ------------------------------------------------------
        # PARAGRAPH
        # ------------------------------------------------------

        paragraph_buffer.append(
            line.strip()
        )

        i += 1

    # Flush cuối file.
    flush_paragraph(
        elements,
        paragraph_buffer,
        current_page,
        current_chapter,
        current_section,
        current_subsection,
    )

    return {
        "document_id": document_id,
        "document_name": document_name,
        "source_type": "markdown",
        "elements": elements,
    }


# ============================================================
# CHUNKING
# ============================================================

def build_chunks(
    document: dict[str, Any],
) -> list[dict[str, Any]]:

    elements = document["elements"]

    chunks: list[dict[str, Any]] = []

    current_text_parts: list[str] = []

    current_word_count = 0

    current_chapter: str | None = None
    current_section: str | None = None
    current_subsection: str | None = None

    page_start: int | None = None
    page_end: int | None = None

    chunk_index = 1

    for element in elements:

        element_type = element["type"]

        # ------------------------------------------------------
        # HEADING
        # ------------------------------------------------------

        if element_type == "heading":

            current_chapter = element.get(
                "chapter"
            )

            current_section = element.get(
                "section"
            )

            current_subsection = element.get(
                "subsection"
            )

            # Heading cấp cao thường là boundary tốt
            # để kết thúc chunk cũ.
            if current_text_parts:

                chunks.append(
                    create_chunk(
                        document,
                        current_text_parts,
                        chunk_index,
                        current_chapter,
                        current_section,
                        current_subsection,
                        page_start,
                        page_end,
                    )
                )

                chunk_index += 1

                current_text_parts = []
                current_word_count = 0

                page_start = None
                page_end = None

            if INCLUDE_HEADINGS:

                heading_text = element["text"]

                current_text_parts.append(
                    heading_text
                )

                current_word_count += count_words(
                    heading_text
                )

            continue

        # ------------------------------------------------------
        # PARAGRAPH
        # ------------------------------------------------------

        if element_type == "paragraph":

            text = element["text"]

            if not text.strip():
                continue

            words = count_words(text)

            # Nếu thêm paragraph mới vượt quá
            # CHUNK_SIZE thì đóng chunk hiện tại.
            if (
                current_text_parts
                and current_word_count + words
                > CHUNK_SIZE
            ):

                chunks.append(
                    create_chunk(
                        document,
                        current_text_parts,
                        chunk_index,
                        current_chapter,
                        current_section,
                        current_subsection,
                        page_start,
                        page_end,
                    )
                )

                chunk_index += 1

                current_text_parts = []
                current_word_count = 0

                page_start = None
                page_end = None

                # Giữ heading context cho chunk mới.
                if (
                    INCLUDE_HEADINGS
                    and current_subsection
                ):
                    current_text_parts.append(
                        current_subsection
                    )

                elif (
                    INCLUDE_HEADINGS
                    and current_section
                ):
                    current_text_parts.append(
                        current_section
                    )

                elif (
                    INCLUDE_HEADINGS
                    and current_chapter
                ):
                    current_text_parts.append(
                        current_chapter
                    )

            current_text_parts.append(text)

            current_word_count += words

            page = element.get("page")

            if page is not None:

                if page_start is None:
                    page_start = page

                page_end = page

            continue

        # ------------------------------------------------------
        # LIST
        # ------------------------------------------------------

        if element_type == "list":

            item_texts = [
                item["text"]
                for item in element.get(
                    "items",
                    [],
                )
            ]

            text = "\n".join(
                f"- {item}"
                for item in item_texts
            )

            words = count_words(text)

            if (
                current_text_parts
                and current_word_count + words
                > CHUNK_SIZE
            ):

                chunks.append(
                    create_chunk(
                        document,
                        current_text_parts,
                        chunk_index,
                        current_chapter,
                        current_section,
                        current_subsection,
                        page_start,
                        page_end,
                    )
                )

                chunk_index += 1

                current_text_parts = []
                current_word_count = 0

                page_start = None
                page_end = None

            current_text_parts.append(text)

            current_word_count += words

            page = element.get("page")

            if page is not None:

                if page_start is None:
                    page_start = page

                page_end = page

            continue

        # ------------------------------------------------------
        # TABLE
        # ------------------------------------------------------

        if element_type == "table":

            rows = element.get(
                "rows",
                [],
            )

            table_text = "\n".join(
                " | ".join(row)
                for row in rows
            )

            words = count_words(
                table_text
            )

            if (
                current_text_parts
                and current_word_count + words
                > CHUNK_SIZE
            ):

                chunks.append(
                    create_chunk(
                        document,
                        current_text_parts,
                        chunk_index,
                        current_chapter,
                        current_section,
                        current_subsection,
                        page_start,
                        page_end,
                    )
                )

                chunk_index += 1

                current_text_parts = []
                current_word_count = 0

                page_start = None
                page_end = None

            current_text_parts.append(
                table_text
            )

            current_word_count += words

            page = element.get("page")

            if page is not None:

                if page_start is None:
                    page_start = page

                page_end = page

    # ----------------------------------------------------------
    # FINAL CHUNK
    # ----------------------------------------------------------

    if current_text_parts:

        chunks.append(
            create_chunk(
                document,
                current_text_parts,
                chunk_index,
                current_chapter,
                current_section,
                current_subsection,
                page_start,
                page_end,
            )
        )

    return chunks


# ============================================================
# CHUNK CREATION
# ============================================================

def create_chunk(
    document: dict[str, Any],
    text_parts: list[str],
    chunk_index: int,
    chapter: str | None,
    section: str | None,
    subsection: str | None,
    page_start: int | None,
    page_end: int | None,
) -> dict[str, Any]:

    content = "\n\n".join(
        part.strip()
        for part in text_parts
        if part.strip()
    )

    chunk_id = (
        f"{document['document_id']}"
        f"_chunk_{chunk_index:05d}"
    )

    return {
        "chunk_id": chunk_id,
        "document_id": document["document_id"],
        "document_name": document["document_name"],
        "source_type": document["source_type"],
        "page_start": page_start,
        "page_end": page_end,
        "chapter": chapter,
        "section": section,
        "subsection": subsection,
        "content": content,
        "word_count": count_words(content),
    }


# ============================================================
# TABLE
# ============================================================

def is_table_start(
    lines: list[str],
    index: int,
) -> bool:

    if index + 1 >= len(lines):
        return False

    first = lines[index].strip()
    second = lines[index + 1].strip()

    if "|" not in first:
        return False

    return bool(
        TABLE_SEPARATOR_RE.match(second)
    )


def parse_table(
    lines: list[str],
    start_index: int,
) -> tuple[list[list[str]], int]:

    rows: list[list[str]] = []

    # Header
    rows.append(
        split_table_row(
            lines[start_index]
        )
    )

    index = start_index + 2

    while index < len(lines):

        line = lines[index]

        if not line.strip():
            break

        if "|" not in line:
            break

        rows.append(
            split_table_row(line)
        )

        index += 1

    return rows, index


def split_table_row(
    line: str,
) -> list[str]:

    text = line.strip()

    if text.startswith("|"):
        text = text[1:]

    if text.endswith("|"):
        text = text[:-1]

    cells = text.split("|")

    return [
        clean_inline_markdown(
            cell.strip()
        )
        for cell in cells
    ]


# ============================================================
# HEADING HIERARCHY
# ============================================================

def update_hierarchy(
    level: int,
    heading_text: str,
    chapter: str | None,
    section: str | None,
    subsection: str | None,
) -> tuple[
    str | None,
    str | None,
    str | None,
]:

    if level == 1:

        chapter = heading_text
        section = None
        subsection = None

    elif level == 2:

        section = heading_text
        subsection = None

    elif level == 3:

        subsection = heading_text

    return (
        chapter,
        section,
        subsection,
    )


# ============================================================
# PARAGRAPH
# ============================================================

def flush_paragraph(
    elements: list[dict[str, Any]],
    paragraph_buffer: list[str],
    page: int | None,
    chapter: str | None,
    section: str | None,
    subsection: str | None,
) -> None:

    if not paragraph_buffer:
        return

    text = " ".join(
        line.strip()
        for line in paragraph_buffer
        if line.strip()
    ).strip()

    paragraph_buffer.clear()

    if not text:
        return

    elements.append(
        {
            "type": "paragraph",
            "text": clean_inline_markdown(
                text
            ),
            "page": page,
            "chapter": chapter,
            "section": section,
            "subsection": subsection,
        }
    )


# ============================================================
# PAGE
# ============================================================

def parse_page_marker(
    line: str,
) -> int | None:

    match = PAGE_RE.match(
        line.strip()
    )

    if not match:
        return None

    value = (
        match.group(1)
        or match.group(2)
    )

    try:
        return int(value)

    except (TypeError, ValueError):
        return None


# ============================================================
# LIST
# ============================================================

def is_list_item(
    line: str,
) -> bool:

    return bool(
        UNORDERED_LIST_RE.match(line)
        or ORDERED_LIST_RE.match(line)
    )


# ============================================================
# INLINE MARKDOWN
# ============================================================

def clean_inline_markdown(
    text: str,
) -> str:

    result = text.strip()

    # Images
    result = re.sub(
        r"!\[([^\]]*)\]\([^)]+\)",
        r"\1",
        result,
    )

    # Links
    result = re.sub(
        r"\[([^\]]+)\]\([^)]+\)",
        r"\1",
        result,
    )

    # Inline code
    result = re.sub(
        r"`([^`]+)`",
        r"\1",
        result,
    )

    # Bold
    result = re.sub(
        r"\*\*(.*?)\*\*",
        r"\1",
        result,
    )

    result = re.sub(
        r"__(.*?)__",
        r"\1",
        result,
    )

    # Italic
    result = re.sub(
        r"(?<!\*)\*([^*]+)\*(?!\*)",
        r"\1",
        result,
    )

    result = re.sub(
        r"(?<!\w)_([^_]+)_(?!\w)",
        r"\1",
        result,
    )

    return result.strip()


# ============================================================
# UTILITY
# ============================================================

def count_words(
    text: str,
) -> int:

    return len(
        re.findall(
            r"\S+",
            text,
        )
    )


def make_document_id(
    path: Path,
) -> str:

    document_id = path.stem.strip()

    document_id = re.sub(
        r"\s+",
        "_",
        document_id,
    )

    document_id = re.sub(
        r"[^\w.-]",
        "_",
        document_id,
        flags=re.UNICODE,
    )

    return (
        document_id
        or "document"
    )


# ============================================================
# JSON and JSONL 
# ============================================================

def save_json(
    chunks: list[dict[str, Any]],
    output_file: Path,
) -> None:
    """
    Lưu toàn bộ chunks thành một JSON array.
    """
    output_file.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with output_file.open(
        "w",
        encoding="utf-8",
    ) as f:
        json.dump(
            chunks,
            f,
            ensure_ascii=False,
            indent=2,
        )


def save_jsonl(
    chunks: list[dict[str, Any]],
    output_file: Path,
) -> None:
    """
    Lưu chunks thành JSONL:
    mỗi dòng = một chunk.
    """
    output_file.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with output_file.open(
        "w",
        encoding="utf-8",
    ) as f:
        for chunk in chunks:
            f.write(
                json.dumps(
                    chunk,
                    ensure_ascii=False,
                )
                + "\n"
            )

# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":

    process_directory(
        INPUT_DIR,
        OUTPUT_DIR,
    )