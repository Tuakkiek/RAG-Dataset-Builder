import sys
from pathlib import Path
from docling.document_converter import DocumentConverter

# Fix encoding for Windows terminal
sys.stdout.reconfigure(encoding="utf-8")

converter = DocumentConverter()

data_dir = Path(__file__).parent.parent / "data"
pdf_files = list(data_dir.glob("*.pdf"))

if not pdf_files:
    raise FileNotFoundError(f"No PDF found in: {data_dir}")

pdf_path = pdf_files[0]
print(f"Processing: {pdf_path.name}")

result = converter.convert(str(pdf_path))

document = result.document

print(document)