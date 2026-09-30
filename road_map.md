# ROADMAP 21 NGÀY — TỰ XÂY DỰNG `chunk_dataset.py` CHO DỮ LIỆU MINERU

> Mục tiêu: sau 21 ngày có thể viết được một chương trình Python đọc dữ liệu MinerU, phân tích cấu trúc tài liệu, chia chunk theo ngữ nghĩa/cấu trúc, giữ metadata trang–tiêu đề–bảng–công thức–ảnh, và xuất dataset dùng cho RAG.
>
> Nguyên tắc:
> 1. Không bắt đầu bằng LangChain/LlamaIndex.
> 2. Hiểu nguyên lý trước rồi mới code.
> 3. Mỗi ngày chỉ thêm một lớp phức tạp.
> 4. Luôn giữ phiên bản cũ để benchmark.
> 5. Không kết luận chunk size tối ưu nếu chưa đo.

---

# 0. KẾT QUẢ CUỐI CÙNG CẦN ĐẠT

Pipeline cuối:

```text
MinerU output
    │
    ├── structured_content.json
    ├── markdown.md
    └── images/
            │
            ▼
      Load document
            │
            ▼
      Normalize blocks
            │
            ▼
      Remove noise
            │
            ▼
      Build heading hierarchy
            │
            ▼
      Group semantic blocks
            │
            ▼
      Split oversized groups
            │
            ▼
      Parent / Child chunks
            │
            ▼
      Attach metadata
            │
            ├── page_start
            ├── page_end
            ├── section_path
            ├── image_refs
            ├── has_table
            ├── has_equation
            └── source
            │
            ▼
      Validation
            │
            ▼
      chunks.jsonl
```

File cuối:

```text
chunk_dataset.py
```

Input:

```text
data/mineru/
```

Output:

```text
data/chunked/
├── chunks.jsonl
├── parents.jsonl
├── chunk_stats.json
└── errors.jsonl
```

---

# PHASE 1 — HIỂU DỮ LIỆU VÀ PYTHON CƠ BẢN

## DAY 1 — Hiểu bài toán chunking

### Mục tiêu
Hiểu:
- chunk là gì;
- vì sao RAG cần chunk;
- chunk khác page thế nào;
- chunk size ảnh hưởng retrieval ra sao;
- overlap để làm gì;
- vì sao không nên cắt văn bản tùy ý.

### Cần hiểu

```text
Document
    ↓
Section
    ↓
Chunk
```

Chunk không đồng nghĩa với trang PDF.

Một chunk tốt cần:
- đủ ngữ cảnh;
- không quá dài;
- tránh cắt giữa câu;
- biết tài liệu nguồn;
- biết section;
- biết trang.

### Bài tập
Tự trả lời:
1. Tại sao không dùng `1 trang = 1 chunk`?
2. Chunk 100 token có nhược điểm gì?
3. Chunk 2000 token có nhược điểm gì?
4. Overlap có lợi gì?
5. Metadata có cần embedding không?

### Output
`notes/day01_chunking.md`

---

## DAY 2 — Ôn Python cần thiết

### Học
- `list`
- `dict`
- `for`
- `if`
- function
- `pathlib.Path`
- UTF-8
- JSON
- JSONL
- exception

### Code tay

```python
import json
from pathlib import Path

path = Path("sample.json")

with path.open("r", encoding="utf-8") as f:
    data = json.load(f)
```

Tập dùng:

```python
block["type"]
block.get("content", "")
```

### Bài tập
Viết `inspect_json.py` in:
- số trang;
- tổng block;
- các loại block;
- số lượng mỗi loại.

### Output
`inspect_json.py`

---

## DAY 3 — Hiểu `structured_content.json`

### Mục tiêu
Hiểu chính xác dữ liệu MinerU trước khi chunk.

### Việc cần làm
Dùng 1 tài liệu duy nhất và xem:
- `page_idx`
- `blocks`
- `type`
- `content`
- `level`
- `image_source`
- caption
- table
- equation

### Tạo bảng ghi chú

| type | Ý nghĩa | Giữ? | Embedding? |
|---|---|---:|---:|
| text | đoạn văn | yes | yes |
| paragraph_title | tiêu đề | yes | context |
| table | bảng | yes | yes |
| equation | công thức | yes | yes |
| image | ảnh | yes | caption/description |
| header | header | no | no |
| page_number | số trang | metadata | no |

### Code
Viết:

```python
def count_block_types(data):
    ...
```

### Output
`inspect_mineru.py`

---

# PHASE 2 — CHUNKING CƠ BẢN

## DAY 4 — Fixed Character Chunking

### Mục tiêu
Viết chunker đơn giản nhất.

```python
def split_by_characters(text, chunk_size=1000):
    chunks = []

    for start in range(0, len(text), chunk_size):
        end = start + chunk_size
        chunks.append(text[start:end])

    return chunks
```

### Test
- 500 chars
- 1000 chars
- 2000 chars

Thống kê:
- số chunk;
- min length;
- max length;
- average length.

### Nhận xét bắt buộc
Hiểu tại sao cách này có thể cắt giữa từ/câu.

### Output
`chunk_v01_character.py`

---

## DAY 5 — Word-based Chunking

### Mục tiêu
Không cắt giữa từ.

Dùng:

```python
words = text.split()
```

Test:
- 100 từ;
- 200 từ;
- 300 từ.

### Cần hiểu
Word count không giống token count.

### Output
`chunk_v02_words.py`

---

## DAY 6 — Token-based Chunking

### Mục tiêu
Hiểu token thật sự.

### Học
- token là gì;
- tokenizer là gì;
- token khác word;
- model khác nhau có tokenizer khác nhau.

### Viết

```python
def count_tokens(text):
    ...

def split_by_tokens(text, max_tokens):
    ...
```

### Experiment
- 300
- 500
- 800
- 1000 token

### Output
`chunk_v03_tokens.py`

---

## DAY 7 — Overlap

### Mục tiêu
Hiểu sliding window.

Ví dụ:

```text
chunk_size = 500
overlap = 50
```

Công thức:

```python
step = chunk_size - overlap
```

### Test
- overlap 0
- overlap 50
- overlap 100

### Tự trả lời
- overlap lớn giúp gì?
- tăng storage bao nhiêu?
- có làm retrieval bị duplicate không?

### Output
`chunk_v04_overlap.py`

---

# PHASE 3 — CHIA THEO CẤU TRÚC VĂN BẢN

## DAY 8 — Paragraph-aware Chunking

### Mục tiêu
Ưu tiên giữ nguyên paragraph.

Ý tưởng:

```text
paragraph
paragraph
paragraph
   ↓
gom đến gần max_tokens
```

Pseudo-code:

```python
current_chunk = []

for paragraph in paragraphs:
    if tokens(current + paragraph) <= max_tokens:
        add paragraph
    else:
        save current
        current = [paragraph]
```

Nếu một paragraph > max token:
`fallback → token split`

### Output
`chunk_v05_paragraph.py`

---

## DAY 9 — Sentence-aware fallback

### Mục tiêu
Nếu paragraph quá dài, cắt theo câu trước khi cắt token.

Thứ tự:

```text
Section
 ↓
Paragraph
 ↓
Sentence
 ↓
Token
```

Có thể bắt đầu:

```python
re.split(r'(?<=[.!?])\s+', text)
```

### Output
`chunk_v06_sentence.py`

---

## DAY 10 — Metadata cơ bản

### Mục tiêu
Chunk không chỉ chứa text.

Tạo:

```json
{
  "chunk_id": "doc01_chunk_001",
  "doc_id": "doc01",
  "text": "...",
  "page_start": 1,
  "page_end": 2
}
```

### Học
Metadata:
- dùng filter;
- dùng citation;
- thường không embedding;
- giúp truy vết nguồn.

### Output
`chunk_v07_metadata.py`

---

# PHASE 4 — TẬN DỤNG CẤU TRÚC MINERU

## DAY 11 — Đọc block thay vì Markdown

### Mục tiêu
Từ đây dùng `structured_content.json` làm nguồn chính.

Chuẩn hóa block:

```json
{
  "type": "text",
  "text": "...",
  "page": 3,
  "source_index": 10
}
```

Viết:

```python
def normalize_block(block, page_idx):
    ...
```

### Output
`mineru_normalizer.py`

---

## DAY 12 — Noise filtering

### Mục tiêu
Loại:
- header;
- footer;
- page_number;
- text rỗng.

Ví dụ:

```python
IGNORE_TYPES = {
    "header",
    "footer",
    "page_number",
}
```

Viết:

```python
def should_keep_block(block):
    ...
```

### Nguyên tắc

```text
raw
 ↓
normalized
 ↓
filtered
```

Không sửa dữ liệu MinerU gốc.

### Output
`filter_blocks.py`

---

## DAY 13 — Heading hierarchy

### Mục tiêu
Hiểu cấu trúc:
- H1
- H2
- H3
- H4

Tạo `heading_stack`.

Metadata:

```json
{
  "section_path": [
    "2. Phương pháp",
    "2.1 Dữ liệu",
    "2.1.1 Tiền xử lý"
  ]
}
```

Viết:

```python
def update_heading_stack(stack, title, level):
    ...
```

### Bài tập
Mô phỏng stack:

```text
H1
H2
H3
H2
H3
H1
```

### Output
`heading_parser.py`

---

## DAY 14 — Section-aware Chunking

### Mục tiêu
Không ghép tùy tiện nội dung của hai section khác nhau.

Quy tắc:

```text
gặp heading mới
→ ưu tiên đóng chunk hiện tại
```

Không lấy 70 token đầu của section mới chỉ để chunk cũ đủ 500 token.

### Output
`chunk_v08_sections.py`

---

# PHASE 5 — XỬ LÝ BLOCK ĐẶC BIỆT

## DAY 15 — Equation-aware Chunking

### Mục tiêu
Giữ công thức gần đoạn giải thích.

Ví dụ:

```text
Hàm mất mát được xác định bởi:
L = ...
Trong đó...
```

nên cùng chunk khi có thể.

Metadata:

```json
{
  "has_equation": true
}
```

### Output
`chunk_v09_equation.py`

---

## DAY 16 — Table-aware Chunking

### Mục tiêu
Giữ:
- caption;
- table headers;
- rows.

Table nhỏ:
`caption + table` → 1 chunk.

Table lớn:
chia theo row nhưng lặp lại tên bảng và column headers.

### Metadata

```json
{
  "has_table": true
}
```

### Output
`chunk_v10_table.py`

---

## DAY 17 — Image-aware Chunking

### Mục tiêu
Không embedding đường dẫn ảnh như text.

Chunk:

```json
{
  "text": "...",
  "images": [
    {
      "path": "images/page_4_image_1.jpg",
      "caption": "Hình 2..."
    }
  ]
}
```

### Hiểu
Text retrieval tìm chunk → backend lấy `image_ref` nếu cần.

Chưa cần image embedding ở giai đoạn này.

### Output
`chunk_v11_image_refs.py`

---

## DAY 18 — Page continuity

### Mục tiêu
Không coi đổi trang là hard boundary.

Ví dụ:

```text
Page 10:
"... mô hình có khả năng"

Page 11:
"học biểu diễn tốt hơn..."
```

vẫn có thể thuộc cùng chunk.

Metadata:

```json
{
  "page_start": 10,
  "page_end": 11
}
```

### Output
`chunk_v12_page_continuity.py`

---

# PHASE 6 — CHUNKING NÂNG CAO

## DAY 19 — Parent / Child Chunking

### Mục tiêu
Hiểu hierarchical retrieval.

Ví dụ:

```text
Parent ≈ 1500 tokens

├── Child 1 ≈ 450
├── Child 2 ≈ 500
└── Child 3 ≈ 400
```

Embedding child, nhưng có thể mở rộng về parent khi đưa context vào LLM.

Chunk:

```json
{
  "chunk_id": "child_002",
  "parent_id": "parent_010"
}
```

### Output
`chunk_v13_parent_child.py`

---

## DAY 20 — Adaptive Chunk Size

### Mục tiêu
Không ép mọi chunk đúng 500 token.

Cấu hình:

```python
MIN_TOKENS = 200
TARGET_TOKENS = 500
MAX_TOKENS = 800
```

Logic:

```text
< MIN
→ thử merge nếu cùng section

MIN → MAX
→ hợp lệ

> MAX
→ split tiếp
```

### Cần hiểu
`TARGET_TOKENS` khác `MAX_TOKENS`.

### Output
`chunk_v14_adaptive.py`

---

# PHASE 7 — GHÉP PIPELINE HOÀN CHỈNH

## DAY 21 — Viết `chunk_dataset.py`

### Mục tiêu
Không thêm thuật toán mới.

Chỉ refactor mọi thứ thành một file rõ ràng.

Skeleton:

```python
# 1. Imports

# 2. Configuration

# 3. Loading
def load_structured_content(...):
    pass

# 4. Normalization
def normalize_block(...):
    pass

# 5. Filtering
def filter_blocks(...):
    pass

# 6. Heading hierarchy
def update_heading_stack(...):
    pass

# 7. Token counting
def count_tokens(...):
    pass

# 8. Semantic grouping
def group_blocks(...):
    pass

# 9. Chunk splitting
def split_group(...):
    pass

# 10. Special blocks
def handle_table(...):
    pass

def handle_equation(...):
    pass

def handle_image(...):
    pass

# 11. Parent-child
def build_parent_child(...):
    pass

# 12. Validation
def validate_chunk(...):
    pass

# 13. Export
def write_jsonl(...):
    pass

# 14. Main
def main():
    pass

if __name__ == "__main__":
    main()
```

---

# FORMAT CHUNK CUỐI CÙNG

```json
{
  "chunk_id": "VI_PP_001_C0001",
  "parent_id": "VI_PP_001_P0001",
  "doc_id": "VI_PP_001",
  "document_title": "Cải tiến mô hình dịch máy...",
  "section_path": [
    "2. Đối tượng và phương pháp nghiên cứu",
    "2.1 Đối tượng nghiên cứu",
    "2.1.1 Đồ thị tri thức"
  ],
  "page_start": 2,
  "page_end": 3,
  "text": "Nội dung chunk...",
  "token_count": 487,
  "block_types": [
    "text",
    "equation",
    "text"
  ],
  "images": [
    {
      "path": "images/page_2_image_6.jpg",
      "caption": "Hình 1. Minh họa đồ thị tri thức"
    }
  ],
  "has_image": true,
  "has_table": false,
  "has_equation": true,
  "source_file": "structured_content.json"
}
```

---

# CHECKLIST VALIDATION

Mỗi chunk:

```text
[ ] text không rỗng
[ ] chunk_id duy nhất
[ ] doc_id tồn tại
[ ] page_start <= page_end
[ ] token_count <= MAX_TOKENS
[ ] section_path hợp lệ
[ ] image path tồn tại nếu có
[ ] không còn header/footer/page_number
[ ] table không mất header
[ ] equation không bị cắt vô lý
```

---

# SAU 21 NGÀY — PHASE BENCHMARK CHO BÀI BÁO

Không nên viết:

> “500 token là tối ưu.”

nếu chưa benchmark.

Tạo các experiment:

```text
A — Fixed 300 / overlap 50
B — Fixed 500 / overlap 50
C — Fixed 800 / overlap 80
D — Structure-aware / target 500
E — Parent-child / child 400–600
```

Đánh giá retrieval:

```text
Recall@K
MRR
HitRate@K
nDCG@K
```

Đánh giá answer:

```text
Faithfulness
Answer Correctness
Context Precision
Citation Accuracy
```

---

# GIỮ TOÀN BỘ PHIÊN BẢN

```text
chunk_v01_character.py
chunk_v02_words.py
chunk_v03_tokens.py
chunk_v04_overlap.py
chunk_v05_paragraph.py
chunk_v06_sentence.py
chunk_v07_metadata.py
chunk_v08_sections.py
chunk_v09_equation.py
chunk_v10_table.py
chunk_v11_image_refs.py
chunk_v12_page_continuity.py
chunk_v13_parent_child.py
chunk_v14_adaptive.py

chunk_dataset.py
```

Điều này rất hữu ích cho phần:
- phương pháp;
- thực nghiệm;
- so sánh thuật toán;
- ablation study.

---

# CÁCH HỌC MỖI NGÀY

Khoảng 1.5–2.5 giờ:

```text
20 phút   → lý thuyết
30 phút   → đọc ví dụ
45–60 phút → tự code
20 phút   → test
15 phút   → ghi chú
```

Cuối ngày ghi:

```markdown
## Hôm nay tôi hiểu gì?

## Tôi đã code gì?

## Bug tôi gặp?

## Vì sao bug xảy ra?

## Tôi có thể tự viết lại không?

## Ngày mai học gì?
```

---

# NGUYÊN TẮC QUAN TRỌNG

## 1. Không copy nguyên file hoàn chỉnh ngay

Mỗi ngày chỉ code phần đang học.

## 2. Luôn tự viết lại lần hai

```text
Đọc code mẫu
      ↓
Hiểu từng dòng
      ↓
Đóng code mẫu
      ↓
Tự code lại
      ↓
So sánh kết quả
```

## 3. Luôn in dữ liệu để quan sát

```python
print("TYPE:", block["type"])
print("PAGE:", page_idx)
print("TEXT:", block.get("content"))
```

## 4. Một function chỉ nên làm một nhiệm vụ

Tốt:

```python
load_document()
normalize_blocks()
filter_blocks()
build_sections()
split_chunks()
save_chunks()
```

## 5. Không nhờ AI sửa bug ngay lập tức

Khi lỗi:

```text
1. đọc traceback
2. xác định dòng lỗi
3. print biến
4. tự giải thích nguyên nhân
5. thử sửa
6. sau đó mới hỏi AI
```

---

# 5 MỐC KIỂM TRA

## Mốc 1 — Day 4
Tự viết được:

```text
text → fixed chunks
```

## Mốc 2 — Day 8
Giải thích được:

```text
character
word
token
paragraph
sentence
overlap
```

## Mốc 3 — Day 14
Giải thích và code được:

```text
heading hierarchy
section_path
section-aware chunking
page metadata
```

## Mốc 4 — Day 18
Giải thích được tại sao:

```text
equation
table
image
```

không nên xử lý giống plain text.

## Mốc 5 — Day 21
Không nhìn code cũ, tự viết skeleton:

```text
load
normalize
filter
structure
chunk
validate
export
```

---

# SAU ROADMAP BẠN PHẢI TỰ TRẢ LỜI ĐƯỢC

1. Chunk là gì?
2. Tại sao page không phải chunk?
3. Token khác word thế nào?
4. Overlap có tác dụng gì?
5. Khi nào overlap gây hại?
6. Vì sao phải lưu metadata?
7. Vì sao heading hierarchy quan trọng?
8. Tại sao không merge hai section chỉ để đủ token?
9. Paragraph lớn hơn `MAX_TOKENS` thì làm gì?
10. Table nên split thế nào?
11. Equation nên đi cùng block nào?
12. Image path được lưu ở đâu?
13. `page_start/page_end` tính thế nào?
14. Parent-child chunking giải quyết gì?
15. `TARGET_TOKENS` khác `MAX_TOKENS` thế nào?
16. Vì sao phải giữ baseline fixed-token?
17. Làm sao chứng minh phương pháp mới tốt hơn?
18. Recall@5 đo gì?
19. MRR đo gì?
20. Làm sao tái lập thí nghiệm?

---

# MỤC TIÊU CUỐI CÙNG

Không phải:

```text
AI viết chunk_dataset.py cho tôi.
```

Mà là:

```text
Tôi tự viết chunk_dataset.py.

Tôi hiểu:
- tại sao mỗi function tồn tại;
- tại sao chọn thuật toán đó;
- điểm yếu của nó;
- tham số nào cần benchmark;
- dữ liệu đầu vào biến đổi thế nào;
- output được tạo ra thế nào;
- và có thể bảo vệ lựa chọn của mình trong bài báo.
```
