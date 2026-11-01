# Các bước thử nghiệm chunking

Thư mục này lưu 19 script `day2.py` đến `day20.py` theo `road_map.md`. Ngày 1 là phần lý thuyết; ngày 21 được tổng hợp thành `src/chunk_dataset.py`.

Để chunk toàn bộ `data/mineru`, chạy chương trình hoàn chỉnh từ thư mục gốc dự án:

```powershell
.\.venv\Scripts\python.exe src\chunk_dataset.py --input data\mineru --output-dir data\chunked
```

Các script trong thư mục này chỉ phục vụ việc xem lại quá trình phát triển thuật toán. `day13.py` đến `day20.py` vẫn trỏ đến `data/processed` theo đường dẫn gốc dự án. `day2.py` đến `day12.py` dùng dữ liệu mẫu/đường dẫn tương đối cũ; hãy kiểm tra input trước khi chạy riêng lẻ. `day19.py` ghi vào `data/chunked`, nên sẽ thay các file output hiện có nếu chạy trực tiếp.
