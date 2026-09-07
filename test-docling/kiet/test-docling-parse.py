import sys
from pathlib import Path
from docling.document_converter import DocumentConverter

sys.stdout.reconfigure(encoding="utf-8")

converter = DocumentConverter()

data_dir = Path(__file__).parent.parent / "data"

pdf_path = data_dir / "Học sâu – chẩn đoán bệnh phổi thông qua hình ảnh X-quang.pdf"

if not pdf_path.exists():
    raise FileNotFoundError(f"PDF not found: {pdf_path}")

print(f"Processing: {pdf_path.name}")

result = converter.convert(str(pdf_path))

document = result.document

output_path = data_dir / "ket_qua_Học sâu – chẩn đoán bệnh phổi thông qua hình ảnh X-quang.json"

output_path.write_text(
    document.model_dump_json(indent=2),
    encoding="utf-8"
)

print("Done!")
print(f"Saved to: {output_path}")