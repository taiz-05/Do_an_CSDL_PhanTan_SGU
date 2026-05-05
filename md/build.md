🚀 Hướng dẫn Cài đặt & Khởi chạy
###Bước 1: Khởi động Hệ thống CSDL (Docker)
Yêu cầu máy tính đã cài đặt và bật phần mềm Docker Desktop.

Mở Terminal tại thư mục gốc của dự án.

Chạy lệnh khởi tạo 2 Node CSDL:


Bash
docker compose up -d

*(Lưu ý: Đợi khoảng 30s để MySQL khởi động xong và mở port 3306, 3307).*





### Bước 2: Khởi động Backend API
Yêu cầu máy tính đã cài đặt **Python**.
1. Mở Terminal, di chuyển vào thư mục `backend`:
   ```bash
   cd backend
   
Tạo và kích hoạt môi trường ảo (tùy chọn nhưng khuyến nghị):

Bash
python -m venv .venv
.\.venv\Scripts\activate   # Trên Windows


3. Cài đặt thư viện:
   ```bash
   pip install -r requirements.txt
Chạy máy chủ Backend:

Bash
python app.py

*(Backend sẽ chạy tại địa chỉ: `http://localhost:5000`)*

### Bước 3: Mở Giao diện Frontend
1. Cài đặt tiện ích **Live Server** trên VS Code.
2. Click chuột phải vào file `frontend/index.html` -> Chọn **Open with Live Server**.
3. Bắt đầu thao tác trên giao diện web.

---

## 🎯 Kịch bản Demo (Dành cho báo cáo)

* **Demo 1 - Phân quyền DB1 (Nhân viên):** Bấm nút đăng nhập "Nhân viên". Hệ thống gọi vào DB1, chỉ trả về Tên và Phòng ban. Dữ liệu lương được bảo mật hoàn toàn.

* **Demo 2 - Phân quyền DB2 (Kế toán):** Bấm nút đăng nhập "Kế toán". Hệ thống gọi vào DB2, chỉ trả về Mã NV và Lương. 

* **Demo 3 - Tính Trong Suốt (Admin):** Bấm nút đăng nhập "Admin". Hệ thống gọi vào View `vw_HoSoToanDien` ở DB1. Mặc dù dữ liệu nằm ở 2 server khác nhau, hệ thống vẫn trả về một bảng thống nhất (có cả Tên và Lương) một cách tự động nhờ `FEDERATED Engine`.

* **Demo 4 - Đồng bộ & Tính Toàn Vẹn (Thêm Nhân sự):** Nhập thông tin nhân viên mới và bấm Lưu. Dữ liệu sẽ tự động được cắt dọc: Tên vào DB1, Lương vào DB2. Nếu 1 trong 2 Node sập, giao dịch sẽ tự động Rollback không để lại dữ liệu rác.