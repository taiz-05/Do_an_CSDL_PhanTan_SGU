# 🎯 KỊCH BẢN DEMO ĐỒ ÁN CSDL PHÂN TÁN (ĐỀ TÀI 1)

Tài liệu này hướng dẫn chi tiết các bước thực hiện demo trước Hội đồng bảo vệ để chứng minh toàn bộ các yêu cầu của Đề tài 1: Phân mảnh dọc, Phân quyền bảo mật, Tính trong suốt và Tính toàn vẹn dữ liệu[cite: 15].

---

## 🛠 CHUẨN BỊ TRƯỚC KHI DEMO
1. **Docker:** Đảm bảo Docker Desktop đang mở. 2 container (`mysql-hanhchinh` và `mysql-luong`) đang ở trạng thái **Running**.
2. **Backend:** Mở Terminal trong VS Code, chạy lệnh `python app.py` và đảm bảo Terminal báo đang chạy ở cổng `5000`.
3. **Frontend:** Mở file `index.html` bằng Live Server trên trình duyệt (Chrome/Edge).
4. **Công cụ Database (Tùy chọn):** Mở sẵn DBeaver hoặc Navicat, kết nối vào `localhost:3306` (DB1) và `localhost:3307` (DB2) để show dữ liệu thực tế nếu Giảng viên yêu cầu.

---

## 🟢 KỊCH BẢN 1: BẢO MẬT PHÂN MẢNH - TÀI KHOẢN NHÂN VIÊN
**Mục tiêu:** Chứng minh Nhân viên chỉ truy cập được dữ liệu thông tin chung, hoàn toàn không thấy thông tin lương[cite: 15].

1. **Thao tác:** Click vào menu **"👨‍💼 Nhân viên (DB1)"** bên thanh điều hướng trái.
2. **Kết quả:** Bảng dữ liệu hiện ra chỉ có các cột: `MaNV`, `HoTen`, `PhongBan`.
3. **🗣️ Lời thuyết trình:** 
   > *"Thưa thầy/cô, hệ thống của nhóm em sử dụng kỹ thuật Phân mảnh dọc, tách làm 2 CSDL vật lý độc lập[cite: 15]. Khi tài khoản Nhân viên đăng nhập, API chỉ kết nối thẳng vào Node 1 (Hành chính). Em đã dùng lệnh `GRANT` trong MySQL để giới hạn quyền `SELECT` của user này. Do đó, dữ liệu lương thưởng hoàn toàn bị ẩn đi, đảm bảo tính bảo mật tuyệt đối[cite: 15]."*

---

## 🟠 KỊCH BẢN 2: BẢO MẬT PHÂN MẢNH - TÀI KHOẢN KẾ TOÁN
**Mục tiêu:** Chứng minh Kế toán chỉ truy cập được dữ liệu tài chính, không thấy thông tin hành chính cá nhân[cite: 15].

1. **Thao tác:** Click vào menu **"💰 Kế toán (DB2)"** bên thanh điều hướng trái.
2. **Kết quả:** Bảng dữ liệu thay đổi, chỉ còn hiện các cột: `MaNV`, `LuongCoBan`, `HeSo`.
3. **🗣️ Lời thuyết trình:** 
   > *"Tương tự, đối với bộ phận Kế toán, API sẽ dùng tài khoản riêng để kết nối thẳng vào Node 2 (port 3307 chứa DB Lương). Hệ thống này được quản lý vật lý hoàn toàn độc lập, kế toán chỉ làm việc với các con số tài chính và Mã nhân viên, đáp ứng đúng yêu cầu chia tách dữ liệu nhạy cảm của đề bài[cite: 15]."*

---

## 🔴 KỊCH BẢN 3: TÍNH TRONG SUỐT - TÀI KHOẢN ADMIN
**Mục tiêu:** Chứng minh khả năng truy vấn gộp xuyên server mà ở tầng ứng dụng không cần biết dữ liệu đang bị phân mảnh ở đâu[cite: 15].

1. **Thao tác:** Click vào menu **"👑 Quản trị viên"** bên thanh điều hướng trái.
2. **Kết quả:** Bảng dữ liệu hiện ra **đầy đủ tất cả các cột** (Họ Tên, Phòng Ban, Lương, Hệ Số).
3. **🗣️ Lời thuyết trình:** 
   > *"Điểm mấu chốt của CSDL Phân tán là Tính trong suốt (Transparency)[cite: 15]. Dưới góc nhìn của Admin, họ vẫn quản lý nhân sự như trên một bảng duy nhất[cite: 15]. Để làm được điều này, nhóm em đã cấu hình **FEDERATED Engine** móc nối DB2 vào DB1, sau đó tạo một `VIEW` tự động `JOIN` dữ liệu 2 bên lại với nhau qua khóa `MaNV`[cite: 15]. Tầng Ứng dụng chỉ việc `SELECT` trên View này mà không cần quan tâm dữ liệu thực tế đang nằm ở server nào[cite: 15]."*

---

## 🔥 KỊCH BẢN 4: ĐỒNG BỘ THAO TÁC & TÍNH TOÀN VẸN (ROLLBACK)
**Mục tiêu:** Chứng minh khi Insert dữ liệu, hệ thống tự tách vào 2 DB, và nếu có sự cố thì Transaction sẽ tự động Rollback[cite: 15].

### Phần A: Thêm dữ liệu thành công (Happy Path)
1. **Thao tác:** Ở form Thêm nhân sự, nhập thông tin: 
   - Mã NV: `99`
   - Họ Tên: `Nguyễn Văn Test`
   - Phòng Ban: `IT`
   - Lương Cơ Bản: `20000000`
   - Hệ Số: `1.5`
2. Bấm **"Lưu Dữ Liệu"**.
3. **🗣️ Lời thuyết trình:** 
   > *"Khi Admin thêm nhân sự mới, API sẽ gọi vào một `Stored Procedure` trên DB1[cite: 15]. SP này sử dụng Transaction để tự động cắt dữ liệu làm đôi: Tên và Phòng ban được `INSERT` vào DB1, Lương và Hệ số được `INSERT` xuyên qua mạng (via Federated Table) để lưu vào DB2[cite: 15]. Mọi thứ diễn ra hoàn toàn tự động."*

### Phần B: Giả lập sự cố đứt mạng (Lấy điểm tuyệt đối)
1. **Thao tác:** Mở phần mềm Docker Desktop. Tìm container `mysql-luong` (DB2) và bấm nút **Stop** (Giả lập máy chủ chứa lương bị sập/đứt cáp).
2. Quay lại giao diện Web, thử thêm nhân viên mới: 
   - Mã NV: `100`
   - Họ Tên: `Trần Lỗi Mạng`
3. Bấm **"Lưu Dữ Liệu"**.
4. **Kết quả:** Hệ thống hiện thông báo lỗi Transaction (Toast màu đỏ).
5. **Thao tác kiểm chứng:** Click lại vào menu **"👨‍💼 Nhân viên (DB1)"** để xem danh sách. **Hoàn toàn không có nhân viên mã 100 nào tên "Trần Lỗi Mạng" được lưu vào.**
6. **🗣️ Lời thuyết trình:** 
   > *"Thưa thầy/cô, em vừa tắt đột ngột máy chủ chứa DB Lương. Khi em cố tình thêm nhân sự mới, do kết nối sang DB2 thất bại, lệnh `ROLLBACK` trong Stored Procedure lập tức kích hoạt để hủy bỏ luôn lệnh thêm tên vào DB1[cite: 15]. Điều này đảm bảo Tính Toàn Vẹn dữ liệu 100%, không bao giờ xảy ra tình trạng 'có tên ở DB1 mà lại bị mất lương ở DB2'[cite: 15]."*