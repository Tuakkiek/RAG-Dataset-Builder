<!-- page: 1 -->

# Machine Learning
Minh Pham Van
January, 2026

<!-- page: 2 -->

# Contents
Lời nói đầu
1
1
Introduction to Machine Learning
3
1.1
Overview and Definitions
. . . . . . . . . . . . . . . . . . . . . . . . . . . .
3
1.1.1
Basic Concepts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3
1.1.2
Arthur Samuel Definition (1959) . . . . . . . . . . . . . . . . . . . .
3
1.2
Formal Definition (Tom Mitchell - 1998) . . . . . . . . . . . . . . . . . . . .
3
1.2.1
Well-posed Learning Problem . . . . . . . . . . . . . . . . . . . . . .
3
1.2.2
Example: Spam Email Filter
. . . . . . . . . . . . . . . . . . . . . .
4
1.3
Classification of Machine Learning Algorithms
. . . . . . . . . . . . . . . .
4
1.3.1
Main Branches . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4
1.3.2
Deep Dive: Supervised Learning (SL)
. . . . . . . . . . . . . . . . .
4
1.4
Supervised Learning Example: Housing Price Prediction . . . . . . . . . . .
5
1.4.1
Problem Description . . . . . . . . . . . . . . . . . . . . . . . . . . .
5
1.4.2
Characteristics of Supervised Learning . . . . . . . . . . . . . . . . .
6
1.5
Unsupervised Learning (USL) . . . . . . . . . . . . . . . . . . . . . . . . . .
6
1.5.1
Characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6
Linear Regression
7
2.1
Problem Definition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7
2.1.1
Data and Goal . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7
2.1.2
Model Representation . . . . . . . . . . . . . . . . . . . . . . . . . .
8
2.2
Loss Function (Cost Function)
. . . . . . . . . . . . . . . . . . . . . . . . .
8
2.2.1
Distance Metrics . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
8
2.2.2
Objective . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
8
2.3
Optimization Derivatives . . . . . . . . . . . . . . . . . . . . . . . . . . . .
8
2.3.1
Concept of Derivative
. . . . . . . . . . . . . . . . . . . . . . . . . .
8
2.4
Gradient Descent . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
9
2.4.1
Update Rule
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
9
2.4.2
Applying to Linear Regression
. . . . . . . . . . . . . . . . . . . . .
9
2.5
Chain Rule Backpropagation . . . . . . . . . . . . . . . . . . . . . . . . . .
10
2.5.1
Computing Derivatives . . . . . . . . . . . . . . . . . . . . . . . . . .
10
3
Gradient Descent Derivation
11
3.1
Giới thiệu và Hàm GiảThuyết (Hypothesis Function)
. . . . . . . . . . . .
11
3.1.1
Tập dữ liệu huấn luyện (Training Set) . . . . . . . . . . . . . . . . .
11
3.2
Hàm Mất Mát (MSE Cost Function) . . . . . . . . . . . . . . . . . . . . . .
11
3.3
Thuật toán Gradient Descent . . . . . . . . . . . . . . . . . . . . . . . . . .
12

<!-- page: 3 -->

3.3.1
Khái niệm và Quy tắc cập nhật . . . . . . . . . . . . . . . . . . . . .
12
3.3.2
Mô phỏng quá trình hội tụ
. . . . . . . . . . . . . . . . . . . . . . .
12
3.4
Phân tích Trực quan (Intuition) . . . . . . . . . . . . . . . . . . . . . . . . .
13
3.4.1
Độlớn và Dấu của Đạo hàm
. . . . . . . . . . . . . . . . . . . . . .
13
3.4.2
Vai trò của Learning Rate (α)
. . . . . . . . . . . . . . . . . . . . .
13
3.4.3
Tiêu chuẩn dừng . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
14
3.5
Đạo hàm chi tiết cho Hồi quy Tuyến tính
. . . . . . . . . . . . . . . . . . .
14
3.5.1
Các bước chứng minh (Derivation Steps)
. . . . . . . . . . . . . . .
14
4
Logistic Regression (Classification)
15
4.1
Giới thiệu vềBài toán Phân loại (Classification)
. . . . . . . . . . . . . . .
15
4.1.1
Tại sao không dùng Linear Regression?
. . . . . . . . . . . . . . . .
15
4.2
Mô hình Logistic Regression . . . . . . . . . . . . . . . . . . . . . . . . . . .
16
4.2.1
Hàm Sigmoid . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
16
4.2.2
Ý nghĩa của đầu ra (Interpretation)
. . . . . . . . . . . . . . . . . .
17
4.3
Ranh giới Quyết định (Decision Boundary)
. . . . . . . . . . . . . . . . . .
17
4.3.1
Ví dụ: Linear Decision Boundary . . . . . . . . . . . . . . . . . . . .
17
4.3.2
Ví dụ: Non-linear Decision Boundary
. . . . . . . . . . . . . . . . .
18
4.4
Hàm Mất Mát (Cost Function) . . . . . . . . . . . . . . . . . . . . . . . . .
18
4.4.1
Tại sao không dùng MSE? . . . . . . . . . . . . . . . . . . . . . . . .
18
4.4.2
Logistic Regression Cost Function (Log Loss) . . . . . . . . . . . . .
19
4.4.3
Công thức thu gọn (Simplified Cost Function)
. . . . . . . . . . . .
19
4.5
Gradient Descent cho Logistic Regression
. . . . . . . . . . . . . . . . . . .
20
4.6
Phân loại Đa lớp (Multiclass Classification) . . . . . . . . . . . . . . . . . .
20
4.6.1
Phương pháp One-vs-All (One-vs-Rest)
. . . . . . . . . . . . . . . .
20
5
Regularization (Điều chuẩn)
22
5.1
Vấn đềOverfitting và Underfitting . . . . . . . . . . . . . . . . . . . . . . .
22
5.1.1
Định nghĩa các trạng thái của mô hình . . . . . . . . . . . . . . . . .
22
5.2
Giải pháp khắc phục Overfitting
. . . . . . . . . . . . . . . . . . . . . . . .
23
5.3
Hàm Chi phí (Cost Function) có Regularization . . . . . . . . . . . . . . . .
23
5.3.1
Trực giác (Intuition) . . . . . . . . . . . . . . . . . . . . . . . . . . .
23
5.3.2
Công thức tổng quát . . . . . . . . . . . . . . . . . . . . . . . . . . .
23
5.4
Vai trò của tham sốλ
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
24
5.5
Regularized Gradient Descent . . . . . . . . . . . . . . . . . . . . . . . . . .
24
5.5.1
Cập nhật θ0 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
24
5.5.2
Cập nhật θj (với j = 1, 2, . . . , n)
. . . . . . . . . . . . . . . . . . . .
24
6
Non-linear Hypotheses & Neural Networks
25
6.1
Non-linear Classification (Phân loại phi tuyến)
. . . . . . . . . . . . . . . .
25
6.1.1
Hạn chếcủa Linear/Logistic Regression . . . . . . . . . . . . . . . .
25
6.1.2
Ví dụ: Computer Vision (Thịgiác máy tính)
. . . . . . . . . . . . .
25
6.2
Neural Networks (Mạng Nơ-ron)
. . . . . . . . . . . . . . . . . . . . . . . .
26
6.2.1
Lịch sửvà Nguồn gốc
. . . . . . . . . . . . . . . . . . . . . . . . . .
26
6.2.2
Giảthuyết "One Learning Algorithm" . . . . . . . . . . . . . . . . .
26
6.3
Mô hình Neural Network (Model Representation) . . . . . . . . . . . . . . .
26
6.3.1
Mô phỏng Nơ-ron sinh học
. . . . . . . . . . . . . . . . . . . . . . .
26
6.3.2
Nơ-ron nhân tạo (Artificial Neuron)
. . . . . . . . . . . . . . . . . .
27

<!-- page: 4 -->

6.3.3
Kiến trúc Mạng Nơ-ron
. . . . . . . . . . . . . . . . . . . . . . . . .
28
6.4
Forward Propagation (Lan truyền xuôi) . . . . . . . . . . . . . . . . . . . .
28
6.4.1
Tính toán từng bước (Vectorized Implementation) . . . . . . . . . .
30
6.5
Trực giác vềNeural Network (Logic Gates)
. . . . . . . . . . . . . . . . . .
31
6.5.1
Ví dụđơn giản: Cổng AND . . . . . . . . . . . . . . . . . . . . . . .
31
6.5.2
Bài toán XNOR (Non-linear) . . . . . . . . . . . . . . . . . . . . . .
31
6.6
Multi-class Classification (Phân loại đa lớp) . . . . . . . . . . . . . . . . . .
34
7
Neural Network: Cost Function & Propagation
36
7.1
Tổng quan và Ký hiệu . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
36
7.1.1
Ký hiệu kiến trúc mạng . . . . . . . . . . . . . . . . . . . . . . . . .
36
7.1.2
Phân loại (Classification Types)
. . . . . . . . . . . . . . . . . . . .
36
7.2
Hàm Chi phí (Cost Function) . . . . . . . . . . . . . . . . . . . . . . . . . .
37
7.3
Forward Propagation (Lan truyền xuôi) . . . . . . . . . . . . . . . . . . . .
37
7.3.1
Các bước tính toán . . . . . . . . . . . . . . . . . . . . . . . . . . . .
37
7.4
Backward Propagation (Lan truyền ngược)
. . . . . . . . . . . . . . . . . .
38
7.4.1
Đạo hàm tại lớp đầu ra
. . . . . . . . . . . . . . . . . . . . . . . . .
38
7.4.2
Gradient của trọng sốlớp Output (W (2))
. . . . . . . . . . . . . . .
38
7.4.3
Gradient của trọng sốlớp Input/Hidden (W (1)) . . . . . . . . . . . .
39
7.5
Tổng kết Công thức Cập nhật . . . . . . . . . . . . . . . . . . . . . . . . . .
39
8
Advice for Applying Machine Learning
40
8.1
Debugging a Learning Algorithm (Gỡlỗi thuật toán học)
. . . . . . . . . .
40
8.2
Evaluating a Hypothesis (Đánh giá giảthuyết)
. . . . . . . . . . . . . . . .
40
8.2.1
Training / Test Split (Chia tập Huấn luyện / Kiểm tra) . . . . . . .
40
8.2.2
Công thức tính lỗi trên tập test . . . . . . . . . . . . . . . . . . . . .
41
8.3
Model Selection (Lựa chọn mô hình) . . . . . . . . . . . . . . . . . . . . . .
41
8.3.1
Cross Validaton . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
41
8.3.2
Quy trình lựa chọn mô hình . . . . . . . . . . . . . . . . . . . . . . .
43
8.4
Diagnosing Bias vs Variance (Chẩn đoán Độlệch và Phương sai) . . . . . .
43
8.4.1
Phân tích dựa trên đồthịlỗi
. . . . . . . . . . . . . . . . . . . . . .
44
8.5
Regularization và Bias/Variance
. . . . . . . . . . . . . . . . . . . . . . . .
44
8.6
Learning Curves (Đường cong học tập) . . . . . . . . . . . . . . . . . . . . .
45
8.6.1
Trường hợp High Bias (Underfitting) . . . . . . . . . . . . . . . . . .
45
8.6.2
Trường hợp High Variance (Overfitting) . . . . . . . . . . . . . . . .
46
8.7
Tổng kết giải pháp (Deciding What to Do Next)
. . . . . . . . . . . . . . .
47
9
Machine Learning System Design (Thiết kếhệthống học máy)
48
9.1
Building a Spam Classifier (Xây dựng bộphân loại thư rác) . . . . . . . . .
48
9.1.1
Problem Description (Mô tảbài toán) . . . . . . . . . . . . . . . . .
48
9.1.2
Feature Representation (Biểu diễn đặc trưng) . . . . . . . . . . . . .
48
9.1.3
Debugging a Learning Algorithm (Gỡlỗi thuật toán học)
. . . . . .
48
9.2
Error Analysis (Phân tích lỗi) . . . . . . . . . . . . . . . . . . . . . . . . . .
49
9.2.1
Ví dụthực tế. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
49
9.3
Error Metrics for Skewed Classes (Độđo lỗi cho lớp lệch)
. . . . . . . . . .
50
9.3.1
Vấn đềvới Accuracy (Độchính xác) . . . . . . . . . . . . . . . . . .
50
9.4
Precision and Recall (Độchính xác và Độphủ) . . . . . . . . . . . . . . . .
50
9.4.1
Định nghĩa
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
50
9.5
Trading off Precision and Recall (Đánh đổi giữa Precision và Recall) . . . .
50

<!-- page: 5 -->

9.6
F1 Score (Điểm F1)
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
51
9.6.1
Tổng quát: Fβ Score . . . . . . . . . . . . . . . . . . . . . . . . . . .
51
10 Clustering (Phân cụm)
52
10.1 Giới thiệu vềClustering . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
52
10.1.1 Các ứng dụng của Clustering . . . . . . . . . . . . . . . . . . . . . .
53
10.2 Thuật toán K-means . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
53
10.2.1 Quy trình thuật toán
. . . . . . . . . . . . . . . . . . . . . . . . . .
53
10.3 Hàm Mục tiêu (Optimization Objective) . . . . . . . . . . . . . . . . . . . .
55
10.4 Chứng minh hàm tối ưu: . . . . . . . . . . . . . . . . . . . . . . . . . . .
56
10.5 Khởi tạo ngẫu nhiên (Random Initialization)
. . . . . . . . . . . . . . . . .
56
10.6 Lựa chọn sốcụm K (Choosing the Value of K)
. . . . . . . . . . . . . . . .
57
10.6.1 Phương pháp Elbow (Khuỷu tay) . . . . . . . . . . . . . . . . . . . .
57
10.6.2 Dựa trên mục đích sử dụng (Downstream Purpose) . . . . . . . . . .
57
10.6.3 Khi nào thì sử dụng K-Means ? . . . . . . . . . . . . . . . . . . . . .
58
11 Dimensionality Reduction (Giảm chiều dữ liệu)
59
11.1 Giới thiệu vềDimensionality Reduction
. . . . . . . . . . . . . . . . . . . .
59
11.1.1 Động lực (Motivation) . . . . . . . . . . . . . . . . . . . . . . . . . .
59
11.1.2 Ví dụminh họa . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
60
11.2 Principal Component Analysis (PCA)
. . . . . . . . . . . . . . . . . . . . .
60
11.2.1 Định nghĩa bài toán . . . . . . . . . . . . . . . . . . . . . . . . . . .
60
11.2.2 Các bước thực hiện PCA
. . . . . . . . . . . . . . . . . . . . . . . .
62
11.3 Bản chất PCA
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
63
11.4 Lựa chọn sốchiều K (Choosing K) . . . . . . . . . . . . . . . . . . . . . . .
64
11.5 Lời khuyên khi áp dụng PCA . . . . . . . . . . . . . . . . . . . . . . . . . .
65
11.5.1 Khi nào nên dùng PCA? . . . . . . . . . . . . . . . . . . . . . . . . .
65
11.5.2 Sai lầm thường gặp (Bad use of PCA) . . . . . . . . . . . . . . . . .
65
12 Anomaly Detection (Phát hiện bất thường)
66
12.1 Giới thiệu vềAnomaly Detection . . . . . . . . . . . . . . . . . . . . . . . .
66
12.1.1 Ví dụminh họa: Động cơ máy bay . . . . . . . . . . . . . . . . . . .
66
12.1.2 Phương pháp Density Estimation (Ước lượng mật độ) . . . . . . . .
67
12.2 Các ứng dụng phổbiến
. . . . . . . . . . . . . . . . . . . . . . . . . . . . .
67
12.3 Gaussian (Normal) Distribution . . . . . . . . . . . . . . . . . . . . . . . . .
68
12.3.1 Hàm mật độxác suất (PDF) . . . . . . . . . . . . . . . . . . . . . .
68
12.3.2 Gaussian Distribution Example)
. . . . . . . . . . . . . . . . . . . .
68
12.3.3 Ước lượng tham số(Parameter Estimation) . . . . . . . . . . . . . .
69
12.4 Thuật toán Anomaly Detection . . . . . . . . . . . . . . . . . . . . . . . . .
70
12.5 Anomaly Detection vs Supervised Learning . . . . . . . . . . . . . . . . . .
70
12.6 Xửlý đặc trưng (Feature Engineering) . . . . . . . . . . . . . . . . . . . . .
70
12.6.1 Non-Gaussian Features
. . . . . . . . . . . . . . . . . . . . . . . . .
70
12.6.2 Error Analysis
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
71
12.7 Multivariate Gaussian Distribution (Phân phối chuẩn đa biến)
. . . . . . .
72
12.7.1 Hạn chếcủa mô hình gốc . . . . . . . . . . . . . . . . . . . . . . . .
72
12.7.2 Mô hình đa biến . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
72
12.7.3 So sánh mô hình . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
72

<!-- page: 6 -->

13 Recommender Systems (Hệthống gợi ý)
73
13.1 Problem Definition (Định nghĩa bài toán) . . . . . . . . . . . . . . . . . . .
73
13.1.1 Ví dụ: Dựđoán đánh giá phim (Predicting movie ratings) . . . . . .
73
13.2 Content-based Recommendations (Gợi ý dựa trên nội dung) . . . . . . . . .
74
13.2.1 Mô hình hóa
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
74
13.2.2 Hàm tối ưu (Optimization Objective)
. . . . . . . . . . . . . . . . .
74
13.3 Collaborative Filtering (Lọc cộng tác) . . . . . . . . . . . . . . . . . . . . .
74
13.3.1 Ý tưởng cốt lõi . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
74
13.3.2 Hàm tối ưu đồng thời (Simultaneous Optimization)
. . . . . . . . .
75
13.3.3 Thuật toán (Collaborative Filtering Algorithm) . . . . . . . . . . . .
75
13.4 Low Rank Matrix Factorization (Phân rã ma trận hạng thấp) . . . . . . . .
75
14 Support Vector Machines (SVM)
76
14.1 Optimization Objective (Mục tiêu tối ưu hóa) . . . . . . . . . . . . . . . . .
76
14.1.1 TừLogistic Regression đến SVM . . . . . . . . . . . . . . . . . . . .
76
14.1.2 Hàm chi phí của SVM . . . . . . . . . . . . . . . . . . . . . . . . . .
77
14.2 Large Margin Intuition (Trực giác vềLềlớn)
. . . . . . . . . . . . . . . . .
77
14.2.1 Điều kiện an toàn
. . . . . . . . . . . . . . . . . . . . . . . . . . . .
77
14.2.2 Decision Boundary (Ranh giới quyết định) . . . . . . . . . . . . . . .
78
14.3 Mathematics Behind Large Margin Classification (Toán học đằng sau) . . .
78
14.3.1 Inner Product . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
78
14.3.2 Tối ưu hóa Margin . . . . . . . . . . . . . . . . . . . . . . . . . . . .
78
14.4 Kernels (Hạt nhân) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
79
14.4.1 Ý tưởng Landmarks (Điểm mốc) . . . . . . . . . . . . . . . . . . . .
79
14.4.2 Gaussian Kernel (RBF Kernel) . . . . . . . . . . . . . . . . . . . . .
79
14.4.3 Ảnh hưởng của σ2 . . . . . . . . . . . . . . . . . . . . . . . . . . . .
80
14.4.4 Feature Scaling cho SVM
. . . . . . . . . . . . . . . . . . . . . . . .
80
14.5 SVM trong thực tế(Using an SVM)
. . . . . . . . . . . . . . . . . . . . . .
81
14.5.1 Các bước thực hiện . . . . . . . . . . . . . . . . . . . . . . . . . . . .
81
14.5.2 So sánh Logistic Regression và SVM . . . . . . . . . . . . . . . . . .
81
A Appendix: Summary & Cheat Sheet (Phụlục và Tóm tắt)
82
A.1 Bảng chọn lựa thuật toán (Algorithm Selection Guide) . . . . . . . . . . . .
82
A.2 Bảng ký hiệu toán học (Mathematical Notation)
. . . . . . . . . . . . . . .
82
A.3 Các bước xây dựng hệthống ML (Pipeline Checklist)
. . . . . . . . . . . .
82
A.4 Thư viện Python tham khảo
. . . . . . . . . . . . . . . . . . . . . . . . . .
83

<!-- page: 1 -->

# Lời nói đầu
Chào mừng bạn đọc đến với thếgiới của Machine Learning (Học máy).
Trong kỷnguyên sốhóa hiện nay, Trí tuệnhân tạo (AI) và Học máy không còn là những
khái niệm viễn tưởng mà đã hiện hữu trong từng ngóc ngách của đời sống và công nghệ. Từ
những hệthống gợi ý phim ảnh, xe tựhành, đến các công cụchẩn đoán y khoa, Machine
Learning đang thay đổi cách chúng ta giải quyết các vấn đềphức tạp.
Mục đích của cuốn sách
Cuốn sách này được mình biên soạn dựa trên các ghi chú và bài giảng nền tảng từkhóa
học ML của Standford, với mục tiêu trởthành **tấm bản đồnhập môn** cho những ai
mới bắt đầu bước chân vào lĩnh vực rộng lớn này. Chúng tôi tập trung hệthống hóa các
khái niệm cốt lõi, từcác thuật toán cơ bản như Linear Regression, Logistic Regression đến
các kiến thức phức tạp hơn như Neural Networks, Support Vector Machines (SVM) hay
Dimensionality Reduction.
Mục tiêu của mình không phải là bao quát toàn bộtri thức nhân loại vềAI, mà là giúp
bạn xây dựng một **tư duy toán học vững chắc** và hiểu rõ **bản chất bên dưới** của
các dòng lệnh.
Phạm vi kiến thức và Lời khuyên
Điều quan trọng cần nhấn mạnh: **Những gì trình bày trong cuốn sách này chỉlà những
kiến thức rất cơ bản.**
Lĩnh vực Machine Learning phát triển với tốc độchóng mặt. Những thuật toán "stateof-the-art" (tiên tiến nhất) hôm nay có thểtrởnên lỗi thời vào ngày mai. Do đó, cuốn sách
này không thểthay thếcho quá trình tựrèn luyện liên tục. Đểthực sựlàm chủcông nghệ
này, bạn đọc cần:
1. Chủđộng đào sâu: Hãy coi các công thức và khái niệm ởđây là từkhóa. Bạn cần
chủđộng tìm đọc thêm các tài liệu chuyên sâu, các bài báo khoa học (papers) và sách
giáo trình nâng cao đểhiểu tường tận các biến thểvà cải tiến của chúng.
2. Thực hành không ngừng: Lý thuyết chỉlà màu xám. Hãy bắt tay vào viết code
(sử dụng Python, NumPy, PyTorch, TensorFlow...) đểhiện thực hóa các thuật toán
này. Chỉkhi tựtay gỡlỗi (debug) một mô hình, bạn mới thực sựhiểu nó hoạt động
ra sao.
3. Tư duy phản biện: Đừng chỉáp dụng thuật toán một cách máy móc. Hãy luôn
đặt câu hỏi: "Tại sao lại dùng thuật toán này?", "Dữliệu này có phù hợp không?",
"Làm sao đểcải thiện độchính xác?".

<!-- page: 2 -->

Mình hy vọng cuốn sách này sẽlà viên gạch đầu tiên vững chắc, giúp bạn tựtin xây
dựng nên những công trình tri thức đồsộhơn trong tương lai.
Chúc các bạn kiên trì và tìm thấy niềm vui trong hành trình chinh phục tri thức.
Minh Pham Van
(Ngày 3 tháng 1 năm 2026)

<!-- page: 3 -->

# Chapter 1: Introduction to Machine Learning
## 1.1 Overview and Definitions
### 1.1.1 Basic Concepts
Giới thiệu sơ lược vềbối cảnh và ứng dụng của Machine Learning (ML).
- Ứng dụng của ML: Lọc email spam, database mining, và các ứng dụng không thể
lập trình thủcông (Application can’t program by hand).
- Nguồn gốc: ML phát triển từAI (Artificial Intelligence). ML là một tập con của
AI.
- Cấu thành của AI: AI bao gồm FS (Fuzzy Systems?), ML (Machine Learning), ES
(Expert Systems).
### 1.1.2 Arthur Samuel Definition (1959)
Định nghĩa cổđiển vềMachine Learning:
"Machine Learning: Field of study that gives computers the ability to learn
without being explicitly programmed."
Ghi chú:
- Explicitly: Lập trình tường minh.
- Implicitly: Lập trình không tường minh (ML hướng tới điều này).
## 1.2 Formal Definition (Tom Mitchell - 1998)
### 1.2.1 Well-posed Learning Problem
Tom Mitchell đưa ra định nghĩa hiện đại và chặt chẽhơn vềML:
"A computer program is said to learn from experience E with respect to some
task T and some performance measure P, if its performance on T, as measured
by P, improves with experience E."

<!-- page: 4 -->

Quy trình lặp lại (Loop):
Experience (E) →Task (T) →Performance (P) →E . . .
(E giải quyết task T đánh giá bởi P và cải thiện E...)
### 1.2.2 Example: Spam Email Filter
Phân tích các thành phần T, P, E trong bài toán lọc thư rác (Spam Filter):
- Context: Chương trình email theo dõi xem bạn đánh dấu email nào là spam hoặc
không phải spam, và dựa vào đó học cách lọc spam tốt hơn.
- Task (T): Classifying emails as spam or not spam (Phân loại email).
- Experience (E): Watching you label emails as spam or not spam (Quan sát người
dùng gán nhãn).
- Performance (P): The number (or fraction) of emails correctly classified as spam/not
spam (Tỉlệphân loại đúng).
## 1.3 Classification of Machine Learning Algorithms
### 1.3.1 Main Branches
Dựa vào cách học và dữ liệu đầu vào, ML được chia thành các nhánh chính sau:
1. Supervised Learning (SL) - Học có giám sát
2. Unsupervised Learning (USL) - Học không giám sát
3. Reinforcement Learning (RL) - Học tăng cường
Ngoài ra còn có Recommender Systems, Random Forest (RF), và các thuật toán lai (hybrid)
ngày nay.
### 1.3.2 Deep Dive: Supervised Learning (SL)
Trong Supervised Learning, chúng ta chia nhỏthành:
- Regression (Hồi quy): Dùng cho dữ liệu đầu ra liên tục (continuous).
- Classification (Phân loại): Dùng cho dữ liệu đầu ra rời rạc (discrete).

<!-- page: 5 -->

ML
SL
Regression
(Continuous)
Classification
(Discrete)
USL
RL
![Hinh: fig-11-1]
Figure 1.1: Sơ đồphân loại các thuật toán Machine Learning
## 1.4 Supervised Learning Example: Housing Price Prediction
### 1.4.1 Problem Description
Ví dụvềdự đoán giá nhà dựa trên diện tích (Size in feet).
- Trục tung (Y): Price ($ in 1000’s) - Giá trịliên tục.
- Trục hoành (X): Size in feet (500, 1000, 1500, . . . ).
- Dataset: Các điểm đánh dấu X (crosses) trên biểu đồlà thông tin thu thập được từ
thực tế.
![Hinh: fig-11-2]
Figure 1.2: Housing Price Prediction Plot (Regression Problem)

<!-- page: 6 -->

### 1.4.2 Characteristics of Supervised Learning
Dựa trên ví dụnày, ta rút ra đặc điểm của SL:
- Với Supervised Learning, các đáp án đúng (output/label) đã có sẵn trong dataset.
- Mục tiêu là tìm ra mối quan hệ(đường cong hoặc đường thẳng) khớp với các điểm
dữ liệu này đểdự đoán giá trịmới (ví dụ: nhà 750 feet có giá bao nhiêu?).
## 1.5 Unsupervised Learning (USL)
### 1.5.1 Characteristics
Khác với SL, Unsupervised Learning (USP/USL):
- Chỉdựa vào các đặc trưng (features) và phân phối của các điểm dữ liệu đầu vào.
- Cơ chế: Learn from input data →find hidden patterns →output.
- Không có nhãn (labels) hay đáp án đúng trước.
![Hinh: fig-12-1]
Figure 1.3: Minh họa Unsupervised Learning (Phân cụm dữ liệu)

<!-- page: 7 -->

# Chapter 2: Linear Regression
## 2.1 Problem Definition
### 2.1.1 Data and Goal
Bài toán Linear Regression (Hồi quy tuyến tính) bắt đầu với dữ liệu đầu vào (Features) và
giá trịcần dự đoán (Label).
- Input (Features): Dữliệu đầu vào (ví dụ: Diện tích nhà - Area).
- Output (Label): Giá trịthực tế(ví dụ: Giá nhà - Price).
- Goal: Tìm hàm f(x) sao cho "fit" (khớp) nhất với dữ liệu đã cho.

| Features (Area) | Label (Price) |
| --- | --- |
| 6.7 | 9.1 |
| 4.6 | 5.9 |
| 3.5 | 4.6 |
| 5.5 | 6.7 |

*Table 2.1: Bảng dữ liệu ví dụ(Area vs Price)*

![Hinh: fig-13-1]
Figure 2.1: Minh họa mô hình dự đoán

<!-- page: 8 -->

### 2.1.2 Model Representation
Hàm tuyến tính cần tìm có dạng:
ˆy = f(x) = ax + b
Trong đó:
- ˆy: Giá trịdự đoán.
- a, b: Các tham sốcần tìm dựa trên dữ liệu.
## 2.2 Loss Function (Cost Function)
### 2.2.1 Distance Metrics
Đểđánh giá độsai lệch giữa giá trịdự đoán (ˆy) và giá trịthực (y), ta dùng hàm khoảng
cách (Distance):
1. Mean Absolute Error (MAE): |ˆy −y|
2. Mean Squared Error (MSE): (ˆy −y)2
Lựa chọn: Người ta thường chọn cách (2) (ˆy −y)2 vì việc tính đạo hàm dễdàng hơn phục
vụcho tối ưu hóa.
### 2.2.2 Objective
Mục tiêu của bài toán là tìm cực tiểu (minimum) của hàm khoảng cách:
L = (ˆy −y)2 →min
## 2.3 Optimization Derivatives
### 2.3.1 Concept of Derivative
Đểtìm cực tiểu, ta sử dụng đạo hàm. Đạo hàm thểhiện sựbiến thiên của hàm số. Tại
điểm cực trị(cực tiểu hoặc cực đại), đạo hàm bằng 0.

<!-- page: 9 -->

![Hinh: fig-15-1]
Figure 2.2: Minh họa tìm cực tiểu bằng đạo hàm
dy
dx = f′(x) = 0 →Điểm cực trị
Mục tiêu là di chuyển các tham sốsao cho giá trịhàm sốđi dần vềđiểm cực tiểu.
## 2.4 Gradient Descent
### 2.4.1 Update Rule
Đểcập nhật tham sốnhằm giảm thiểu sai số, ta sử dụng thuật toán Gradient Descent. Quy
tắc cập nhật tổng quát:
xnew = xold −η · d
dxf(x)
Trong đó η (eta) là Learning rate (tốc độhọc). Cần điều chỉnh η phù hợp đểviệc cập
nhật chính xác hơn.
### 2.4.2 Applying to Linear Regression
Áp dụng cho các tham sốa và b của hàm f(x) = ax + b với hàm mất mát L = (ˆy −y)2:
anew = aold −ηdL
da
(2.1)
bnew = bold −ηdL
db
(2.2)

<!-- page: 10 -->

![Hinh: fig-16-1]
Figure 2.3: Minh họa cập nhật trọng sốcho a và b
## 2.5 Chain Rule Backpropagation
### 2.5.1 Computing Derivatives
Sửdụng Chain Rule (quy tắc chuỗi) đểtính đạo hàm của hàm L theo a và b.
Sơ đồtính toán:
x, a, b
hàm f
−−−−→ˆy hàm L
−−−−→Loss
Đạo hàm chi tiết: Ta có L = (ˆy −y)2. Đạo hàm của L theo ˆy:
dL
dˆy = 2(ˆy −y)
1. Đạo hàm theo a:
dL
da = dL
dˆy · dˆy
da = 2(ˆy −y) · x
2. Đạo hàm theo b:
dL
db = dL
dˆy · dˆy
db = 2(ˆy −y) · 1 = 2(ˆy −y)
Kết luận:
- a và b là các tham sốcần cập nhật.
- x và y là dữ liệu thực tế(hằng sốtrong quá trình đạo hàm).
- (ˆy −y) là thành phần đạo hàm theo y (gradient).

<!-- page: 11 -->

# Chapter 3: Gradient Descent Derivation
## 3.1 Giới thiệu và Hàm GiảThuyết (Hypothesis Function)
Trong bài toán Hồi quy tuyến tính (Linear Regression), chúng ta khởi đầu với một hàm giả
thuyết tuyến tính (Linear Hypothesis Function). Đây là hàm sốthực hiện việc ánh xạdữ
liệu đầu vào sang đầu ra dự đoán.
Hàm giảthuyết được định nghĩa như sau:
h(x) = θ0 + θ1x
(3.1)
Lưu ý thuật ngữ:
- Linear: Mô hình dùng cho dữ liệu có tính chất biến đổi tuyến tính.
- Regression: Ám chỉbài toán có đầu ra là các giá trịliên tục (continuous).
Mục tiêu cốt lõi là tìm kiếm các giá trịcủa tham sốθ0 và θ1 sao cho hàm giảthuyết
khớp ("fit") tốt nhất với tập dữ liệu huấn luyện (training set).
### 3.1.1 Tập dữ liệu huấn luyện (Training Set)
Đểhuấn luyện mô hình, ta cần tập dữ liệu bao gồm các cặp (x, y), trong đó x là đầu vào
và y là đầu ra thực tế.
Ký hiệu cho mẫu huấn luyện thứi là (x(i), y(i)).
Cảnh báo quan trọng: Ký hiệu (i) ởđây chỉlà chỉsốthứtựcủa mẫu huấn
luyện, tuyệt đối không được nhầm lẫn là sốmũ.
## 3.2 Hàm Mất Mát (MSE Cost Function)
Đểđánh giá độlệch giữa giá trịdự đoán bởi hàm giảthuyết và giá trịthực tế, ta sử dụng
Hàm chi phí (Cost Function), cụthểlà Sai sốBình phương Trung bình (Mean Squared
Error - MSE).
Công thức của hàm chi phí J(θ):
J(θ) = 1
m
m
X
i=1
(hθ(x(i)) −y(i))2
(3.2)
Giải thích các biến số:

<!-- page: 12 -->

- m: Sốlượng mẫu dữ liệu huấn luyện.
- x(i): Vector đầu vào của mẫu thứi.
- y(i): Nhãn lớp (class label) của mẫu thứi.
- θ: Các tham sốtrọng số(weights) (θ0, θ1, . . . ).
- hθ(x(i)): Giá trịdự đoán của thuật toán cho mẫu thứi.
Nhiệm vụtrong hầu hết các bài toán học máy là tìm θ đểcực tiểu hóa J(θ), biểu diễn
toán học là minθ J(θ).
## 3.3 Thuật toán Gradient Descent
Làm thếnào đểchọn đúng giá trịθ giúp giảm thiểu hàm mất mát? Nếu chọn ngẫu nhiên,
ta không thểbiết khi nào mới tìm được giá trịtối ưu. Giải pháp là sử dụng thuật toán
Gradient Descent.
### 3.3.1 Khái niệm và Quy tắc cập nhật
Xét trường hợp đơn giản với hàm chi phí J(θ) = θ2.
- Tại θ = 0, J(θ) đạt cực tiểu.
- Giảsửkhởi tạo θ = 3. Làm sao thuật toán biết cần di chuyển θ vềhướng nào và bao
nhiêu?
Gradient Descent là thuật toán lặp. Tại mỗi bước, ta áp dụng quy tắc cập nhật (với :=
là phép gán):
θ := θ −α d
dθJ(θ)
(3.3)
Trong đó α là learning rate (tốc độhọc). Ví dụ, gán α = 0.1. Đạo hàm của J(θ) = θ2
là 2θ.
### 3.3.2 Mô phỏng quá trình hội tụ
Hình dưới đây minh họa hàm J(θ) và giá trịcủa θ qua 10 vòng lặp. Các dấu "x" thểhiện
quá trình tham sốdi chuyển dần vềđáy của parabol (điểm cực tiểu).
Dưới đây là bảng sốliệu chi tiết cho thấy sai sốgiảm dần về0:

| Iteration | θ (current) | Gradient $\frac{dJ(θ)}{dθ}$ | Update Amount (α × 2θ) |
| --- | ---: | ---: | ---: |
| 0 | 3 | 6 | 0.6 |
| 1 | 2.4 | 4.8 | 0.48 |
| 2 | 1.92 | 3.84 | 0.384 |
| 3 | 1.536 | 3.072 | 0.307 |
| 4 | 1.229 | 2.458 | 0.246 |
| 5 | 0.983 | 1.966 | 0.197 |
| 6 | 0.786 | 1.572 | 0.157 |
| 7 | 0.629 | 1.258 | 0.126 |
| 8 | 0.503 | 1.006 | 0.101 |
| 9 | 0.403 | 0.806 | 0.081 |

0
3
6
0.6
1
2.4
4.8
0.48
2
1.92
3.84
0.384
3
1.536
3.072
0.307
4
1.229
2.458
0.246
5
0.983
1.966
0.197
6
0.786
1.572
0.157
7
0.629
1.258
0.126
8
0.503
1.006
0.101
9
0.403
0.806
0.081

<!-- page: 13 -->

![Hinh: fig-19-1]
Figure 3.1: Minh họa các bước cập nhật
## 3.4 Phân tích Trực quan (Intuition)
Tại sao quy tắc cập nhật theo Gradient lại đảm bảo hàm mất mát chạy vềcực tiểu?
### 3.4.1 Độlớn và Dấu của Đạo hàm
Đạo hàm biểu thịđộdốc (slope):
- Độlớn: Đạo hàm lớn nghĩa là dốc đứng →bước di chuyển lớn. Đạo hàm nhỏnghĩa
là hàm phẳng →bước di chuyển nhỏ.
- Dấu (Hướng):
- Đạo hàm dương: Hàm đang tăng, cần giảm θ (đi ngược chiều dương).
- Đạo hàm âm: Hàm đang giảm, cần tăng θ (đi ngược chiều âm).
→Nguyên tắc: Luôn di chuyển θ ngược dấu với Gradient.
### 3.4.2 Vai trò của Learning Rate (α)
Nếu chỉcập nhật bằng giá trịGradient, bước nhảy có thểquá lớn gây dao động. Ta dùng
α (hyperparameter) nhân với gradient đểđiều chỉnh tốc độ.
- Gradient lớn →nên dùng α nhỏđểhãm lại.
- Có thểtinh chỉnh α qua từng iteration.

<!-- page: 14 -->

### 3.4.3 Tiêu chuẩn dừng
1. Chọn sốvòng lặp cốđịnh (10, 20, 100...).
2. So sánh θ giữa các epoch: Nếu thay đổi không đáng kểthì dừng.
3. Có nhiều phương pháp dừng phức tạp khác.
## 3.5 Đạo hàm chi tiết cho Hồi quy Tuyến tính
Với hàm giảthuyết h(x) = θ0 + θ1x, ta cần cập nhật từng tham sốbằng đạo hàm riêng:
### 3.5.1 Các bước chứng minh (Derivation Steps)
Xét hàm mục tiêu:
J(θ0, θ1) = 1
m
m
X
i=1
(hθ(x(i)) −y(i))2
Bước 1 (Tính tuyến tính): Đạo hàm của tổng bằng tổng các đạo hàm.
∂J
∂θ0
= 1
m
m
X
i=1
∂
∂θ0
(hθ(x(i)) −y(i))2
Bước 2 (Chain Rule): Áp dụng quy tắc chuỗi
d
dxf(g(x)) = f′(g(x))g′(x).
= 1
m
m
X
i=1
2(hθ(x(i)) −y(i)) · ∂
∂θ0
(hθ(x(i)) −y(i))
Bước 3 (Đạo hàm hàm hợp): Vì hθ(x(i)) = θ0 + θ1x(i), đạo hàm riêng theo θ0 là 1.
∂
∂θ0
(. . . ) = 1
Kết quảcho θ0:
∂J
∂θ0
= 2
m
m
X
i=1
(hθ(x(i)) −y(i))
(3.4)
Tương tựvới θ1, nhưng đạo hàm riêng của hàm hợp theo θ1 là x(i):
∂J
∂θ1
= 2
m
m
X
i=1
(hθ(x(i)) −y(i)) · x(i)
(3.5)

<!-- page: 15 -->

# Chapter 4: Logistic Regression (Classification)
## 4.1 Giới thiệu vềBài toán Phân loại (Classification)
Trong Machine Learning, bài toán phân loại (Classification) là bài toán dự đoán đầu ra rời
rạc (discrete values). Các ví dụphổbiến bao gồm:
- Email: Spam (Thư rác) hay Not Spam (Không phải thư rác)?
- Giao dịch trực tuyến: Lừa đảo (Fraudulent - Yes) hay Không (No)?
- Khối u (Tumor): Ác tính (Malignant) hay Lành tính (Benign)?
Trong bài toán Phân loại Nhịphân (Binary Classification), ta quy ước:
- y ∈{0, 1}
- 0: "Negative Class" (ví dụ: khối u lành tính - benign tumor).
- 1: "Positive Class" (ví dụ: khối u ác tính - malignant tumor).
### 4.1.1 Tại sao không dùng Linear Regression?
Xét ví dụdự đoán khối u dựa trên kích thước (Tumor Size).
Nếu ta áp dụng Linear
Regression (hθ(x) = θT x) và chọn ngưỡng (threshold) là 0.5:
- Nếu hθ(x) ≥0.5 →dự đoán y = 1.
- Nếu hθ(x) < 0.5 →dự đoán y = 0.
Vấn đề(Outlier Issue):
- Ban đầu, Linear Regression có thểhoạt động ổn.
- Tuy nhiên, nếu xuất hiện một điểm dữ liệu có kích thước khối u rất lớn (cực phải
trên đồthị- dữ liệu chuẩn, không phải nhiễu). Đường hồi quy sẽbị"kéo" nghiêng về
phía dữ liệu đó đểgiảm thiểu sai số.
- Kết quả: Ngưỡng 0.5 bịdịch chuyển, khiến các điểm dữ liệu bên trái (đang được phân
loại đúng) bịphân loại sai thành lành tính.
- Kết luận: Linear Regression không phù hợp vì nó nhạy cảm với dữ liệu ngoại lai và
giá trịdự đoán có thểvượt ra ngoài khoảng [0, 1].

<!-- page: 16 -->

![Hinh: fig-22-1]
Figure 4.1: Minh họa outlier với Linear Regression
## 4.2 Mô hình Logistic Regression
Đểgiải quyết vấn đềtrên, ta cần một hàm giảthuyết (hypothesis) luôn trảvềgiá trịtrong
khoảng 0 ≤hθ(x) ≤1. Ta sử dụng Hàm Sigmoid (hay Logistic function).
### 4.2.1 Hàm Sigmoid
Công thức hàm giảthuyết:
hθ(x) = g(θT x) =
1
1 + e−θT x
(4.1)
Trong đó g(z) là hàm Sigmoid:
g(z) =
1
1 + e−z
(4.2)
![Hinh: fig-22-2]
Figure 4.2: Đồthịhàm sigmoid.
Đặc điểm của hàm Sigmoid:
- Biến đổi giá trịliên tục vô hạn (z ∈[−∞, +∞]) vềkhoảng [0, 1].

<!-- page: 17 -->

- Đồthịhình chữS (S-shaped), rất mượt ("smooth").
- Đạo hàm dễtính toán: g′(z) = g(z)(1 −g(z)).
- Được sử dụng như một ràng buộc (constraints) đểquy vềbài toán xác suất.
### 4.2.2 Ý nghĩa của đầu ra (Interpretation)
Giá trịhθ(x) được hiểu là xác suất ước lượng đểy = 1 với đầu vào x:
hθ(x) = P(y = 1|x; θ)
(4.3)
Ví dụ: Nếu x là kích thước khối u và hθ(x) = 0.7, điều này có nghĩa là "Bệnh nhân có
70% nguy cơ khối u là ác tính".
Vì đây là bài toán nhịphân (tổng xác suất bằng 1), ta có:
P(y = 0|x; θ) = 1 −P(y = 1|x; θ) = 1 −hθ(x)
(4.4)
## 4.3 Ranh giới Quyết định (Decision Boundary)
Mặc dù hàm Sigmoid trảvềxác suất, ta cần một ngưỡng đểđưa ra quyết định cuối cùng
(y = 1 hoặc y = 0). Thông thường ta chọn ngưỡng 0.5:
- Dựđoán y = 1 nếu hθ(x) ≥0.5 ⇒θT x ≥0 (vì g(z) ≥0.5 khi z ≥0).
- Dựđoán y = 0 nếu hθ(x) < 0.5 ⇒θT x < 0.
![Hinh: fig-23-1]
Figure 4.3: Minh họa decision boundary.
### 4.3.1 Ví dụ: Linear Decision Boundary
Xét hàm giảthuyết với tham sốθ = [−3, 1, 1]T :
hθ(x) = g(−3 + x1 + x2)
Ta dự đoán y = 1 khi:
−3 + x1 + x2 ≥0 ⇒x1 + x2 ≥3
Đường thẳng x1 + x2 = 3 chính là Decision Boundary.

<!-- page: 18 -->

- Phần bên phải/trên đường thẳng (x1 + x2 ≥3) là vùng dự đoán y = 1.
- Phần bên trái/dưới đường thẳng (x1 + x2 < 3) là vùng dự đoán y = 0.
Lưu ý: Trong thực tế, các tham sốθ được học thông qua thuật toán (như Gradient Descent)
chứkhông phải chọn cốđịnh.
### 4.3.2 Ví dụ: Non-linear Decision Boundary
Đểphân loại dữ liệu phức tạp hơn (ví dụphân bốhình tròn), ta có thểthêm các đặc trưng
bậc cao (polynomial features). Xét giảthuyết:
hθ(x) = g(θ0 + θ1x1 + θ2x2 + θ3x2
1 + θ4x2
2)
Giảsửta học được θ = [−1, 0, 0, 1, 1]T , khi đó điều kiện dự đoán y = 1 là:
−1 + x2
1 + x2
2 ≥0 ⇒x2
1 + x2
2 ≥1
Đây là phương trình đường tròn bán kính 1.
- Bên ngoài đường tròn: y = 1.
- Bên trong đường tròn: y = 0.
- Bản chất: Tuy biểu thức θT x là hàm tuyến tính, nhưng g là hàm phi tuyến -> biến
nó thành hàm phi tuyến -> h là hàm phi tuyến.
## 4.4 Hàm Mất Mát (Cost Function)
Ta có tập dữ liệu huấn luyện m mẫu: {(x(1), y(1)), . . . , (x(m), y(m))}. Làm thếnào đểchọn
tham sốθ?
### 4.4.1 Tại sao không dùng MSE?
Nếu dùng hàm Mean Squared Error (như Linear Regression):
J(θ) = 1
m
m
X
i=1
1
2(hθ(x(i)) −y(i))2
(1/2 ởđây chỉlà đểđạo hàm triệt tiêu, không có cũng chẳng sao)
Do hθ(x) là hàm Sigmoid (phi tuyến), hàm J(θ) sẽtrởthành Non-convex (không lồi).
- Non-convex: Có nhiều cực trịđịa phương (local optima), khiến thuật toán Gradient
Descent khó tìm được cực trịtoàn cục (global minimum).
- Convex: Hình cái bát, chỉcó một cực trịtoàn cục duy nhất.

<!-- page: 19 -->

![Hinh: fig-25-1]
Figure 4.4: Minh họa hàm Convex/Non-convex.
### 4.4.2 Logistic Regression Cost Function (Log Loss)
Ta xây dựng hàm Cost function mới phù hợp hơn:
Cost(hθ(x), y) =
(
−log(hθ(x))
if y = 1
−log(1 −hθ(x))
if y = 0
(4.5)
![Hinh: fig-25-2]
Figure 4.5: Minh họa Log Loss bằng đồthị.
Phân tích trực quan:
- Trường hợp y = 1:
- Nếu dự đoán hθ(x) ≈1 (đúng) →Cost ≈0.
- Nếu dự đoán hθ(x) →0 (sai) →Cost →∞(Phạt cực nặng lỗi sai).
- Trường hợp y = 0:
- Nếu dự đoán hθ(x) ≈0 (đúng) →Cost ≈0.
- Nếu dự đoán hθ(x) →1 (sai) →Cost →∞.
### 4.4.3 Công thức thu gọn (Simplified Cost Function)
Vì y chỉcó thểlà 0 hoặc 1, ta có thểgộp 2 trường hợp trên thành một công thức duy nhất
(Binary Cross Entropy):
Cost(hθ(x), y) = −y log(hθ(x)) −(1 −y) log(1 −hθ(x))
(4.6)

<!-- page: 20 -->

Hàm mất mát toàn cục trên m mẫu dữ liệu:
J(θ) = −1
m
m
X
i=1
h
y(i) log(hθ(x(i))) + (1 −y(i)) log(1 −hθ(x(i)))
(4.7)
Mục tiêu: Tìm minθ J(θ).
## 4.5 Gradient Descent cho Logistic Regression
Đểcực tiểu hóa J(θ), ta sử dụng thuật toán Gradient Descent. Quy tắc cập nhật (Update
rule):
θj := θj −α ∂
∂θj
J(θ)
(4.8)
Sau khi tính đạo hàm riêng (có thểtựchứng minh bằng tay), ta thu được công thức cập
nhật:
θj := θj −α 1
m
m
X
i=1
(hθ(x(i)) −y(i))x(i)
j
(4.9)
(Cập nhật đồng thời cho tất cảcác j).
Lưu ý:
- Công thức này nhìn giống hệt Linear Regression.
- Tuy nhiên, sựkhác biệt nằm ởhθ(x):
- Linear Regression: hθ(x) = θT x
- Logistic Regression: hθ(x) =
1
1+e−θT x
- α là learning rate (tốc độhọc).
## 4.6 Phân loại Đa lớp (Multiclass Classification)
Trong thực tế, ta thường gặp bài toán có nhiều hơn 2 nhãn (y ∈{0, 1, . . . , n}). Ví dụ:
- Phân loại Email: Công việc, Bạn bè, Gia đình, Sởthích.
- Thời tiết: Nắng, Mưa, Mây, Tuyết.
- Chẩn đoán y tế: Không bệnh, Cảm lạnh, Cúm.
### 4.6.1 Phương pháp One-vs-All (One-vs-Rest)
Ý tưởng: Biến bài toán đa lớp thành nhiều bài toán nhịphân.

<!-- page: 21 -->

![Hinh: fig-27-1]
Figure 4.6: Minh họa multi-class classification.
Quy trình:
1. Với mỗi lớp i, ta huấn luyện một mô hình Logistic Regression h(i)
θ (x) đểdự đoán xác
suất y = i (coi lớp i là Positive, tất cảcác lớp còn lại là Negative).
2. Ta sẽcó n hàm giảthuyết:
h(1)
θ (x) = P(y = 1|x; θ), . . . , h(n)
θ (x) = P(y = n|x; θ)
3. Dựđoán (Prediction): Với một đầu vào x mới, ta chọn lớp i có giá trịxác suất
cao nhất:
max
h(i)
θ (x)
(4.10)

<!-- page: 22 -->

# Chapter 5: Regularization (Điều chuẩn)
## 5.1 Vấn đềOverfitting và Underfitting
Trong các bài toán học máy (ví dụ: Linear Regression dự đoán giá nhà), việc lựa chọn các
đặc trưng (features) và độ phức tạp của mô hình là rất quan trọng đểđảm bảo độchính
xác.
### 5.1.1 Định nghĩa các trạng thái của mô hình
Xét ví dụdự đoán giá nhà dựa trên kích thước (x). Ta có ba trường hợp điển hình:
![Hinh: fig-28-1]
Figure 5.1: Minh họa mối liên hệgiữa độ phức tạp và chất lượng mô hình.
- Underfitting (High Bias - Độlệch cao): Mô hình quá đơn giản, không thểnắm
bắt được cấu trúc của dữ liệu.
- Just Right (Vừa vặn): Mô hình phù hợp với xu hướng chung của dữ liệu.
- Overfitting (High Variance - Phương sai cao): Mô hình quá phức tạp, cốgắng
đi qua tất cảcác điểm dữ liệu (bao gồm cảnhiễu).
Hệquảcủa Overfitting: Nếu chúng ta có quá nhiều đặc trưng (features), giảthuyết học
được có thểkhớp rất tốt với tập huấn luyện (J(θ) ≈0) nhưng lại thất bại trong việc tổng

<!-- page: 23 -->

quát hóa (generalize) với các dữ liệu mới (dữ liệu kiểm tra - test set). Nếu xây dựng model
quá phức tạp, nó sẽ"học vẹt" cảcác điểm nhiễu.
Tương tự, hiện tượng này cũng xảy ra với Logistic Regression khi ranh giới quyết định
(decision boundary) quá phức tạp đểbao quanh chính xác tuyệt đối các điểm dữ liệu huấn
luyện.
## 5.2 Giải pháp khắc phục Overfitting
Có hai phương pháp chính đểgiải quyết vấn đềnày:
1. Giảm sốlượng đặc trưng (Reduce number of features):
- Chọn lọc thủcông các đặc trưng quan trọng cần giữlại.
- Sửdụng thuật toán lựa chọn mô hình (Model selection algorithm).
2. Regularization (Điều chuẩn):
- Giữlại tất cảcác đặc trưng, nhưng giảm độlớn (magnitude) hoặc làm triệt tiêu
ảnh hưởng của các tham sốθj.
- Phương pháp này hoạt động hiệu quảkhi chúng ta có nhiều đặc trưng và mỗi
đặc trưng đóng góp một phần nhỏvào việc dự đoán y.
## 5.3 Hàm Chi phí (Cost Function) có Regularization
### 5.3.1 Trực giác (Intuition)
Giảsửta có hàm giảthuyết bậc 4: θ0 + θ1x + θ2x2 + θ3x3 + θ4x4. Đểtránh overfitting, ta
muốn làm giảm ảnh hưởng của các thành phần bậc cao (θ3, θ4).
Ta thay đổi hàm mất mát bằng cách cộng thêm một lượng phạt (penalize) cực lớn cho
θ3 và θ4:
min
θ
1
2m
m
X
i=1
(hθ(x(i)) −y(i))2 + 1000θ2
3 + 1000θ2
4
(5.1)
Việc đặt hệsốphạt rất lớn (1000) sẽép các tham sốθ3, θ4 xấp xỉvề0 trong quá trình tối
ưu hóa, từđó làm mô hình trởnên đơn giản hơn (vềcơ bản trởthành hàm bậc 2).
### 5.3.2 Công thức tổng quát
Nguyên lý chung: Giá trịtham sốθ0, . . . , θn càng nhỏthì giảthuyết càng đơn giản và ít bị
overfitting.
Hàm chi phí Regularized Linear Regression được định nghĩa như sau:
J(θ) =
1
2m


m
X
i=1
(hθ(x(i)) −y(i))2 + λ
n
X
j=1
θ2
j


(5.2)
Lưu ý quan trọng:
- λ (Lambda) là tham sốđiều chuẩn (Regularization Parameter).
- Pn
j=1 θ2
j gọi là thành phần điều chuẩn (Regularization Term).

<!-- page: 24 -->

- Theo quy ước (convention), ta không điều chuẩn tham sốθ0 (bias unit), do đó tổng
chỉchạy từj = 1 đến n.
## 5.4 Vai trò của tham sốλ
Tham sốλ đóng vai trò kiểm soát sựcân bằng giữa hai mục tiêu:
1. Khớp tốt với tập huấn luyện (giảm MSE).
2. Giữcho các tham sốnhỏ(đơn giản hóa mô hình).
- Nếu λ quá lớn (ví dụ1010): Mô hình bịphạt quá nặng, dẫn đến tất cảθj ≈0 (trừ
θ0). Hàm giảthuyết trởthành đường thẳng nằm ngang hθ(x) = θ0. Điều này gây ra
hiện tượng Underfitting.
- Nếu λ quá nhỏ(hoặc bằng 0): Thành phần điều chuẩn không có tác dụng, mô
hình quay trởlại bài toán ban đầu và có nguy cơ bịOverfitting.
## 5.5 Regularized Gradient Descent
Đểtối ưu hóa hàm J(θ) có chứa thành phần điều chuẩn, ta áp dụng Gradient Descent. Do
θ0 không bịđiều chuẩn, ta tách quy tắc cập nhật thành hai phần riêng biệt.
### 5.5.1 Cập nhật θ0
θ0 := θ0 −α 1
m
m
X
i=1
(hθ(x(i)) −y(i))x(i)
0
(5.3)
(Giữnguyên như công thức Gradient Descent truyền thống).
### 5.5.2 Cập nhật θj (với j = 1, 2, . . . , n)
Đạo hàm riêng của phần Regularization term là
∂
∂θj ( λ
2mθ2
j) = λ
mθj. Khi đưa vào công thức
cập nhật, ta có:
θj := θj −α
"
1
m
m
X
i=1
(hθ(x(i)) −y(i))x(i)
j
+ λ
mθj
#
(5.4)
Ta có thểviết lại công thức này dưới dạng thu gọn đểthấy rõ bản chất "co lại"
(shrinkage) của tham số:
θj := θj

1 −α λ
m

−α 1
m
m
X
i=1
(hθ(x(i)) −y(i))x(i)
j
(5.5)
Phân tích: Thành phần
1 −α λ
m

thường là một sốdương nhỏhơn 1 một chút (ví dụ
0.99). Điều này có nghĩa là ởmỗi bước lặp, thuật toán sẽthu nhỏgiá trịθj đi một chút
trước khi thực hiện cập nhật theo Gradient của loss.

<!-- page: 25 -->

# Chapter 6: Non-linear Hypotheses & Neural Networks
## 6.1 Non-linear Classification (Phân loại phi tuyến)
### 6.1.1 Hạn chếcủa Linear/Logistic Regression
Trước đây, chúng ta sử dụng Logistic Regression đểgiải quyết bài toán phân loại. Phương
pháp này hoạt động tốt khi tìm kiếm một đường Decision Boundary (Ranh giới quyết
định) đơn giản hoặc phi tuyến tính cơ bản (như hình tròn, elip) với sốlượng Features (Đặc
trưng/Thuộc tính) ít.
Tuy nhiên, trong thực tế, các bài toán thường có rất nhiều features.
Ví dụ:
- Giảsửta có n = 100 features (x1, . . . , x100).
- Đểtạo ra ranh giới phi tuyến phức tạp, ta cần các sốhạng bậc cao (polynomial terms)
như x2
1, x1x2, . . . .
- Sốlượng features bậc 2 sẽtăng theo O(n2) ≈n2
2 . Với n = 100, ta có khoảng 5000
features. Với n lớn hơn, con sốnày bùng nổ(ví dụbậc 3 là O(n3)).
Việc có quá nhiều features khiến mô hình Logistic Regression trởnên cồng kềnh, tốn
kém tài nguyên tính toán và dễbịOverfitting.
### 6.1.2 Ví dụ: Computer Vision (Thịgiác máy tính)
Xét bài toán Car Detection (Phát hiện xe hơi). Máy tính nhìn nhận một bức ảnh dưới
dạng ma trận các con số(cường độđiểm ảnh - pixel intensity grid).
- Với một bức ảnh nhỏ50 × 50 pixels, ta có n = 2500 features (hoặc 7500 nếu là ảnh
màu RGB).
- Nếu dùng Logistic Regression với các features bậc 2 (Quadratic features xixj), số
lượng features sẽlên tới khoảng 3 triệu (≈25002
2
).
Điều này cho thấy Logistic Regression không khảthi cho các bài toán phức tạp như
Computer Vision. Chúng ta cần một giải thuật khác có khảnăng học được các giảthuyết
phi tuyến phức tạp (θ thay đổi) một cách hiệu quảhơn. Đó chính là Neural Networks.

<!-- page: 26 -->

![Hinh: fig-32-1]
Figure 6.1: Minh họa cách máy tính nhận đầu vào trong bài toán Car Detection.
## 6.2 Neural Networks (Mạng Nơ-ron)
### 6.2.1 Lịch sửvà Nguồn gốc
Neural Networks là các thuật toán được thiết kếđểmô phỏng hoạt động của bộnão con
người.
- Được sử dụng rộng rãi vào những năm 80 và đầu 90.
- Suy giảm sựphổbiến vào cuối những năm 90 (do sựnổi lên của SVM và hạn chếvề
phần cứng/dữ liệu).
- Hồi sinh mạnh mẽtừkhoảng 2011-2012 nhờsựphát triển của phần cứng (GPU) và dữ
liệu lớn (Big Data), trởthành kỹthuật "State-of-the-art" (hiện đại nhất) cho nhiều
ứng dụng.
### 6.2.2 Giảthuyết "One Learning Algorithm"
Các nhà khoa học nhận thấy vỏnão (cortex) có khảnăng thích nghi tuyệt vời (Neuroplasticity).
- Thí nghiệm trên động vật: Cắt dây thần kinh từtai đến vùng Auditory Cortex
(Vỏnão thính giác) và nối dây thần kinh từmắt vào đó. Kết quảlà vùng não này
học cách "nhìn" thay vì "nghe".
- Tương tựvới vùng Somatosensory Cortex (Vỏnão xúc giác).
Điều này dẫn đến giảthuyết rằng có thểbộnão sử dụng một thuật toán học tập duy
nhất ("One Learning Algorithm") đểxử lý mọi loại dữ liệu (hình ảnh, âm thanh, xúc giác).
Neural Network cốgắng xấp xỉthuật toán này.
## 6.3 Mô hình Neural Network (Model Representation)
### 6.3.1 Mô phỏng Nơ-ron sinh học
Một nơ-ron sinh học bao gồm:

<!-- page: 27 -->

- Dendrites (Sợi nhánh): Dây nhận tín hiệu đầu vào (Input wires).
- Cell body (Thân tếbào): Xửlý thông tin (Nucleus).
- Axon (Sợi trục): Dây truyền tín hiệu đầu ra (Output wire).
![Hinh: fig-33-1]
Figure 6.2: Minh họa nơ ron sinh học của động vật.
### 6.3.2 Nơ-ron nhân tạo (Artificial Neuron)
Trong máy tính, ta mô phỏng nơ-ron dưới dạng một Logistic Unit:
![Hinh: fig-33-2]
Figure 6.3: Minh họa Logistic Regression bằng Neuron Network.
- Input: x = [x0, x1, x2, . . . ]T (với x0 = 1 là Bias Unit).
người ta muốn mô phỏng chính xác theo bộnão con người -> trước khi gặp dữ liệu,
nó đã có 1 phần phán đoán vềdữ liệu -> đúng cách bộnão con người hoạt động ->
cộng thêm x0.

<!-- page: 28 -->

- Weights (Trọng số): θ = [θ0, θ1, θ2, . . . ]T .
- Output: hθ(x) =
1
1+e−θT x .
- Hàm kích hoạt (Activation Function): Ta sử dụng hàm Sigmoid (logistic function)
g(z) =
1
1+e−z .
### 6.3.3 Kiến trúc Mạng Nơ-ron
Một Neural Network là tập hợp các nơ-ron được kết nối với nhau theo các lớp (Layers).
![Hinh: fig-34-1]
Figure 6.4: Minh họa Neuron Network cơ bản.
1. Input Layer (Lớp đầu vào): Chứa các features x.
2. Hidden Layer (Lớp ẩn): Các lớp ởgiữa. Gọi là "ẩn" vì ta không trực tiếp thấy giá
trịcủa chúng trong tập dữ liệu huấn luyện (tư tưởng Black Box).
3. Output Layer (Lớp đầu ra): Đưa ra giá trịdự đoán cuối cùng.
## 6.4 Forward Propagation (Lan truyền xuôi)
Đểtính toán đầu ra của mạng, ta thực hiện quá trình lan truyền xuôi từInput đến Output.
Ký hiệu:
- a(j)
i : "Activation" (giá trịkích hoạt) của đơn vịi trong lớp j.
- Θ(j): Ma trận trọng sốkiểm soát ánh xạtừlớp j sang lớp j + 1.

<!-- page: 29 -->

![Hinh: fig-35-1]
Figure 6.5: Minh họa quá trình lan truyền xuôi của Neuron Network.
![Hinh: fig-35-2]
Figure 6.6: Minh họa quá trình lan truyền xuôi của Neuron Network (viết gọn hơn).

<!-- page: 30 -->

![Hinh: fig-36-1]
Figure 6.7: Minh họa quá trình lan truyền xuôi của Neuron Network (chi tiết).
### 6.4.1 Tính toán từng bước (Vectorized Implementation)
Giảsửmạng có 3 lớp (Input x, 1 Hidden, Output).
1. Tại lớp 2 (Hidden Layer): Tính z(2) và kích hoạt a(2):
z(2) = Θ(1)a(1)
(với a(1) = x)
(6.1)
a(2) = g(z(2))
(6.2)
(Thêm bias unit a(2)
0
= 1 sau bước này).
2. Tại lớp 3 (Output Layer): Tính z(3) và đầu ra hΘ(x):
z(3) = Θ(2)a(2)
(6.3)
hΘ(x) = a(3) = g(z(3))
(6.4)
Kiến trúc này cho phép mạng nơ-ron học các đặc trưng phức tạp hơn của dữ liệu thông
qua các lớp ẩn, thay vì chỉdựa vào input thô ban đầu.

<!-- page: 31 -->

## 6.5 Trực giác vềNeural Network (Logic Gates)
![Hinh: fig-37-1]
Figure 6.8: Non-linear classification sử dụng Neuron Network.
Tại sao Neural Network có thểhọc được các hàm phi tuyến phức tạp? Ta có thểchứng
minh thông qua việc mô phỏng các cổng logic (Logic Gates) như AND, OR, NOT, XNOR.
### 6.5.1 Ví dụđơn giản: Cổng AND
Giảsửx1, x2 ∈{0, 1}. Ta muốn y = x1 AND x2. Ta thiết lập một nơ-ron với trọng số:
θ0 = −30, θ1 = 20, θ2 = 20.
Hàm giảthuyết: hΘ(x) = g(−30 + 20x1 + 20x2).
- Nếu x1 = 0, x2 = 0 →g(−30) ≈0.
- Nếu x1 = 0, x2 = 1 →g(−10) ≈0.
- Nếu x1 = 1, x2 = 0 →g(−10) ≈0.
- Nếu x1 = 1, x2 = 1 →g(10) ≈1.
→Đây chính xác là hàm AND.
### 6.5.2 Bài toán XNOR (Non-linear)

<!-- page: 32 -->

![Hinh: fig-38-1]
Figure 6.9: Cổng XOR.
Bài toán XNOR (hoặc XOR) là bài toán phi tuyến điển hình mà Logistic Regression
đơn thuần không giải quyết được (không thểphân chia bằng 1 đường thẳng). XNOR là sự
kết hợp của các cổng logic cơ bản: (x1 AND x2) OR ((NOT x1) AND (NOT x2)).
Trong Neural Network:
- Layer 1: Input x1, x2.
- Layer 2: Tính toán các thành phần con (AND, NOR,...).
- Layer 3: Kết hợp kết quảtừLayer 2 (OR) đểra kết quảXNOR.
Việc chồng nhiều layer ("Deep" Network) cho phép mô hình học các hàm sốcực kỳ
phức tạp từcác hàm đơn giản hơn.

<!-- page: 33 -->

![Hinh: fig-39-1]
Figure 6.10: Tạo hàm logic AND sử dụng Neuron Network.
![Hinh: fig-39-2]
Figure 6.11: Tạo hàm logic OR sử dụng Neuron Network.
![Hinh: fig-39-3]
Figure 6.12: Tạo hàm logic Negation (NOT) sử dụng Neuron Network.

<!-- page: 34 -->

![Hinh: fig-40-1]
Figure 6.13: Tạo hàm logic XOR sử dụng Neuron Network.
## 6.6 Multi-class Classification (Phân loại đa lớp)
Đểphân loại nhiều lớp (ví dụ: Người đi bộ, Xe hơi, Xe máy, Xe tải →4 lớp), ta sử dụng
phương pháp One-vs-All mởrộng.
- Thay vì hΘ(x) trảvề1 sốthực, nó sẽtrảvềmột vector ∈RK (với K là sốlớp).
- Ví dụvới 4 lớp:
- Người đi bộ≈[1, 0, 0, 0]T
- Xe hơi ≈[0, 1, 0, 0]T
- Xe máy ≈[0, 0, 1, 0]T
- Xe tải ≈[0, 0, 0, 1]T
Mỗi đơn vịởlớp đầu ra sẽdự đoán xác suất P(y = i|x) cho lớp i tương ứng.

<!-- page: 35 -->

![Hinh: fig-41-1]
Figure 6.14: Multiple output unit: One-vs-all.

<!-- page: 36 -->

# Chapter 7: Neural Network: Cost Function & Propagation
## 7.1 Tổng quan và Ký hiệu
Xét bài toán phân loại với tập dữ liệu huấn luyện gồm m mẫu:
{(x(1), y(1)), (x(2), y(2)), . . . , (x(m), y(m))}
![Hinh: fig-42-1]
Figure 7.1: Neural Network for Classification
### 7.1.1 Ký hiệu kiến trúc mạng
- L: Tổng sốlớp (layers) trong mạng.
- sl: Sốlượng đơn vị(units) trong lớp l (không tính bias unit).
- K: Sốlượng đơn vịđầu ra (Output units), tương ứng với sốlớp cần phân loại.
### 7.1.2 Phân loại (Classification Types)
1. Binary Classification (Phân loại nhịphân):
- y = 0 hoặc 1.
- Chỉcó 1 unit đầu ra (sL = 1).
2. Multi-class Classification (Phân loại đa lớp):

<!-- page: 37 -->

- y ∈RK (Ví dụ: Người đi bộ, Xe hơi, Xe máy, Xe tải).
- Có K units đầu ra (sL = K).
## 7.2 Hàm Chi phí (Cost Function)
Đối với Neural Network, hàm chi phí là sựmởrộng của Logistic Regression, áp dụng cho K
đầu ra và bao gồm thành phần điều chuẩn (Regularization term) cho tất cảcác trọng số.
Công thức tổng quát:
J(Θ) = −1
m
" m
X
i=1
K
X
k=1
y(i)
k log(hΘ(x(i)))k + (1 −y(i)
k ) log(1 −(hΘ(x(i)))k)
#
+ λ
2m
L−1
X
l=1
sl
X
i=1
sl+1
X
j=1
(Θ(l)
ji )2
(7.1)
Giải thích thành phần:
- Phần đầu (Loss): Là tổng sai sốBinary Cross Entropy (BCE) trên tất cảK đầu
ra và m mẫu dữ liệu.
- Phần sau (Regularization term): Tổng bình phương của tất cảcác trọng sốΘ(l)
ji
trong mạng (trừbias unit).
- Θ(l)
ji : Trọng sốnối từunit i của lớp l đến unit j của lớp l + 1.
- hΘ(x) ∈R; (hΘ(x))i = ith output.
## 7.3 Forward Propagation (Lan truyền xuôi)
Sau khi định nghĩa hàm chi phí, ta cần tính toán giá trịđầu ra và loss. Quá trình này gọi
là Forward Propagation. Đểđơn giản hóa, giảsửmạng có 1 lớp ẩn (hidden layer), đầu vào
x ∈Rd và không tính bias term.
### 7.3.1 Các bước tính toán
Bước 1: Tại lớp ẩn (Hidden Layer) Tính biến trung gian z và giá trịkích hoạt h:
z = W (1)x
(7.2)
h = ϕ(z)
(7.3)
Trong đó:
- W (1) ∈Rh×d: Ma trận trọng sốlớp ẩn.
- ϕ(z): Hàm kích hoạt (Activation function), ví dụSigmoid hoặc ReLU.
Bước 2: Tại lớp đầu ra (Output Layer) Tính đầu ra o:
o = W (2)h
(7.4)
Trong đó W (2) ∈Rq×h là trọng sốlớp đầu ra.

<!-- page: 38 -->

Bước 3: Tính hàm mục tiêu (Objective Function) Hàm mục tiêu J bao gồm Loss L
và Regularization term s:
L = l(o, y)
(Loss trên một mẫu)
(7.5)
s = λ
2 (||W (1)||2
F + ||W (2)||2
F )
(Regularization term)
(7.6)
J = L + s
(7.7)
Ghi chú: Nếu λ cực bé, regularization không có tác động. Nếu λ cực lớn, trọng sốsẽbịép
vềgiá trịrất nhỏđểgiảm thiểu loss.
## 7.4 Backward Propagation (Lan truyền ngược)
Backward Propagation sử dụng quy tắc chuỗi (Chain Rule) đểtính đạo hàm của hàm mục
tiêu J theo từng trọng sốW, từđó cập nhật tham sốnhằm cực tiểu hóa J.
### 7.4.1 Đạo hàm tại lớp đầu ra
Ký hiệu chain rule:
∂Z
∂X = prod(∂Z
∂Y , ∂Y
∂X )
(7.8)
Ta có:
∂J
∂L = 1 and ∂J
∂s = 1
(7.9)
Đầu tiên, ta tính đạo hàm của J theo biến đầu ra o:
∂J
∂o = prod(∂J
∂L, ∂L
∂o ) = ∂L
∂o ∈Rq
(7.10)
Đạo hàm của thành phần điều chuẩn s theo trọng số:
∂s
∂W (l) = λW (l)
(7.11)
### 7.4.2 Gradient của trọng sốlớp Output (W (2))
Áp dụng quy tắc chuỗi (chain rule):
∂J
∂W (2) = prod(∂J
∂o ,
∂o
∂W (2) ) + prod(∂J
∂s ,
∂s
∂W (2) ) = ∂J
∂o hT + λW (2)
(7.12)
(Lưu ý: hT là chuyển vịcủa vector kích hoạt lớp ẩn, dùng đểthực hiện phép nhân ma
trận).

<!-- page: 39 -->

### 7.4.3 Gradient của trọng sốlớp Input/Hidden (W (1))
Đểtính gradient cho W (1), ta cần lan truyền sai sốngược vềlớp ẩn.
Bước 1: Gradient tại đầu ra lớp ẩn (h)
∂J
∂h = prod(∂J
∂o , ∂o
∂h) = W (2)T ∂J
∂o
(7.13)
Bước 2: Gradient tại biến trung gian (z) Do hàm kích hoạt áp dụng theo từng
phần tử(element-wise), ta sử dụng phép nhân Hadamard (kí hiệu ⊙):
∂J
∂z = prod(∂J
∂h, ∂h
∂z ) = ∂J
∂h ⊙ϕ′(z)
(7.14)
- hàm kích hoạt hoạt động độc lập trên từng phần tử→Jacobian là ma trận đường
chéo -> dùng element wise.
- mỗi output phụthuộc vào nhiều input →Jacobian là ma trận đầy đủ→phép nhân
tuyến tính -> dùng prod (matrix multiply).
(Ví dụ: Nếu ϕ là sigmoid, thì ϕ′(z) = ϕ(z)(1 −ϕ(z))).
Bước 3: Gradient cuối cùng cho W (1)
∂J
∂W (1) = prod(∂J
∂z ,
∂z
∂W (1) ) + prod(∂J
∂s ,
∂s
∂W (1) ) = ∂J
∂z xT + λW (1)
(7.15)
## 7.5 Tổng kết Công thức Cập nhật
Quy tắc chung đểtính đạo hàm Loss theo trọng sốtại bất kỳlớp nào:
Gradient của W = (Gradient của Loss theo biến đổi tuyến tính tại lớp đó) +
(Regularization term)
Việc tính toán này cho phép ta sử dụng các thuật toán tối ưu (như Gradient Descent) để
huấn luyện mạng nơ-ron sâu.

<!-- page: 40 -->

# Chapter 8: Advice for Applying Machine Learning
## 8.1 Debugging a Learning Algorithm (Gỡlỗi thuật toán học)
Giảsửbạn đã triển khai thuật toán Regularized Linear Regression (Hồi quy tuyến tính
có điều chuẩn) đểdự đoán giá nhà. Tuy nhiên, khi kiểm tra giảthuyết (hypothesis) trên
dữ liệu mới, bạn nhận thấy sai sốdự đoán quá lớn. Bạn nên làm gì tiếp theo?
Thông thường, chúng ta sẽnghĩ đến các phương án sau:
- Thu thập thêm dữ liệu huấn luyện (Get more training examples).
- Thửgiảm bớt sốlượng đặc trưng (Try smaller sets of features).
- Thửbổsung thêm đặc trưng mới (Try getting additional features).
- Thửthêm các đặc trưng đa thức (Try adding polynomial features) như x2
1, x2
2, x1x2, . . . .
- Thửgiảm tham sốđiều chuẩn λ (Try decreasing λ).
- Thửtăng tham sốđiều chuẩn λ (Try increasing λ).
Thay vì thửsai ngẫu nhiên rất tốn thời gian, chúng ta cần sử dụng Machine Learning
Diagnostic (Chẩn đoán học máy). Đây là phương pháp kiểm tra đểhiểu rõ thuật toán
đang gặp vấn đềgì (ví dụ: đang bịHigh Bias hay High Variance) và hướng dẫn cách cải
thiện hiệu suất tốt nhất.
## 8.2 Evaluating a Hypothesis (Đánh giá giảthuyết)
Đểđánh giá xem giảthuyết hθ(x) có hoạt động tốt hay không và tránh hiện tượng
Overfitting (Quá khớp - khi mô hình học cảnhiễu của tập huấn luyện và thất bại trên dữ
liệu mới), ta cần chia dữ liệu.
### 8.2.1 Training / Test Split (Chia tập Huấn luyện / Kiểm tra)
Phương pháp tiêu chuẩn là chia dữ liệu thành 2 phần (thường là 70% cho huấn luyện và
30% cho kiểm tra):

<!-- page: 41 -->

- Training Set: {(x(1), y(1)), . . . , (x(m), y(m))} dùng đểtìm tham sốθ nhằm cực tiểu
hóa hàm mất mát huấn luyện Jtrain(θ).
- Test Set: {(x(1)
test, y(1)
test), . . . , (x(mtest)
test
, y(mtest)
test
)} dùng đểđánh giá sai sốtổng quát hóa.
### 8.2.2 Công thức tính lỗi trên tập test
1. Linear Regression:
Jtest(θ) =
1
2mtest
mtest
X
i=1
(hθ(x(i)
test) −y(i)
test)2
(8.1)
2. Logistic Regression:
Jtest(θ) = −
1
mtest
mtest
X
i=1
(y(i)
testlog(hθ(x(i)
test)) −(1 −y(i)
test)log(hθ(x(i)
test))
(8.2)
## 8.3 Model Selection (Lựa chọn mô hình)
Nếu ta dùng tập Test đểlựa chọn bậc của đa thức (degree of polynomial d), tham sốθ sẽ
bịtối ưu cho tập Test đó, dẫn đến kết quảđánh giá không còn khách quan (công bằng).
Khách hàng là người quyết định vấn đềcần giải quyết, khách hàng mới biết được nhu
cầu thực sựcủa mình -> Khách hàng sẽlà người chia train/test data, họsẽgiữphần test
data lại, mình sẽsử dụng phần còn lại đểphát triển mô hình -> mình chỉlấy 1 phần cho
training, phần còn lại cho validation -> Nếu không tốt trên validation set, mình có thểbóc
tách các phần sai, và cải thiện mô hình.
Giải pháp là chia dữ liệu thành 3 phần:
- Training Set (60%): Dùng đểhuấn luyện tham sốθ.
- Cross Validation Set (20%) (Tập kiểm định chéo - CV): Dùng đểlựa chọn mô
hình (chọn bậc d, chọn λ).
- Test Set (20%): Dùng đểđánh giá cuối cùng.
### 8.3.1 Cross Validaton
Có thểmột sốđiểm dữ liệu có ích cho quá trình train đã bịbạn ném vào đểlàm validation,
test và model không có cơ hội học điểm dữ liệu đó. Thậm chí, đôi khi do ít dữ liệu nên có
một vài class chỉcó trong validation, test mà không có trong train (do việc chia train, val
là hoàn toàn ngẫu nhiên) dẫn đến một kết quảtồi tệkhi validation và test. Và nếu chúng
ta dựa ngay vào kết quảđó đểđánh giá rằng model không tốt thì thật là oan uổng cho nó
giống như một học sinh không được học Tiếng Anh mà phải đi thi TOEFL vậy.
Test data ởđây là validation mà ta đềcập ởtrên, còn test data sẽđc đểriêng và dành
cho bước đánh giá cuối cùng nhằm kiểm tra “phản ứng” của model khi gặp các dữ liệu
unseen hoàn toàn
Phần dữ liệu Training thì sẽđược chia ngẫu nhiên thành K phần (K là một sốnguyên,
hay chọn là 5 hoặc 10). Sau đó train model K lần, mỗi lần train sẽchọn 1 phần làm dữ liệu
validation và K-1 phần còn lại làm dữ liệu training. Kết quảđánh giá model cuối cùng sẽ

<!-- page: 42 -->

![Hinh: fig-48-1]
Figure 8.1: Minh họa Cross Validation.
là trung bình cộng kết quảđánh giá của K lần train. Đó chính là lý do vì sao ta đánh giá
khách quan và chính xác hơn.
Sau khi đánh giá xong model và nếu cảm thấy kết quả(ví dụaccuracy trung bình) chấp
nhận được thì ta có thểthực hiện một trong 2 cách sau đểtạo ra model cuối cùng (đểmang
đi dùng predict):
- Cách một: Trong quá trình train các fold, ta lưu lại model tốt nhất và mang model
đó di dùng luôn. Cách này sẽcó ưu điểm là không cần train lại nhưng lại có nhược
điểm là model sẽkhông nhìn được all data và có thểkhông làm việc tốt với các dữ
liệu trong thực tế.
- Cách hai: train model 1 lần nữa với toàn bộdữ liệu (không chia train, val nữa) và
sau đó save lại và mang đi predict với test set đểxem kết quảnhư nào
Chú ý: Còn có một cách khác mà theo mình thấy là nó mởrộng từK-Fold CV và hay
hơn nhiều là Stratified K-Fold CV. Với phương pháp này thì nó sẽchỉshuffle dữ liệu một
lần đầu tiên trước khi bắt đầu chia fold và nó sẽcốgắng chia sao cho tỷlệcác class trong
các fold là tương đồng nhau.

<!-- page: 43 -->

![Hinh: fig-49-1]
Figure 8.2: Công thức tính loss train/valid/test.
![Hinh: fig-49-2]
Figure 8.3: Minh họa Cross Validation model selection.
10 mô hình →10 validation loss →pick model có validation loss thấp nhất đểtest trên
test data
### 8.3.2 Quy trình lựa chọn mô hình
1. Huấn luyện các mô hình với bậc khác nhau (ví dụd = 1, d = 2, . . . , d = 10) trên tập
Training.
2. Tính sai sốtrên tập Cross Validation (Jcv) cho từng mô hình.
3. Chọn mô hình có Jcv thấp nhất.
4. Đánh giá sai sốtổng quát (Jtest) của mô hình đã chọn trên tập Test.
## 8.4 Diagnosing Bias vs Variance (Chẩn đoán Độlệch và Phương
sai)
Nếu mô hình có kết quảdự đoán kém, thường nó rơi vào một trong hai trường hợp: High
Bias (Underfitting - Chưa khớp) hoặc High Variance (Overfitting - Quá khớp).

<!-- page: 44 -->

### 8.4.1 Phân tích dựa trên đồthịlỗi
Chúng ta vẽđồthịcủa Jtrain(θ) và Jcv(θ) theo bậc của đa thức d.
![Hinh: fig-50-1]
Figure 8.4: Bias and Variance Traceoff.
- High Bias (Underfitting - d nhỏ):
- Jtrain cao (mô hình không khớp tốt dữ liệu huấn luyện).
- Jcv cao (xấp xỉJtrain).
- Đặc điểm: Cảhai lỗi đều cao và gần nhau.
- High Variance (Overfitting - d lớn):
- Jtrain thấp (mô hình khớp rất tốt dữ liệu huấn luyện).
- Jcv cao (thất bại trên dữ liệu mới).
- Đặc điểm: Jcv ≫Jtrain (Khoảng cách giữa hai đường lớn).
## 8.5 Regularization và Bias/Variance
Tham sốđiều chuẩn λ ảnh hưởng trực tiếp đến Bias và Variance.
J(θ) =
1
2m
m
X
i=1
(hθ(x(i)) −y(i))2 + λ
2m
n
X
j=1
θ2
j
(8.3)
- Large λ (Quá lớn): Phạt nặng các tham sốθ, ép chúng vềgần 0. Mô hình trở
thành đường thẳng (hoặc hằng số). →High Bias (Underfitting).
- Small λ (Quá nhỏhoặc bằng 0): Không có điều chuẩn, mô hình quá phức tạp.
→High Variance (Overfitting).
- Intermediate λ (Vừa phải): Cân bằng tốt, cho kết quả"Just right".

<!-- page: 45 -->

## 8.6 Learning Curves (Đường cong học tập)
Learning Curves là đồthịbiểu diễn lỗi (Jtrain và Jcv) theo sốlượng mẫu huấn luyện m
(training set size).
![Hinh: fig-51-1]
Figure 8.5: Learning Curves.
Thực tếngười ta luôn muốn loss càng thấp càng tốt và validation loss và training loss
càng gần nhau càng tốt.
→thực tếmỗi lần tính training error thì phải plot ra 1 lần
### 8.6.1 Trường hợp High Bias (Underfitting)
Tình huống underfit
![Hinh: fig-51-2]
Figure 8.6: Underfit
Mô hình quá đơn giản (ví dụđường thẳng cho dữ liệu cong).
- Khi m tăng, Jtrain tăng dần (khó khớp hết dữ liệu).
- Jcv giảm nhưng hội tụởmức cao.
- Kết luận: Nếu mô hình bịHigh Bias, việc thêm dữ liệu huấn luyện không giúp ích
nhiều.

<!-- page: 46 -->

### 8.6.2 Trường hợp High Variance (Overfitting)
Tình huống gặp nhiều nhất: training error gặp cực tiểu rất nhanh, sau đó loss nó càng ngày
càng xuống →overfit
![Hinh: fig-52-1]
Figure 8.7: Overfit
Mô hình quá phức tạp, khớp quá kỹtập huấn luyện.
- Jtrain rất thấp.
- Jcv cao hơn nhiều so với Jtrain (có khoảng cách lớn - gap).
- Khi m tăng, Jcv có xu hướng giảm xuống và Jtrain tăng lên, khoảng cách thu hẹp lại.
- Kết luận: Nếu mô hình bịHigh Variance, việc thêm dữ liệu huấn luyện có khả
năng giúp ích.
![Hinh: fig-52-2]
Figure 8.8: Diagnosing bias vs variance.

<!-- page: 47 -->

## 8.7 Tổng kết giải pháp (Deciding What to Do Next)
Quay lại các giải pháp ban đầu, ta có thểánh xạchúng vào từng vấn đềcụthể:

| Giải pháp | Khắc phục vấn đề |
| --- | --- |
| Get more training examples (Thêm dữ liệu) | High Variance |
| Try smaller sets of features (Giảm đặc trưng) | High Variance |
| Try getting additional features (Thêm đặc trưng) | High Bias |
| Try adding polynomial features (Thêm đặc trưng bậc cao) | High Bias |
| Try decreasing λ (Giảm λ) | High Bias |
| Try increasing λ (Tăng λ) | High Variance |

*Table 8.1: Các giải pháp khắc phục dựa trên chẩn đoán mô hình*

Chỉdùng bảng này là đủđểcải thiện model chưa ?
- Chưa, cách này còn quá đơn giản.
- Đa phần chỉlà tune hyperparameters.
- Có nhiều trường hợp đặc biệt, cần phân tích rõ hơn mới có thểtìm ra giải pháp.

<!-- page: 48 -->

# Chapter 9: Machine Learning System Design (Thiết kếhệthống học máy)
## 9.1 Building a Spam Classifier (Xây dựng bộphân loại thư
rác)
### 9.1.1 Problem Description (Mô tảbài toán)
Xét bài toán phân loại email là Spam (thư rác) hay Non-spam (thư thường). Đây là một
bài toán Supervised Learning (Học có giám sát) điển hình.
- y = 1: Spam.
- y = 0: Non-spam.
- x: Các Features (Đặc trưng) của email.
### 9.1.2 Feature Representation (Biểu diễn đặc trưng)
Đểbiểu diễn một email thành vector đặc trưng x, ta thường chọn một danh sách các từkhóa
(ví dụ: 100 từ) thường xuất hiện đểphân biệt spam/non-spam (như: deal, buy, discount,
andrew, now...).
Vector x ∈R100 được xác định như sau:
xj =
(
1
nếu từthứj xuất hiện trong email
0
nếu ngược lại
(9.1)
Lưu ý thực tế: Thay vì chọn thủcông 100 từ, người ta thường lấy danh sách các từ
xuất hiện nhiều nhất (n từ, từ10,000 đến 50,000) trong tập dữ liệu huấn luyện.
### 9.1.3 Debugging a Learning Algorithm (Gỡlỗi thuật toán học)
Giảsửbạn đã triển khai thuật toán Regularized Linear Regression (Hồi quy tuyến tính
có điều chuẩn) đểdự đoán giá nhà, nhưng kết quảdự đoán trên dữ liệu mới có sai sốquá
lớn. Bạn nên làm gì?
Dưới đây là bảng tổng hợp các phương pháp và vấn đềmà chúng giải quyết:

<!-- page: 49 -->

| Phương pháp (Action) | Khắc phục vấn đề (Fixes) |
| --- | --- |
| Get more training examples (Thêm dữ liệu) | High Variance (Overfitting) |
| Try smaller sets of features (Giảm đặc trưng) | High Variance (Overfitting) |
| Try getting additional features (Thêm đặc trưng) | High Bias (Underfitting) |
| Try adding polynomial features (Thêm đặc trưng bậc cao) | High Bias (Underfitting) |
| Try decreasing λ (Giảm tham số λ) | High Bias (Underfitting) |
| Try increasing λ (Tăng tham số λ) | High Variance (Overfitting) |

*Table 9.1: Các giải pháp khắc phục lỗi mô hình*

Tuy nhiên, bảng trên khá đơn giản. Trong thực tế, có nhiều trường hợp đặc biệt (corner
cases). Thay vì thửsai ngẫu nhiên, ta nên phân tích các mẫu bịlỗi (error analysis) đểtìm
nguyên nhân cụthể.
## 9.2 Error Analysis (Phân tích lỗi)
Quy trình khuyến nghịđểgiải quyết một bài toán học máy:
1. Bắt đầu với một thuật toán đơn giản, cài đặt nhanh chóng (ví dụtrong 24 giờ).
2. VẽLearning Curves (Đường cong học tập) đểquyết định xem có cần thêm dữ liệu
hay thêm đặc trưng không.
3. Thực hiện Error Analysis: Kiểm tra thủcông các ví dụ(trong tập Cross Validation)
mà thuật toán dự đoán sai.
### 9.2.1 Ví dụthực tế
Giảsửmcv = 500 và thuật toán phân loại sai 100 email. Ta kiểm tra thủcông 100 email
này và phân loại chúng dựa trên:
- Loại email: Pharma (Thuốc), Replica/Fake (Hàng giả), Steal passwords (Đánh cắp
mật khẩu), Khác.
- Dấu hiệu (Cues): Những đặc điểm nào có thểgiúp thuật toán phân loại đúng?
Kết quảphân tích:
- Pharma: 12
- Replica: 4
- Steal passwords: 53
- Khác: 31
→Lỗi chủyếu đến từloại "Steal passwords". Ta có thểtập trung cải thiện việc nhận diện
loại này
ví dụ: Tìm xem loại này có điểm gì chung, ví dụhay xuất hiện 1 chuỗi hay từnào đó
=> preprocessing (tiền xử lí, loại bỏstop words) + rule-based + xét threshold -> không
cần thay đổi weights.

<!-- page: 50 -->

## 9.3 Error Metrics for Skewed Classes (Độđo lỗi cho lớp lệch)
### 9.3.1 Vấn đềvới Accuracy (Độchính xác)
Xét bài toán phân loại ung thư (Cancer Classification): y = 1 (ung thư), y = 0 (lành
tính). Giảsửmô hình đạt 1% lỗi trên tập test (99% Accuracy). Tuy nhiên, thực tếchỉcó
0.5% bệnh nhân bịung thư. Đây là trường hợp Skewed Classes (Lớp dữ liệu bịlệch).
Nếu ta viết một hàm đơn giản luôn dự đoán y = 0 (luôn lành tính):
function predictCancer(x):
return 0
Hàm này sẽđạt độchính xác 99.5% (chỉsai 0.5%). Rõ ràng Accuracy không phải là thước
đo tốt trong trường hợp này.
## 9.4 Precision and Recall (Độchính xác và Độphủ)
Đểđánh giá tốt hơn, ta sử dụng Precision và Recall. Ta xây dựng Confusion Matrix
(Ma trận nhầm lẫn):
Actual: 1
Actual: 0
Predicted: 1
True Positive (TP)
False Positive (FP)
Predicted: 0
False Negative (FN)
True Negative (TN)
### 9.4.1 Định nghĩa
- Precision (Độchính xác): Trong sốcác bệnh nhân được dự đoán ung thư (y = 1),
bao nhiêu phần trăm thực sựbịung thư?
Precision =
True Positives
Total Predicted Positive =
TP
TP + FP
(9.2)
- Recall (Độphủ/Độnhạy): Trong sốtất cảbệnh nhân thực sựbịung thư, bao
nhiêu phần trăm chúng ta phát hiện được?
Recall =
True Positives
Total Actual Positive =
TP
TP + FN
(9.3)
Nếu mô hình luôn dự đoán y = 0, thì TP = 0 →Recall = 0, ta biết ngay mô hình này
vô dụng.
## 9.5 Trading off Precision and Recall (Đánh đổi giữa Precision
và Recall)
Đối với Logistic Regression, ta dự đoán y = 1 nếu hθ(x) ≥threshold (ngưỡng).
- Tăng ngưỡng (ví dụ0.7, 0.9):
- Chỉdự đoán ung thư khi rất tựtin.

<!-- page: 51 -->

- Kết quả: High Precision (ít báo động giả), Low Recall (bỏsót bệnh nhân).
- Giảm ngưỡng (ví dụ0.3, 0.1):
- Tránh bỏsót các ca ung thư (tránh False Negatives).
- Kết quả: High Recall (phát hiện được nhiều), Low Precision (nhiều báo động
giả).
## 9.6 F1 Score (Điểm F1)
Làm thếnào đểso sánh các thuật toán với các cặp sốPrecision/Recall khác nhau?
Nếu dùng trung bình cộng P+R
2
, ta có thểbịlừa bởi các thuật toán cực đoan (ví dụRecall
= 1 nhưng Precision cực thấp).
Ta sử dụng F1 Score (Trung bình điều hòa của P và R):
F1 Score = 2 P · R
P + R
(9.4)
- Nếu P = 0 hoặc R = 0 →F1 = 0.
- Nếu P = 1 và R = 1 →F1 = 1.
### 9.6.1 Tổng quát: Fβ Score
Công thức tổng quát cho phép điều chỉnh trọng sốgiữa Precision và Recall:
Fβ Score = (1 + β2)
P · R
(β2 · P) + R
(9.5)
- β = 1: Cân bằng (F1 Score).
- β = 0.5: Ưu tiên Precision.
- β = 2: Ưu tiên Recall.

<!-- page: 52 -->

# Chapter 10: Clustering (Phân cụm)
## 10.1 Giới thiệu vềClustering
![Hinh: fig-58-1]
Figure 10.1: Supervised Learning vs Unsupervised Learning.
Clustering là một họthuật toán lớn thuộc nhóm Unsupervised Learning (Học không
giám sát). Khác với Supervised Learning (có nhãn y), Unsupervised Learning làm việc với
tập dữ liệu huấn luyện không có nhãn:
{x(1), x(2), . . . , x(m)}

<!-- page: 53 -->

Mục tiêu của Clustering là tìm kiếm các mẫu ẩn (hidden patterns) hoặc cấu trúc trong
dữ liệu đểnhóm các điểm dữ liệu tương đồng lại với nhau.
### 10.1.1 Các ứng dụng của Clustering
- Market Segmentation (Phân khúc thịtrường): Phân nhóm khách hàng dựa
trên dữ liệu nhân khẩu học, hành vi mua sắm đểcó chiến lược kinh doanh phù hợp
-> đây là một trong các bài toán kinh điển của Unsupervised Leaning.
- Social Network Analysis (Phân tích mạng xã hội): Tìm các cộng đồng hoặc
nhóm người dùng có liên kết chặt chẽ.
- Organize Computing Clusters: Tối ưu hóa việc sắp xếp các cụm máy tính.
- Astronomical Data Analysis: Phân tích dữ liệu thiên văn.
- Anomaly Detection (Phát hiện bất thường): Khi dữ liệu có rất ít hoặc không
có nhãn bất thường, Clustering có thểgiúp phát hiện các điểm dữ liệu sai khác so với
phần còn lại.
## 10.2 Thuật toán K-means
K-means là thuật toán phân cụm đơn giản và phổbiến nhất. Thuật toán hoạt động lặp đi
lặp lại đểchia dữ liệu thành K cụm.
### 10.2.1 Quy trình thuật toán
Input:
![Hinh: fig-59-1]
Figure 10.2: K-means input.
- K: Sốlượng cụm mong muốn.
- Tập dữ liệu huấn luyện {x(1), x(2), . . . , x(m)} (với x(i) ∈Rn).

<!-- page: 54 -->

Các bước thực hiện:
1. Initialization (Khởi tạo tâm cụm): Với mỗi cụm sẽcó một centroids, là vịtrí chính
giữa của cụm. Chọn ngẫu nhiên K điểm làm tâm cụm ban đầu (cluster centroids),
hoặc tốt hơn thì dựa trên phân bốcủa dữ liệu -> khởi tạo được K cluster centroids
µ1, µ2, . . . , µK.
![Hinh: fig-60-1]
Figure 10.3: K-means khởi tạo tâm cụm.
2. Loop (Lặp lại cho đến khi hội tụ):
- Cluster Assignment Step (Gán cụm): Duyệt qua từng điểm dữ liệu x(i),
tính khoảng cách tới tất cảcác tâm cụm µk. Gán x(i) vào cụm có tâm gần nhất.
c(i) := arg min
k
||x(i) −µk||2
Trong đó c(i) là chỉsốcụm (từ1 đến K) của điểm x(i).
![Hinh: fig-60-2]
Figure 10.4: K-means phân cụm cho các điểm dữ liệu.

<!-- page: 55 -->

- Move Centroids Step (Cập nhật tâm cụm): Với mỗi cụm k, tính trung
bình (mean) của tất cảcác điểm dữ liệu đã được gán vào cụm đó và cập nhật
µk thành giá trịtrung bình mới.
µk :=
1
|Ck|
X
i∈Ck
x(i)
![Hinh: fig-61-1]
Figure 10.5: K-means cập nhật tâm cụm.
Nếu tâm cụm vẫn còn dịch chuyển thì tiếp tục vòng lặp (quay vềCluster Assignment
Step)
Thuật toán dừng lại khi các tâm cụm không còn thay đổi (hội tụ).
## 10.3 Hàm Mục tiêu (Optimization Objective)
K-means thực chất là quá trình tối ưu hóa một hàm chi phí, gọi là Distortion function
(Hàm độméo dạng).
Ký hiệu:
- c(i): Chỉsốcụm của điểm dữ liệu x(i).
c(i) := arg min
k
||x(i) −µk||2
- µc(i): Tâm cụm tương ứng với điểm x(i) (tâm của cụm chứa điểm x(i)).
Hàm tối ưu J:
J(c(1), . . . , c(m), µ1, . . . , µK) = 1
m
m
X
i=1
||x(i) −µc(i)||2
(10.1)
Mục tiêu của K-means là tìm các c(i) và µk đểcực tiểu hóa J:
min
c,µ J(c, µ)

<!-- page: 56 -->

## 10.4 Chứng minh hàm tối ưu:
Tại sao Cluster Assignment Step lại tương đương việc tìm điểm dữ liệu i thuộc cụm nào từ
c(1) đến c(m) đểlàm sao minimize được J ?
J(c(1), . . . , c(m), µ1, . . . , µK) = 1
m
m
X
i=1
||x(i) −µc(i)||2
(10.2)
Điều kiện đểtối ưu hàm J là đểtối ưu m cái c(i), chứkhông phải tối ưu mỗi 1 điểm c.
→phải chứng minh được việc tối ưu hàm J đồng thời các ci thì = tối ưu độc lập lần lượt
các c
→phải chứng minh được đẳng thức sau:
min
ci J(c(1), . . . , c(m), µ1, . . . , µK) = min
ci ( 1
m
m
X
i=1
||x(i) −µc(i)||2) = 1
m
m
X
i=1
min
ci ||x(i) −µc(i)||2
(10.3)
Đẳng thức này đúng khi loss J cho các điểm i độc lập với nhau, tức là ||x(i) −µc(i)||2
độc lập với nhau.
-> Chúng độc lập với nhau khi cập nhật đồng thời và cập nhật độc lập c(i) là như nhau
-> Hay là công thức sau độc lập với mỗi i
c(i) = arg
min
k∈{1,...,K} ||x(i) −µk||2
-> Điều này là hiển nhiên.
=> Cluster Assignment Step chính là cốđịnh µ và tối ưu c(i) đểgiảm J.
Chứng minh tương tự=> Move Centroids Step chính là cốđịnh c(i) và tối ưu µ đểgiảm
J.
Từđó suy ra:
- Cluster Assignment Step chính là cốđịnh µ và tối ưu c(i) đểgiảm J.
- Move Centroids Step chính là cốđịnh c(i) và tối ưu µ đểgiảm J.
## 10.5 Khởi tạo ngẫu nhiên (Random Initialization)
Kết quảcủa K-means có thểphụthuộc vào việc khởi tạo tâm cụm ban đầu và có nguy cơ
rơi vào Local Optima (Cực trịđịa phương), dẫn đến kết quảphân cụm không tốt.
Giải pháp: Thực hiện K-means nhiều lần (ví dụ: 50-100 lần) với các khởi tạo ngẫu
nhiên khác nhau.
1. For i = 1 to 100:
2. Khởi tạo ngẫu nhiên K tâm cụm.
3. Chạy K-means đểnhận được c(i) và µk.
4. Tính giá trịhàm chi phí J.
5. Cuối cùng, chọn kết quảcó giá trịJ nhỏnhất.
Trên thực tếngười ta sẽkhông dùng khởi tạo random mà khởi tạo có phân tích dữ liệu hơn.

<!-- page: 57 -->

## 10.6 Lựa chọn sốcụm K (Choosing the Value of K)
Việc chọn K thường không dễdàng và đôi khi mang tính chủquan hoặc phụthuộc vào bài
toán cụthể.
### 10.6.1 Phương pháp Elbow (Khuỷu tay)
Vẽđồthịgiá trịhàm chi phí J theo sốlượng cụm K.
![Hinh: fig-63-1]
Figure 10.6: Elbow method
- Khi K tăng, J sẽgiảm.
- Ta tìm điểm "khuỷu tay" (elbow point) - nơi mà tốc độgiảm của J bắt đầu chậm lại
đáng kể. Đó có thểlà giá trịK hợp lý.
Lưu ý: Đôi khi đồthịgiảm đều và không xuất hiện điểm khuỷu tay rõ ràng, khi đó
phương pháp này không hiệu quả.
-> khi đó cần phân tích dữ liệu và dowstream task đểchọn k phù hợp.
### 10.6.2 Dựa trên mục đích sử dụng (Downstream Purpose)
Chọn K dựa trên nhu cầu thực tếcủa bài toán kinh doanh.
Ví dụT-shirt sizing:

<!-- page: 58 -->

![Hinh: fig-64-1]
Figure 10.7: Chọn k cho K-Means.
- Nếu muốn làm 3 cỡáo (S, M, L) →Chọn K = 3.
- Nếu muốn làm 5 cỡáo (XS, S, M, L, XL) →Chọn K = 5.
Kết luận: Với các dạng phân bốphức tạp hơn (ví dụ: hình cánh hoa, lồng vào nhau),
cần xem xét các thuật toán phân cụm khác.
### 10.6.3 Khi nào thì sử dụng K-Means ?
K-means hoạt động tốt nhất với các cụm dữ liệu có dạng hình cầu (spherical) vì tâm của
dữ liệu hình cầu là tâm của hình cầu đó →không cần cập nhật tâm cụm nhiều.
Khi nào thì người ta chọn làm k-means ?
- Phân tích kĩ dữ liệu, xem dữ liệu có dạng gì, có phù hợp với k-means không
- Nó phân bốnhiều hay 1 dạng cầu
- Nếu 1 dạng cầu thường k phù hợp lắm →thành 1 tâm →người ta muốn nhiều dạng
cầu
- Hoặc là nó có 1 dạng cầu, nhưng kiểu hình hơi cánh hoa, thì phù hợp k-means
- Xác định k là phần nan giải của k-means
- Có thểsử dụng các thuật toán phân cụm khác

<!-- page: 59 -->

# Chapter 11: Dimensionality Reduction (Giảm chiều dữ liệu)
## 11.1 Giới thiệu vềDimensionality Reduction
### 11.1.1 Động lực (Motivation)
Giảm chiều dữ liệu (Dimensionality Reduction) là kỹthuật quan trọng trong Machine
Learning với hai mục đích chính:
1. Data Compression (Nén dữ liệu):
![Hinh: fig-65-1]
Figure 11.1: Minh họa Data Compression.

<!-- page: 60 -->

- Giảm không gian lưu trữ(bộnhớ/ổđĩa).
- Tăng tốc độthuật toán học máy (Supervised learning speedup).
- Loại bỏcác đặc trưng dư thừa (redundant features) hoặc có tương quan cao (ví
dụ: độdài tính bằng cm và inches).
2. Data Visualization (Trực quan hóa dữ liệu):
![Hinh: fig-66-1]
Figure 11.2: Minh họa Data Visualization.
- Dữliệu nhiều chiều (ví dụ50D, 1000D) rất khó hình dung.
- Giảm xuống 2D hoặc 3D giúp ta vẽđồthịvà hiểu rõ hơn vềcấu trúc dữ liệu.
### 11.1.2 Ví dụminh họa
Từ2D xuống 1D: Xét các điểm dữ liệu nằm rải rác gần một đường thẳng. Ta có thể
chiếu chúng xuống đường thẳng đó đểchuyển từvector x(i) ∈R2 sang một sốthực z(i) ∈R.
Từ3D xuống 2D: Chiếu các điểm dữ liệu trong không gian 3D xuống một mặt phẳng
2D phù hợp nhất.
## 11.2 Principal Component Analysis (PCA)
### 11.2.1 Định nghĩa bài toán
PCA (Phân tích thành phần chính) là thuật toán giảm chiều dữ liệu phổbiến nhất.
Mục tiêu của PCA: Tìm một không gian con (đường thẳng, mặt phẳng, siêu phẳng...) có
sốchiều thấp hơn sao cho khi chiếu dữ liệu lên đó, tổng bình phương khoảng cách từcác
điểm dữ liệu đến hình chiếu của nó (Projection Error) là nhỏnhất.

<!-- page: 61 -->

![Hinh: fig-67-1]
Figure 11.3: Minh họa ý tưởng của thuật toán PCA 2 chiều -> 1 chiều.
Giảm n →k chiều thì tìm k vector sao cho khi chiếu các điểm dữ liệu xuống hyperplane
thì khoảng cách chiếu là nhỏnhất (minimize projection error).
![Hinh: fig-67-2]
Figure 11.4: Minh họa ý tưởng của thuật toán PCA.

<!-- page: 62 -->

Sựkhác biệt giữa PCA và Linear Regression:
![Hinh: fig-68-1]
Figure 11.5: Minh họa sựkhác biệt giữa PCA và Linear Regression.
- Linear Regression: Tìm đường thẳng đểcực tiểu hóa sai sốdự đoán theo phương
dọc (vuông góc với trục hoành). Cốgắng dự đoán giá trịy từx.
- PCA: Tìm đường thẳng đểcực tiểu hóa khoảng cách vuông góc từđiểm dữ liệu đến
đường thẳng đó. Không có phân biệt biến x và y (tất cảđều là features).
Tại sao khi giảm n chiều dữ liệu xuống k chiều dữ liệu, chúng ta lại cần tìm k
vectors sao cho khi chiếu xuống, khoảng cách hình chiếu (projection error) là
nhỏnhất ?
- Giảm chiều khi các chiều có lượng thông tin đóng góp nhưng không nhiều.
- Yếu tốtiên quyết khi giảm chiểu dữ liệu là giảm mất mát thông tin của dữ liệu →dữ
liệu ban đầu phải không thay đổi nhiều (ít dịch chuyển nhất).
- Tương đương với việc tìm vector đểkhoảng cách hình chiếu là nhỏnhất.
PCA giảm chiều dữ liệu theo hướng mà variance của dữ liệu lớn nhất.
### 11.2.2 Các bước thực hiện PCA
Bước 1: Data Preprocessing (Tiền xử lý dữ liệu) Trước khi chạy PCA, bắt buộc
phải thực hiện chuẩn hóa dữ liệu:
- Mean Normalization: Đưa trung bình của mỗi feature về0.
µj = 1
m
m
X
i=1
x(i)
j
x(i)
j
←x(i)
j
−µj
- Feature Scaling: Nếu các feature có độlớn khác nhau (ví dụ: diện tích nhà vs số
phòng ngủ), cần chia cho độlệch chuẩn hoặc khoảng giá trịđểchúng có cùng tỉlệ.
x(i)
j
←
(x(i)
j
−µj)
sj

<!-- page: 63 -->

Bước 2: Tính Covariance Matrix (Ma trận hiệp phương sai) Tính ma trận Σ
(Sigma):
Σ = 1
m
m
X
i=1
(x(i))(x(i))T = 1
mXT X
(11.1)
Bước 3: Tính Eigenvectors và Eigenvalues Sửdụng phân tích SVD (Singular Value
Decomposition) hoặc ‘eig‘ đểtìm các vector riêng và trịriêng của ma trận Σ:
[U, S, V ] = svd(Σ)
Trong đó U là ma trận các vector riêng (Principal Components).
Bước 4: Chọn K Eigenvectors ứng với K Eigenvalues lớn nhất Đểgiảm từn
chiều xuống k chiều, ta chọn k cột đầu tiên của ma trận U (gọi là Ureduce).
Bước 5: Chiếu dữ liệu Tính vector mới z(i) trong không gian k chiều:
z(i) = UT
reducex(i)
(11.2)
## 11.3 Bản chất PCA
1. Tại sao trước khi áp dụng PCA, chúng ta cần bắt buộc làm mean normalization ?
nếu không thì sao ?
- Việc normalization đểchuẩn hóa giúp variance nó không phụthuộc nhiều vào
giá trịlớn (1 triệu VND và 10 độthì 1 triệu » 10 nhưng độchênh lệnh thực tế
giữa 2 đơn vịkhác nhau là khác nhau).
- Cái mà chúng ta quan tâm chỉlà độbiến thiên dữ liệu →nếu chiếu dữ liệu theo
chiều có độbiến thiên lớn nhất thì sẽgiữđược nhiều thông tin nhất (ma trận
hiệp phương sai chứa đầy đủđộbiến thiên của dữ liệu).
- Nếu không mean normalization, thì khi PCA với mong muốn tìm chiều có độ
biến thiên nhiều nhất thì khảnăng rất cao là 1 trong các vector riêng sẽhướng
dữ liệu vềgốc (mất đi 1 chiều đểgiữthông tin) vì ma trận hiệp phương sai sẽ
có dạng như hình.
![Hinh: fig-69-1]
Figure 11.6: Minh họa PCA nếu không Normalization.
2. tại sao việc maximize variance <=> minimize projection error ?

<!-- page: 64 -->

![Hinh: fig-70-1]
Figure 11.7: Maximize variance vs minimize projection error.
Variance + projection error là 1 hằng số-> muốn giảm projection error thì phải tăng
variance
## 11.4 Lựa chọn sốchiều K (Choosing K)
Làm sao đểchọn k phù hợp? Thông thường, ta chọn k nhỏnhất sao cho giữlại được phần
lớn phương sai (variance) của dữ liệu (ví dụ: 99% variance retained).
Công thức kiểm tra:
1
m
Pm
i=1 ||x(i) −x(i)
approx||2
1
m
Pm
i=1 ||x(i)||2
≤0.01
(Tửsốlà sai sốchiếu trung bình, mẫu sốlà tổng phương sai dữ liệu).

<!-- page: 65 -->

## 11.5 Lời khuyên khi áp dụng PCA
### 11.5.1 Khi nào nên dùng PCA?
- Đểnén dữ liệu nhằm giảm bộnhớhoặc tăng tốc thuật toán học máy.
- Đểtrực quan hóa dữ liệu (chọn k = 2 hoặc k = 3).
### 11.5.2 Sai lầm thường gặp (Bad use of PCA)
KHÔNG dùng PCA đểchống Overfitting: Mặc dù PCA giảm sốlượng features (giống
như feature selection), nhưng nó không quan tâm đến nhãn y. Nó chỉdựa trên phương sai
của x. Do đó, nó có thểloại bỏcác thông tin quan trọng giúp phân biệt các lớp. →Đểgiải
quyết Overfitting, hãy dùng Regularization thay vì PCA.
Lưu ý quy trình: Chỉtính toán các tham sốPCA (ma trận Ureduce) trên tập Training
Set, sau đó áp dụng cùng tham sốđó đểbiến đổi tập Cross Validation và Test Set.

<!-- page: 66 -->

# Chapter 12: Anomaly Detection (Phát hiện bất thường)
## 12.1 Giới thiệu vềAnomaly Detection
Anomaly Detection là một bài toán quan trọng trong Machine Learning, được ứng dụng
rộng rãi trong nhiều lĩnh vực thực tếnhư phát hiện gian lận, giám sát hệthống, và sản
xuất công nghiệp.
### 12.1.1 Ví dụminh họa: Động cơ máy bay
Giảsửta có tập dữ liệu vềcác động cơ máy bay với các đặc trưng:
- x1: Nhiệt lượng tỏa ra (heat generated).
- x2: Cường độrung (vibration intensity).
Tập dữ liệu: {x(1), x(2), . . . , x(m)}. Khi có một động cơ mới xtest, ta cần xác định xem nó
có bất thường (anomaly) hay không.
![Hinh: fig-72-1]
Figure 12.1: Ví dụvềAnomaly Detextion.

<!-- page: 67 -->

### 12.1.2 Phương pháp Density Estimation (Ước lượng mật độ)
![Hinh: fig-73-1]
Figure 12.2: Density estimation cho bài toán Anomaly Detection.
Mô hình hóa p(x) (xác suất xuất hiện của x) dựa trên tập dữ liệu đã có.
- Nếu p(xtest) < ϵ: Đánh dấu là bất thường (Anomaly).
- Nếu p(xtest) ≥ϵ: Đánh dấu là bình thường (OK).
Lưu ý vềkhái niệm: Trong miền liên tục, xác suất tại một điểm cụthểxấp xỉbằng 0.
Do đó, ta sử dụng khái niệm Density (mật độxác suất) thay vì Probability, Density của
một điểm sẽlà Propability của các điểm xung quanh nó (tính tích phân). Những điểm bất
thường thường có mật độphân bốthấp (hiếm khi xảy ra).
## 12.2 Các ứng dụng phổbiến
1. Fraud Detection (Phát hiện gian lận):
- x(i): Các đặc trưng hoạt động của người dùng i.
- Xây dựng mô hình p(x) từdữ liệu người dùng bình thường.
- Xác định các hành vi bất thường khi p(x) < ϵ.
2. Manufacturing (Sản xuất): Kiểm tra sản phẩm lỗi.
3. Monitoring Data Centers (Giám sát trung tâm dữ liệu):
- x1: Sửdụng bộnhớ.
- x2: Sốlượng truy cập đĩa/giây.
- x3: Tải CPU.
- x4: Tải mạng.

<!-- page: 68 -->

## 12.3 Gaussian (Normal) Distribution
### 12.3.1 Hàm mật độxác suất (PDF)
![Hinh: fig-74-1]
Figure 12.3: Normal Gaussian Distribution.
(f(x) ởđây là công thức đã được tính ra từphép tích phân
Phân phối chuẩn Gaussian với trung bình µ và phương sai σ2 được ký hiệu là N(µ, σ2).
Công thức hàm mật độ:
p(x; µ, σ2) =
1
√
2πσ exp

−(x −µ)2
2σ2

(12.1)
- µ (Mean): Xác định vịtrí trung tâm của phân phối.
- σ (Standard Deviation - Độlệch chuẩn): Xác định độrộng (độphân tán) của phân
phối.
### 12.3.2 Gaussian Distribution Example)
- Toàn bộphân phối = 1.
- Standard deviation (độlệch chuẩn) =
√
variance
- Standard deviation ảnh hưởng đến độthưa của phân bố(khoảng cách các điểm dữ
liệu và mean của nó).
- Khi σ giảm thì chiều cao phải tăng lên là do nó luôn phải giữcho diện tích = 1.

<!-- page: 69 -->

![Hinh: fig-75-1]
Figure 12.4: Gaussian Distribution Example.
### 12.3.3 Ước lượng tham số(Parameter Estimation)
Đểbiểu diễn phân bốcủa 1 tập dữ liệu, ta cần ước lượng các tham sốnhư µ, σ
![Hinh: fig-75-2]
Figure 12.5: Parameter Estimation.
- µ ởđây là mean của tập mẫu.
- σ =
√
variance
- variance = trung bình khoảng cách giữa các điểm dữ liệu →mean.
Với tập dữ liệu {x(1), . . . , x(m)}, ta ước lượng các tham sốnhư sau:
µ = 1
m
m
X
i=1
x(i)
(12.2)
σ2 = 1
m
m
X
i=1
(x(i) −µ)2
(12.3)
Công thức trên là công thức ước lượng cho cảbiến ngẫu nhiên (ởđây đang ước lượng
theo công thức tính trung bình mẫu, phương sai mẫu)

<!-- page: 70 -->

## 12.4 Thuật toán Anomaly Detection
![Hinh: fig-76-1]
Figure 12.6: Anomaly Detection Algorithm.
Giảsửdữ liệu có n đặc trưng độc lập, ta mô hình hóa p(x) là tích của các xác suất
riêng lẻ:
p(x) = p(x1; µ1, σ2
1) × p(x2; µ2, σ2
2) × · · · × p(xn; µn, σ2
n) =
n
Y
j=1
p(xj; µj, σ2
j )
(12.4)
Quy trình thực hiện:
1. Chọn các đặc trưng xi quan trọng có khảnăng chỉbáo bất thường.
2. Tính toán các tham sốµ1, . . . , µn và σ2
1, . . . , σ2
n từtập dữ liệu.
3. Với một mẫu mới x, tính p(x) theo công thức tích phân phối chuẩn.
4. Nếu p(x) < ϵ, kết luận là bất thường.
Nhưng trong thực tếthì các feature gần như không thểhoàn toàn độc lập được với
nhau. -> người ta thường dùng multivariate gaussian distribution.
## 12.5 Anomaly Detection vs Supervised Learning
Tại sao không dùng Supervised Learning cho các bài toán như phát hiện thư rác (Spam)?
## 12.6 Xửlý đặc trưng (Feature Engineering)
### 12.6.1 Non-Gaussian Features
Nên chọn các feature nào đểdự đoán ?
- Visualize lên, xem feature nào phân phối gauss
- Thực tếsẽcó nhiều phân phối ̸= gauss, có thểlà long tail distribution (đuôi dài)

<!-- page: 71 -->

Anomaly Detection
Supervised Learning
Sốlượng mẫu dương (y = 1, bất thường)
rất nhỏ(0-20 mẫu). Sốlượng mẫu âm
(y = 0, bình thường) rất lớn.
Sốlượng mẫu dương và mẫu âm đều lớn.
Có nhiều loại bất thường khác nhau. Khó
đểhọc được đặc trưng chung từsốít mẫu
dương.
Đủmẫu dương đểthuật toán học được
đặc trưng của lớp dương.
Các bất thường trong tương lai có thể
hoàn toàn khác với những gì đã thấy.
Các mẫu dương tương lai có khảnăng
giống với tập huấn luyện.
Rất ít điểm bất thường trong dataset,
thậm chí nó còn chưa xuất hiện (tức là
đang hoạt động tốt, vẫn phải tìm ra điểm
bất thường).
Có các mẫu negative rồi, mình chỉcần
học có giám sát →ngay cảkhi không biết
bất thường ởđiểm nào, thì cũng mong
muốn phân loại được spam
Ví dụ: Gian lận tài chính, lỗi sản xuất.
Ví dụ: Phân loại Spam, dựbáo thời tiết,
ung thư.
![Hinh: fig-77-1]
Figure 12.7: Non-gaussian features.
- Cách 1: vứt feature này đi
- Hoặc nếu thấy nó ảnh hưởng output →có thểđưa qua log transform, dùng biến
thểlog, dùng hàm mũ, . . .
Nếu biểu đồhistogram của một đặc trưng không có dạng hình chuông (Gaussian), ta
nên chuyển đổi nó vềdạng Gaussian bằng các hàm như log(x), log(x + c), √x, hoặc x1/3.
### 12.6.2 Error Analysis
Nếu thuật toán thất bại trong việc phát hiện một mẫu bất thường, hãy phân tích mẫu đó
đểtìm ra đặc trưng mới giúp phân biệt nó với các mẫu bình thường. Ví dụ: Tạo đặc trưng
mới x3 =
CPU Load
Memory Use đểphát hiện máy tính bịkẹt vòng lặp vô hạn.

<!-- page: 72 -->

## 12.7 Multivariate Gaussian Distribution (Phân phối chuẩn
đa biến)
### 12.7.1 Hạn chếcủa mô hình gốc
Mô hình gốc (tích các p(xj)) giảđịnh các đặc trưng độc lập với nhau. Điều này có thể
dẫn đến việc bỏsót các bất thường có sựtương quan giữa các đặc trưng (ví dụ: CPU thấp
nhưng Memory cao bất thường) bởi vì trong thực tếthì các đặc trưng gần như không thể
nào hoàn toàn độc lập với nhau.
### 12.7.2 Mô hình đa biến
![Hinh: fig-78-1]
Figure 12.8: Anomaly Detect with the multivariate Gaussian.
Sửdụng phân phối chuẩn đa biến đểmô hình hóa sựtương quan:
p(x; µ, Σ) =
1
(2π)n/2|Σ|1/2 exp

−1
2(x −µ)T Σ−1(x −µ)

(12.5)
Trong đó:
- µ ∈Rn: Vector trung bình.
- Σ ∈Rn×n: Ma trận hiệp phương sai (Covariance Matrix).
### 12.7.3 So sánh mô hình
- Original Model: Tính toán đơn giản, hoạt động tốt ngay cảkhi m (sốmẫu) nhỏ.
Tuy nhiên, cần tạo thủcông các đặc trưng kết hợp nếu có sựtương quan.
- Multivariate Model: Tựđộng nắm bắt sựtương quan giữa các đặc trưng. Tuy
nhiên, chi phí tính toán cao (tính nghịch đảo ma trận Σ−1) và yêu cầu sốlượng mẫu
lớn (m > n, tốt nhất là m ≥10n).

<!-- page: 73 -->

# Chapter 13: Recommender Systems (Hệthống gợi ý)
## 13.1 Problem Definition (Định nghĩa bài toán)
### 13.1.1 Ví dụ: Dựđoán đánh giá phim (Predicting movie ratings)
![Hinh: fig-79-1]
Figure 13.1: Example predict movie ratings.
Giảsửta có dữ liệu vềviệc người dùng đánh giá các bộphim theo thang điểm từ0 đến
5 sao.
- nu: Sốlượng người dùng (users).
- nm: Sốlượng phim (movies).
- r(i, j) = 1: Nếu người dùng j đã đánh giá phim i.
- y(i,j): Điểm đánh giá của người dùng j cho phim i (chỉxác định nếu r(i, j) = 1).
Mục tiêu: Dựđoán các giá trịbịthiếu (dấu "?") trong bảng đánh giá đểgợi ý phim
mới cho người dùng.

<!-- page: 74 -->

## 13.2 Content-based Recommendations (Gợi ý dựa trên nội
dung)
Phương pháp này dựa vào thông tin mô tả(content) của sản phẩm (có thểđược cung cấp
bởi nhà sản xuất, nhà phê bình,..). Ví dụ, mỗi bộphim có các đặc trưng (features) như:
mức độlãng mạn (x1), mức độhành động (x2), v.v.
### 13.2.1 Mô hình hóa
Với mỗi người dùng j, ta học một vector tham sốθ(j) ∈Rn+1 thểhiện sởthích của họ. Dự
đoán đánh giá của người dùng j cho phim i bằng:
(θ(j))T x(i)
(13.1)
Trong đó x(i) là vector đặc trưng của phim i.
### 13.2.2 Hàm tối ưu (Optimization Objective)
Đểhọc tham sốθ(j) cho người dùng j, ta cực minimize MSE loss (kèm theo regularization
term):
min
θ(j)
1
2
X
i:r(i,j)=1
((θ(j))T x(i) −y(i,j))2 + λ
2
n
X
k=1
(θ(j)
k )2
(13.2)
Tổng hợp cho tất cảngười dùng:
min
θ(1),...,θ(nu)
1
2
nu
X
j=1
X
i:r(i,j)=1
((θ(j))T x(i) −y(i,j))2 + λ
2
nu
X
j=1
n
X
k=1
(θ(j)
k )2
(13.3)
Vấn đềthực tế: Việc thu thập đầy đủvà chính xác các đặc trưng (features) của phim
(như độlãng mạn, hành động) là rất khó khăn, tốn kém và mang tính chủquan.
## 13.3 Collaborative Filtering (Lọc cộng tác)
Đây là phương pháp khắc phục nhược điểm của Content-based. Thay vì cần đặc trưng
phim có sẵn, ta có thểtựhọc các đặc trưng này dựa trên đánh giá của cộng đồng người
dùng.
### 13.3.1 Ý tưởng cốt lõi
- Nếu ta có θ (sởthích người dùng), ta có thểhọc x (đặc trưng phim).
- Nếu ta có x (đặc trưng phim), ta có thểhọc θ (sởthích người dùng).
- Collaborative Filtering: Thực hiện lặp đi lặp lại hoặc đồng thời việc học cảx và
θ.

<!-- page: 75 -->

### 13.3.2 Hàm tối ưu đồng thời (Simultaneous Optimization)
Hàm chi phí kết hợp cảsai sốdự đoán và điều chuẩn cho cảx và θ:
J(x(1), . . . , x(nm), θ(1), . . . , θ(nu)) = 1
2
X
(i,j):r(i,j)=1
((θ(j))T x(i)−y(i,j))2+λ
2
nm
X
i=1
n
X
k=1
(x(i)
k )2+λ
2
nu
X
j=1
n
X
k=1
(θ(j)
k )2
(13.4)
Mục tiêu:
min
x(1),...,x(nm),θ(1),...,θ(nu) J(. . . )
(13.5)
### 13.3.3 Thuật toán (Collaborative Filtering Algorithm)
1. Khởi tạo: Gán giá trịngẫu nhiên nhỏcho x(1), . . . , x(nm) và θ(1), . . . , θ(nu).
2. Tối ưu hóa: Sửdụng Gradient Descent (hoặc thuật toán khác) đểcực tiểu hóa J.
- Cập nhật x(i):
x(i)
k := x(i)
k −α


X
j:r(i,j)=1
((θ(j))T x(i) −y(i,j))θ(j)
k
+ λx(i)
k


- Cập nhật θ(j):
θ(j)
k
:= θ(j)
k
−α


X
i:r(i,j)=1
((θ(j))T x(i) −y(i,j))x(i)
k + λθ(j)
k


3. Dựđoán: Với một người dùng có tham sốθ và một bộphim có đặc trưng x, điểm dự
đoán là θT x.
## 13.4 Low Rank Matrix Factorization (Phân rã ma trận hạng
thấp)
Collaborative Filtering còn được gọi là Low Rank Matrix Factorization. Ma trận dự
đoán Ypred được tính bằng tích của hai ma trận:
Ypred = XΘT
(13.6)
Trong đó:
- X: Ma trận các vector đặc trưng phim (kích thước nm × n).
- Θ: Ma trận các vector tham sốngười dùng (kích thước nu × n).
Ý nghĩa: Phương pháp này cốgắng phân tách ma trận đánh giá ban đầu (thường rất
lớn và thưa) thành tích của hai ma trận con có hạng thấp (low rank). Điều này giúp:
- Giảm chiều dữ liệu cần lưu trữvà tính toán.
- Nắm bắt được các đặc trưng ẩn (latent features) quan trọng nhất.
- Ví dụ: Thay vì lưu ma trận 5 × 4 (20 phần tử), ta lưu 2 ma trận con 5 × 2 và 4 × 2
(tổng 18 phần tử), khi dữ liệu lớn hiệu quảnén sẽrất đáng kể(chưa tính đến việc chỉ
lưu trữcác cột độc lập tuyến tính, hang của ma trận sẽnhỏđi nhiều).

<!-- page: 76 -->

# Chapter 14: Support Vector Machines (SVM)
## 14.1 Optimization Objective (Mục tiêu tối ưu hóa)
### 14.1.1 TừLogistic Regression đến SVM
Đểhiểu SVM, ta bắt đầu xem xét lại hàm chi phí của Logistic Regression. Với một mẫu
dữ liệu (x, y), hàm mất mát là:
−(y log hθ(x) + (1 −y) log(1 −hθ(x)))
Trong đó hθ(x) =
1
1+e−θT x .
Logistic Regresion chỉchọn ra Decision Boundary phân loại đúng cho dữ liệu, không
phải là Decision Boundary hợp lí nhất-> Nó sẽphân loại sai nhiều trường hợp
Ý tưởng của SVM là tìm ra Decision Boundary sao cho phân tách tốt nhất, tách bạch
nhất giữa các class.
Trong SVM, chúng ta thay thếhàm −log(. . . ) bằng một cost function mới gọi là **Hinge
Loss** (Hàm gãy khúc), ký hiệu là cost1(z) và cost0(z).
- Nếu y = 1 (muốn θT x ≫0): Hàm cost1(z) bằng 0 khi z ≥1. Nếu z < 1, cost tăng
tuyến tính.
- Nếu y = 0 (muốn θT x ≪0): Hàm cost0(z) bằng 0 khi z ≤−1. Nếu z > −1, cost
tăng tuyến tính.

<!-- page: 77 -->

![Hinh: fig-83-1]
Figure 14.1: SVM’s Cost function idea.
### 14.1.2 Hàm chi phí của SVM
Công thức tổng quát của SVM (bỏqua hằng số
1
m và thay thếλ bằng C):
J(θ) = C
m
X
i=1
h
y(i)cost1(θT x(i)) + (1 −y(i))cost0(θT x(i))
+ 1
2
n
X
j=1
θ2
j
(14.1)
Phân tích tham sốC:
- C đóng vai trò tương tựnhư 1
λ.
- Nếu C rất lớn: Tương đương λ ≈0 (Không điều chuẩn). SVM sẽcốgắng phân loại
đúng mọi điểm dữ liệu, dễbịảnh hưởng bởi điểm nhiễu (outliers) →High Variance
(Overfitting).
- Nếu C nhỏ: Tương đương λ lớn. SVM chấp nhận một sốlỗi sai đểđổi lấy lề(margin)
rộng hơn →High Bias (Underfitting).
## 14.2 Large Margin Intuition (Trực giác vềLềlớn)
Tại sao SVM còn được gọi là **Large Margin Classifier**?
### 14.2.1 Điều kiện an toàn
Khác với Logistic Regression chỉcần θT x ≥0 đểdự đoán y = 1, SVM yêu cầu điều kiện
khắt khe hơn đểCost = 0:
- Nếu y = 1, ta muốn θT x ≥1 (không phải chỉ≥0).
- Nếu y = 0, ta muốn θT x ≤−1 (không phải chỉ< 0).
Điều này tạo ra một "vùng an toàn" hoặc khoảng đệm giữa các lớp.

<!-- page: 78 -->

### 14.2.2 Decision Boundary (Ranh giới quyết định)
Khi C rất lớn, SVM sẽtìm đường phân cách sao cho khoảng cách ngắn nhất từđường đó
đến các điểm dữ liệu (gọi là Margin) là lớn nhất.
![Hinh: fig-84-1]
Figure 14.2: SVM tìm kiếm Hyperplane sao cho khoảng cách đến các Support Vectors là
lớn nhất.
Lúc training thì sẽtrain theo Support Vectors, còn inference vẫn dùng
Decision Boundary.
Xửlý nhiễu (Outliers): Nếu có một điểm dữ liệu nhiễu nằm xen vào giữa, một C
quá lớn sẽkhiến Decision Boundary bịlệch hẳn đi đểbao lấy điểm đó (Margin nhỏlại).
Nếu giảm C, SVM sẽbỏqua điểm nhiễu đó đểgiữđược Margin lớn chung cho tổng thể.
## 14.3 Mathematics Behind Large Margin Classification (Toán
học đằng sau)
### 14.3.1 Inner Product
Phép toán đằng sau đó bản chất là inner product. Các bạn có thểtìm hiểu kỹhơn toán
học đằng sau SVM.
Xét u, v ∈R2: uT v = p · ||u||, trong đó:
- ||u||: Độdài của vector u.
- p: Độdài hình chiếu của vector v lên vector u.
### 14.3.2 Tối ưu hóa Margin
Hàm mục tiêu của SVM là cực tiểu hóa 1
2||θ||2. Ta có: θT x(i) = p(i) · ||θ||.
- ĐểθT x(i) ≥1, nếu ||θ|| nhỏ(do cực tiểu hóa), thì p(i) (hình chiếu của x lên θ) phải
lớn.

<!-- page: 79 -->

- p(i) lớn đồng nghĩa với việc các điểm dữ liệu x(i) nằm xa vector pháp tuyến θ (tức là
nằm xa đường phân cách).
- →Tạo ra Large Margin.
## 14.4 Kernels (Hạt nhân)
Khi dữ liệu không thểphân tách tuyến tính (Non-linear), ta cần tạo ra các đặc trưng phức
tạp hơn.
### 14.4.1 Ý tưởng Landmarks (Điểm mốc)
Thay vì tạo đa thức bậc cao (x2
1, x1x2, . . . ), ta chọn các điểm mốc l(1), l(2), . . . trong không
gian. Với mỗi điểm dữ liệu x, ta tính độtương đồng (Similarity) với các landmarks này.
### 14.4.2 Gaussian Kernel (RBF Kernel)
Công thức tính độtương đồng:
fi = similarity(x, l(i)) = exp

−||x −l(i)||2
2σ2
!
(14.2)
Phân tích:
- Nếu x ≈l(i): Tửsố≈0 ⇒fi ≈e0 = 1 (Rất giống).
- Nếu x xa l(i): Tửsốlớn ⇒fi ≈e−∞= 0 (Không giống).
Trong thực tế, ta chọn l(i) = x(i) (Mỗi điểm training là một landmark). Vậy nếu có m
mẫu, ta sẽcó m features mới f ∈Rm.
![Hinh: fig-85-1]
Figure 14.3: Ví dụcách tính feature bằng Gaussian kernel.

<!-- page: 80 -->

![Hinh: fig-86-1]
Figure 14.4: Minh họa ảnh hưởng của variance.
### 14.4.3 Ảnh hưởng của σ2
- σ2 lớn: Đỉnh chuông Gaussian rộng và thoải. Feature fi biến thiên chậm. →High
Bias (Underfitting).
- σ2 nhỏ: Đỉnh chuông nhọn và dốc. Feature fi giảm cực nhanh khi rời xa landmark.
→High Variance (Overfitting).
### 14.4.4 Feature Scaling cho SVM
![Hinh: fig-86-2]
Figure 14.5: SVM Feature Scaling example.
- Ởđây đang bỏqua x0, coi x ∈Rn.

<!-- page: 81 -->

- khi feet lớn, còn lại nhỏ, thì ||x−l||2 gần như hoàn toàn bịchi phối bởi feet, các phần
khác như bedroom sẽbịbỏqua.
→cần phải "do perform feature scaling before using the Gaussian kernel" (ví dụcó
thểdùng Standardization)
## 14.5 SVM trong thực tế(Using an SVM)
Không nên tựcode SVM từđầu (trừkhi đểhọc). Hãy dùng các thư viện tối ưu cao như
libsvm, linear-svm (trong sklearn).
### 14.5.1 Các bước thực hiện
1. Chọn tham sốC.
2. Chọn Kernel:
- No Kernel (Linear Kernel): Dùng khi sốlượng features n lớn, sốmẫu m nhỏ.
- Gaussian Kernel: Dùng khi n nhỏ, m trung bình.
- Bắt buộc phải Feature Scaling trước khi dùng.
### 14.5.2 So sánh Logistic Regression và SVM
Giảsửn là sốfeatures, m là sốmẫu.

| Trường hợp | Ví dụ | Khuyên dùng |
| --- | --- | --- |
| $n \ge m$ | $n=10k,\ m=10..1k$ (Genomics, Text) | Logistic Regression hoặc SVM Linear. (Không đủ dữ liệu để học Kernel phức tạp). |
| n nhỏ, m vừa | $n=1..1k,\ m=10..10k$ | SVM Gaussian Kernel. (Hoạt động cực tốt). |
| n nhỏ, m rất lớn | $n=1..1k,\ m=50k+$ | Tạo thêm features thủ công, rồi dùng Logistic Regression hoặc SVM Linear. (Gaussian Kernel sẽ rất chậm). |

*Table 14.1: Hướng dẫn lựa chọn thuật toán*

Lưu ý: Neural Network hoạt động tốt trong tất cảcác trường hợp trên nhưng có thể
chậm hơn và khó huấn luyện hơn (Local optima). SVM (với hàm lồi) đảm bảo luôn tìm
được Global Optimum.
Nếu muốn thì mình hoàn toàn có thểdùng Kernel cho các thuật toán Clustering khác
như Logistic Regression, nhưng các trick tính toán của Kernel chỉhỗtrợtốt cho SVM,
không khái quát hóa tốt cho các thuật toán khác (ví dụnếu dùng cho Logistic Regresion
thì có thểsẽtính rất chậm.)

<!-- page: 82 -->

# Appendix: Summary & Cheat
Sheet (Phụlục và Tóm tắt)
## A.1 Bảng chọn lựa thuật toán (Algorithm Selection Guide)
Khi đối mặt với một bài toán thực tế, câu hỏi đầu tiên luôn là: "Nên dùng thuật toán
nào?". Dưới đây là bảng tóm tắt dựa trên tính chất dữ liệu và mục tiêu bài toán.
## A.2 Bảng ký hiệu toán học (Mathematical Notation)
Đểtránh nhầm lẫn trong quá trình đọc lại các công thức, dưới đây là quy ước ký hiệu
chung cho toàn bộtài liệu:
| Ký hiệu | Ý nghĩa |
| --- | --- |
| $m$ | Số lượng mẫu dữ liệu huấn luyện (training examples). |
| $n$ | Số lượng đặc trưng (features) (không tính bias unit $x_0$). |
| $x^{(i)}$ | Vector đầu vào (input features) của mẫu thứ $i$. |
| $y^{(i)}$ | Giá trị đầu ra thực tế (output/label) của mẫu thứ $i$. |
| $(x^{(i)}, y^{(i)})$ | Một mẫu huấn luyện (training example). |
| $h_\theta(x)$ | Hàm giả thuyết (Hypothesis function). |
| $\theta$ (hoặc $W$) | Các tham số (parameters/weights) của mô hình. |
| $J(\theta)$ | Hàm chi phí (Cost function/Loss function). |
| $\alpha$ | Tốc độ học (Learning rate). |
| $\lambda$ | Tham số điều chuẩn (Regularization parameter). |
| $L$ | Tổng số lớp (layers) trong Neural Network. |
| $s_l$ | Số lượng đơn vị (units) trong lớp $l$. |
| $\Sigma$ | Ma trận hiệp phương sai (Covariance Matrix) trong PCA/Anomaly Detection. |
| $\mu$ | Vector trung bình (Mean vector). |

## A.3 Các bước xây dựng hệthống ML (Pipeline Checklist)
Khi bắt đầu một dựán mới, hãy tuân theo quy trình sau đểtiết kiệm thời gian:
1. Khởi tạo nhanh: Xây dựng một thuật toán đơn giản nhất có thể(quick and dirty)
đểchạy được ngay.

<!-- page: 83 -->

| Loại bài toán | Dữ liệu đầu ra (y) | Thuật toán gợi ý | Lưu ý |
| --- | --- | --- | --- |
| Regression (Hồi quy) | Liên tục (Continuous) Vd: Giá nhà, nhiệt độ | Linear Regression (Có thể thêm Polynomial) | Dùng Regularization nếu bị Overfitting. |
| Classification (Phân loại) | Rời rạc (Discrete) Vd: 0/1, Spam/Non-spam | Logistic Regression (đơn giản); Neural Networks (phức tạp, phi tuyến) | Neural Net mạnh mẽ với dữ liệu lớn (ảnh, âm thanh). |
| Clustering (Phân cụm) | Không có nhãn (Unlabeled) | K-Means | Cần chọn K hợp lý (Elbow method). |
| Anomaly Detection (Phát hiện bất thường) | Không có nhãn (hoặc rất ít nhãn dương) | Gaussian Distribution (Density Estimation) | Dùng khi số lượng y = 1 rất nhỏ (0-20 mẫu). |
| Recommender (Gợi ý) | Ma trận đánh giá thưa (Sparse Matrix) | Collaborative Filtering (Low Rank Matrix Factorization) | Tự học đặc trưng (x) và sở thích (θ). |
| Data Compression (Nén/Trực quan hóa) | Dữ liệu nhiều chiều (n lớn) | PCA (Principal Component Analysis) | Đừng dùng PCA để chống Overfitting. |

*Table A.1: Hướng dẫn chọn thuật toán Machine Learning cơ bản*

2. Chia dữ liệu: Chia dataset thành 3 phần: Training (60%) - Cross Validation (20%)
- Test (20%).
3. VẽLearning Curves: Kiểm tra xem mô hình đang bịHigh Bias (cần thêm features,
tăng độ phức tạp) hay High Variance (cần thêm data, regularization).
4. Phân tích lỗi (Error Analysis): Kiểm tra thủcông các mẫu bịdự đoán sai trong
tập Cross Validation đểtìm quy luật.
5. Đánh giá: Sửdụng Precision/Recall hoặc F1-Score nếu dữ liệu bịlệch (skewed
classes), không chỉdựa vào Accuracy.
## A.4 Thư viện Python tham khảo
Các thuật toán lý thuyết trên được hiện thực hóa qua các thư viện phổbiến sau:
- NumPy & Pandas: Xửlý ma trận, vector và đọc dữ liệu (X, y).
- Matplotlib & Seaborn: Vẽđồthị(Learning curves, Data visualization).

<!-- page: 84 -->

- Scikit-Learn (sklearn):
- sklearn.linear_model: Linear/Logistic Regression.
- sklearn.cluster.KMeans: K-Means.
- sklearn.decomposition.PCA: PCA.
- sklearn.svm: Support Vector Machines (thường dùng thay thếNeural Net cho
bài toán nhỏ).
- sklearn.model_selection: Train/Test split, Cross-validation.
- TensorFlow / PyTorch: Dùng cho Neural Networks phức tạp (Deep Learning).
