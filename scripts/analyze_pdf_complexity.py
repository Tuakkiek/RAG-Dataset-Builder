from __future__ import annotations

import argparse
import csv
import math
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable

import pymupdf


# ============================================================
# DATA MODEL
# ============================================================

@dataclass
class PdfAnalysis:
    relative_path: str
    filename: str

    status: str

    size_mb: float
    pages: int

    total_chars: int
    avg_chars_per_page: float

    total_images: int
    avg_images_per_page: float
    image_heavy_pages: int

    scanned_pages: int
    scanned_ratio: float

    low_text_pages: int
    low_text_ratio: float

    blank_pages: int

    multi_column_pages: int
    multi_column_ratio: float

    formula_proxy_count: int
    formula_proxy_per_page: float

    table_proxy_count: int
    table_proxy_per_page: float

    complexity_score: float
    complexity_level: str

    recommended_model: str
    recommended_effort: str
    recommended_batch_size: int

    recommended_stage: str


# ============================================================
# REGEX / HEURISTICS
# ============================================================

FORMULA_PATTERNS = [
    re.compile(r"[=≤≥≈≠∑∏√∫∂∞±×÷]"),
    re.compile(r"[α-ωΑ-ΩβΓΔΘΛΞΠΣΦΨΩ]"),
    re.compile(r"\b[A-Za-z]\s*[\^_]\s*[\{\[\(]?\w+"),
    re.compile(
        r"\b[A-Za-z][A-Za-z0-9_]*\s*=\s*[^.;]{2,}"
    ),
]

TABLE_PATTERNS = [
    re.compile(r"\t.*\t"),
    re.compile(r"(?:\S+\s{3,}){2,}\S+"),
    re.compile(r"\b(?:table|tbl\.)\s*\d+\b", re.IGNORECASE),
    re.compile(
        r"\b(?:mean|std|accuracy|precision|recall|f1|score)\b"
        r".*\b\d+(?:\.\d+)?\b",
        re.IGNORECASE,
    ),
]


# ============================================================
# GENERAL HELPERS
# ============================================================

def safe_mean(values: Iterable[float]) -> float:
    values = list(values)

    if not values:
        return 0.0

    return sum(values) / len(values)


def clamp(value: float, minimum: float, maximum: float) -> float:
    return max(minimum, min(maximum, value))


def count_formula_proxies(text: str) -> int:
    total = 0

    for pattern in FORMULA_PATTERNS:
        total += len(pattern.findall(text))

    return total


def count_table_proxies(text: str) -> int:
    total = 0

    for line in text.splitlines():
        line = line.strip()

        if not line:
            continue

        for pattern in TABLE_PATTERNS:
            if pattern.search(line):
                total += 1
                break

    return total


def is_low_text_page(text: str) -> bool:
    return len(text.strip()) < 150


def is_probably_scanned_page(text: str, image_count: int) -> bool:
    """
    Heuristic only.

    Very little extracted text + one or more images often indicates
    a scanned/image-based PDF page.
    """
    return len(text.strip()) < 80 and image_count > 0


# ============================================================
# MULTI-COLUMN DETECTION
# ============================================================

def detect_multi_column(blocks: list[tuple]) -> bool:
    """
    Heuristic detection of a two-column page.

    This is NOT a definitive layout detector.
    """

    candidates = []

    for block in blocks:
        if len(block) < 5:
            continue

        x0, y0, x1, y1, text = block[:5]

        if not isinstance(text, str):
            continue

        text = text.strip()

        if not text:
            continue

        width = max(1.0, x1 - x0)

        candidates.append(
            {
                "x0": x0,
                "y0": y0,
                "x1": x1,
                "y1": y1,
                "width": width,
                "text": text,
            }
        )

    if len(candidates) < 6:
        return False

    page_width = max(block["x1"] for block in candidates)

    # Ignore blocks spanning most of the page.
    candidates = [
        block
        for block in candidates
        if block["width"] < page_width * 0.65
    ]

    if len(candidates) < 6:
        return False

    left_blocks = [
        block
        for block in candidates
        if block["x0"] < page_width * 0.48
    ]

    right_blocks = [
        block
        for block in candidates
        if block["x0"] > page_width * 0.48
    ]

    if len(left_blocks) < 3 or len(right_blocks) < 3:
        return False

    # Check that left/right blocks are reasonably separated.
    separated_pairs = []

    for left in left_blocks:
        for right in right_blocks:
            if right["x0"] > left["x1"]:
                separated_pairs.append(
                    right["x0"] - left["x1"]
                )

    if not separated_pairs:
        return False

    minimum_gap = min(separated_pairs)

    return minimum_gap >= 5


# ============================================================
# COMPLEXITY SCORING
# ============================================================

def calculate_complexity_score(
    pages: int,
    size_mb: float,
    scanned_ratio: float,
    low_text_ratio: float,
    image_avg: float,
    image_heavy_ratio: float,
    multi_column_ratio: float,
    formula_count: int,
    table_count: int,
    blank_ratio: float,
) -> float:
    """
    Heuristic 0–100 complexity score.

    This score is intended for workflow planning only.
    It is NOT a scientific measure of document quality.
    """

    # --------------------------------------------------------
    # 1. Document length: max 25
    # --------------------------------------------------------

    page_score = clamp(
        (pages / 160.0) * 25.0,
        0,
        25,
    )

    # --------------------------------------------------------
    # 2. File size: max 8
    # --------------------------------------------------------

    size_score = clamp(
        (size_mb / 10.0) * 8.0,
        0,
        8,
    )

    # --------------------------------------------------------
    # 3. Scanned/OCR dependence: max 18
    # --------------------------------------------------------

    scan_score = scanned_ratio * 18.0

    # --------------------------------------------------------
    # 4. Low-text pages: max 5
    # --------------------------------------------------------

    low_text_score = low_text_ratio * 5.0

    # --------------------------------------------------------
    # 5. Images: max 8
    # --------------------------------------------------------

    image_score = clamp(
        (image_avg / 2.0) * 8.0,
        0,
        8,
    )

    # --------------------------------------------------------
    # 6. Image-heavy pages: max 3
    # --------------------------------------------------------

    image_heavy_score = image_heavy_ratio * 3.0

    # --------------------------------------------------------
    # 7. Multi-column layout: max 10
    # --------------------------------------------------------

    layout_score = multi_column_ratio * 10.0

    # --------------------------------------------------------
    # 8. Formula proxy: max 12
    # --------------------------------------------------------

    formula_per_page = formula_count / max(pages, 1)

    formula_score = clamp(
        (formula_per_page / 8.0) * 12.0,
        0,
        12,
    )

    # --------------------------------------------------------
    # 9. Table proxy: max 7
    # --------------------------------------------------------

    table_per_page = table_count / max(pages, 1)

    table_score = clamp(
        (table_per_page / 2.0) * 7.0,
        0,
        7,
    )

    # --------------------------------------------------------
    # 10. Blank pages: max 2
    # --------------------------------------------------------

    blank_score = clamp(
        blank_ratio * 2.0,
        0,
        2,
    )

    score = (
        page_score
        + size_score
        + scan_score
        + low_text_score
        + image_score
        + image_heavy_score
        + layout_score
        + formula_score
        + table_score
        + blank_score
    )

    return round(
        clamp(score, 0, 100),
        2,
    )


# ============================================================
# COMPLEXITY LEVEL
# ============================================================

def classify_complexity(score: float) -> str:
    if score >= 75:
        return "VERY_HARD"

    if score >= 55:
        return "HARD"

    if score >= 35:
        return "MEDIUM"

    return "EASY"


# ============================================================
# MODEL RECOMMENDATION
# ============================================================

def recommend_model(
    level: str,
    pages: int,
    scanned_ratio: float,
    multi_column_ratio: float,
    formula_count: int,
    image_avg: float,
) -> tuple[str, str, int]:
    """
    Workflow recommendation.

    Default:
        Sonnet 5 + High

    Escalate to:
        Opus 5 + High

    for harder documents.
    """

    formula_per_page = formula_count / max(pages, 1)

    if level == "VERY_HARD":
        return (
            "Opus 5",
            "High",
            1,
        )

    if level == "HARD":
        difficult_layout = (
            scanned_ratio >= 0.20
            or multi_column_ratio >= 0.35
            or formula_per_page >= 5
            or image_avg >= 1.5
        )

        if difficult_layout:
            return (
                "Opus 5",
                "High",
                1,
            )

        return (
            "Sonnet 5",
            "High",
            1,
        )

    if level == "MEDIUM":
        return (
            "Sonnet 5",
            "High",
            1 if pages > 80 else 2,
        )

    # EASY
    if pages <= 40:
        return (
            "Sonnet 5",
            "High",
            4,
        )

    return (
        "Sonnet 5",
        "High",
        2,
    )


def recommend_stage(
    level: str,
    model: str,
) -> str:
    if model == "Opus 5":
        return "OPUS_SINGLE"

    if level == "HARD":
        return "HARD_SINGLE"

    if level == "MEDIUM":
        return "MEDIUM_BATCH"

    return "EASY_BATCH"


# ============================================================
# PDF ANALYSIS
# ============================================================

def analyze_pdf(
    pdf_path: Path,
    raw_root: Path,
    status: str,
) -> PdfAnalysis:

    relative_path = pdf_path.relative_to(raw_root)

    size_mb = pdf_path.stat().st_size / (
        1024 * 1024
    )

    document = pymupdf.open(pdf_path)

    page_char_counts: list[int] = []
    page_image_counts: list[int] = []

    total_chars = 0
    total_images = 0

    scanned_pages = 0
    low_text_pages = 0
    blank_pages = 0
    multi_column_pages = 0
    image_heavy_pages = 0

    formula_proxy_count = 0
    table_proxy_count = 0

    for page in document:
        text = page.get_text("text") or ""

        chars = len(
            text.strip()
        )

        images = page.get_images(
            full=True
        )

        image_count = len(images)

        blocks = page.get_text(
            "blocks"
        )

        if detect_multi_column(
            blocks
        ):
            multi_column_pages += 1

        if is_probably_scanned_page(
            text,
            image_count,
        ):
            scanned_pages += 1

        if is_low_text_page(
            text
        ):
            low_text_pages += 1

        if chars == 0:
            blank_pages += 1

        if image_count >= 2:
            image_heavy_pages += 1

        formula_proxy_count += count_formula_proxies(
            text
        )

        table_proxy_count += count_table_proxies(
            text
        )

        total_chars += chars
        total_images += image_count

        page_char_counts.append(chars)
        page_image_counts.append(image_count)

    document.close()

    pages = len(page_char_counts)

    avg_chars_per_page = safe_mean(
        page_char_counts
    )

    avg_images_per_page = safe_mean(
        page_image_counts
    )

    scanned_ratio = (
        scanned_pages / max(pages, 1)
    )

    low_text_ratio = (
        low_text_pages / max(pages, 1)
    )

    multi_column_ratio = (
        multi_column_pages / max(pages, 1)
    )

    image_heavy_ratio = (
        image_heavy_pages / max(pages, 1)
    )

    formula_proxy_per_page = (
        formula_proxy_count / max(pages, 1)
    )

    table_proxy_per_page = (
        table_proxy_count / max(pages, 1)
    )

    blank_ratio = (
        blank_pages / max(pages, 1)
    )

    complexity_score = calculate_complexity_score(
        pages=pages,
        size_mb=size_mb,
        scanned_ratio=scanned_ratio,
        low_text_ratio=low_text_ratio,
        image_avg=avg_images_per_page,
        image_heavy_ratio=image_heavy_ratio,
        multi_column_ratio=multi_column_ratio,
        formula_count=formula_proxy_count,
        table_count=table_proxy_count,
        blank_ratio=blank_ratio,
    )

    complexity_level = classify_complexity(
        complexity_score
    )

    model, effort, batch_size = recommend_model(
        level=complexity_level,
        pages=pages,
        scanned_ratio=scanned_ratio,
        multi_column_ratio=multi_column_ratio,
        formula_count=formula_proxy_count,
        image_avg=avg_images_per_page,
    )

    stage = recommend_stage(
        level=complexity_level,
        model=model,
    )

    return PdfAnalysis(
        relative_path=str(relative_path),
        filename=pdf_path.name,
        status=status,
        size_mb=round(size_mb, 2),
        pages=pages,
        total_chars=total_chars,
        avg_chars_per_page=round(
            avg_chars_per_page,
            1,
        ),
        total_images=total_images,
        avg_images_per_page=round(
            avg_images_per_page,
            2,
        ),
        image_heavy_pages=image_heavy_pages,
        scanned_pages=scanned_pages,
        scanned_ratio=round(
            scanned_ratio,
            3,
        ),
        low_text_pages=low_text_pages,
        low_text_ratio=round(
            low_text_ratio,
            3,
        ),
        blank_pages=blank_pages,
        multi_column_pages=multi_column_pages,
        multi_column_ratio=round(
            multi_column_ratio,
            3,
        ),
        formula_proxy_count=formula_proxy_count,
        formula_proxy_per_page=round(
            formula_proxy_per_page,
            2,
        ),
        table_proxy_count=table_proxy_count,
        table_proxy_per_page=round(
            table_proxy_per_page,
            2,
        ),
        complexity_score=complexity_score,
        complexity_level=complexity_level,
        recommended_model=model,
        recommended_effort=effort,
        recommended_batch_size=batch_size,
        recommended_stage=stage,
    )


# ============================================================
# PDF ↔ MARKDOWN MAPPING
# ============================================================

def matching_markdown_path(
    pdf_path: Path,
    raw_root: Path,
    parsed_root: Path,
) -> Path:

    relative = pdf_path.relative_to(
        raw_root
    )

    return (
        parsed_root
        / relative.with_suffix(".md")
    )


# ============================================================
# BATCH BUILDER
# ============================================================

def build_batches(
    analyses: list[PdfAnalysis],
) -> list[list[PdfAnalysis]]:

    pending = [
        item
        for item in analyses
        if item.status == "PENDING"
    ]

    # Hardest first
    pending.sort(
        key=lambda item: (
            -item.complexity_score,
            -item.pages,
            item.filename.lower(),
        )
    )

    batches: list[list[PdfAnalysis]] = []

    easy_batch: list[PdfAnalysis] = []
    medium_batch: list[PdfAnalysis] = []

    for item in pending:

        # ----------------------------------------------------
        # VERY HARD / OPUS
        # ----------------------------------------------------

        if (
            item.complexity_level == "VERY_HARD"
            or item.recommended_model == "Opus 5"
        ):
            if easy_batch:
                batches.append(
                    easy_batch
                )
                easy_batch = []

            if medium_batch:
                batches.append(
                    medium_batch
                )
                medium_batch = []

            batches.append(
                [item]
            )

            continue

        # ----------------------------------------------------
        # HARD
        # ----------------------------------------------------

        if item.complexity_level == "HARD":
            if easy_batch:
                batches.append(
                    easy_batch
                )
                easy_batch = []

            if medium_batch:
                batches.append(
                    medium_batch
                )
                medium_batch = []

            batches.append(
                [item]
            )

            continue

        # ----------------------------------------------------
        # MEDIUM
        # ----------------------------------------------------

        if item.complexity_level == "MEDIUM":
            if easy_batch:
                batches.append(
                    easy_batch
                )
                easy_batch = []

            medium_batch.append(item)

            if len(medium_batch) == 2:
                batches.append(
                    medium_batch
                )
                medium_batch = []

            continue

        # ----------------------------------------------------
        # EASY
        # ----------------------------------------------------

        easy_batch.append(item)

        if len(easy_batch) == 4:
            batches.append(
                easy_batch
            )
            easy_batch = []

    if easy_batch:
        batches.append(
            easy_batch
        )

    if medium_batch:
        batches.append(
            medium_batch
        )

    return batches


# ============================================================
# CSV OUTPUT
# ============================================================

def save_csv_report(
    analyses: list[PdfAnalysis],
    output_path: Path,
) -> None:

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    rows = [
        asdict(item)
        for item in analyses
    ]

    if not rows:
        return

    fieldnames = list(
        rows[0].keys()
    )

    with output_path.open(
        "w",
        encoding="utf-8-sig",
        newline="",
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames,
        )

        writer.writeheader()
        writer.writerows(rows)


# ============================================================
# BATCH PLAN OUTPUT
# ============================================================

def save_batch_plan(
    batches: list[list[PdfAnalysis]],
    output_path: Path,
) -> None:

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with output_path.open(
        "w",
        encoding="utf-8",
    ) as file:

        file.write(
            "PDF → MARKDOWN BATCH PLAN\n"
        )

        file.write(
            "=" * 100 + "\n\n"
        )

        for index, batch in enumerate(
            batches,
            start=1,
        ):

            model = batch[0].recommended_model
            effort = batch[0].recommended_effort

            total_pages = sum(
                item.pages
                for item in batch
            )

            max_score = max(
                item.complexity_score
                for item in batch
            )

            file.write(
                f"BATCH {index}\n"
            )

            file.write(
                f"MODEL: {model}\n"
            )

            file.write(
                f"EFFORT: {effort}\n"
            )

            file.write(
                f"FILES: {len(batch)}\n"
            )

            file.write(
                f"TOTAL PAGES: {total_pages}\n"
            )

            file.write(
                f"MAX COMPLEXITY: {max_score}\n\n"
            )

            for number, item in enumerate(
                batch,
                start=1,
            ):

                file.write(
                    f"{number}. "
                    f"{item.filename}\n"
                )

                file.write(
                    f"   Pages: {item.pages}\n"
                )

                file.write(
                    f"   Size: {item.size_mb} MB\n"
                )

                file.write(
                    f"   Complexity: "
                    f"{item.complexity_score} "
                    f"({item.complexity_level})\n"
                )

                file.write(
                    f"   Model: "
                    f"{item.recommended_model}\n"
                )

                file.write(
                    f"   Batch size recommendation: "
                    f"{item.recommended_batch_size}\n"
                )

                file.write(
                    f"   Stage: "
                    f"{item.recommended_stage}\n"
                )

                file.write(
                    f"   Path: "
                    f"{item.relative_path}\n\n"
                )

            file.write(
                "-" * 100 + "\n\n"
            )


# ============================================================
# CONSOLE SUMMARY
# ============================================================

def print_summary(
    analyses: list[PdfAnalysis],
) -> None:

    total = len(analyses)

    done = sum(
        item.status == "DONE"
        for item in analyses
    )

    pending = sum(
        item.status == "PENDING"
        for item in analyses
    )

    in_progress = sum(
        item.status == "IN_PROGRESS"
        for item in analyses
    )

    print()
    print("=" * 110)
    print("PDF COMPLEXITY ANALYSIS")
    print("=" * 110)

    print(
        f"Total PDF          : {total}"
    )

    print(
        f"Already done       : {done}"
    )

    print(
        f"Pending            : {pending}"
    )

    print(
        f"In progress        : {in_progress}"
    )

    print()

    header = (
        f"{'Score':>7} "
        f"{'Level':<11} "
        f"{'Pages':>6} "
        f"{'SizeMB':>8} "
        f"{'Scan%':>7} "
        f"{'Cols%':>7} "
        f"{'Math/p':>8} "
        f"{'Img/p':>7} "
        f"{'Model':<10} "
        f"Filename"
    )

    print(header)
    print("-" * 110)

    sorted_items = sorted(
        analyses,
        key=lambda item: (
            -item.complexity_score,
            item.filename.lower(),
        ),
    )

    for item in sorted_items:

        print(
            f"{item.complexity_score:7.2f} "
            f"{item.complexity_level:<11} "
            f"{item.pages:6d} "
            f"{item.size_mb:8.2f} "
            f"{item.scanned_ratio * 100:7.1f} "
            f"{item.multi_column_ratio * 100:7.1f} "
            f"{item.formula_proxy_per_page:8.2f} "
            f"{item.avg_images_per_page:7.2f} "
            f"{item.recommended_model:<10} "
            f"{item.filename}"
        )


def print_batch_plan(
    batches: list[list[PdfAnalysis]],
) -> None:

    print()
    print("=" * 110)
    print("RECOMMENDED BATCH PLAN")
    print("=" * 110)

    for index, batch in enumerate(
        batches,
        start=1,
    ):

        total_pages = sum(
            item.pages
            for item in batch
        )

        print()
        print(
            f"BATCH {index} | "
            f"MODEL={batch[0].recommended_model} | "
            f"EFFORT={batch[0].recommended_effort} | "
            f"FILES={len(batch)} | "
            f"TOTAL_PAGES={total_pages}"
        )

        for number, item in enumerate(
            batch,
            start=1,
        ):

            print(
                f"  {number}. "
                f"[{item.complexity_score:5.1f}] "
                f"{item.complexity_level:<10} "
                f"{item.pages:4d} pages | "
                f"{item.filename}"
            )


# ============================================================
# CLI
# ============================================================

def parse_args() -> argparse.Namespace:

    parser = argparse.ArgumentParser(
        description=(
            "Analyze PDF complexity and "
            "recommend PDF → Markdown batches."
        )
    )

    parser.add_argument(
        "--root",
        default="data/01_raw/other-AI-resources",
        help="Root folder containing PDFs.",
    )

    parser.add_argument(
        "--parsed-root",
        default="data/02_parsed/other-AI-resources",
        help="Root folder containing Markdown files.",
    )

    parser.add_argument(
        "--csv",
        default="reports/pdf_complexity_analysis.csv",
        help="CSV output path.",
    )

    parser.add_argument(
        "--plan",
        default="reports/pdf_batch_plan.txt",
        help="Batch plan output path.",
    )

    parser.add_argument(
        "--pending-only",
        action="store_true",
        help="Only include PDFs without matching Markdown in the plan.",
    )

    parser.add_argument(
        "--exclude",
        action="append",
        default=[],
        help=(
            "Exclude a filename or filename fragment from "
            "batch planning. Can be repeated."
        ),
    )

    return parser.parse_args()


# ============================================================
# MAIN
# ============================================================

def main() -> int:

    args = parse_args()

    raw_root = Path(
        args.root
    ).resolve()

    parsed_root = Path(
        args.parsed_root
    ).resolve()

    if not raw_root.exists():
        print(
            f"ERROR: Raw root does not exist:\n"
            f"{raw_root}"
        )
        return 1

    pdf_files = sorted(
        raw_root.rglob("*.pdf"),
        key=lambda path: str(path).lower(),
    )

    if not pdf_files:
        print(
            f"ERROR: No PDF files found in:\n"
            f"{raw_root}"
        )
        return 1

    analyses: list[PdfAnalysis] = []

    for pdf_path in pdf_files:

        markdown_path = matching_markdown_path(
            pdf_path,
            raw_root,
            parsed_root,
        )

        if markdown_path.exists():

            status = "DONE"

        else:

            excluded = any(
                fragment.lower()
                in pdf_path.name.lower()
                for fragment in args.exclude
            )

            status = (
                "IN_PROGRESS"
                if excluded
                else "PENDING"
            )

        if (
            args.pending_only
            and status == "DONE"
        ):
            continue

        print(
            f"Analyzing: {pdf_path.name}"
        )

        analysis = analyze_pdf(
            pdf_path,
            raw_root,
            status,
        )

        analyses.append(
            analysis
        )

    # Only truly pending files go into batch planning.
    batches = build_batches(
        analyses
    )

    print_summary(
        analyses
    )

    print_batch_plan(
        batches
    )

    save_csv_report(
        analyses,
        Path(args.csv),
    )

    save_batch_plan(
        batches,
        Path(args.plan),
    )

    print()
    print("=" * 110)
    print("OUTPUT FILES")
    print("=" * 110)

    print(
        f"CSV : {args.csv}"
    )

    print(
        f"PLAN: {args.plan}"
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(
        main()
    )