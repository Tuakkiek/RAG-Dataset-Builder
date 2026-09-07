import json
from docling.document_converter import DocumentConverter

converter = DocumentConverter()

# 1. ĐỌC FILE NÀY (Nhớ giữ chữ 'r' ở đầu)
duong_dan_doc = r"D:\GITHUB\RAG-Dataset-Builder\test-docling\tzan\giao-trinh-xu-ly-anh.pdf"
result = converter.convert(duong_dan_doc) 

# Lấy nội dung tài liệu dưới dạng Dictionary (từ điển Python)
noi_dung_dict = result.document.export_to_dict()

# 2. CHỈ ĐỊNH VỊ TRÍ LƯU FILE JSON
duong_dan_luu = r"D:\GITHUB\RAG-Dataset-Builder\test-docling\tzan\ket_qua.json"

# Mở file và ghi dữ liệu JSON
with open(duong_dan_luu, "w", encoding="utf-8") as file:
    # indent=4 giúp định dạng file JSON thụt lề cho dễ đọc
    # ensure_ascii=False giúp hiển thị đúng tiếng Việt hoặc ký tự đặc biệt
    json.dump(noi_dung_dict, file, indent=4, ensure_ascii=False)

print(f"Đã chuyển đổi và lưu thành công JSON vào: {duong_dan_luu}")