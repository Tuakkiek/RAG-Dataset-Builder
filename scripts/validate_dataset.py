from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path


def collect_markdown_files(root: Path) -> list[Path]:
    """Recursively collect all Markdown files under root."""
    return sorted(
        path
        for path in root.rglob("*.md")
        if path.is_file()
    )


def run_validator(validator: Path, file_path: Path) -> tuple[int, str]:
    """
    Run validate_markdown.py for one file and return:
    (exit_code, output)
    """
    import subprocess

    command = [
        sys.executable,
        str(validator),
        str(file_path),
    ]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )

    output = result.stdout

    if result.stderr:
        output += "\n" + result.stderr

    return result.returncode, output


def extract_metrics(output: str) -> dict:
    """Extract key metrics from the single-file validator output."""
    metrics = {
        "pages": "",
        "last_page": "",
        "headings": "",
        "tables": "",
        "figures": "",
        "size_bytes": "",
        "lines": "",
        "status": "FAIL",
    }

    for line in output.splitlines():
        line = line.strip()

        if line.startswith("Size:"):
            metrics["size_bytes"] = line.split(":", 1)[1].strip()

        elif line.startswith("Lines:"):
            metrics["lines"] = line.split(":", 1)[1].strip()

        elif line.startswith("Page markers:"):
            metrics["pages"] = line.split(":", 1)[1].strip()

        elif line.startswith("Last page:"):
            metrics["last_page"] = line.split(":", 1)[1].strip()

        elif line.startswith("Headings:"):
            metrics["headings"] = line.split(":", 1)[1].strip()

        elif line.startswith("Tables:"):
            metrics["tables"] = line.split(":", 1)[1].strip()

        elif line.startswith("Figures:"):
            metrics["figures"] = line.split(":", 1)[1].strip()

        elif "VALIDATION: PASS" in line:
            metrics["status"] = "PASS"

        elif "VALIDATION: FAIL" in line:
            metrics["status"] = "FAIL"

    return metrics


def save_csv_report(report_path: Path, rows: list[dict]) -> None:
    """Save validation summary as CSV."""
    report_path.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = [
        "file",
        "status",
        "pages",
        "last_page",
        "headings",
        "tables",
        "figures",
        "lines",
        "size_bytes",
    ]

    with report_path.open(
        "w",
        encoding="utf-8-sig",
        newline="",
    ) as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate all Markdown files in data/02_parsed."
    )

    parser.add_argument(
        "--root",
        default="data/02_parsed",
        help="Root directory containing Markdown files.",
    )

    parser.add_argument(
        "--validator",
        default="scripts/validate_markdown.py",
        help="Path to single-file validator.",
    )

    parser.add_argument(
        "--report",
        default="reports/markdown_validation.csv",
        help="CSV report output path.",
    )

    args = parser.parse_args()

    root = Path(args.root)
    validator = Path(args.validator)
    report_path = Path(args.report)

    if not root.exists():
        print(f"ERROR: root directory not found: {root}")
        return 1

    if not validator.exists():
        print(f"ERROR: validator not found: {validator}")
        return 1

    files = collect_markdown_files(root)

    print("=" * 80)
    print("RAG DATASET MARKDOWN VALIDATION")
    print("=" * 80)
    print(f"Root:       {root}")
    print(f"Validator:  {validator}")
    print(f"Files found: {len(files)}")
    print()

    if not files:
        print("No Markdown files found.")
        return 1

    rows = []
    passed = 0
    failed = 0

    for index, file_path in enumerate(files, start=1):
        print(f"[{index}/{len(files)}] {file_path}")

        exit_code, output = run_validator(
            validator=validator,
            file_path=file_path,
        )

        metrics = extract_metrics(output)

        relative_path = file_path.relative_to(root)

        row = {
            "file": str(relative_path),
            **metrics,
        }

        rows.append(row)

        if exit_code == 0 and metrics["status"] == "PASS":
            passed += 1
            print("    STATUS: PASS")
        else:
            failed += 1
            print("    STATUS: FAIL")
            print()

            # Print the actual validator output for failed files.
            print(output)

        print()

    save_csv_report(report_path, rows)

    print("=" * 80)
    print("FINAL SUMMARY")
    print("=" * 80)
    print(f"Total files : {len(files)}")
    print(f"PASS        : {passed}")
    print(f"FAIL        : {failed}")
    print(f"Report      : {report_path}")
    print()

    if failed == 0:
        print("DATASET VALIDATION: PASS")
        return 0

    print("DATASET VALIDATION: FAIL")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())