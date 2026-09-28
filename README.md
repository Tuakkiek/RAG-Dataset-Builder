# RAG-Dataset-Builder

Kho dữ liệu đa thể loại chuẩn hóa phục vụ xây dựng hệ thống RAG (Retrieval-Augmented Generation) cho môn Trí tuệ Nhân tạo.

---

## 1. Cấu Trúc Thư Mục Dữ Liệu

Hệ thống được chia theo **[Thể loại tài liệu] $\rightarrow$ [Ngôn ngữ / Trường ĐH]**, đồng bộ 1:1 giữa `data/01_raw/` (tài liệu gốc) và `data/mineru/` (kết quả trích xuất Markdown):

```text
data/01_raw/ & data/mineru/
├── 01_sach/                      # Sách tham khảo (en, vi)
├── 02_giao-trinh/                # Giáo trình học thuật (en, vi)
├── 03_bai-bao-khoa-hoc/          # Bài báo nghiên cứu khoa học (en, vi)
├── 04_luan-van-do-an/            # Luận văn Thạc sĩ, Tiến sĩ, Đồ án (en, vi)
├── 05_bao-cao-ky-thuat/          # Báo cáo kỹ thuật, Whitepaper (en, vi)
├── 06_slide-bai-giang/           # Slide thuyết trình bài giảng (en, vi)
├── 07_tai-lieu-hoc-tap-notes/    # Ghi chú, Note bài giảng (en)
├── 08_tai-lieu-huong-dan-guides/ # Hướng dẫn, Tutorials (en)
└── 09_tai-lieu-dai-hoc-quoc-te/  # Tài liệu các trường ĐH lớn
    ├── cornell/                  # Cornell University (advanced-ai, cs4700)
    ├── maryland/                 # University of Maryland (ai-planning-learning)
    ├── mit/                      # MIT (ai-101, exams, lecture-notes, projects...)
    └── uc-berkeley/              # UC Berkeley CS188 (2013 -> 2026)
```

---

## 2. Quy Chuẩn Đặt Tên Tệp (Naming Convention)

### <ngôn ngữ> _ <loại tài liệu> _ <mã số> _ <tên rút gọn theo chủ đề>

### 📋 Bảng Giải Mã Ký Hiệu:

| Thành phần | Mã ký hiệu | Ý nghĩa chi tiết | Ví dụ minh họa |
| :--- | :---: | :--- | :--- |
| **Ngôn ngữ** | **`EN`** | Tiếng Anh (*English*) | `EN_BK_001_AI Agents in Depth.pdf` |
| | **`VI`** | Tiếng Việt (*Vietnamese* - không dấu) | `VI_BK_002_Co so tri tue nhan tao.pdf` |
| **Loại tài liệu** | **`BK`** | Sách tham khảo (*Book*) | `EN_BK_001_AI Agents in Depth.pdf` |
| | **`TX`** | Giáo trình học thuật (*Textbook*) | `VI_TX_001_Tri tue nhan tao he chuyen gia.pdf` |
| | **`PP`** | Bài báo khoa học (*Paper*) | `EN_PP_004_Attention Is All You Need.pdf` |
| | **`TH`** | Luận văn, đồ án (*Thesis*) | `VI_TH_001_Xac thuc nguoi noi dung hoc sau.pdf` |
| | **`TR`** | Báo cáo kỹ thuật (*Technical Report*) | `EN_TR_001_Deep Learning Technical Intro.pdf` |
| | **`SL`** | Slide bài giảng (*Slides*) | `VI_SL_001_Bai 12-13 ML Logistic regression.pdf` |
| | **`LN`** | Ghi chép học tập (*Lecture Notes*) | `EN_LN_001_Stanford CS229 ML Main Notes.pdf` |
| | **`GD`** | Tài liệu hướng dẫn (*Guide / Tutorial*) | `EN_GD_001_Tutorial on DNN Intelligent Systems.pdf` |
| | **`UM`** | Tài liệu ĐH Quốc tế (*University Material*) | *(Xem chi tiết mã trường bên dưới)* |

#### 🎓 Mã các trường Đại học Quốc tế (`UM`):
* `EN_UM_COR-...`: 
    - Đại học **Cornell** 
    - `COR-ADV`: Advanced AI
    - `COR-CS47`: CS4700
* `EN_UM_MIT-...`: 
    - Học viện **MIT** 
    - `MIT-AI101`: AI101
    - `MIT-AI-EXAM`: AI-EXAM
    - `MIT-AI-LN`: AI-LN
    - `MIT-TIA-...`: TIA-...
* `EN_UM_UCB-[NĂM]_...`: 
    - Đại học **UC Berkeley**
    - CS188
* `EN_UM_UMD-...`: 
    - Đại học **Maryland**
    - UMD-PLAN

---
