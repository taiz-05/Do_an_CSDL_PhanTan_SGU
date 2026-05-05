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
   
* Tạo và kích hoạt môi trường ảo (tùy chọn nhưng khuyến nghị):

Bash

python -m venv .venv
.\.venv\Scripts\activate   # Trên Windows


3. Cài đặt thư viện:

   ```bash
   pip install -r requirements.txt

* Chạy máy chủ Backend:

Bash
python app.py

*(Backend sẽ chạy tại địa chỉ: `http://localhost:5000`)*

### Bước 3: Mở Giao diện Frontend
1. Cài đặt tiện ích **Live Server** trên VS Code.
2. Click chuột phải vào file `frontend/index.html` -> Chọn **Open with Live Server**.
3. Bắt đầu thao tác trên giao diện web.

---
