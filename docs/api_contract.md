# API Contract — Ứng dụng Web RAG

> **Phiên bản:** 4.0.0  
> **Trạng thái:** Hợp đồng API cho MVP  
> **Cập nhật lần cuối:** 2026-09-16

---

# 0. Quy tắc HTTP chung

## Base URL

### Môi trường phát triển

```text
http://localhost:8000
```

## Tiền tố API

```text
/api/v1
```

## Content-Type

Các API sử dụng JSON:

```http
Content-Type: application/json
Accept: application/json
```

Riêng API upload ảnh sử dụng `multipart/form-data` như mô tả tại phần **Chat đa phương thức**.

## Xác thực

Hệ thống sử dụng **HttpOnly Secure Cookie** để xác thực.

Frontend phải gửi kèm thông tin xác thực khi trình duyệt/client yêu cầu.

Các endpoint được bảo vệ yêu cầu người dùng đã xác thực.

> **Lưu ý:** MVP chỉ sử dụng một cơ chế xác thực là Cookie. Xác thực bằng Bearer Token không thuộc phạm vi của hợp đồng API này.

## Timestamp

Tất cả timestamp sử dụng chuẩn **ISO 8601 theo UTC**.

Ví dụ:

```text
2026-09-13T10:00:00Z
```

## Request ID

Backend tạo một `request_id` cho mỗi HTTP request để phục vụ tracing và ghi log.

Đối với response lỗi, `request_id` luôn được trả về.

Đối với response Chat, `request_id` cũng được trả về vì request có thể cần được theo dõi xuyên suốt pipeline RAG.

Các response CRUD/xác thực thành công khác không bắt buộc phải trả `request_id`.

Ví dụ:

```text
req_8f91d123
```

---

# 1. Xác thực

## POST `/api/v1/auth/register`

Đăng ký tài khoản mới.

### Xác thực

Không yêu cầu.

### Request

```json
{
  "user_name": "CNTT2311001",
  "full_name": "Nguyễn Văn A",
  "password": "CNTT2311"
}
```

### Validation

```text
user_name:
- kiểu dữ liệu: string
- bắt buộc
- không được rỗng
- maxLength = 100

full_name:
- kiểu dữ liệu: string
- bắt buộc
- không được rỗng
- maxLength = 200

password:
- kiểu dữ liệu: string
- bắt buộc
- minLength = 8
- maxLength = 128
```

### Role

Tài khoản mới luôn được tạo với role:

```text
USER
```

Client không được chỉ định hoặc ghi đè role khi đăng ký.

### Thành công — `201 Created`

```json
{
  "message": "Đăng ký tài khoản thành công",
  "user": {
    "id": 1,
    "user_name": "CNTT2311001",
    "full_name": "Nguyễn Văn A",
    "role": "USER"
  }
}
```

### Lỗi — `409 Conflict`

```json
{
  "error": {
    "code": "USERNAME_ALREADY_EXISTS",
    "message": "Tên người dùng đã tồn tại.",
    "request_id": "req_123"
  }
}
```

### Lỗi — `422 Unprocessable Entity`

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Dữ liệu request không vượt qua kiểm tra hợp lệ.",
    "request_id": "req_123",
    "details": {
      "password": "Mật khẩu phải có ít nhất 8 ký tự."
    }
  }
}
```

---

## POST `/api/v1/auth/login`

Đăng nhập.

### Xác thực

Không yêu cầu.

### Request

```json
{
  "user_name": "CNTT2311001",
  "password": "CNTT2311"
}
```

### Validation

```text
user_name:
- kiểu dữ liệu: string
- bắt buộc
- không được rỗng
- maxLength = 100

password:
- kiểu dữ liệu: string
- bắt buộc
- không được rỗng
- maxLength = 128
```

### Thành công — `200 OK`

```json
{
  "message": "Đăng nhập thành công",
  "user": {
    "id": 1,
    "user_name": "CNTT2311001",
    "full_name": "Nguyễn Văn A",
    "role": "USER"
  }
}
```

Phiên xác thực được thiết lập bằng **HttpOnly Secure Cookie** đã cấu hình.

### Lỗi — `401 Unauthorized`

```json
{
  "error": {
    "code": "INVALID_CREDENTIALS",
    "message": "Tên người dùng hoặc mật khẩu không đúng.",
    "request_id": "req_123"
  }
}
```

---

## GET `/api/v1/auth/me`

Lấy thông tin người dùng hiện tại.

### Xác thực

Yêu cầu đã đăng nhập.

### Thành công — `200 OK`

```json
{
  "id": 1,
  "user_name": "CNTT2311001",
  "full_name": "Nguyễn Văn A",
  "role": "USER"
}
```

### Lỗi — `401 Unauthorized`

```json
{
  "error": {
    "code": "UNAUTHORIZED",
    "message": "Yêu cầu xác thực.",
    "request_id": "req_123"
  }
}
```

---

## POST `/api/v1/auth/logout`

Đăng xuất.

### Xác thực

Yêu cầu đã đăng nhập.

### Thành công — `200 OK`

```json
{
  "message": "Đăng xuất thành công"
}
```

Backend vô hiệu hóa và/hoặc xóa phiên xác thực.

---

# 2. Thông tin cá nhân và mật khẩu

## GET `/api/v1/auth/me`

Lấy thông tin cá nhân của người dùng hiện tại.

> Endpoint này đã được định nghĩa ở phần **Xác thực** và đồng thời là API đọc thông tin cá nhân.

Không có API cho phép thay đổi `user_name`.

## PATCH `/api/v1/auth/password`

Đổi mật khẩu cho người dùng hiện tại.

### Xác thực

Yêu cầu đã đăng nhập.

### Request

```json
{
  "current_password": "OldPassword123",
  "new_password": "NewPassword123"
}
```

### Validation

```text
current_password:
- kiểu dữ liệu: string
- bắt buộc
- không được rỗng
- maxLength = 128

new_password:
- kiểu dữ liệu: string
- bắt buộc
- minLength = 8
- maxLength = 128
- phải khác current_password
```

### Thành công — `200 OK`

```json
{
  "message": "Đổi mật khẩu thành công"
}
```

### Lỗi — `401 Unauthorized`

```json
{
  "error": {
    "code": "INVALID_CURRENT_PASSWORD",
    "message": "Mật khẩu hiện tại không đúng.",
    "request_id": "req_123"
  }
}
```

### Lỗi — `422 Unprocessable Entity`

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Dữ liệu request không vượt qua kiểm tra hợp lệ.",
    "request_id": "req_123",
    "details": {
      "new_password": "Mật khẩu mới phải có ít nhất 8 ký tự."
    }
  }
}
```

### Các trường không được thay đổi

Trong MVP, người dùng không được phép thay đổi các trường:

```text
user_name
id
role
```

MVP chỉ cho phép người dùng tự thay đổi `password`.

---

# 3. Health Check

## GET `/api/v1/health`

Kiểm tra Backend có đang hoạt động hay không.

### Xác thực

Không yêu cầu.

### Thành công — `200 OK`

```json
{
  "status": "ok",
  "service": "rag-backend",
  "version": "1.0.0"
}
```

Endpoint này kiểm tra tiến trình Backend có đang hoạt động hay không.

---

## GET `/api/v1/health/ready`

Kiểm tra Backend và các dependency cần thiết để phục vụ request.

### Xác thực

Không yêu cầu.

### Thành công — `200 OK`

```json
{
  "status": "ready",
  "database": "ok",
  "rag_service": "ok"
}
```

### Chưa sẵn sàng — `503 Service Unavailable`

```json
{
  "status": "degraded",
  "database": "ok",
  "rag_service": "offline"
}
```

Endpoint trả về `503 Service Unavailable` khi một dependency bắt buộc không khả dụng.

> **Phạm vi:** Phase 2.

---

# 4. Conversations — Đoạn chat

## POST `/api/v1/conversations`

Tạo một đoạn chat mới.

### Xác thực

Yêu cầu đã đăng nhập.

### Request

```json
{
  "title": "Deep Learning"
}
```

`title` có thể là `null` nếu Backend tự động sinh tiêu đề.

### Validation

```text
title:
- string | null
- maxLength = 200
```

### Thành công — `201 Created`

```json
{
  "id": 1,
  "title": "Deep Learning",
  "created_at": "2026-09-13T10:00:00Z",
  "updated_at": "2026-09-13T10:00:00Z"
}
```

---

## GET `/api/v1/conversations`

Lấy danh sách các đoạn chat của người dùng hiện tại.

### Xác thực

Yêu cầu đã đăng nhập.

### Query Parameters

```text
page:
- integer
- tùy chọn
- mặc định = 1
- min = 1

limit:
- integer
- tùy chọn
- mặc định = 20
- min = 1
- max = 100
```

### Thành công — `200 OK`

```json
{
  "items": [
    {
      "id": 1,
      "title": "Deep Learning",
      "created_at": "2026-09-13T10:00:00Z",
      "updated_at": "2026-09-13T10:00:00Z"
    },
    {
      "id": 2,
      "title": "RAG",
      "created_at": "2026-09-13T11:00:00Z",
      "updated_at": "2026-09-13T11:10:00Z"
    }
  ],
  "page": 1,
  "limit": 20,
  "total": 2
}
```

---

## GET `/api/v1/conversations/{conversation_id}`

Lấy thông tin của một đoạn chat.

### Xác thực

Yêu cầu đã đăng nhập.

### Path Parameter

```text
conversation_id:
- integer
- bắt buộc
```

### Thành công — `200 OK`

```json
{
  "id": 1,
  "title": "Deep Learning",
  "created_at": "2026-09-13T10:00:00Z",
  "updated_at": "2026-09-13T10:10:00Z"
}
```

### Lỗi — `404 Not Found`

Resource không tồn tại hoặc không thuộc người dùng hiện tại.

```json
{
  "error": {
    "code": "RESOURCE_NOT_FOUND",
    "message": "Không tìm thấy đoạn chat.",
    "request_id": "req_123"
  }
}
```

> Không trả `403` khi resource tồn tại nhưng thuộc người dùng khác, nhằm tránh tiết lộ sự tồn tại của resource.

---

## PATCH `/api/v1/conversations/{conversation_id}`

Cập nhật đoạn chat.

Trong MVP, chỉ hỗ trợ thay đổi `title`.

### Xác thực

Yêu cầu đã đăng nhập.

### Request

```json
{
  "title": "CNN và Computer Vision"
}
```

### Validation

```text
title:
- string
- bắt buộc
- maxLength = 200
```

### Thành công — `200 OK`

```json
{
  "id": 1,
  "title": "CNN và Computer Vision",
  "created_at": "2026-09-13T10:00:00Z",
  "updated_at": "2026-09-13T10:20:00Z"
}
```

### Lỗi — `404 Not Found`

```json
{
  "error": {
    "code": "RESOURCE_NOT_FOUND",
    "message": "Không tìm thấy đoạn chat.",
    "request_id": "req_123"
  }
}
```

---

## DELETE `/api/v1/conversations/{conversation_id}`

Xóa đoạn chat.

### Xác thực

Yêu cầu đã đăng nhập.

### Thành công — `204 No Content`

Không có response body.

### Lỗi — `404 Not Found`

```json
{
  "error": {
    "code": "RESOURCE_NOT_FOUND",
    "message": "Không tìm thấy đoạn chat.",
    "request_id": "req_123"
  }
}
```

---

# 5. Messages — Tin nhắn

## GET `/api/v1/conversations/{conversation_id}/messages`

Lấy lịch sử tin nhắn của một đoạn chat.

### Xác thực

Yêu cầu đã đăng nhập.

### Query Parameters

```text
limit:
- integer
- tùy chọn
- mặc định = 50
- min = 1
- max = 100

before_id:
- integer
- tùy chọn
```

`before_id` được sử dụng để lấy các tin nhắn cũ hơn một tin nhắn cụ thể.

### Thành công — `200 OK`

```json
{
  "items": [
    {
      "id": 101,
      "role": "user",
      "content": "CNN là gì?",
      "created_at": "2026-09-13T10:01:00Z"
    },
    {
      "id": 102,
      "role": "assistant",
      "content": "CNN là một kiến trúc mạng nơ-ron...",
      "created_at": "2026-09-13T10:01:05Z"
    }
  ],
  "has_more": false
}
```

### Role

Chỉ cho phép:

```text
user
assistant
```

### Attachments

Mỗi message có thể có 0 hoặc nhiều attachment. Trong MVP, chỉ hỗ trợ attachment dạng ảnh.

```json
{
  "id": 1,
  "type": "image",
  "original_filename": "leaf.jpg",
  "mime_type": "image/jpeg",
  "url": "https://res.cloudinary.com/example/image/upload/..."
}
```

### Lỗi — `404 Not Found`

Conversation không tồn tại hoặc không thuộc người dùng hiện tại.

---

# 6. Chat / RAG

## POST `/api/v1/chat`

Gửi câu hỏi đến hệ thống RAG.

### Xác thực

Yêu cầu đã đăng nhập.

### Request

```json
{
  "conversation_id": 1,
  "message": "CNN là gì?"
}
```

`conversation_id` có thể là `null`.

Khi:

```text
conversation_id = null
```

Backend sẽ tự động tạo một conversation mới.

### Validation

```text
message:
- string
- bắt buộc
- minLength = 1
- maxLength = 4000

conversation_id:
- integer | null
```

### Thành công — `200 OK`

```json
{
  "request_id": "req_8f91d123",
  "conversation_id": 1,
  "answer": "CNN là một kiến trúc mạng nơ-ron tích chập...",
  "sources": [
    {
      "document_name": "deep-learning.pdf",
      "page": 12,
      "content": "CNN là..."
    }
  ]
}
```

### Không có source

```json
{
  "request_id": "req_123",
  "conversation_id": 1,
  "answer": "Tôi không tìm thấy thông tin phù hợp...",
  "sources": []
}
```

`sources` luôn là một mảng và không bao giờ là `null`.

### Lỗi — `404 Not Found`

Conversation không tồn tại hoặc không thuộc người dùng hiện tại.

```json
{
  "error": {
    "code": "RESOURCE_NOT_FOUND",
    "message": "Không tìm thấy đoạn chat.",
    "request_id": "req_123"
  }
}
```

### Lỗi — `503 Service Unavailable`

Dịch vụ RAG không khả dụng.

```json
{
  "error": {
    "code": "RAG_SERVICE_UNAVAILABLE",
    "message": "Dịch vụ RAG hiện không khả dụng.",
    "request_id": "req_123"
  }
}
```

### Lỗi — `504 Gateway Timeout`

Dịch vụ RAG không phản hồi trong thời gian cho phép.

```json
{
  "error": {
    "code": "RAG_SERVICE_TIMEOUT",
    "message": "Yêu cầu tới dịch vụ RAG đã quá thời gian chờ.",
    "request_id": "req_123"
  }
}
```

---

## POST `/api/v1/chat/multimodal`

Gửi câu hỏi kèm ảnh đến AI/RAG và lưu ảnh người dùng trên **Cloudinary**.

Endpoint này được sử dụng khi người dùng gửi câu hỏi có kèm hình ảnh. Backend upload ảnh lên Cloudinary, lưu metadata trong MySQL và lưu message vào conversation. Sau đó Backend gửi dữ liệu cần thiết đến RAG service trên Kaggle để inference.

### Xác thực

Yêu cầu đã đăng nhập.

### Content-Type

```http
Content-Type: multipart/form-data
```

### Form Fields

```text
conversation_id:
- integer | null
- tùy chọn
- nếu null, Backend tự tạo conversation mới

message:
- string
- bắt buộc
- minLength = 1
- maxLength = 4000

image:
- file
- bắt buộc
- chỉ chấp nhận image/jpeg, image/png, image/webp
- maxSize = 10 MB
```

### Quy trình xử lý

```text
Frontend
  ↓
Backend
  ↓
kiểm tra ảnh
  ↓
upload ảnh → Cloudinary
  ↓
lưu metadata attachment → MySQL
  ↓
lưu user message → MySQL
  ↓
gọi RAG service → Kaggle/ngrok
  ↓
lưu assistant message → MySQL
  ↓
trả response
```

### Lưu trữ trên Cloudinary

Cloudinary là nơi lưu trữ ảnh lâu dài cho người dùng. Kaggle **không** được sử dụng làm persistent image storage.

Mỗi ảnh upload phải có tối thiểu các metadata:

```text
storage_provider
public_id
secure_url
original_filename
mime_type
file_size
created_at
```

### Quy tắc đặt tên đối tượng trên Cloudinary

Backend nên đặt `public_id` theo conversation/message để dễ quản lý và xóa, ví dụ:

```text
rag_app/conversations/{conversation_id}/messages/{message_id}/{unique_id}
```

`unique_id` do Backend sinh và không được phụ thuộc vào `username`.

### Quy tắc lưu trữ

1. Ảnh phải được upload lên Cloudinary trước khi trả response thành công.
2. Metadata ảnh phải được lưu trong MySQL và liên kết với `message_id`.
3. Frontend không được chứa Cloudinary API secret.
4. Cloudinary API secret chỉ được lưu trong biến môi trường của Backend.
5. Kaggle chỉ xử lý inference; không phải nơi lưu trữ lâu dài dữ liệu ảnh của người dùng.
6. Khi xóa conversation, Backend phải xóa các attachment record trong MySQL và các Cloudinary object tương ứng.
7. Nếu upload Cloudinary thành công nhưng lưu DB thất bại, Backend phải cleanup Cloudinary object để tránh file mồ côi.
8. Nếu request RAG thất bại sau khi ảnh đã được lưu, Backend có thể giữ attachment và user message để retry/debug theo chính sách hệ thống.

### Mô hình Attachment trong MySQL

Bảng `message_attachments` tối thiểu gồm:

```text
id
message_id
storage_provider
public_id
secure_url
original_filename
mime_type
file_size
created_at
```

Quan hệ:

```text
messages 1 ─── N message_attachments
```

### Thành công — `200 OK`

```json
{
  "request_id": "req_8f91d123",
  "conversation_id": 1,
  "message_id": 101,
  "answer": "Trong hình là một sơ đồ mạng nơ-ron...",
  "sources": [],
  "attachments": [
    {
      "id": 1,
      "type": "image",
      "original_filename": "diagram.png",
      "mime_type": "image/png",
      "url": "https://res.cloudinary.com/example/image/upload/..."
    }
  ]
}
```

### Lỗi — `400 Bad Request`

```json
{
  "error": {
    "code": "INVALID_IMAGE",
    "message": "Định dạng hoặc nội dung file ảnh không hợp lệ.",
    "request_id": "req_123"
  }
}
```

### Lỗi — `404 Not Found`

Conversation không tồn tại hoặc không thuộc người dùng hiện tại.

### Lỗi — `413 Content Too Large`

```json
{
  "error": {
    "code": "IMAGE_TOO_LARGE",
    "message": "Kích thước ảnh vượt quá giới hạn 10 MB.",
    "request_id": "req_123"
  }
}
```

### Lỗi — `415 Unsupported Media Type`

```json
{
  "error": {
    "code": "UNSUPPORTED_MEDIA_TYPE",
    "message": "Chỉ hỗ trợ ảnh JPEG, PNG và WebP.",
    "request_id": "req_123"
  }
}
```

### Lỗi — `502 Bad Gateway`

Lỗi upload ảnh lên Cloudinary.

```json
{
  "error": {
    "code": "IMAGE_STORAGE_ERROR",
    "message": "Dịch vụ lưu trữ ảnh gặp lỗi.",
    "request_id": "req_123"
  }
}
```

### Lỗi — `503 Service Unavailable`

Dịch vụ RAG không khả dụng.

```json
{
  "error": {
    "code": "RAG_SERVICE_UNAVAILABLE",
    "message": "Dịch vụ RAG hiện không khả dụng.",
    "request_id": "req_123"
  }
}
```

### Lỗi — `504 Gateway Timeout`

Dịch vụ RAG không phản hồi trong thời gian cho phép.

```json
{
  "error": {
    "code": "RAG_SERVICE_TIMEOUT",
    "message": "Yêu cầu tới dịch vụ RAG đã quá thời gian chờ.",
    "request_id": "req_123"
  }
}
```

### Quy tắc kiểm tra ảnh

- Backend phải kiểm tra MIME type và nội dung file thực tế.
- Backend không được tin tưởng phần mở rộng file do client gửi lên.
- Không chấp nhận file vượt quá 10 MB.
- Chỉ chấp nhận JPEG, PNG và WebP trong MVP.
- Metadata EXIF không được trả về Frontend trong MVP.

---

# 7. Source Object — Nguồn tài liệu

Source object dùng để mô tả tài liệu được RAG sử dụng để tạo câu trả lời.

```json
{
  "document_name": "deep-learning.pdf",
  "page": 12,
  "content": "CNN là..."
}
```

## Schema

```text
document_name:
- string
- bắt buộc

page:
- integer | null

content:
- string
- bắt buộc
```

`sources` luôn là một mảng.

> `document_id`, `chunk_id` và `score` chưa thuộc MVP contract. Có thể bổ sung khi Frontend cần mở tài liệu, định vị chunk hoặc hiển thị độ liên quan.

---

# 8. Error Response — Phản hồi lỗi

Tất cả API lỗi sử dụng format:

```json
{
  "error": {
    "code": "ERROR_CODE",
    "message": "Thông báo lỗi dễ đọc.",
    "request_id": "req_123"
  }
}
```

Validation error có thể bổ sung `details`:

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Dữ liệu request không vượt qua kiểm tra hợp lệ.",
    "request_id": "req_123",
    "details": {
      "password": "Mật khẩu phải có ít nhất 8 ký tự."
    }
  }
}
```

## HTTP Status

### `400 Bad Request`

```text
INVALID_REQUEST
```

Request không hợp lệ ở mức HTTP hoặc cấu trúc request.

### `401 Unauthorized`

```text
UNAUTHORIZED
INVALID_CREDENTIALS
```

Các trường hợp:

- Chưa xác thực.
- Session không hợp lệ.
- Username/password không đúng.

### `403 Forbidden`

```text
FORBIDDEN
```

Đã xác thực nhưng không có quyền thực hiện hành động.

> Các conversation không thuộc người dùng hiện tại sử dụng `404 RESOURCE_NOT_FOUND` thay vì `403` để tránh tiết lộ resource tồn tại.

### `404 Not Found`

```text
RESOURCE_NOT_FOUND
```

Resource không tồn tại hoặc không thuộc người dùng hiện tại.

### `409 Conflict`

```text
USERNAME_ALREADY_EXISTS
```

Có xung đột với resource hiện tại.

### `422 Unprocessable Entity`

```text
VALIDATION_ERROR
```

Request đúng cấu trúc nhưng dữ liệu không vượt qua validation.

### `429 Too Many Requests`

```text
RATE_LIMIT_EXCEEDED
```

Client vượt quá rate limit.

### `413 Content Too Large`

```text
IMAGE_TOO_LARGE
```

Payload upload vượt giới hạn kích thước cho phép.

### `415 Unsupported Media Type`

```text
UNSUPPORTED_MEDIA_TYPE
```

`Content-Type` hoặc định dạng file không được hỗ trợ.

### `500 Internal Server Error`

```text
INTERNAL_SERVER_ERROR
```

Lỗi không xác định phía Backend.

### `503 Service Unavailable`

```text
RAG_SERVICE_UNAVAILABLE
```

RAG service hoặc dependency cần thiết hiện không khả dụng.

### `504 Gateway Timeout`

```text
RAG_SERVICE_TIMEOUT
```

RAG service không phản hồi trong thời gian cho phép.

---

# 9. User Roles — Vai trò người dùng

Hệ thống có 2 role:

```text
USER
ADMIN
```

## USER

```json
{
  "id": 1,
  "user_name": "CNTT2311001",
  "full_name": "Nguyễn Văn A",
  "role": "USER"
}
```

## ADMIN

```json
{
  "id": 2,
  "user_name": "admin",
  "full_name": "Administrator",
  "role": "ADMIN"
}
```

API không phân biệt `USER` là sinh viên hay giáo viên.

Role được quyết định bởi Backend.

Client không được tự đặt role khi đăng ký.

---

# 10. Request ID

Backend tạo `request_id` cho mỗi HTTP request.

Ví dụ:

```text
req_8f91d123
```

`request_id` được sử dụng để:

- theo dõi request;
- đối chiếu Backend logs;
- debug lỗi;
- hỗ trợ theo dõi RAG request.

## Quy tắc Response

`request_id` bắt buộc trong:

- Error response.
- Chat success response.

Các response CRUD/xác thực thành công khác không bắt buộc trả `request_id`.

---

# 11. Pagination — Phân trang

## Conversations

Sử dụng phân trang theo page:

```http
GET /api/v1/conversations?page=1&limit=20
```

Response:

```json
{
  "items": [],
  "page": 1,
  "limit": 20,
  "total": 100
}
```

## Messages

Sử dụng phân trang kiểu cursor:

```http
GET /api/v1/conversations/1/messages?before_id=500&limit=50
```

Response:

```json
{
  "items": [],
  "has_more": true
}
```

Mục tiêu là tránh phải tải toàn bộ lịch sử conversation trong một request.

---

# 12. CORS / Hành vi trình duyệt

Nếu Frontend và Backend chạy khác origin:

- Backend phải cấu hình CORS cho các frontend origin được phép.
- Khi sử dụng authentication bằng Cookie, client phải gửi credentials.
- Không cho phép wildcard origin (`*`) khi credentials được sử dụng.

CORS configuration là cấu hình triển khai, không phải endpoint API.

---

# 13. Phạm vi chức năng

| Chức năng | API | Trạng thái |
|---|---|---|
| Tạo đoạn chat mới | `POST /api/v1/conversations` hoặc `POST /api/v1/chat` với `conversation_id = null` | Đã có |
| Xem danh sách lịch sử chat | `GET /api/v1/conversations` | Đã có |
| Xem nội dung lịch sử của một chat | `GET /api/v1/conversations/{conversation_id}/messages` | Đã có |
| Xóa lịch sử chat | `DELETE /api/v1/conversations/{conversation_id}` | Đã có |
| Xem thông tin cá nhân | `GET /api/v1/auth/me` | Đã có |
| Đổi mật khẩu | `PATCH /api/v1/auth/password` | Đã có |
| Đổi username | Không cung cấp API | Cố ý không hỗ trợ |
| Upload ảnh để hỏi AI | `POST /api/v1/chat/multimodal` | Đã có |
| Lưu ảnh người dùng | Cloudinary + `message_attachments` | Đã có |
| Xóa ảnh khi xóa conversation | Cascade DB + Cloudinary delete | Đã có |

---

# 14. Tóm tắt API

## MVP

```text
POST   /api/v1/auth/register
POST   /api/v1/auth/login
POST   /api/v1/auth/logout
GET    /api/v1/auth/me
PATCH  /api/v1/auth/password

GET    /api/v1/health

GET    /api/v1/conversations
POST   /api/v1/conversations
GET    /api/v1/conversations/{conversation_id}
PATCH  /api/v1/conversations/{conversation_id}
DELETE /api/v1/conversations/{conversation_id}

GET    /api/v1/conversations/{conversation_id}/messages

POST   /api/v1/chat
POST   /api/v1/chat/multimodal
```

## Phase 2

```text
GET    /api/v1/health/ready
POST   /api/v1/chat/stream
```

---

# 15. Phase 2 — Streaming

## POST `/api/v1/chat/stream`

Streaming câu trả lời.

### Trạng thái

Phase 2.

### Trạng thái Contract

**Chưa hoàn thiện / chưa chốt.**

Frontend không được tích hợp endpoint này cho đến khi Backend và Frontend thống nhất:

- giao thức streaming;
- Content-Type;
- định dạng event;
- định dạng event lỗi;
- event hoàn tất;
- hành vi khi disconnect/reconnect.

Định hướng hiện tại:

```text
SSE (Server-Sent Events)
```

endpoint này chưa thuộc MVP contract.

---

# 16. Quyết định phạm vi MVP


1. Authentication sử dụng HttpOnly Secure Cookie.
2. Chỉ có `USER` và `ADMIN`.
3. User mới đăng ký luôn có role `USER`.
4. Conversation thuộc user nào thì chỉ user đó được truy cập.
5. Resource của user khác được trả `404`, không trả `403`.
6. Error response luôn có `request_id`.
7. Chat response luôn có `request_id`.
8. `sources` luôn là array.
9. Timestamp sử dụng UTC ISO 8601.
10. Conversations sử dụng page-based pagination.
11. Messages sử dụng cursor-style pagination.
12. Streaming chưa được chốt cho MVP.
13. Source Object MVP chỉ gồm `document_name`, `page`, `content`.

---
