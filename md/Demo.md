# 🎯 KỊCH BẢN DEMO ĐỒ ÁN CSDL PHÂN TÁN (ĐỀ TÀI 1)

Tài liệu này hướng dẫn chi tiết 7 bước thực hiện demo trước Hội đồng bảo vệ để chứng minh toàn bộ các yêu cầu: Phân mảnh dọc, Phân quyền bảo mật, Tính trong suốt, Tính toàn vẹn dữ liệu và Tính tự trị[cite: 10].

---

## 🟢 KỊCH BẢN 1: BẢO MẬT PHÂN MẢNH - TÀI KHOẢN NHÂN VIÊN
**Mục tiêu:** Chứng minh Nhân viên chỉ truy cập được dữ liệu thông tin chung, hoàn toàn không thấy thông tin lương[cite: 10].

1. **Thao tác:** Click vào menu **"👨‍💼 Nhân viên (DB1)"**.
2. **Kết quả:** Bảng dữ liệu hiện ra chỉ có các cột: `MaNV`, `HoTen`, `PhongBan`[cite: 10].
3. **🗣️ Lời thuyết trình:** 
   > *"Thưa thầy/cô, hệ thống của nhóm em sử dụng kỹ thuật Phân mảnh dọc, tách làm 2 CSDL vật lý độc lập. Khi tài khoản Nhân viên đăng nhập, API chỉ kết nối thẳng vào Node 1 (Hành chính). Em đã dùng lệnh `GRANT` trong MySQL để giới hạn quyền `SELECT` của user này. Do đó, dữ liệu lương thưởng hoàn toàn bị ẩn đi, đảm bảo tính bảo mật tuyệt đối[cite: 10]."*

---

## 🟠 KỊCH BẢN 2: BẢO MẬT PHÂN MẢNH - TÀI KHOẢN KẾ TOÁN
**Mục tiêu:** Chứng minh Kế toán chỉ truy cập được dữ liệu tài chính, không thấy thông tin hành chính cá nhân[cite: 10].

1. **Thao tác:** Click vào menu **"💰 Kế toán (DB2)"**.
2. **Kết quả:** Bảng dữ liệu thay đổi, chỉ còn hiện các cột: `MaNV`, `LuongCoBan`, `HeSo`[cite: 10].
3. **🗣️ Lời thuyết trình:** 
   > *"Tương tự, đối với bộ phận Kế toán, API sẽ dùng tài khoản riêng để kết nối thẳng vào Node 2 (port 3307 chứa DB Lương). Hệ thống này được quản lý vật lý hoàn toàn độc lập, kế toán chỉ làm việc với các con số tài chính và Mã nhân viên, đáp ứng đúng yêu cầu chia tách dữ liệu nhạy cảm của đề bài[cite: 10]."*

---

## 🔴 KỊCH BẢN 3: TÍNH TRONG SUỐT - TÀI KHOẢN ADMIN
**Mục tiêu:** Chứng minh khả năng truy vấn gộp xuyên server mà ở tầng ứng dụng không cần biết dữ liệu đang bị phân mảnh ở đâu[cite: 10].

1. **Thao tác:** Click vào menu **"👑 Quản trị viên"**.
2. **Kết quả:** Bảng dữ liệu hiện ra **đầy đủ tất cả các cột** (Họ Tên, Phòng Ban, Lương, Hệ Số)[cite: 10].
3. **🗣️ Lời thuyết trình:** 
   > *"Điểm mấu chốt của CSDL Phân tán là Tính trong suốt. Dưới góc nhìn của Admin, họ vẫn quản lý nhân sự như trên một bảng duy nhất. Để làm được điều này, nhóm em đã cấu hình **FEDERATED Engine** móc nối DB2 vào DB1, sau đó tạo một `VIEW` tự động `JOIN` dữ liệu 2 bên lại với nhau. Tầng Ứng dụng chỉ việc `SELECT` trên View này mà không cần quan tâm dữ liệu thực tế đang nằm ở server nào[cite: 10]."*

---

## 🔥 KỊCH BẢN 4: ĐỒNG BỘ THAO TÁC (THÊM NHÂN SỰ)
**Mục tiêu:** Chứng minh khi Insert dữ liệu, hệ thống tự động chẻ dữ liệu làm đôi và lưu vào đúng 2 DB.

1. **Thao tác:** Ở form Thêm nhân sự, nhập thông tin: Mã NV (99), Họ Tên (Nguyễn Văn A), Phòng Ban (IT), Lương (20000000), Hệ Số (1.5). Bấm **"Lưu Dữ Liệu"**.
2. **Kết quả:** Hệ thống báo thành công. Bảng Admin hiện nhân viên mới.
3. **🗣️ Lời thuyết trình:** 
   > *"Khi Admin thêm nhân sự mới, API gọi vào một `Stored Procedure`. SP này sử dụng Transaction để tự động cắt dữ liệu làm đôi: Tên và Phòng ban được lưu vào DB1, Lương và Hệ số được chèn xuyên qua mạng (via Federated Table) để lưu vào DB2. Mọi thứ diễn ra hoàn toàn tự động."*

---

## 🗑️ KỊCH BẢN 5: ĐỒNG BỘ THAO TÁC (XÓA NHÂN SỰ)
**Mục tiêu:** Khép kín chu trình quản lý, chứng minh khi xóa 1 nhân sự, dữ liệu ở cả 2 Node vật lý đều bị xóa sạch sẽ cùng lúc.

1. **Thao tác:** Ở ô Xóa nhân sự, nhập số `99` (Mã NV vừa tạo). Bấm **"Thực thi Xóa"**.
2. **Kết quả:** Hệ thống báo xóa thành công. Mã 99 biến mất khỏi danh sách.
3. **🗣️ Lời thuyết trình:** 
   > *"Khi một nhân viên nghỉ việc, Admin chỉ cần gọi 1 hàm duy nhất. Cơ chế Transaction sẽ đảm bảo nhân viên này bị xóa sạch sẽ ở cả 2 máy chủ vật lý cùng một thời điểm, không để lại dữ liệu mồ côi (tên bị xóa nhưng vẫn còn quỹ lương ở DB2)."*

---

## 🌩️ KỊCH BẢN 6: XỬ LÝ SỰ CỐ & TÍNH TOÀN VẸN (ROLLBACK)
**Mục tiêu:** Chứng minh nếu có sự cố đứt mạng giữa 2 Node, Transaction sẽ tự động Rollback[cite: 10].

1. **Thao tác 1:** Mở phần mềm Docker Desktop. Tìm container `mysql-luong` (DB2) và bấm nút **Stop** (Giả lập máy chủ chứa lương bị sập/đứt cáp).
2. **Thao tác 2:** Quay lại giao diện Web, thử thêm nhân viên mới (Mã 100 - Trần Lỗi Mạng). Bấm **"Lưu Dữ Liệu"**. Hệ thống hiện thông báo lỗi Transaction (Toast màu đỏ).
3. **Thao tác kiểm chứng:** Click lại vào menu **"👨‍💼 Nhân viên (DB1)"** để xem danh sách.
4. **Kết quả:** **Hoàn toàn không có** nhân viên mã 100 nào được lưu vào DB1.
5. **🗣️ Lời thuyết trình:** 
   > *"Thưa thầy/cô, em vừa tắt đột ngột máy chủ chứa DB Lương. Khi cố tình thêm nhân sự mới, do kết nối sang DB2 thất bại, lệnh `ROLLBACK` trong Stored Procedure lập tức kích hoạt để hủy bỏ luôn lệnh thêm tên vào DB1. Điều này đảm bảo Tính Toàn Vẹn dữ liệu 100%, không bao giờ xảy ra lỗi 'có tên ở DB1 mà lại bị mất lương ở DB2'[cite: 10]."*

---

## 🛡️ KỊCH BẢN 7: TÍNH TỰ TRỊ ĐỊA PHƯƠNG (LOCAL AUTONOMY)
**Mục tiêu:** Chứng minh một Node sập không được làm chết toàn bộ hệ thống.

1. **Thao tác:** (Bật lại `mysql-luong` trước). Tiếp tục mở Docker Desktop, bấm nút **Stop** tắt container `mysql-hanhchinh` (DB1).
2. **Thao tác 2:** Lên Web, bấm nút **"👨‍💼 Nhân viên"** -> Báo Lỗi. Bấm nút **"👑 Quản trị viên"** -> Báo lỗi.
3. **Thao tác 3:** Bấm nút **"💰 Kế toán (DB2)"**.
4. **Kết quả:** Dữ liệu bảng lương vẫn hiện ra xanh mượt!
5. **🗣️ Lời thuyết trình:** 
   > *"Thưa thầy/cô, Server Trụ sở chính vừa bị sập hoàn toàn. Thông thường các hệ thống tập trung sẽ chết đứng. Nhưng nhờ Phân mảnh vật lý, Server Lương (DB2) vẫn có Tính Tự Trị. Phòng Kế toán vẫn truy cập DB2 bình thường để tính lương, không gây gián đoạn kinh doanh."*