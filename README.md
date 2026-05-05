# Đồ án: Quản lý Lương & Hồ sơ Nhân sự (Cơ sở dữ liệu Phân tán)

## 📌 Giới thiệu đồ án
Đồ án áp dụng kỹ thuật **Phân mảnh dọc (Vertical Fragmentation)** để giải quyết bài toán bảo mật dữ liệu nhạy cảm trong doanh nghiệp. Hệ thống tách biệt hoàn toàn CSDL thông tin hành chính công khai và CSDL lương thưởng thành 2 Node vật lý độc lập. 

### Mục tiêu đạt được:
1. **Phân mảnh dọc:** Tách DB thành `db_hanhchinh` và `db_luong`.
2. **Tính trong suốt:** Sử dụng tính năng `FEDERATED Engine` và `VIEW` của MySQL để gộp dữ liệu xuyên server.
3. **Phân quyền bảo mật:** Ngăn chặn tuyệt đối nhân viên truy cập dữ liệu lương bằng cơ chế phân quyền tài khoản dưới đáy Database.
4. **Đồng bộ thao tác:** Sử dụng `Stored Procedure` (Thêm & Xóa) và `Transaction Rollback` để đảm bảo thao tác luôn nhất quán.
5. **Tính tự trị địa phương:** Khả năng hoạt động độc lập của từng Node khi có sự cố.

---

## 🚀 Hướng dẫn Cài đặt & Khởi chạy

### Bước 1: Khởi động Hệ thống CSDL (Docker)
Yêu cầu máy tính đã cài đặt và bật phần mềm Docker Desktop.
1. Mở Terminal tại thư mục gốc của dự án.
2. Chạy lệnh khởi tạo 2 Node CSDL:
   ```bash
   docker compose up -d

   (Lưu ý: Đợi khoảng 30s để MySQL khởi động xong và mở port 3306, 3307).

### Bước 2: Khởi động Backend API
Yêu cầu máy tính đã cài đặt Python.

1. Mở Terminal, di chuyển vào thư mục backend:

Bash
cd backend

2. Tạo và kích hoạt môi trường ảo:

Bash
python -m venv .venv
.\.venv\Scripts\activate   # Trên Windows

3. Cài đặt thư viện:

Bash
pip install -r requirements.txt

4. Chạy máy chủ Backend:

Bash
python app.py

*(Backend sẽ chạy tại địa chỉ: `http://localhost:5000`)*

### Bước 3: Mở Giao diện Frontend
1. Cài đặt tiện ích **Live Server** trên VS Code.
2. Click chuột phải vào file `frontend/index.html` -> Chọn **Open with Live Server**.

---

## 🎯 Danh sách 7 Kịch bản Demo Hệ thống
* **Demo 1 - Phân quyền DB1 (Nhân viên):** Kiểm tra giới hạn quyền xem thông tin chung.
* **Demo 2 - Phân quyền DB2 (Kế toán):** Kiểm tra giới hạn quyền xem thông tin lương.
* **Demo 3 - Tính Trong Suốt (Admin):** Kiểm tra View gộp (FEDERATED).
* **Demo 4 - Đồng bộ Thêm Nhân Sự:** Transaction tự động phân tách dữ liệu.
* **Demo 5 - Đồng bộ Xóa Nhân Sự:** Transaction tự động xóa dữ liệu mồ côi trên cả 2 Node.
* **Demo 6 - Xử lý Sự cố (Rollback):** Giả lập đứt mạng, kiểm tra Rollback toàn vẹn dữ liệu.
* **Demo 7 - Tính Tự Trị Địa Phương:** Tắt DB1, kiểm tra DB2 vẫn hoạt động bình thường.