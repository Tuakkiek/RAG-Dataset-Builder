from docling.document_converter import DocumentConverter

converter = DocumentConverter()

# 1. ĐỌC FILE NÀY:
# Nhớ thêm chữ 'r' ở đầu chuỗi để tránh lỗi đường dẫn trên Windows
duong_dan_doc = r"D:\GITHUB\RAG-Dataset-Builder\test-docling\data\4.-Artificial-intelligence-and-Privacy-Author-Datatilsynet.pdf"
result = converter.convert(duong_dan_doc) 

# Lấy nội dung văn bản dưới dạng Markdown
noi_dung = result.document.export_to_markdown()

# 2. CHỈ ĐỊNH VỊ TRÍ LƯU FILE KẾT QUẢ
# Điền đường dẫn đầy đủ tới thư mục bạn muốn lưu + tên file (nhớ thêm chữ 'r' ở đầu)
# Ví dụ mình lưu luôn vào cùng thư mục data:
duong_dan_luu = r"D:\GITHUB\RAG-Dataset-Builder\test-docling\data\ket_qua.md"

# Mở file tại vị trí đã chỉ định và ghi nội dung vào
with open(duong_dan_luu, "w", encoding="utf-8") as file:
    file.write(noi_dung)

print(f"Đã chuyển đổi và lưu thành công vào: {duong_dan_luu}")