<!-- page: 1 -->
# TRÍ TUỆ NHÂN TẠO (A.I) DÀNH CHO MỌI NGƯỜI

Bài giảng biên soạn theo giáo trình “A.I for everyone” của Nhà khoa học A.I Ông Andrew Ng (Google Brain - Baidu AI - Deeplearning.ai - Đại học Stanford)

Understanding the Science for Tomorrow: Myth and Reality của GS Jeffrey C. Grossman

Học viện Công nghệ Massachusetts (MIT)

<!-- page: 2 -->
![Hinh: fig-2-1]

Nhà khoa học A.I Ông Andrew Ng

Google Brain - Baidu AI - Deeplearning.ai - Đại học Stanford

<!-- page: 3 -->
![Hinh: fig-3-1]

Thạc sỹ - Nguyễn Ngọc Tú

NCS Tiến sỹ tại Strasbourg University - CFVG HCM.

Giám đốc điều hành của Tổ chức Trí Tuệ Nhân Tạo Việt (VietAI). (www.vietai.org)

Chuyên gia Phân tích dữ liệu Doanh Nghiệp (Business Data Analytics), Giám đốc Công ty Dataservices

<!-- page: 4 -->
![Hinh: fig-4-1]

## WHY WE EXIST

Artificial Intelligence (AI) is all around us under many forms from virtual and smart mobile devices, assistants, to robots and self-driving cars. Despite rapid progress in AI over the last few years in many countries, Vietnam still lags behind, merely touching at the surface of the technology.

<!-- page: 5 -->
![Hinh: fig-5-1]

## Introduction

### AI value creation by 2030

$13 trillion

- Retail: $0.8T
- Travel: $480B
- Transport & Logistics: $475B
- Automotive & Assembly: $405B
- Basic Materials: $300B
- Advanced Electronics/Semiconductors: $291B
- Healthcare Systems and Services: $267B
- High Tech: $267B
- Telecom: $174B
- Oil & Gas: $173B
- Agriculture: $164B

(Source: McKinsey Global Institute.)

<!-- page: 6 -->
## GIẢI MÃ A.I

### A.I

### ANI

ARTIFICIAL NARROW INTELLIGENCE

TRÍ TUỆ NHÂN TẠO HẸP

VD: XE TỰ HÀNH, LOA THÔNG MINH, TRÍ TUỆ NHÂN TẠO ỨNG DỤNG TRONG NHÀ MÁY, NÔNG TRẠI…

### AGI

ARTIFICIAL GENERAL INTELLIGENCE

TRÍ TUỆ NHÂN TẠO PHỔ QUÁT

LÀM ĐƯỢC TẤT CẢ NHỮNG GÌ NHƯ MỘT CON NGƯỜI THẬT

<!-- page: 7 -->
## NỘI DUNG CHƯƠNG TRÌNH

1. A.I – TRÍ TUỆ NHÂN TẠO LÀ GÌ?
   - HỌC MÁY – MACHINE LEARNING
   - DỮ LIỆU - DATA
   - MỘT CÔNG TY AI LÀ NHƯ THẾ NÀO?
   - NHỮNG ĐIỀU HỌC MÁY CÓ THỂ VÀ KHÔNG THỂ LÀM.
   - GIẢI THÍCH VỀ HỌC SÂU (DEEP LEARNING)

2. XÂY DỰNG MỘT DỰ ÁN A.I

3. XÂY DỰNG A.I CHO CÔNG TY/ TỔ CHỨC CỦA BẠN

4. A.I VÀ TÁC ĐỘNG XÃ HỘI CỦA NÓ

<!-- page: 8 -->
## CHÚNG TA MONG MUỐN ĐẠT ĐƯỢC GÌ SAU BUỔI CHIA SẺ?

1. BIẾT ĐƯỢC A.I LÀM ĐƯỢC GÌ.
2. BIẾT ĐƯỢC CÁCH XÂY DỰNG CHIẾN LƯỢC A.I CHO CÔNG TY MÌNH.
3. BIẾT CÁCH PHÂN BỔ NGUỒN LỰC XD A.I

<!-- page: 9 -->
## LƯỢC SỬ AI

History of AI

<!-- page: 10 -->
![Hinh: fig-10-1]
![Hinh: fig-10-2]
![Hinh: fig-10-3]

Engima

Alan Turing - 1927

Bombe

<!-- page: 11 -->
## A.I – TRÍ TUỆ NHÂN TẠO LÀ GÌ ?

- Học Máy – Machine Learning

<!-- page: 12 -->
![Hinh: fig-12-1]

MACHINE LEARNING

<!-- page: 13 -->
## Ví Dụ

![Hinh: fig-13-1]
![Hinh: fig-13-2]

Mommy…?

(Nguồn: Simple Neural Network implementation in Ruby)

<!-- page: 14 -->
![Hinh: fig-14-1]

<!-- page: 15 -->
![Hinh: fig-15-1]

## ARTIFICIAL INTELLIGENCE

The ability of a computer program or a machine to think like humans do.

### MACHINE LEARNING

Subfield of AI giving machines the skills to learn from examples without being explicitly programmed.

Examples: Fraud detection, marketing personalization, email classification

### DEEP LEARNING

Specialized machine learning technique enabling machines to train themselves to perform tasks.

Examples: Image classification, vehicle detection, sentiment analysis

<!-- page: 16 -->
![Hinh: fig-16-1]

### Machine Learning

Input → Feature extraction → Classification → Output

### Deep Learning

Input → Feature extraction + Classification → Output

<!-- page: 17 -->
![Hinh: fig-17-1]

### Machine learning workflow

Unsupervised → Feature extraction → Grouping of objects → Annotated data

Supervised → Feature extraction → Machine learning algorithm → Predictive model → New Data

<!-- page: 18 -->
## SUPERVISED LEARNING

### HỌC CÓ GIÁM SÁT

A → B

Input (Đầu vào) → Output (Đầu ra)

<!-- page: 19 -->
| Đầu vào (Input) | Đầu ra (Output) | Ứng dụng (Applications) |
| --- | --- | --- |
| Email | Thư rác? | Bộ lọc thư rác. |
| Âm thanh | Văn bản | Nhận dạng giọng nói |
| Tiếng Anh | Tiếng Việt | Máy dịch (Machine translation) |
| Q/C, thông tin người dùng | Nhấp chuột? (0/1) | Quảng cáo online |

<!-- page: 20 -->
| Đầu vào (Input) | Đầu ra (Output) | Ứng dụng (Applications) |
| --- | --- | --- |
| Hình ảnh, Thông tin rada | Vị trí của các xe ô tô | Xe tự lái (tự hành) |
| Hình ảnh của chiếc điện thoại | Bị hư hỏng? (0/1) | Kiểm tra trực quan |

<!-- page: 21 -->
![Hinh: fig-21-1]

## How Supervised Machine Learning Works

### STEP 1

Provide the machine learning algorithm uncategorized, unlabeled input and output data to learn.

### STEP 2

Feed the machine new, unlabeled information to see if it tags new data appropriately. If not, continue refining the algorithm.

### TYPES OF PROBLEMS TO WHICH IT’S SUITED

- CLASSIFICATION: Sorting items into categories
- REGRESSION: Identifying real values (dollars, weight, etc.)

<!-- page: 22 -->
## Bài toán

Có dữ liệu bệnh nhân như bảng dưới đây. Hãy xây dựng model để tiên đoán khả năng bị bệnh tim của Bệnh nhân số 09 -10

| STT | Cân nặng | Chiều cao | Huyết áp | Vận động | Bệnh tim |
| --- | --- | --- | --- | --- | --- |
| 1 | Nhẹ | Trung bình | Trung bình | Nhiều | Không |
| 2 | Nặng | Thấp | Cao | Ít | Có |
| 3 | Nhẹ | Thấp | Cao | Ít | Có |
| 4 | Nặng | Cao | Cao | Trung bình | Không |
| 5 | Nhẹ | Cao | Cao | Nhiều | Không |
| 6 | Trung bình | Thấp | Trung bình | Nhiều | Không |
| 7 | Trung bình | Trung bình | Trung Bình | Ít | Không |
| 8 | Nặng | Thấp | Thấp | Nhiều | Có |
| 9 | Nhẹ | Cao | Trung bình | Ít | ??? |
| 10 | Nhẹ | Cao | Trung bình | Nhiều | ??? |

<!-- page: 23 -->
## Bài toán

Có dữ liệu bệnh nhân như bảng dưới đây. Hãy xây dựng model để tiên đoán khả năng bị bệnh tim của Bệnh nhân số 09 -10

| STT | Cân nặng | Chiều cao | Huyết áp | Vận động | Bệnh tim |
| --- | --- | --- | --- | --- | --- |
| 1 | Nhẹ | Trung bình | Trung bình | Nhiều | Không |
| 2 | Nặng | Thấp | Cao | Ít | Có |
| 3 | Nhẹ | Thấp | Cao | Ít | Có |
| 4 | Nặng | Cao | Cao | Trung bình | Không |
| 5 | Nhẹ | Cao | Cao | Nhiều | Không |
| 6 | Trung bình | Thấp | Trung bình | Nhiều | Không |
| 7 | Trung bình | Trung bình | Trung Bình | Ít | Không |
| 8 | Nặng | Thấp | Thấp | Nhiều | Có |
| 9 | Nhẹ | Cao | Trung bình | Ít | ??? |
| 10 | Nhẹ | Cao | Trung bình | Nhiều | ??? |

<!-- page: 24 -->
## QUY ƯỚC

### Input

| STT | Tên | Giá trị |
| --- | --- | --- |
| 1 | Nhẹ | 1 |
| 2 | Thấp | 2 |
| 3 | Trung bình | 3 |
| 4 | Cao | 4 |
| 5 | Nặng | 5 |
| 6 | Ít | 6 |
| 7 | Nhiều | 7 |

### Output

| Tên | Giá trị |
| --- | --- |
| Có | 1 |
| Không | 0 |

<!-- page: 25 -->
## DỰ ĐOÁN

| STT | Cân nặng | Chiều cao | Huyết áp | Vận động | Bệnh tim |
| --- | --- | --- | --- | --- | --- |
| 9 | Nhẹ | Cao | Trung bình | Ít | ??? |

Đặc trưng: 1, 4, 3, 6, ???

<!-- page: 26 -->
## UN-SUPERVISED LEARNING

### HỌC KHÔNG GIÁM SÁT

A → B

Input (Đầu vào) → Output?? (Đầu ra)

<!-- page: 27 -->
![Hinh: fig-27-1]

<!-- page: 28 -->
![Hinh: fig-28-1]

## How Unsupervised Machine Learning Works

### STEP 1

Provide the machine learning algorithm uncategorized, unlabeled input data to see what patterns it finds.

### STEP 2

Observe and learn from the patterns the machine identifies.

### TYPES OF PROBLEMS TO WHICH IT’S SUITED

- CLUSTERING: Identifying similarities in groups
- ANOMALY DETECTION: Identifying anomalies in data

<!-- page: 29 -->
![Hinh: fig-29-1]

## ARTIFICIAL INTELLIGENCE IS NOT NEW

### ARTIFICIAL INTELLIGENCE

Any technique which enables computers to mimic human behavior

### MACHINE LEARNING

AI techniques that give computers the ability to learn without being explicitly programmed to do so

### DEEP LEARNING

A subset of ML which make the computation of multi-layer neural networks feasible

1950s → 1960s → 1970s → 1980s → 1990s → 2000s → 2010s

<!-- page: 30 -->
## TẠI SAO BÂY GIỜ LẠI NÓI VỀ A.I?

<!-- page: 31 -->
## DỮ LIỆU LỚN!

<!-- page: 32 -->
## A.I – TRÍ TUỆ NHÂN TẠO LÀ GÌ?

- Dữ Liệu – Data

<!-- page: 33 -->
![Hinh: fig-33-1]

DATA

SORTED

ARRANGED

PRESENTED VISUALLY

<!-- page: 34 -->
## VÍ DỤ CỦA BẢNG SỐ LIỆU (TẬP DỮ LIỆU - DATASET)

| Diện tích căn nhà (m2) | Giá nhà (tỷ đồng) |
| --- | --- |
| 100 | 4.5 |
| 150 | 6.0 |
| 135 | 5.5 |
| 200 | 6.7 |
| 500 | 10 |
| 600 | 15 |
| 1,000 | 20 |

A → B

<!-- page: 35 -->
## VÍ DỤ CỦA BẢNG SỐ LIỆU (TẬP DỮ LIỆU - DATASET)

| Diện tích căn nhà (m2) | Số lượng phòng ngủ | Giá nhà (tỷ đồng) |
| --- | --- | --- |
| 100 | 3 | 4.5 |
| 150 | 4 | 6.0 |
| 135 | 4 | 5.5 |
| 200 | 5 | 6.7 |
| 500 | 5 | 10 |
| 600 | 6 | 15 |
| 1,000 | 8 | 20 |

A → B

<!-- page: 36 -->
## VÍ DỤ CỦA BẢNG SỐ LIỆU (TẬP DỮ LIỆU - DATASET)

| Diện tích căn nhà (m2) | Số lượng phòng ngủ | Giá nhà (tỷ đồng) |
| --- | --- | --- |
| 100 | 3 | 4.5 |
| 150 | 4 | 6.0 |
| 135 | 4 | 5.5 |
| 200 | 5 | 6.7 |
| 500 | 5 | 10 |
| 600 | 6 | 15 |
| 1,000 | 8 | 20 |

B → A

<!-- page: 37 -->
## VÍ DỤ CỦA BẢNG SỐ LIỆU (TẬP DỮ LIỆU - DATASET)

| Hình ảnh | Nhãn |
| --- | --- |
| ![Hinh: fig-37-1] | Mèo |
| ![Hinh: fig-37-2] | Không phải mèo |
| ![Hinh: fig-37-3] | Mèo |
| ![Hinh: fig-37-4] | Không phải mèo |

<!-- page: 38 -->
## VÍ DỤ CỦA BẢNG SỐ LIỆU - (TẬP DỮ LIỆU - DATASET)

| Hình ảnh | Nhãn |
| --- | --- |
| ![Hinh: fig-38-1] | Mèo |
| ![Hinh: fig-38-2] | Không phải mèo |
| ![Hinh: fig-38-3] | Mèo |
| ![Hinh: fig-38-4] | Không phải mèo |

A → B

<!-- page: 39 -->
## THU THẬP DỮ LIỆU (ACQUIRING)

![Hinh: fig-39-1]
![Hinh: fig-39-2]
![Hinh: fig-39-3]
![Hinh: fig-39-4]

### DÁN NHÃN THỦ CÔNG

Mèo

Mèo

Không phải Mèo

Không phải Mèo

<!-- page: 40 -->
## THU THẬP DỮ LIỆU (ACQUIRING)

- QUAN SÁT HÀNH VI

![Hinh: fig-40-1]

<!-- page: 41 -->
## THU THẬP DỮ LIỆU (ACQUIRING)

- QUAN SÁT HÀNH VI

A

B

![Hinh: fig-41-1]

- LƯU GIỮ XUỐNG TỪ WEBSITES/ĐỐI TÁC

<!-- page: 42 -->
## SỬ DỤNG DỮ LIỆU HIỆU QUẢ

Đừng “ném” dữ liệu bạn có cho đội nhóm AI và tự cho rằng nó sẽ có giá trị!

<!-- page: 43 -->
## VẤN ĐỀ CỦA DỮ LIỆU

- Vào thế nào, ra như vậy !

Garbage in, garbage out!

<!-- page: 44 -->
## VẤN ĐỀ CỦA DỮ LIỆU

- Dữ liệu có vấn đề của nó!
- Sai lệch nhãn
- Thiếu giá trị

Diện tích căn nhà (m2)

Số lượng phòng ngủ

Giá nhà (tỷ đồng)

100
150
135
200
500
#Không biết
1,000

3
4
4
#Không biết
5
6
#Không biết

4.5
#0.09
5.5
6.7
10
#Không biết
20

<!-- page: 45 -->
## VẤN ĐỀ CỦA DỮ LIỆU

- Đa dạng về loại dữ liệu
- Hình ảnh, âm thanh, câu chữ (Dữ liệu Phi cấu trúc Un-structed)

Dữ liệu có cấu trúc (Structed data)

<!-- page: 46 -->
![Hinh: fig-46-1]

ROBBIE, STOP MISBEHAVING OR WILL SEND YOU BACK TO DATA CLEANING!

MACHINE LEARNING CLASS

DIRTY DATA

<!-- page: 47 -->
## A.I – TRÍ TUỆ NHÂN TẠO LÀ GÌ ?

- Các Thuật ngữ trong AI – The terminology of AI

<!-- page: 48 -->
## HỌC MÁY vs. KHOA HỌC DỮ LIỆU

Machine Learning vs. Data Science

| Diện tích căn nhà (m2) | Số lượng phòng ngủ | Số lượng phòng tắm | Mới sửa chữa | Giá nhà (tỷ đồng) |
| --- | --- | --- | --- | --- |
| 100 | 3 | 2 | N | 4.5 |
| 150 | 4 | 3 | Y | 5.0 |
| 135 | 4 | 3 | Y | 5.5 |
| 200 | 5 | 4 | N | 6.7 |
| 500 | 5 | 5 | Y | 10 |
| 600 | 6 | 5 | Y | 15 |
| 1,000 | 8 | 8 | N | 20 |

<!-- page: 49 -->
## HỌC MÁY vs. KHOA HỌC DỮ LIỆU

Machine Learning vs. Data Science

| Diện tích căn nhà (m2) | Số lượng phòng ngủ | Số lượng phòng tắm | Mới sửa chữa | Giá nhà (tỷ đồng) |
| --- | --- | --- | --- | --- |
| 100 | 3 | 2 | N | 4.5 |
| 150 | 4 | 3 | N | 5.0 |
| 145 | 4 | 3 | Y | 5.5 |
| 200 | 5 | 4 | N | 6.7 |
| 500 | 5 | 5 | Y | 10 |
| 600 | 6 | 5 | Y | 15 |
| 1,000 | 8 | 8 | N | 20 |

<!-- page: 50 -->
## HỌC MÁY vs. KHOA HỌC DỮ LIỆU

### HỌC MÁY

Lĩnh vực khoa học nghiên cứu mà giúp cho các máy tính có khả năng tự học được mà không cần đến một chương trình/phần mềm cụ thể.

Arthur Samuel (1959)

PHẦN MỀM/ SOFTWARE

### KHOA HỌC DỮ LIỆU

Ngành khoa học khai thác tri thức và tìm ra những ý nghĩa ẩn từ dữ liệu.

BÁO CÁO/TỔNG HỢP

<!-- page: 51 -->
![Hinh: fig-51-1]

## HỌC SÂU

DEEP LEARNING

HỌC SÂU

<!-- page: 52 -->
## HỌC SÂU

![Hinh: fig-52-1]

#Diện tích nhà

#Số phòng ngủ

#Mới sửa

Neuron

#Giá nhà

Các phương trình toán học phức tạp

Mạng nơ-ron được thiết kế dựa trên bộ não con người, nhưng cách thức chúng vận hành thì hoàn toàn không giống cách bộ não sinh học của con người hoạt động.

<!-- page: 53 -->
## AI – TRÍ TUỆ NHÂN TẠO CÓ NHIỀU CÔNG CỤ

- Học máy và Khoa học dữ liệu
- Học sâu và Mạng nơ-ron
- Và các thuật ngữ biến khác như: Học không giám sát (Un-supervised Learning), Học tăng cường (Reinforcement Learning), mô hình đồ họa (Graphical models)…

<!-- page: 54 -->
![Hinh: fig-54-1]

## Khoa học Dữ Liệu

Trí tuệ Nhân Tạo (AI)

Học máy (ML)

Học sâu (DL)

Khoa học Dữ Liệu

<!-- page: 55 -->
## A.I – TRÍ TUỆ NHÂN TẠO LÀ GÌ ?

- Những điều ML có thể và không thể làm.

<!-- page: 56 -->
## HỌC CÓ GIÁM SÁT

| Đầu vào (Input) | Đầu ra (Output) | Ứng dụng (Applications) |
| --- | --- | --- |
| Email | Thư rác? | Bộ lọc thư rác. |
| Âm thanh | Văn bản | Nhận dạng giọng nói |
| Tiếng Anh | Tiếng Việt | Máy dịch (Machine translation) |
| Q/C, thông tin người dùng | Nhấp chuột? (0/1) | Quảng cáo online |

Những điều mà bạn có thể làm mà chỉ cần tốn 01 giây để suy nghĩ, thì sớm muộn cũng tự động hóa

<!-- page: 57 -->
![Hinh: fig-57-1]

## Supervised Learning

| Input (A) | Output (B) | Application |
| --- | --- | --- |
| email | spam? (0/1) | spam filtering |
| audio | text transcripts | speech recognition |
| English | Chinese | machine translation |
| ad, user info | click? (0/1) | online advertising |
| image, radar info | position of other cars | Self-driving car |
| image of phone | defect? (0/1) | visual inspection |

Anything you can do with 1 second of thought, we can probably now or soon automate.

<!-- page: 58 -->
## HỌC MÁY CÓ THỂ VÀ KHÔNG THỂ LÀM!

Ví dụ: Bạn đặt mua trên mạng 1 món hàng để làm quà tặng cho cháu gái của bạn nhân dịp sinh nhật của cô bé. Không may, món hàng bị giao trễ. Bạn gọi điện thoại đến tổng đài CSKH và nói: “Tôi có thể trả lại không nhận được không?” Nếu tổng đài là 01 AI (Voice chat). Chuyện gì sẽ xảy ra?

Input text

“Yêu cầu hoàn tiền”

Hoàn tiền/Phí giao hàng/Một số yêu cầu khác

A → B

“Tôi xin lỗi phải nghe thấy vậy!”

“Chúc cháu 1 ngày sinh nhật vui vẻ”

“Vâng, tôi có thể giúp gì với….”

<!-- page: 59 -->
## NẾU BẠN TIẾP TỤC CỐ GẮNG?

Đầu vào (Người dùng email) → Đầu ra (Cài đặt 2 -3 dòng tự động trả lời)

1000 ví dụ

“Cái hộp đựng của tôi bị bể?” → Cám ơn bạn đã gửi email!

“Tôi có thể viết nhận xét ở đâu?” → Cám ơn bạn đã gửi email!

“Chính sách trả hàng là ntn?” → Cám ơn bạn đã gửi email!

“Khi nào hàng của tôi được giao?” → Cám ơn bạn đã gửi email!

<!-- page: 60 -->
![Hinh: fig-60-1]

## What happens if you try?

| Input (A) | Output (B) |
| --- | --- |
| User email | 2-3 paragraph response |
| “My box was damaged.” | Thank you for your email. |
| “Where do I write a review?” | Thank you for your email. |
| “What’s the return policy?” | Thank you for your email. |
| “When is my box arriving?” | Thank you now your.... |

<!-- page: 61 -->
## CÁI GÌ GIÚP M/L TRỞ THÀNH ĐƠN GIẢN?

1. Học 1 vấn đề đơn giản? <= 1 giây
2. Cần rất nhiều dữ liệu. A → B

<!-- page: 62 -->
## A.I – TRÍ TUỆ NHÂN TẠO LÀ GÌ ?

- Những điều ML có thể và không thể làm. Thêm ví dụ!

<!-- page: 63 -->
![Hinh: fig-63-1]

## Self-driving car

### Can do

image → position of other cars

### Cannot do

- stop
- hitchhiker
- bike turn left signal

A → B

<!-- page: 64 -->
![Hinh: fig-64-1]

## Self-driving car

### Can do

image → position of other cars

A → B

### Cannot do

- stop
- hitchhiker
- bike turn left signal

1. Data
2. Need high accuracy

<!-- page: 65 -->
![Hinh: fig-65-1]

## X-ray diagnosis

### Can do

Diagnose pneumonia from ~10,000 labeled images

A → B

### Cannot do

Diagnose pneumonia from 10 images of a medical textbook chapter explaining pneumonia

<!-- page: 66 -->
## ĐIỂM MẠNH – YẾU CỦA HỌC MÁY

### HỌC MÁY CÓ THỂ LÀM RẤT TỐT KHI:

1. Học một khái niệm “đơn giản”.
2. Có sẵn nhiều dữ liệu.

### HỌC MÁY CÓ THỂ LÀ KÉM:

1. Học các khái niệm phức tạp với số lượng dữ liệu hạn chế.
2. Yêu cầu thực hiện một công việc cũ với kiểu dữ liệu mới, khác.

<!-- page: 67 -->
## A.I – TRÍ TUỆ NHÂN TẠO LÀ GÌ ?

- Học sâu (Deep Learning) Dành cho Không chuyên Kỹ thuật

<!-- page: 68 -->
![Hinh: fig-68-1]

## DỰ ĐOÁN NHU CẦU NGƯỜI DÙNG

<!-- page: 69 -->
![Hinh: fig-69-1]

## Demand prediction

price → demand

“neuron”

<!-- page: 70 -->
## DỰ ĐOÁN NHU CẦU NGƯỜI DÙNG

GIÁ BÁN (PRICE)

PHÍ VẬN CHUYỂN (SHIPPING COST)

CHI PHÍ TIẾP THỊ (MARKETING)

NGUYÊN VẬT LIỆU

NHU CẦU

<!-- page: 71 -->
## DỰ ĐOÁN NHU CẦU NGƯỜI DÙNG

GIÁ BÁN (PRICE)

PHÍ VẬN CHUYỂN (SHIPPING COST)

CHI PHÍ TIẾP THỊ (MARKETING)

NGUYÊN VẬT LIỆU

Giá hợp lý

Chất lượng

NHU CẦU

A → B

<!-- page: 72 -->
## DỰ ĐOÁN NHU CẦU NGƯỜI DÙNG

GIÁ BÁN (PRICE)

PHÍ VẬN CHUYỂN (SHIPPING COST)

CHI PHÍ TIẾP THỊ (MARKETING)

NGUYÊN VẬT LIỆU

Giá hợp lý

Chất lượng

NHU CẦU

A → B

<!-- page: 73 -->
## A.I – TRÍ TUỆ NHÂN TẠO LÀ GÌ ?

- Học sâu (Deep Learning) Dành cho Không chuyên Kỹ thuật

<!-- page: 74 -->
![Hinh: fig-74-1]

## NHẬN DẠNG KHUÔN MẶT

Face recognition

<!-- page: 75 -->
![Hinh: fig-75-1]

## Face recognition

30 32 22 22 12 10 10 12 33 35 30

12 11 12 234 170 176 13 15 12 12 234 222 299 0 230 200 222 999 230 234 56 78 190 22 990 186 112 110 110 112 180 30 32 19

These values represent the visible numeric feature grid.

<!-- page: 76 -->
![Hinh: fig-76-1]

## Face recognition

identity

A → B

1,000
1,000,000
3,000,000

3,000,060

<!-- page: 77 -->
![Hinh: fig-77-1]

## H.I: Pilot

Data is the fuel.

Machine learning algorithms are the engines.

<!-- page: 78 -->
## KIỂM TRA KIẾN THỨC

<!-- page: 79 -->
## THỰC HIỆN 1 DỰ ÁN A.I

- Giới thiệu

<!-- page: 80 -->
## THỰC HIỆN 1 DỰ ÁN A.I

- Các bước thực hiện
- Lựa chọn 1 dự án
- Tổ chức đội ngũ và cơ sở dữ liệu cho dự án.

<!-- page: 81 -->
![Hinh: fig-81-1]

## THỰC HIỆN DỰ ÁN NHẬN GIỌNG NÓI

Amazon Echo / Alexa

Google Home

Apple Siri

Baidu DuerOS

<!-- page: 82 -->
![Hinh: fig-82-1]

### Các bước chính:

1. Thu thập dữ liệu.

<!-- page: 83 -->
![Hinh: fig-83-1]

### Các bước chính:

2. Huấn luyện mô hình (Model).

Lặp đi, lặp lại cho đến khi đủ tốt.

A → B

#Giọng nói 1 --- “Hello”

#Giọng nói 2 ----”Siri”

#Giọng nói 3 – “Âm nhạc”

<!-- page: 84 -->
![Hinh: fig-84-1]

### Các bước chính:

3. Cài đặt (Deploy).

Sử dụng các dữ liệu đã có sẵn.

Duy trì và cập nhật mô hình (model)

<!-- page: 85 -->
![Hinh: fig-85-1]

## Key steps of a machine learning project

Echo / Alexa

1. Collect data
2. Train model — Iterate many times until good enough
3. Deploy model — Get data back; Maintain / update model

<!-- page: 86 -->
![Hinh: fig-86-1]

## Key steps of a machine learning project

Self-driving car

1. Collect data — image → position of other cars
2. Train model — Iterate many times until good enough
3. Deploy model — Get data back; Maintain / update model

<!-- page: 87 -->
## THỰC HIỆN 1 DỰ ÁN A.I

- Các bước thực hiện dự án Khoa học dữ liệu

<!-- page: 88 -->
![Hinh: fig-88-1]
![Hinh: fig-88-2]
![Hinh: fig-88-3]

## Ghé Trang web

Trang sản phẩm

<!-- page: 89 -->
![Hinh: fig-89-1]

## Chọn mua sản phẩm

<!-- page: 90 -->
![Hinh: fig-90-1]

## THANH TOÁN

<!-- page: 91 -->
### Các bước chính:

1. Thu thập dữ liệu.

| User ID | Khu vực | Thời gian | Website |
| --- | --- | --- | --- |
| 2009 | HCM | 08:03:15 Jan 19 | Tiki.vn |
| 2017 | HN | 14:05:00 Dec 18 | Shoppe.vn |
| 4963 | Singapore | 09:00:15 Mar 19 | Amazon.com |

<!-- page: 92 -->
![Hinh: fig-92-1]

### Các bước chính:

2. Phân tích dữ liệu. (Thử đi, thử lại)

<!-- page: 93 -->
![Hinh: fig-93-1]

### Các bước chính:

2. Phân tích dữ liệu. (Thử đi, thử lại)

<!-- page: 94 -->
![Hinh: fig-94-1]

### Các bước chính:

2. Đề xuất các hành động

Tích hợp các thay đổi (Xây mới trang web, thêm video quảng cáo, Khuyến mãi…)

Tiếp tục phân tích với dữ liệu mới.

<!-- page: 95 -->
![Hinh: fig-95-1]

## Key steps of a data science project

Manufacturing line

Mix clay → Shape mug → Add glaze → Fire kiln → Final inspection

<!-- page: 96 -->
![Hinh: fig-96-1]

## Key steps of a data science project

Manufacturing line

Mix clay → Shape mug → Add glaze → Fire kiln → Final inspection

1. Collect data
2. Analyze data — Iterate many times to get good insights
3. Suggest hypotheses/actions — Deploy changes — Re-analyze new data periodically

| Clay batch # | Supplier | Mixing time (minutes) |
| --- | --- | --- |
| 001 | ClayCo | 35 |
| 034 | GooClay | 22 |
| 109 | BrownStuff | 28 |

| Mug batch # | Humidity in kiln | Temperature in kiln (F) | Duration in kiln (hours) |
| --- | --- | --- | --- |
| 301 | 0.002% | 1410° | 22 |
| 302 | 0.003% | 1520° | 24 |
| 303 | 0.002% | 1420° | 22 |

<!-- page: 97 -->
## THỰC HIỆN 1 DỰ ÁN A.I

- Mọi vị trí công việc cần biết cách sử dụng Dữ liệu

<!-- page: 98 -->
![Hinh: fig-98-1]

## BỘ PHẬN BÁN HÀNG

Data science

Machine learning

Optimize sales funnel

Automated lead sorting

<!-- page: 99 -->
![Hinh: fig-99-1]

## BỘ PHẬN QUẢN LÝ SẢN XUẤT Ở NHÀ MÁY

Data science

Mix clay → Shape mug → Add glaze → Fire kiln → Final inspection

Optimize manufacturing line

Machine learning

ok

ok

defect

Automated visual inspection

<!-- page: 100 -->
## BỘ PHẬN TUYỂN DỤNG NHÂN SỰ

Liên hệ qua email

Phỏng vấn qua điện thoại

Phỏng vấn tại văn phòng

Tuyển dụng

### THÚY KIỀU

Thông tin cá nhân

Học vấn

Chuyên môn

Kinh nghiệm

### HOẠN THƯ

Thông tin cá nhân

Học vấn

Chuyên môn

Kinh nghiệm

Tối ưu hóa quy trình tuyển dụng

Tự động hóa quá trình đọc SYLL

ĐẠT

CHƯA ĐẠT

<!-- page: 101 -->
![Hinh: fig-101-1]

## BỘ PHẬN MARKETING

Data science

A/B testing

Machine learning

Customized product recommendation

<!-- page: 102 -->
![Hinh: fig-102-1]

## NGÀNH NÔNG NGHIỆP

Data science

Crop analytics

Machine learning

Precision weed killing

<!-- page: 103 -->
![Hinh: fig-103-1]

## AI technical tools

### Machine learning frameworks

- TensorFlow
- PyTorch
- Keras
- MXNet
- CNTK
- Caffe
- PaddlePaddle
- Scikit-learn
- R
- Weka

<!-- page: 104 -->
![Hinh: fig-104-1]

## AI technical tools

### Machine learning frameworks

- TensorFlow
- PyTorch
- Keras
- MXNet
- CNTK
- Caffe
- PaddlePaddle
- Scikit-learn
- R
- Weka

### Research publications

- Arxiv

### Open source repositories

- GitHub

<!-- page: 105 -->
![Hinh: fig-105-1]

## CPU vs. GPU

CPU: Computer processor (Central Processing Unit)

GPU: Graphics Processing Unit

## Cloud vs. On-premises

Edge

<!-- page: 106 -->
## XÂY DỰNG MỘT CÔNG TY A.I

- Trường hợp: Loa thông minh

<!-- page: 107 -->
![Hinh: fig-107-1]

## LOA THÔNG MINH

“Hey Google, Kể 1 câu truyện cười”

<!-- page: 108 -->
## “Hey Google, Kể 1 câu truyện cười”

### Các bước để thực hiện lệnh:

1. Xác nhận “Khẩu lệnh khởi động”

“Audio” “Hey Google” (0/1)

2. Nhận dạng giọng nói.

“Audio” “Kể một câu chuyện cười” (0/1)

3. Nhận dạng câu lệnh/ý định.

“Thời tiết”

“Âm nhạc”

“Thực hiện cuộc gọi”

“Kể một câu chuyện cười”

A → B

<!-- page: 109 -->
## “Hey Google, Kể 1 câu truyện cười”

### Các bước để thực hiện lệnh:

4. Thực hiện kể chuyện

CÂU KHỞI ĐỘNG (TRIGGER WORD DETECTION)

NHẬN DẠNG GIỌNG NÓI (SPEECH RECOGNATION)

NHẬN DẠNG CÂU LỆNH (INTENT RECOGNATION)

THỰC HIỆN LỆNH (EXECUTION)

QUÁ TRÌNH THỰC HIỆN CÔNG VIỆC CỦA A.I (A.I PIPELINE)

<!-- page: 110 -->
## XÂY DỰNG MỘT CÔNG TY A.I

- Trường hợp: Loa thông minh
- Thêm ví dụ

<!-- page: 111 -->
## XÂY DỰNG MỘT CÔNG TY A.I

- Trường hợp: Xe tự lái

<!-- page: 112 -->
![Hinh: fig-112-1]

“ÔTÔ TỰ LÁI”

<!-- page: 113 -->
![Hinh: fig-113-1]

## “Các bước ra quyết định lái xe”

Hình ảnh /Radar /Lidar

Xác định xe hơi

Xác định Người đi bộ

<!-- page: 114 -->
![Hinh: fig-114-1]

## “Các bước ra quyết định lái xe”

Hình ảnh /Radar /Lidar

Xác định xe hơi

Xác định Người đi bộ

Kế hoạch chuyển động

Tăng tốc

Giảm tốc

Điều chỉnh hướng

<!-- page: 115 -->
![Hinh: fig-115-1]

## Key steps:

1. Car detection

<!-- page: 116 -->
![Hinh: fig-116-1]

## Key steps:

1. Car detection
2. Pedestrian detection

<!-- page: 117 -->
![Hinh: fig-117-1]

## Key steps:

1. Car detection
2. Pedestrian detection
3. Motion planning

<!-- page: 118 -->
![Hinh: fig-118-1]

## Key steps:

1. Car detection
2. Pedestrian detection
3. Motion planning

<!-- page: 119 -->
![Hinh: fig-119-1]

## Steps for deciding how to drive

Image/Radar/Lidar → Car detection / Pedestrian detection → Motion planning → Steer/Accelerate/Brake

<!-- page: 120 -->
![Hinh: fig-120-1]

## Steps for deciding how to drive

Image/Radar/Lidar + GPS, Maps → Car detection / Pedestrian detection → Motion planning → Steer/Accelerate/Brake

<!-- page: 121 -->
![Hinh: fig-121-1]

## Steps for deciding how to drive

Image/Radar/Lidar + GPS, Maps → Car detection / Pedestrian detection → Trajectory prediction → Motion planning → Steer/Accelerate/Brake

<!-- page: 122 -->
![Hinh: fig-122-1]

## Steps for deciding how to drive

Image/Radar/Lidar + GPS, Maps → Car detection / Pedestrian detection / Lane detection → Trajectory prediction → Motion planning → Steer/Accelerate/Brake

<!-- page: 123 -->
![Hinh: fig-123-1]

## Steps for deciding how to drive

Image/Radar/Lidar + GPS, Maps → Car detection / Pedestrian detection / Lane detection / Traffic light detection → Trajectory prediction → Motion planning → Steer/Accelerate/Brake

<!-- page: 124 -->
![Hinh: fig-124-1]

## Steps for deciding how to drive

Image/Radar/Lidar + GPS, Maps → Car detection / Pedestrian detection / Lane detection / Traffic light detection / Obstacle detection → Trajectory prediction → Motion planning → Steer/Accelerate/Brake

<!-- page: 125 -->
## XÂY DỰNG MỘT CÔNG TY A.I

- Vai trò trong Nhóm AI

<!-- page: 126 -->
## Các vai trò điển hình

1. Kỹ sư Phần mềm – Software Engineer

“VD: Thực hiện lệnh kể chuyện, đảm bảo độ chính xác khi xe tự lái. ”

2. Kỹ sư Học máy (Machine Learning Engineer)

“A → B”

3. Nhà nghiên cứu Học Máy – ML Researcher

“Tăng cường khả năng của ML, tối ưu các thuật toán”

Vị trí (2) & (3) có thể gọi là: Nhà khoa học Ứng dụng ML

<!-- page: 127 -->
## Các vai trò điển hình

4. Chuyên gia Dữ liệu (Data Scientist)

Phân tích dữ liệu và cung cấp các tri thức (insights).

Tạo các báo cáo cho Nhóm

5. Kỹ sư Dữ liệu (Data Engineer)

Tổ chức dữ liệu

Thực hiện công việc để cho Dữ liệu được lưu trữ đúng cách, an toàn, dễ dàng thực hiện công việc.

6. Quản lý/Giám đốc sản phẩm AI – AI Product Manager

Hỗ trợ, đưa ra quyết định nên làm gì, xác định khả năng, giá trị sp.

<!-- page: 128 -->
## BẮT ĐẦU VỚI MỘT ĐỘI A.I NHỎ

1 Kỹ sư Dữ liệu, hoặc

1 Kỹ sư Học máy (Machine Learning Engineer), 1 Chuyên gia dữ liệu

hoặc

Chẳng có ai ….ngoài bạn !

<!-- page: 129 -->
## XÂY DỰNG MỘT CÔNG TY A.I

- Những thứ cần tránh

<!-- page: 130 -->
## CẦN TRÁNH TRONG A.I

### ĐỪNG NÊN

1. A.I sẽ giải quyết hết được mọi việc/ vấn đề
2. Thuê một vài (2-3) Kỹ sư ML và giao phó hết trách nhiệm cho họ, với mong muốn có được các ứng dụng tốt.

### NÊN

1. Thực tế AI có thể làm và không thể làm gì. Các giới hạn của Công nghệ, dữ liệu và cả tài nguyên kỹ thuật.
2. Xem xét các nguồn lực về nhân sự thấu đáo. Giữa Kỹ thuật và Kinh tế và tìm ra các lựa chọn “khả thi, giá trị”.

<!-- page: 131 -->
## CẦN TRÁNH TRONG A.I

### ĐỪNG NÊN

3. A.I sẽ hoạt động tốt ngay và luôn.
4. Duy trì các kế hoạch cũ, ứng dụng công nghệ mới mà không cần đến sự thay đổi.
5. Cần ngay 1 siêu sao AI trước khi bạn có thể thực hiện mọi thứ.

### NÊN

3. Dành thời gian cho Đội AI thực hiện các thử nghiệm, điều chỉnh cho đến khi thành công.
4. Làm việc với đội AI để lên kế hoạch thời gian, phân bổ lại nguồn lực, xây dựng các thước đo mới, những mục tiêu mới.

<!-- page: 132 -->
## XÂY DỰNG MỘT CÔNG TY A.I

- Thực hiện bước đầu tiên

<!-- page: 133 -->
## A.I VÀ CUỘC SỐNG XÃ HỘI

- Giới thiệu

<!-- page: 134 -->
## A.I VÀ CUỘC SỐNG XÃ HỘI

AI VÀ NHỮNG CÁCH HIỂU CHUNG

GIỚI HẠN CỦA AI

AI VÀ PHÁT TRIỂN KINH TẾ, CÔNG VIỆC

<!-- page: 135 -->
## A.I VÀ CUỘC SỐNG XÃ HỘI

- Nhìn nhận thực tế về AI

<!-- page: 136 -->
## NHỮNG CÁCH HIỂU CHUNG VỀ AI

KHÔNG QUÁ LẠC QUAN VỀ AI: TRÍ THÔNG MINH NHÂN TẠO SIÊU VIỆT SẼ XUẤT HIỆN. ROBOT SÁT THỦ SẼ SỚM RA ĐỜI

KHÔNG QUÁ BI QUAN VỀ AI: TRÍ THÔNG MINH NHÂN TẠO KHÔNG LÀM ĐƯỢC GÌ. CHỈ LÀ TRÀO LƯU. SẼ SỚM BỊ TÀN

CHỈ CẦN HIỂU ĐÚNG: TRÍ TUỆ NHÂN TẠO KHÔNG THỂ LÀM ĐƯỢC MỌI THỨ, NHƯNG NÓ CÓ KHẢ NĂNG GIÚP THAY ĐỔI NHIỀU LĨNH VỰC, NHIỀU NGÀNH CÔNG NGHIỆP.

<!-- page: 137 -->
![Hinh: fig-137-1]

## GIỚI HẠN CỦA AI

AI CÒN NHIỀU HẠN CHẾ. NĂNG LỰC THỰC HIỆN CÓ GIỚI HẠN

GIẢI THÍCH TẠI SAO AI LẠI ĐƯA RA 1 KẾT QUẢ LÀ KHÓ KHĂN

<!-- page: 138 -->
## GIỚI HẠN CỦA AI

BIASED AI ( ĐỊNH KIẾN AI) VÌ NHỮNG ĐỊNH KIẾN VỀ DỮ LIỆU

GIẢI THÍCH TẠI SAO AI LẠI ĐƯA RA 1 KẾT QUẢ LÀ KHÓ KHĂN

<!-- page: 139 -->
## A.I VÀ CUỘC SỐNG XÃ HỘI

- Những cách dùng AI gây hại

<!-- page: 140 -->
## NHỮNG CÁCH DÙNG AI GÂY HẠI

DeepFakes

Cắt ghép hình ảnh, phim và gán cho người khác.

PHÁ HỎNG QUYỀN RIÊNG TƯ VÀ DÂN CHỦ

Theo dõi, kiểm soát bằng các ứng dụng AI

TẠO RA THÔNG TIN GIẢ TẠO

GIẢ MẠO, TẠO RÁC THÔNG TIN, ĐÁNH CẮP

<!-- page: 141 -->
## A.I VÀ CUỘC SỐNG XÃ HỘI

- AI và KINH TẾ

<!-- page: 142 -->
![Hinh: fig-142-1]

## Developing economies

Growth / Time

Current Technology

Emerging Technology

<!-- page: 143 -->
![Hinh: fig-143-1]

## Developing economies

“Leapfrog”

<!-- page: 144 -->
![Hinh: fig-144-1]

## Developing economies

“Leapfrog”

- Mobile phones
- Mobile payments
- Online education

<!-- page: 145 -->
## CÁC QUỐC GIA ĐANG PHÁT TRIỂN ĐỀU CÓ THỂ XÂY DỰNG AI

MẶC DÙ MỸ, TRUNG QUỐC ĐANG DẪN ĐẦU VỀ NGHIÊN CỨU VÀ ỨNG DỤNG AI. TUY NHIÊN, MỌI THỨ VẪN CHƯA CHÍN MUỒI.

TẬP TRUNG PHÁT TRIỂN AI TRONG NHỮNG THẾ MẠNH QUỐC GIA

HỢP TÁC CÔNG-TƯ TRONG VIỆC TĂNG TỐC PHÁT TRIỂN AI

ĐẦU TƯ VÀO GIÁO DỤC

<!-- page: 146 -->
## A.I VÀ CUỘC SỐNG XÃ HỘI

- AI và VIỆC LÀM

<!-- page: 147 -->
![Hinh: fig-147-1]

## TÁC ĐỘNG CỦA AI LÊN VIỆC LÀM TOÀN CẦU

Jobs displaced by 2030: 400-800 mil

Jobs created by 2030: 555-890 mil

(Source: McKinsey Global Institute.)

<!-- page: 148 -->
![Hinh: fig-148-1]

## TÁC ĐỘNG CỦA AI LÊN VIỆC LÀM TOÀN CẦU

Automated for the people

Automation risk by job type, %

- Food preparation
- Construction
- Cleaning
- Driving
- Agricultural labour
- Garment manufacturing
- Personal service
- Sales
- Customer service
- Business administration
- Information technology
- Science & engineering
- Healthcare
- Hospitality & retail management
- Upper management & politics
- Teaching

[Image credit: Economist.com]

[Nedelkoska, L. and G. Quintini. (2018). Automation, skills use and training. OECD Social, Employment and Migration Working Papers, No. 202.]

<!-- page: 149 -->
## CÁM ƠN!
