# ROADMAP — Xây dựng Dataset phục vụ hệ thống RAG cho tài liệu môn Trí tuệ nhân tạo

> **Mục tiêu:** Xây dựng một pipeline có khả năng nhận tài liệu PDF/DOCX/PPTX, sử dụng Docling để trích xuất cấu trúc tài liệu, sau đó xây dựng RAG Dataset gồm nội dung đã chunk + metadata, đánh giá chất lượng retrieval và cuối cùng tích hợp thành hệ thống RAG hỏi đáp dựa trên tài liệu môn Trí tuệ nhân tạo.

---

## 1. Kiến trúc tổng thể

```text
PDF / DOCX / PPTX
        ↓
  Document Parser
      (Docling)
        ↓
Structured Representation
        ↓
   Dataset Builder
        ↓
 ┌──────┴─────────┐
 ↓                ↓
Chunking       Metadata
 ↓                ↓
 └──────┬─────────┘
        ↓
   RAG Dataset
        ↓
    Evaluation
        ↓
    RAG System
```

---

## 2. Mục tiêu đầu ra

Sau khi hoàn thành roadmap, project cần có:

```text
Input Documents
    ↓
Docling Parser
    ↓
Structured Documents
    ↓
Cleaning / Normalization
    ↓
Structure-aware Chunking
    ↓
Metadata Enrichment
    ↓
RAG Dataset
    ↓
Embedding + Vector Database
    ↓
Retriever
    ↓
RAG
    ↓
Evaluation Report
```

### Dataset cuối cùng dự kiến

Mỗi chunk nên có tối thiểu:

```json
{
  "chunk_id": "AI_CH03_SEC01_001",
  "document_id": "GIAO_TRINH_AI_01",
  "document_name": "GiaoTrinh_AI.pdf",
  "page_start": 45,
  "page_end": 46,
  "chapter": "Chương 3",
  "section": "3.1.1 Breadth First Search",
  "content": "Breadth First Search là..."
}
```

---

# PHASE 0 — Chuẩn bị và xác định bài toán

## Ngày 1 — Xác định đề tài

### Học
- RAG là gì?
- Retrieval khác Generation như thế nào?
- Dataset trong RAG khác dataset dùng để fine-tune như thế nào?
- Tại sao cần xây dựng dataset trước khi embedding?

### Làm
- Viết problem statement.
- Xác định input/output.
- Xác định phạm vi: tài liệu môn Trí tuệ nhân tạo.
- Quyết định MVP chỉ xử lý text + heading + paragraph + page + metadata.

### Output

```text
docs/problem_statement.md
docs/scope.md
```

### Commit

```text
docs: define project scope and problem statement
```

---

## Ngày 2 — Khảo sát tài liệu đầu vào

### Làm
Thu thập một bộ tài liệu mẫu:

```text
data/raw/
├── pdf/
├── docx/
└── pptx/
```

Nên có các loại:
- Giáo trình PDF.
- Slide bài giảng.
- DOCX.
- PDF có bảng.
- PDF có công thức.
- Nếu có thể, thêm một PDF scan để kiểm tra OCR.

### Ghi nhận
- Số file.
- Định dạng.
- Số trang.
- Kích thước.
- Có text layer hay không.
- Có bảng/hình/công thức hay không.

### Output

```text
docs/document_inventory.md
```

### Commit

```text
data: add sample educational documents
```

---

## Ngày 3 — Thiết kế kiến trúc project

### Làm

Tạo cấu trúc:

```text
rag-dataset-builder/
├── data/
│   ├── raw/
│   ├── structured/
│   ├── processed/
│   └── evaluation/
│
├── src/
│   ├── parser/
│   ├── cleaner/
│   ├── chunker/
│   ├── metadata/
│   ├── dataset/
│   ├── embedding/
│   ├── retrieval/
│   └── evaluation/
│
├── tests/
├── docs/
├── notebooks/
├── configs/
├── requirements.txt
└── README.md
```

### Output
Project skeleton chạy được.

### Commit

```text
chore: initialize project structure
```

---

# PHASE 1 — Document Parser với Docling

## Ngày 4 — Làm quen với Docling

### Học
- Docling là gì?
- DocumentConverter.
- Document object.
- Export Markdown/JSON/text.
- Document structure.

### Làm
Cài Docling và chạy thử với một PDF.

### Mục tiêu

```text
PDF
 ↓
Docling
 ↓
Document object
```

### Commit

```text
feat: add Docling document parser prototype
```

---

## Ngày 5 — Parse PDF

### Làm

Xây:

```text
src/parser/pdf_parser.py
```

Pipeline:

```text
PDF
 ↓
Docling
 ↓
Document
```

Kiểm tra:
- text
- heading
- paragraph
- page
- table
- image

### Output

```text
data/structured/sample_pdf.json
```

### Commit

```text
feat: parse PDF into structured representation
```

---

## Ngày 6 — Parse DOCX

### Làm

Xây parser DOCX sử dụng Docling.

```text
DOCX
 ↓
Docling
 ↓
Structured Document
```

### Test
So sánh kết quả DOCX với PDF.

### Commit

```text
feat: add DOCX document parsing
```

---

## Ngày 7 — Parse PPTX

### Làm

Xử lý:

```text
PPTX
 ↓
Docling
 ↓
Structured Document
```

Đặc biệt kiểm tra:
- slide number
- title
- bullet list
- text box

### Commit

```text
feat: add PPTX document parsing
```

---

## Ngày 8 — Chuẩn hóa Parser

### Mục tiêu

Dù input là:

```text
PDF
DOCX
PPTX
```

đều trả về một format chung.

Ví dụ:

```json
{
  "document_id": "...",
  "document_name": "...",
  "elements": [
    {
      "type": "heading",
      "text": "...",
      "page": 1
    },
    {
      "type": "paragraph",
      "text": "...",
      "page": 1
    }
  ]
}
```

### Đây là milestone quan trọng

```text
PDF ──┐
DOCX ─┼──> Unified Structured Representation
PPTX ─┘
```

### Commit

```text
refactor: unify document parser output
```

---

# PHASE 2 — Cleaning và Normalization

## Ngày 9 — Làm sạch text

Xử lý:
- whitespace.
- dòng trống.
- ký tự lỗi.
- duplicate text.
- header/footer.

Không được làm mất nội dung kiến thức.

### Commit

```text
feat: add document text cleaning
```

---

## Ngày 10 — Xử lý header/footer/page number

### Làm

Phát hiện các nội dung lặp:

```text
TRƯỜNG ĐẠI HỌC XYZ
CHƯƠNG 3
45
```

và loại bỏ khi cần.

### Commit

```text
feat: remove repeated headers footers and page numbers
```

---

## Ngày 11 — Xử lý heading hierarchy

Mục tiêu:

```text
Chương 3
 └── 3.1 Tìm kiếm
      ├── 3.1.1 BFS
      └── 3.1.2 DFS
```

Xác định:
- chapter
- section
- subsection

### Commit

```text
feat: reconstruct document heading hierarchy
```

---

## Ngày 12 — Kiểm tra bảng và danh sách

### Làm

Đảm bảo:

```text
Table
List
Paragraph
```

không bị trộn sai.

### Chưa cần giải quyết hoàn hảo mọi bảng.

Chỉ cần:
- phát hiện table.
- giữ nội dung.
- lưu metadata table.

### Commit

```text
feat: preserve tables and lists in structured data
```

---

## Ngày 13 — Kiểm tra công thức và hình ảnh

### Làm

Phân loại:

```text
Formula
Picture
Caption
```

MVP:
- giữ reference.
- không cần xây multimodal RAG ngay.

Ví dụ:

```json
{
  "type": "picture",
  "page": 45,
  "caption": "Minh họa thuật toán BFS"
}
```

### Commit

```text
feat: preserve formula and image references
```

---

## Ngày 14 — Xây bộ kiểm thử parser

### Tạo

```text
tests/
├── test_pdf.py
├── test_docx.py
├── test_pptx.py
└── test_cleaner.py
```

### Kiểm tra
- parser không crash.
- page number đúng.
- heading được nhận diện.
- content không rỗng bất thường.

### Commit

```text
test: add document parser test suite
```

---

## Ngày 15 — Milestone 1

### Kiểm tra

```text
PDF / DOCX / PPTX
        ↓
      Docling
        ↓
Structured Representation
        ↓
      Cleaning
```

### Output

Có thể xử lý một thư mục tài liệu.

### Commit

```text
milestone: complete document ingestion pipeline
```

---

# PHASE 3 — Chunking

## Ngày 16 — Học về Chunking

### Học
- Fixed-size chunking.
- Sentence chunking.
- Paragraph chunking.
- Recursive chunking.
- Structure-aware chunking.
- Chunk size.
- Chunk overlap.

### Quan trọng

Không chọn chunk size tùy ý.

Bạn sẽ thử nghiệm sau.

---

## Ngày 17 — Fixed-size baseline

Tạo baseline:

```text
500 tokens/chunk
```

Ví dụ:

```text
Document
 ↓
500 tokens
 ↓
500 tokens
 ↓
500 tokens
```

### Mục đích
Có baseline để so sánh.

### Commit

```text
feat: add fixed-size chunking baseline
```

---

## Ngày 18 — Structure-aware chunking

Mục tiêu:

```text
Chapter
 ↓
Section
 ↓
Paragraph
 ↓
Chunk
```

Không cắt giữa các cấu trúc quan trọng nếu có thể.

### Commit

```text
feat: add structure-aware chunking
```

---

## Ngày 19 — Chunk metadata

Mỗi chunk có:

```json
{
  "chunk_id": "...",
  "document_id": "...",
  "chapter": "...",
  "section": "...",
  "page_start": 45,
  "page_end": 46,
  "content": "..."
}
```

### Commit

```text
feat: attach metadata to document chunks
```

---

## Ngày 20 — Chunk overlap

Thử:

```text
0%
10%
20%
```

Mục tiêu:
- không mất ngữ cảnh giữa hai chunk.

### Commit

```text
feat: support configurable chunk overlap
```

---

## Ngày 21 — Chunk validation

Kiểm tra:
- chunk quá ngắn.
- chunk quá dài.
- chunk chỉ chứa header.
- chunk bị trùng.
- chunk mất context.

### Commit

```text
test: validate generated chunks
```

---

## Ngày 22 — So sánh chunking

Tạo:

```text
dataset_fixed
dataset_structure
```

So sánh:
- số lượng chunk.
- độ dài chunk.
- số chunk/document.
- context completeness.

### Output

```text
docs/chunking_comparison.md
```

### Commit

```text
docs: compare chunking strategies
```

---

# PHASE 4 — RAG Dataset

## Ngày 23 — Thiết kế schema dataset

Chốt schema:

```json
{
  "chunk_id": "",
  "document_id": "",
  "document_name": "",
  "source_type": "",
  "page_start": 0,
  "page_end": 0,
  "chapter": "",
  "section": "",
  "content": ""
}
```

### Commit

```text
feat: define RAG dataset schema
```

---

## Ngày 24 — Dataset Builder

Xây:

```text
src/dataset/builder.py
```

Pipeline:

```text
Structured Document
 ↓
Clean
 ↓
Chunk
 ↓
Metadata
 ↓
JSONL
```

### Output

```text
data/processed/rag_dataset.jsonl
```

### Commit

```text
feat: build RAG dataset from structured documents
```

---

## Ngày 25 — Dataset validation

Kiểm tra:
- missing fields.
- duplicate chunk ID.
- empty content.
- invalid page.
- metadata inconsistency.

### Commit

```text
feat: validate RAG dataset
```

---

## Ngày 26 — Dataset statistics

Thống kê:
- số document.
- số chunk.
- số token.
- độ dài trung bình.
- min/max chunk.
- số chunk theo chapter.
- số chunk theo document.

### Output

```text
docs/dataset_statistics.md
```

### Commit

```text
feat: add RAG dataset statistics
```

---

## Ngày 27 — Xây bộ câu hỏi đánh giá

Tạo evaluation dataset:

```json
{
  "question": "Thuật toán BFS là gì?",
  "expected_source": "GiaoTrinh_AI.pdf",
  "expected_page": 45,
  "expected_section": "3.1.1 BFS"
}
```

Mục tiêu ban đầu:

```text
100 câu hỏi
```

### Phân loại
- Definition.
- Explanation.
- Comparison.
- Application.
- Reasoning.

### Commit

```text
data: add RAG retrieval evaluation questions
```

---

## Ngày 28 — Milestone 2

### Hoàn thành

```text
Documents
 ↓
Docling
 ↓
Structured Representation
 ↓
Cleaning
 ↓
Chunking
 ↓
Metadata
 ↓
RAG Dataset
```

### Commit

```text
milestone: complete RAG dataset builder
```

---

# PHASE 5 — Embedding và Vector Database

## Ngày 29 — Học Embedding

### Học
- Embedding là gì?
- Vector similarity.
- Cosine similarity.
- Semantic search.

### Làm

Embedding thử 100 chunks.

---

## Ngày 30 — Chọn Embedding Model

So sánh một số model phù hợp tiếng Việt/multilingual.

Tiêu chí:
- tiếng Việt.
- tốc độ.
- kích thước.
- chất lượng retrieval.
- khả năng chạy local.

### Output

```text
docs/embedding_model_selection.md
```

---

## Ngày 31 — Embedding Dataset

Pipeline:

```text
RAG Dataset
 ↓
Embedding Model
 ↓
Vectors
```

### Commit

```text
feat: generate embeddings for RAG dataset
```

---

## Ngày 32 — Vector Database

Có thể bắt đầu với:

```text
Chroma
```

Sau đó nếu cần mở rộng có thể nghiên cứu:

```text
Qdrant
```

Pipeline:

```text
Chunk
 ↓
Embedding
 ↓
Vector DB
```

### Commit

```text
feat: store document embeddings in vector database
```

---

## Ngày 33 — Semantic Retrieval

Input:

```text
"Thuật toán A* hoạt động như thế nào?"
```

Output:

```text
Top 5 relevant chunks
```

### Commit

```text
feat: implement semantic document retrieval
```

---

## Ngày 34 — Metadata filtering

Cho phép lọc:

```text
chapter = "Chương 3"
page >= 40
document = "GiaoTrinh_AI.pdf"
```

### Commit

```text
feat: add metadata filtering to retrieval
```

---

# PHASE 6 — Evaluation

## Ngày 35 — Hiểu Retrieval Evaluation

Học:

- Recall@K.
- Precision@K.
- Hit Rate.
- MRR.

Tập trung trước vào:

```text
Recall@5
MRR
Hit Rate@5
```

---

## Ngày 36 — Retrieval Evaluation

Chạy 100 câu hỏi.

Ví dụ:

```text
Question
 ↓
Retriever
 ↓
Top 5 chunks
 ↓
Compare expected source
```

### Output

```text
evaluation/retrieval_results.json
```

---

## Ngày 37 — Baseline Evaluation

Đánh giá:

```text
Fixed-size chunking
```

### Output

```text
Recall@5 = ...
MRR = ...
Hit Rate@5 = ...
```

---

## Ngày 38 — Structure-aware Evaluation

Đánh giá:

```text
Structure-aware chunking
```

So sánh với baseline.

### Output

```text
docs/evaluation_chunking.md
```

---

## Ngày 39 — Chunk size experiment

Thử:

```text
300
500
800
1000 tokens
```

Giữ các thành phần khác giống nhau.

### Mục tiêu

Tìm chunk size tốt nhất cho dataset.

---

## Ngày 40 — Top-K experiment

Thử:

```text
K = 3
K = 5
K = 10
```

Đo:

```text
Recall@K
MRR
```

---

## Ngày 41 — Embedding experiment

So sánh các embedding model đã chọn.

Giữ nguyên:
- dataset.
- chunking.
- vector DB.
- evaluation questions.

Chỉ thay embedding model.

---

## Ngày 42 — Tổng hợp thí nghiệm

Tạo bảng:

```text
Method                Recall@5    MRR
------------------------------------------------
Fixed 300               ...
Fixed 500               ...
Structure 300           ...
Structure 500           ...
Structure 800           ...
```

### Đây là phần quan trọng của báo cáo.

### Commit

```text
docs: summarize retrieval experiments
```

---

# PHASE 7 — RAG System

## Ngày 43 — Chọn LLM

Xác định LLM dùng cho generation.

Có thể dùng:
- API model.
- Local model.

MVP ưu tiên model dễ tích hợp.

---

## Ngày 44 — Prompt RAG

Thiết kế prompt:

```text
Bạn là trợ lý môn Trí tuệ nhân tạo.

Hãy trả lời câu hỏi dựa trên context được cung cấp.

Nếu context không chứa thông tin cần thiết,
hãy nói rằng không tìm thấy thông tin trong tài liệu.

Context:
{context}

Question:
{question}
```

---

## Ngày 45 — RAG pipeline

Xây:

```text
Question
 ↓
Embedding
 ↓
Retriever
 ↓
Top-K chunks
 ↓
Prompt
 ↓
LLM
 ↓
Answer
```

### Commit

```text
feat: implement basic RAG pipeline
```

---

## Ngày 46 — Citation / Source

Câu trả lời cần biết nguồn:

```text
Nguồn:
GiaoTrinh_AI.pdf
Trang 45
Mục 3.1.1 BFS
```

### Đây là feature rất nên có.

### Commit

```text
feat: add source citations to RAG answers
```

---

## Ngày 47 — Hallucination handling

Nếu retrieval không đủ:

```text
Không tìm thấy thông tin phù hợp
trong tài liệu.
```

Không để LLM tự bịa.

### Commit

```text
feat: add insufficient-context handling
```

---

## Ngày 48 — RAG answer evaluation

Tạo:

```text
question
retrieved_context
answer
expected_answer
```

Đánh giá:
- Correctness.
- Relevance.
- Faithfulness.
- Citation correctness.

---

## Ngày 49 — Demo interface

MVP:

```text
┌───────────────────────────────┐
│ AI Assistant                  │
│                               │
│ Question:                     │
│ [ BFS là gì?              ]   │
│                               │
│ [Ask]                         │
│                               │
│ Answer:                       │
│ ...                           │
│                               │
│ Sources:                      │
│ GiaoTrinh_AI.pdf - p.45       │
└───────────────────────────────┘
```

Không cần UI phức tạp.

---

## Ngày 50 — Milestone 3

Hoàn thành:

```text
RAG Dataset
 ↓
Embedding
 ↓
Vector DB
 ↓
Retriever
 ↓
LLM
 ↓
Answer + Source
```

### Commit

```text
milestone: complete educational RAG system
```

---

# PHASE 8 — Nghiên cứu và cải thiện

## Ngày 51 — Phân tích lỗi Retrieval

Lấy các câu hỏi retrieval sai.

Phân loại:

```text
Wrong chunk
Missing chunk
Wrong metadata
Bad chunk boundary
Embedding problem
```

---

## Ngày 52 — Phân tích lỗi Chunking

Kiểm tra:

```text
Question
 ↓
Wrong chunk
 ↓
Tại sao?
```

Ví dụ:
- chunk quá ngắn.
- chunk quá dài.
- section bị chia đôi.
- context nằm ở chunk kế tiếp.

---

## Ngày 53 — Cải thiện metadata

Thử thêm:

```text
document_title
chapter
section
subsection
page
source_type
```

Đánh giá metadata filtering.

---

## Ngày 54 — Parent-child retrieval

Nghiên cứu:

```text
Small child chunk
       ↓
Retrieve
       ↓
Parent section
       ↓
LLM
```

Mục tiêu:
- retrieval chính xác.
- context đầy đủ hơn.

---

## Ngày 55 — Reranking

Thử:

```text
Vector Retrieval
      ↓
Top 20
      ↓
Reranker
      ↓
Top 5
```

So sánh với:

```text
Vector Retrieval
      ↓
Top 5
```

---

## Ngày 56 — Đánh giá Reranking

Đo:

```text
Recall
MRR
Precision
```

và thời gian xử lý.

---

## Ngày 57 — So sánh toàn bộ pipeline

So sánh:

```text
A:
Fixed chunk

B:
Structure-aware chunk

C:
Structure-aware + metadata

D:
Structure-aware + metadata + reranker
```

Đây có thể là **thí nghiệm chính của đề tài**.

---

## Ngày 58 — Đánh giá RAG end-to-end

Đánh giá:

```text
Retrieval quality
+
Answer quality
+
Citation quality
```

---

## Ngày 59 — Performance

Đo:
- parsing time.
- chunking time.
- embedding time.
- retrieval latency.
- generation latency.
- memory/storage.

---

## Ngày 60 — Milestone 4

Chốt phương pháp tốt nhất.

```text
Best Dataset Pipeline
        ↓
Best Retrieval Pipeline
        ↓
Best RAG Configuration
```

### Commit

```text
milestone: finalize RAG optimization experiments
```

---

# PHASE 9 — Hoàn thiện Dataset Builder

## Ngày 61 — CLI

Tạo command:

```bash
python -m src.main ingest ./data/raw
```

hoặc:

```bash
python -m src.main build-dataset ./data/raw
```

---

## Ngày 62 — Config

Tạo:

```text
configs/config.yaml
```

Ví dụ:

```yaml
chunk_size: 500
chunk_overlap: 50
top_k: 5
embedding_model: ...
```

Không hardcode cấu hình.

---

## Ngày 63 — Logging

Log:

```text
Parsing: file.pdf
Pages: 120
Chunks: 542
Errors: 0
```

---

## Ngày 64 — Error handling

Xử lý:
- file hỏng.
- file không hỗ trợ.
- PDF không có text.
- parser lỗi.
- chunk lỗi.

Pipeline không nên dừng toàn bộ chỉ vì một file lỗi.

---

## Ngày 65 — Batch processing

Cho phép:

```text
data/raw/
├── 001.pdf
├── 002.pdf
├── 003.docx
├── 004.pptx
...
```

chạy một lần.

---

## Ngày 66 — Incremental processing

Nếu file đã xử lý:

```text
document_hash
```

thì không parse lại nếu nội dung không thay đổi.

---

## Ngày 67 — Dataset versioning

Ví dụ:

```text
dataset_v1
dataset_v2
dataset_v3
```

Ghi lại:
- parser version.
- chunk size.
- overlap.
- embedding model.
- date.

---

## Ngày 68 — Reproducibility

Tạo file:

```text
configs/experiment_01.yaml
configs/experiment_02.yaml
```

Có thể chạy lại thí nghiệm.

---

# PHASE 10 — Báo cáo và hoàn thiện đề tài

## Ngày 69 — Viết chương tổng quan

Nội dung:
- AI.
- LLM.
- Embedding.
- Vector Database.
- RAG.
- Document Processing.

---

## Ngày 70 — Viết chương phương pháp

Mô tả:

```text
Document
 ↓
Docling
 ↓
Structured Representation
 ↓
Cleaning
 ↓
Chunking
 ↓
Metadata
 ↓
RAG Dataset
```

---

## Ngày 71 — Viết chương thực nghiệm

Mô tả:
- Dataset.
- Số lượng tài liệu.
- Số chunk.
- Embedding models.
- Chunk sizes.
- Top-K.
- Evaluation dataset.

---

## Ngày 72 — Viết kết quả

Đưa bảng:

```text
Method | Recall@5 | MRR | Latency
```

và:

```text
Method | Answer Score | Faithfulness
```

---

## Ngày 73 — Phân tích kết quả

Không chỉ nói:

> Phương pháp A tốt hơn B.

Phải giải thích:

> A tốt hơn B vì cấu trúc section được giữ lại, giúp chunk chứa đầy đủ ngữ cảnh của câu hỏi.

---

## Ngày 74 — Phân tích hạn chế

Ví dụ:
- PDF scan.
- OCR.
- bảng phức tạp.
- công thức.
- hình ảnh.
- tài liệu không có heading rõ ràng.
- lỗi parser.
- hallucination.

---

## Ngày 75 — Viết kết luận

Trả lời:
- Đã xây dựng được gì?
- Dataset có đặc điểm gì?
- Phương pháp nào tốt nhất?
- RAG hoạt động thế nào?
- Hạn chế?
- Hướng phát triển?

---

# PHASE 11 — Hoàn thiện sản phẩm

## Ngày 76 — Refactor code

Kiểm tra:
- module.
- function.
- naming.
- type hints.
- duplicated code.

---

## Ngày 77 — Unit tests

Tăng coverage cho:
- parser.
- cleaner.
- chunker.
- metadata.
- dataset validator.
- retriever.

---

## Ngày 78 — Integration test

Test toàn pipeline:

```text
PDF
 ↓
Docling
 ↓
Dataset
 ↓
Embedding
 ↓
Vector DB
 ↓
RAG
```

---

## Ngày 79 — README

README cần có:

```text
Project overview
Installation
Dataset format
Pipeline
Usage
Configuration
Evaluation
Results
```

---

## Ngày 80 — Final demo

Chuẩn bị demo:

```text
Upload / add documents
        ↓
Process
        ↓
Build dataset
        ↓
Ask question
        ↓
Retrieve
        ↓
Answer
        ↓
Show sources
```

---

# PHASE 12 — Chuẩn bị bảo vệ

## Ngày 81 — Chuẩn bị slide

Slide đề xuất:

1. Problem.
2. Motivation.
3. Objective.
4. Architecture.
5. Document processing.
6. Dataset construction.
7. Chunking.
8. Metadata.
9. Retrieval.
10. RAG.
11. Evaluation.
12. Experimental results.
13. Demo.
14. Limitations.
15. Conclusion.

---

## Ngày 82 — Chuẩn bị demo script

Chuẩn bị 5 câu hỏi:

```text
1. Definition
2. Explanation
3. Comparison
4. Application
5. Difficult question
```

---

## Ngày 83 — Chuẩn bị câu hỏi phản biện

Phải trả lời được:

- Tại sao dùng RAG thay vì fine-tuning?
- Tại sao dùng Docling?
- Tại sao không chuyển PDF sang Markdown?
- Chunking là gì?
- Tại sao chọn chunk size này?
- Embedding là gì?
- Vector Database là gì?
- Recall@K là gì?
- MRR là gì?
- RAG có hallucination không?
- Dataset của bạn khác file PDF ban đầu ở đâu?
- Đóng góp của đề tài là gì?

---

## Ngày 84 — Kiểm tra toàn bộ kết quả

Chạy lại các experiment quan trọng.

Đảm bảo số liệu trong:
- code.
- notebook.
- báo cáo.
- slide

không mâu thuẫn.

---

## Ngày 85 — Final cleanup

Kiểm tra:
- Git repository.
- README.
- requirements.
- configs.
- dataset.
- evaluation.
- screenshots.
- report.
- slides.

---

# PHASE 13 — Buffer / mở rộng

## Ngày 86 — OCR

Nếu tài liệu scan quan trọng:

```text
PDF Scan
 ↓
OCR
 ↓
Structured Document
```

---

## Ngày 87 — Table-aware retrieval

Nghiên cứu retrieval với bảng.

---

## Ngày 88 — Formula-aware processing

Nghiên cứu công thức toán.

---

## Ngày 89 — Multimodal document

Nghiên cứu hình ảnh/sơ đồ trong giáo trình.

Không bắt buộc đưa vào MVP.

---

## Ngày 90 — Tổng kết

Tổng kết toàn bộ pipeline:

```text
PDF / DOCX / PPTX
        ↓
      Docling
        ↓
Structured Representation
        ↓
      Cleaning
        ↓
Structure-aware Chunking
        ↓
      Metadata
        ↓
    RAG Dataset
        ↓
     Embedding
        ↓
   Vector Database
        ↓
     Retrieval
        ↓
     Reranking
        ↓
        LLM
        ↓
 Answer + Citation
        ↓
    Evaluation
```

---

# 3. Các milestone chính

| Milestone | Ngày | Kết quả |
|---|---:|---|
| M1 | 1–15 | Document ingestion |
| M2 | 16–28 | RAG Dataset Builder |
| M3 | 29–50 | RAG System |
| M4 | 51–60 | Experiments & Optimization |
| M5 | 61–68 | Production-ready Dataset Builder |
| M6 | 69–75 | Report |
| M7 | 76–85 | Final Product |
| M8 | 86–90 | Advanced features |

---

# 4. Trọng tâm nghiên cứu của đề tài

Đề tài **không nên chỉ là xây chatbot**.

Trọng tâm nên là:

```text
Document Processing
        +
Dataset Construction
        +
Chunking
        +
Metadata
        +
Retrieval
        +
Evaluation
```

Câu hỏi nghiên cứu chính:

> **Các chiến lược xây dựng dataset từ tài liệu giáo dục ảnh hưởng như thế nào đến chất lượng truy xuất thông tin của hệ thống RAG?**

Các câu hỏi phụ:

1. Fixed-size chunking và structure-aware chunking khác nhau như thế nào?
2. Chunk size nào phù hợp với tài liệu môn Trí tuệ nhân tạo?
3. Metadata có cải thiện retrieval không?
4. Embedding model nào phù hợp với tài liệu tiếng Việt?
5. Reranking có cải thiện kết quả retrieval không?
6. Chất lượng retrieval ảnh hưởng thế nào đến chất lượng câu trả lời của RAG?

---

# 5. Nguyên tắc thực hiện

### Không làm tất cả ngay từ đầu

Luôn đi theo:

```text
MVP
 ↓
Chạy được
 ↓
Đo được
 ↓
Cải thiện
 ↓
Thực nghiệm
```

### Thứ tự ưu tiên

```text
1. Parser
2. Structured Representation
3. Cleaning
4. Chunking
5. Metadata
6. Dataset
7. Retrieval
8. Evaluation
9. RAG
10. Optimization
```

### Không phụ thuộc Markdown

Markdown có thể được sử dụng để debug/visualize nếu cần, nhưng **không phải một bước bắt buộc trong pipeline chính**.

---

# 6. Công nghệ dự kiến

## Core

```text
Python
Docling
```

## Dataset

```text
JSON / JSONL
```

## Embedding

```text
Sentence Transformers
```

## Vector Database

MVP:

```text
Chroma
```

Có thể nghiên cứu thêm:

```text
Qdrant
```

## LLM

Có thể sử dụng API hoặc model local tùy tài nguyên.

## Evaluation

```text
Python
NumPy
Pandas
```

---

# 7. Cấu trúc cuối cùng dự kiến

```text
rag-dataset-builder/
│
├── data/
│   ├── raw/
│   │   ├── pdf/
│   │   ├── docx/
│   │   └── pptx/
│   │
│   ├── structured/
│   ├── processed/
│   └── evaluation/
│
├── src/
│   ├── parser/
│   │   ├── pdf.py
│   │   ├── docx.py
│   │   └── pptx.py
│   │
│   ├── cleaner/
│   ├── chunker/
│   ├── metadata/
│   ├── dataset/
│   ├── embedding/
│   ├── retrieval/
│   ├── reranker/
│   ├── rag/
│   └── evaluation/
│
├── tests/
├── configs/
├── notebooks/
├── docs/
├── requirements.txt
├── README.md
└── main.py
```

---

# 8. Tiêu chí hoàn thành

Đề tài được xem là hoàn thành khi có thể:

```text
[✓] Nhận PDF
[✓] Nhận DOCX
[✓] Nhận PPTX

[✓] Parse bằng Docling
[✓] Tạo structured representation
[✓] Cleaning
[✓] Structure-aware chunking
[✓] Metadata

[✓] Sinh RAG Dataset
[✓] Validate dataset
[✓] Generate embeddings
[✓] Lưu Vector DB

[✓] Retrieval
[✓] Evaluation
[✓] RAG
[✓] Citation

[✓] Có baseline
[✓] Có experiments
[✓] Có số liệu
[✓] Có phân tích
[✓] Có báo cáo
[✓] Có demo
```

---

# 9. Kết quả cuối cùng

Sản phẩm cuối không chỉ là một chatbot.

Nó gồm **hai thành phần chính**:

### Dataset Builder

```text
PDF / DOCX / PPTX
        ↓
      Docling
        ↓
Structured Representation
        ↓
Cleaning
        ↓
Chunking
        ↓
Metadata
        ↓
RAG Dataset
```

### RAG System

```text
Question
    ↓
Embedding
    ↓
Retrieval
    ↓
Reranking
    ↓
Relevant Context
    ↓
LLM
    ↓
Answer
    ↓
Citation
```

**Đóng góp quan trọng của đề tài** là xây dựng và đánh giá một quy trình có hệ thống để biến tài liệu giáo dục thành dataset phù hợp cho RAG, thay vì đơn giản chỉ "đưa PDF vào chatbot".
