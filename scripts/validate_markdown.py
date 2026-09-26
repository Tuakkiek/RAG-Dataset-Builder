from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


PAGE_RE = re.compile(r"^\s*<!--\s*page:\s*(\d+)\s*-->\s*$")
HEADING_RE = re.compile(r"^(#{1,6})\s+.+$")
INVALID_HEADING_RE = re.compile(r"^#{7,}\s+.+$")
FIGURE_RE = re.compile(r"^\s*\[FIGURE:", re.IGNORECASE)

FENCE_RE = re.compile(r"^\s*(`{3,}|~{3,})(.*)$")


def strip_unescaped_pipes(line: str) -> list[str]:
    """
    Split Markdown table columns on unescaped | characters.
    """
    cells = []
    current = []
    escaped = False

    for ch in line:
        if escaped:
            current.append(ch)
            escaped = False
            continue

        if ch == "\\":
            current.append(ch)
            escaped = True
            continue

        if ch == "|":
            cells.append("".join(current).strip())
            current = []
        else:
            current.append(ch)

    cells.append("".join(current).strip())

    # Remove optional empty edge cells caused by leading/trailing |
    if cells and cells[0] == "":
        cells = cells[1:]

    if cells and cells[-1] == "":
        cells = cells[:-1]

    return cells


def is_table_separator(line: str) -> bool:
    cells = strip_unescaped_pipes(line)

    if not cells:
        return False

    for cell in cells:
        cell = cell.strip()
        if not re.fullmatch(r":?-{3,}:?", cell):
            return False

    return True


def find_tables(lines: list[str]) -> list[dict]:
    """
    Detect Markdown tables outside fenced code blocks.
    """
    tables = []
    in_fence = False
    fence_char = None
    i = 0

    while i < len(lines):
        line = lines[i]
        fence = FENCE_RE.match(line)

        if fence:
            token = fence.group(1)
            char = token[0]

            if not in_fence:
                in_fence = True
                fence_char = char
            elif char == fence_char:
                in_fence = False
                fence_char = None

            i += 1
            continue

        if not in_fence and "|" in line and i + 1 < len(lines):
            separator = lines[i + 1]

            if is_table_separator(separator):
                header_cells = strip_unescaped_pipes(line)
                separator_cells = strip_unescaped_pipes(separator)

                table_rows = 2
                j = i + 2

                while j < len(lines):
                    row = lines[j]

                    if not row.strip():
                        break

                    if FENCE_RE.match(row):
                        break

                    if "|" not in row:
                        break

                    table_rows += 1
                    j += 1

                tables.append(
                    {
                        "start": i + 1,
                        "columns": len(header_cells),
                        "separator_columns": len(separator_cells),
                        "rows": table_rows,
                    }
                )

                i = j
                continue

        i += 1

    return tables


def validate_file(path: Path, expected_pages: int | None = None) -> bool:
    errors: list[str] = []
    warnings: list[str] = []

    if not path.exists():
        errors.append(f"FILE_NOT_FOUND: {path}")
        print("\nVALIDATION: FAIL")
        for error in errors:
            print(f"- {error}")
        return False

    if path.suffix.lower() != ".md":
        errors.append("INVALID_EXTENSION: file must have .md extension")

    if path.stat().st_size == 0:
        errors.append("EMPTY_FILE")

    if "data\\01_raw" in str(path).replace("/", "\\"):
        errors.append("WRONG_DIRECTORY: Markdown must not be inside data/01_raw/")

    try:
        text = path.read_text(encoding="utf-8-sig")
    except UnicodeDecodeError as exc:
        errors.append(f"UTF8_ERROR: {exc}")
        text = ""

    if "�" in text:
        warnings.append("REPLACEMENT_CHARACTER_FOUND: found Unicode replacement character '�'")

    lines = text.splitlines()

    # ---------------------------------------------------------
    # PAGE MARKERS
    # ---------------------------------------------------------
    page_numbers = []

    for line in lines:
        match = PAGE_RE.match(line)
        if match:
            page_numbers.append(int(match.group(1)))

    if not page_numbers:
        errors.append("PAGE_MARKER_MISSING")
    else:
        expected_sequence = list(range(1, page_numbers[-1] + 1))

        if page_numbers != expected_sequence:
            errors.append(
                f"PAGE_SEQUENCE_ERROR: found {page_numbers[:10]}..."
            )

        if expected_pages is not None:
            if len(page_numbers) != expected_pages:
                errors.append(
                    f"PAGE_COUNT_ERROR: expected {expected_pages}, "
                    f"found {len(page_numbers)}"
                )

            if page_numbers[-1] != expected_pages:
                errors.append(
                    f"LAST_PAGE_ERROR: expected {expected_pages}, "
                    f"found {page_numbers[-1]}"
                )

    # ---------------------------------------------------------
    # HEADING
    # ---------------------------------------------------------
    heading_count = 0
    invalid_heading_count = 0

    for line in lines:
        if HEADING_RE.match(line):
            heading_count += 1

        if INVALID_HEADING_RE.match(line):
            invalid_heading_count += 1

    if invalid_heading_count:
        errors.append(
            f"HEADING_LEVEL_ERROR: {invalid_heading_count} heading(s) exceed level 6"
        )

    # ---------------------------------------------------------
    # CODE FENCE
    # ---------------------------------------------------------
    fence_stack = []

    for line_number, line in enumerate(lines, start=1):
        match = FENCE_RE.match(line)

        if not match:
            continue

        token = match.group(1)
        char = token[0]

        if not fence_stack:
            fence_stack.append((char, len(token), line_number))
        else:
            open_char, open_len, _ = fence_stack[-1]

            if char == open_char and len(token) >= open_len:
                fence_stack.pop()

    if fence_stack:
        char, length, start_line = fence_stack[-1]
        errors.append(
            f"UNCLOSED_CODE_FENCE: opened at line {start_line}"
        )

    # ---------------------------------------------------------
    # DISPLAY FORMULA
    # ---------------------------------------------------------
    dollar_blocks = text.count("$$")

    if dollar_blocks % 2 != 0:
        errors.append(
            f"FORMULA_DELIMITER_ERROR: $$ count is odd ({dollar_blocks})"
        )

    # ---------------------------------------------------------
    # INLINE MATH
    # ---------------------------------------------------------
    inline_open = len(re.findall(r"\\\(", text))
    inline_close = len(re.findall(r"\\\)", text))

    if inline_open != inline_close:
        errors.append(
            f"INLINE_MATH_ERROR: \\( = {inline_open}, \\) = {inline_close}"
        )

    # ---------------------------------------------------------
    # FIGURES
    # ---------------------------------------------------------
    figure_count = sum(1 for line in lines if FIGURE_RE.match(line))

    # ---------------------------------------------------------
    # TABLES
    # ---------------------------------------------------------
    tables = find_tables(lines)

    for table in tables:
        if table["columns"] != table["separator_columns"]:
            errors.append(
                "TABLE_COLUMN_ERROR: "
                f"table starting line {table['start']} has "
                f"{table['columns']} header columns but "
                f"{table['separator_columns']} separator columns"
            )

    # ---------------------------------------------------------
    # BASIC CONTENT CHECKS
    # ---------------------------------------------------------
    if len(lines) < 10:
        warnings.append("VERY_SHORT_FILE")

    if not text.strip():
        errors.append("NO_TEXT_CONTENT")

    # ---------------------------------------------------------
    # REPORT
    # ---------------------------------------------------------
    print("=" * 70)
    print("MARKDOWN VALIDATION REPORT")
    print("=" * 70)

    print(f"File:            {path}")
    print(f"Size:            {path.stat().st_size:,} bytes")
    print(f"Lines:           {len(lines):,}")
    print(f"Page markers:    {len(page_numbers)}")
    print(f"Last page:       {page_numbers[-1] if page_numbers else 'N/A'}")
    print(f"Headings:        {heading_count}")
    print(f"Tables:          {len(tables)}")
    print(f"Figures:         {figure_count}")
    print(f"$$ delimiters:   {dollar_blocks}")
    print(f"Inline math:     \\( {inline_open} / \\) {inline_close}")
    print()

    if warnings:
        print("WARNINGS:")
        for warning in warnings:
            print(f"  ⚠ {warning}")
        print()

    if errors:
        print("ERRORS:")
        for error in errors:
            print(f"  ✗ {error}")
        print()
        print("VALIDATION: FAIL")
        return False

    print("VALIDATION: PASS")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate RAG Dataset Builder Markdown files."
    )

    parser.add_argument(
        "file",
        help="Path to Markdown file",
    )

    parser.add_argument(
        "--expected-pages",
        type=int,
        default=None,
        help="Expected number of physical PDF pages",
    )

    args = parser.parse_args()

    path = Path(args.file)

    success = validate_file(
        path=path,
        expected_pages=args.expected_pages,
    )

    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())