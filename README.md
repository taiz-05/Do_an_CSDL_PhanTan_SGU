# 🏢 Đồ án: Quản lý Lương & Hồ sơ Nhân sự (CSDL Phân tán)

![MySQL](https://img.shields.io/badge/MySQL-8.0-blue?style=flat-square&logo=mysql)
![Python](https://img.shields.io/badge/Python-Flask-yellow?style=flat-square&logo=python)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?style=flat-square&logo=docker)
![HTML5](https://img.shields.io/badge/Frontend-HTML%2FJS-E34F26?style=flat-square&logo=html5)

## 📌 Giới thiệu đồ án
Đồ án áp dụng kỹ thuật **Phân mảnh dọc (Vertical Fragmentation)** để giải quyết bài toán bảo mật dữ liệu nhạy cảm trong doanh nghiệp. Hệ thống tách biệt hoàn toàn CSDL thông tin hành chính công khai và CSDL lương thưởng thành 2 Node vật lý độc lập, được triển khai qua Docker.

### 🌟 Các Tính năng Kỹ thuật Cốt lõi:
1. **Phân mảnh dọc (Vertical Fragmentation):** Tách DB thành `db_hanhchinh` (Node 1) và `db_luong` (Node 2).
2. **Tính trong suốt (Transparency):** Sử dụng tính năng `FEDERATED Engine` và `VIEW` của MySQL để gộp dữ liệu xuyên server, giúp App thao tác như trên 1 DB duy nhất[cite: 7].
3. **Chu trình CRUD Phân tán:** Thực hiện đầy đủ Thêm, Xem, Sửa, Xóa đồng thời trên 2 Server[cite: 7].
4. **Đồng bộ & Toàn vẹn (Transactions):** Sử dụng `Stored Procedure` kết hợp `ROLLBACK` để đảm bảo dữ liệu luôn nhất quán, không để lại dữ liệu rác nếu 1 Node gặp sự cố đứt mạng[cite: 7].
5. **Thống kê Phân tán (Distributed Aggregation):** Thực thi lệnh `GROUP BY` và `SUM` chéo giữa 2 Node vật lý[cite: 7].
6. **Tính tự trị (Local Autonomy):** Khả năng hoạt động độc lập của từng Node khi có máy chủ khác bị sập[cite: 7].
7. **Bảo mật Tầng đáy (DB Engine Security):** Phân quyền bằng lệnh `GRANT` ngăn chặn truy cập trái phép từ tận lõi Database[cite: 7].

---

## 🚀 Hướng dẫn Cài đặt & Khởi chạy

### Bước 1: Tải mã nguồn từ GitHub (Clone/Pull)
Để tránh lỗi cài đặt môi trường trên Windows, hãy chọn một thư mục gốc an toàn (không nằm trong OneDrive và không chứa dấu tiếng Việt, ví dụ: `C:\Projects` hoặc `D:\Workspace`).
1. Mở Terminal (hoặc Git Bash) tại thư mục bạn muốn lưu dự án.
2. Chạy lệnh sau để tải code về và di chuyển vào thư mục dự án:
   ```bash
   git clone <đường-dẫn-repo-github-của-bạn>
   cd Do_an_CSDL_PhanTan_SGU
   (Lưu ý: Thay <đường-dẫn-repo-github-của-bạn> bằng link thực tế của kho chứa).

Bước 2: Khởi động Hệ thống CSDL (Docker)
Yêu cầu máy tính đã cài đặt và bật phần mềm Docker Desktop[cite: 7].

Mở Terminal tại thư mục gốc của dự án[cite: 7].

Chạy lệnh khởi tạo 2 Node CSDL:

Bash
docker compose up -d

*(Lưu ý: Đợi khoảng 30s để MySQL khởi động xong và mở port 3306, 3307)*[cite: 7].

### Bước 3: Khởi động Backend API & Cài đặt venv
Yêu cầu máy tính đã cài đặt **Python**[cite: 7].
1. Mở Terminal, di chuyển vào thư mục `backend`[cite: 7]:
   ```bash
   cd backend
Tạo môi trường ảo (.venv) để chứa các thư viện độc lập cho dự án:

Bash
python -m venv .venv
Kích hoạt môi trường ảo:

Bash
.\.venv\Scripts\activate

   *(Thành công khi thấy chữ `(.venv)` hiện lên ở đầu dòng lệnh).*
4. Cài đặt các thư viện cần thiết:
   ```bash
   pip install -r requirements.txt
  5. Chạy máy chủ Backend:

Bash
python app.py
*(Backend sẽ chạy tại địa chỉ: `http://localhost:5000`)*[cite: 7]

### Bước 4: Mở Giao diện Frontend
1. Cài đặt tiện ích **Live Server** trên phần mềm VS Code[cite: 7].
2. Click chuột phải vào file `frontend/index.html` -> Chọn **Open with Live Server**[cite: 7].
3. Bắt đầu trải nghiệm hệ thống tại giao diện web[cite: 7].

---

## 🎯 Danh sách 10 Kịch bản Demo Hệ thống

1. **Bảo mật DB1 (Nhân viên):** Giới hạn quyền chỉ xem thông Hành chính (Ẩn Lương)[cite: 7].
2. **Bảo mật DB2 (Kế toán):** Giới hạn quyền chỉ xem thông tin Tài chính (Ẩn Tên)[cite: 7].
3. **Tính Trong Suốt (Admin):** View gộp dữ liệu xuyên mạng qua FEDERATED[cite: 7].
4. **Đồng bộ Thêm (Insert):** Transaction tự động phân tách dữ liệu lưu vào 2 Node[cite: 7].
5. **Đồng bộ Sửa (Update):** Cập nhật đồng thời thông tin ở cả DB1 và DB2[cite: 7].
6. **Thống kê Phân tán:** JOIN, GROUP BY và SUM dữ liệu phức tạp xuyên Server[cite: 7].
7. **Đồng bộ Xóa (Delete):** Transaction tự động xóa sạch dữ liệu liên kết trên toàn hệ thống[cite: 7].
8. **Xử lý Sự cố (Rollback):** Giả lập đứt mạng, kiểm tra Rollback bảo vệ tính toàn vẹn[cite: 7].
9. **Tính Tự Trị Địa Phương:** Tắt DB1, kiểm tra DB2 vẫn hoạt động bình thường và độc lập[cite: 7].
10. **Bảo mật Cấp Đáy:** Bypass giao diện web, truy cập DB bằng Tool (DBeaver/Terminal) bị từ chối hoàn toàn[cite: 7].