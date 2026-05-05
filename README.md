# Đồ án: Quản lý Lương & Hồ sơ Nhân sự (Cơ sở dữ liệu Phân tán)

## 📌 Giới thiệu đồ án
Đồ án áp dụng kỹ thuật **Phân mảnh dọc (Vertical Fragmentation)** để giải quyết bài toán bảo mật dữ liệu nhạy cảm trong doanh nghiệp. Hệ thống tách biệt hoàn toàn CSDL thông tin hành chính công khai và CSDL lương thưởng thành 2 Node vật lý độc lập. 

### Mục tiêu đạt được:
1. **Phân mảnh dọc:** Tách DB thành `db_hanhchinh` và `db_luong`.
2. **Tính trong suốt:** Sử dụng tính năng `FEDERATED Engine` và `VIEW` của MySQL để gộp dữ liệu xuyên server.
3. **Phân quyền bảo mật:** Ngăn chặn tuyệt đối nhân viên truy cập dữ liệu lương bằng cơ chế phân quyền tài khoản dưới đáy Database.
4. **Đồng bộ thao tác:** Sử dụng `Stored Procedure` và `Transaction Rollback` để đảm bảo thao tác thêm nhân sự luôn nhất quán trên cả 2 Node.

---

## ⚙️ Cấu trúc thư mục
```text
do-an-phan-manh-doc/
│
├── backend/                  # Chứa API kết nối CSDL (Python Flask)
│   ├── app.py                # Source code Backend
│   └── requirements.txt      # Khai báo thư viện Python
│
├── frontend/                 # Giao diện hiển thị (HTML/JS)
│   └── index.html            # Giao diện Dashboard quản trị
│
├── docker-compose.yml        # File khởi tạo 2 Node CSDL vật lý
├── db1-init.sql              # Script tạo DB1 (Hành chính + View gộp + Phân quyền)
├── db2-init.sql              # Script tạo DB2 (Lương thưởng + Cấp quyền Federated)
└── README.md                 # Tài liệu hướng dẫn



