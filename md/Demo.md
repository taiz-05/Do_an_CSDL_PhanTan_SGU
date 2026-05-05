# 🎯 KỊCH BẢN DEMO ĐỒ ÁN CSDL PHÂN TÁN (ĐỀ TÀI 1)

Tài liệu này hướng dẫn chi tiết 10 bước thực hiện demo trước Hội đồng bảo vệ để chứng minh toàn bộ các yêu cầu: Phân mảnh dọc, Phân quyền bảo mật, Tính trong suốt, Chu trình CRUD đồng bộ, Tính toàn vẹn dữ liệu, Thống kê phân tán và Tính tự trị địa phương.

---

## 🛠 CHUẨN BỊ TRƯỚC KHI DEMO
1. **Docker:** Đảm bảo Docker Desktop đang mở. 2 container (`mysql-hanhchinh` và `mysql-luong`) đang ở trạng thái **Running**.
2. **Backend:** Mở Terminal trong VS Code, chạy lệnh `python app.py` và đảm bảo Terminal báo đang chạy ở cổng `5000`.
3. **Frontend:** Mở file `index.html` bằng Live Server trên trình duyệt (Chrome/Edge).
4. **Công cụ Database (Tùy chọn):** Mở sẵn DBeaver hoặc Navicat kết nối vào port `3306` (DB1) và `3307` (DB2).

----

## 🟢 KỊCH BẢN 1: BẢO MẬT PHÂN MẢNH - TÀI KHOẢN NHÂN VIÊN
**Mục tiêu:** Chứng minh Nhân viên chỉ truy cập được dữ liệu thông tin chung, hoàn toàn không thấy thông tin lương[cite: 16].

1. **Thao tác:** Click vào menu **"👨‍💼 Nhân viên (DB1)"** bên thanh điều hướng trái[cite: 16].
2. **Kết quả:** Bảng dữ liệu hiện ra chỉ có các cột: `MaNV`, `HoTen`, `PhongBan`[cite: 16].
3. **🗣️ Lời thuyết trình:** 
   > *"Thưa thầy/cô, hệ thống của nhóm em sử dụng kỹ thuật Phân mảnh dọc, tách làm 2 CSDL vật lý độc lập[cite: 16]. Khi tài khoản Nhân viên đăng nhập, API chỉ kết nối thẳng vào Node 1 (Hành chính)[cite: 16]. Em đã dùng lệnh `GRANT` trong MySQL để giới hạn quyền `SELECT` của user này[cite: 16]. Do đó, dữ liệu lương thưởng hoàn toàn bị ẩn đi, đảm bảo tính bảo mật tuyệt đối[cite: 16]."*

---

## 🟠 KỊCH BẢN 2: BẢO MẬT PHÂN MẢNH - TÀI KHOẢN KẾ TOÁN
**Mục tiêu:** Chứng minh Kế toán chỉ truy cập được dữ liệu tài chính, không thấy thông tin hành chính cá nhân[cite: 16].

1. **Thao tác:** Click vào menu **"💰 Kế toán (DB2)"** bên thanh điều hướng trái[cite: 16].
2. **Kết quả:** Bảng dữ liệu thay đổi, chỉ còn hiện các cột: `MaNV`, `LuongCoBan`, `HeSo`[cite: 16].
3. **🗣️ Lời thuyết trình:** 
   > *"Tương tự, đối với bộ phận Kế toán, API sẽ dùng tài khoản riêng để kết nối thẳng vào Node 2 (port 3307 chứa DB Lương)[cite: 16]. Hệ thống này được quản lý vật lý hoàn toàn độc lập, kế toán chỉ làm việc với các con số tài chính và Mã nhân viên, đáp ứng đúng yêu cầu chia tách dữ liệu nhạy cảm của đề bài[cite: 16]."*

---

## 🔴 KỊCH BẢN 3: TÍNH TRONG SUỐT - TÀI KHOẢN ADMIN
**Mục tiêu:** Chứng minh khả năng truy vấn gộp xuyên server mà ở tầng ứng dụng không cần biết dữ liệu đang bị phân mảnh ở đâu[cite: 16].

1. **Thao tác:** Click vào menu **"👑 Quản trị viên"** bên thanh điều hướng trái[cite: 16].
2. **Kết quả:** Bảng dữ liệu hiện ra **đầy đủ tất cả các cột** (Họ Tên, Phòng Ban, Lương, Hệ Số)[cite: 16].
3. **🗣️ Lời thuyết trình:** 
   > *"Điểm mấu chốt của CSDL Phân tán là Tính trong suốt (Transparency)[cite: 16]. Dưới góc nhìn của Admin, họ vẫn quản lý nhân sự như trên một bảng duy nhất[cite: 16]. Để làm được điều này, nhóm em đã cấu hình **FEDERATED Engine** móc nối DB2 vào DB1, sau đó tạo một `VIEW` tự động `JOIN` dữ liệu 2 bên lại với nhau[cite: 16]. Tầng Ứng dụng chỉ việc `SELECT` trên View này mà không cần quan tâm dữ liệu thực tế đang nằm ở server nào[cite: 16]."*

---

## 🔥 KỊCH BẢN 4: ĐỒNG BỘ THAO TÁC (THÊM NHÂN SỰ)
**Mục tiêu:** Chứng minh khi Insert dữ liệu, hệ thống tự động tách dữ liệu thành 2 phần và lưu vào đúng 2 Database vật lý[cite: 16].

1. **Thao tác:** Ở form Thêm nhân sự, nhập thông tin: Mã NV (99), Họ Tên (Nguyễn Văn Test), Phòng Ban (IT), Lương Cơ Bản (20000000), Hệ Số (1.5). Bấm **"Lưu Dữ Liệu"**[cite: 16].
2. **Kết quả:** Hệ thống hiện thông báo Toast màu xanh (Thành công), bảng dữ liệu load lại hiển thị nhân viên mới[cite: 16].
3. **🗣️ Lời thuyết trình:** 
   > *"Khi Admin thêm nhân sự mới, API sẽ gọi vào một `Stored Procedure` trên DB1[cite: 16]. SP này sử dụng Transaction để tự động cắt dữ liệu làm đôi: Tên và Phòng ban được `INSERT` vào DB1, Lương và Hệ số được `INSERT` xuyên qua mạng (via Federated Table) để lưu vào DB2[cite: 16]. Mọi thứ diễn ra hoàn toàn tự động và đồng thời[cite: 16]."*

---

## 📝 KỊCH BẢN 5: ĐỒNG BỘ THAO TÁC (CẬP NHẬT NHÂN SỰ)
**Mục tiêu:** Chứng minh khả năng cập nhật (Update) dữ liệu phân tán ở cả 2 máy chủ cùng một lúc.

1. **Thao tác:** Ở form Cập nhật thông tin, nhập: Mã NV (99), Họ tên mới (Nguyễn Văn VIP), Phòng ban mới (Giám đốc), Lương mới (50000000), Hệ số mới (3.0). Bấm **"Cập Nhật Dữ Liệu"**.
2. **Kết quả:** Dữ liệu nhân viên mã 99 trên bảng lập tức thay đổi toàn bộ.
3. **🗣️ Lời thuyết trình:** 
   > *"Bên cạnh tính năng Thêm, hệ thống cũng xử lý triệt để bài toán Cập nhật. Khi em đổi phòng ban và tăng lương cho nhân sự, một giao dịch (Transaction) sẽ khóa cả 2 bản ghi ở 2 Server, thực hiện lệnh UPDATE song song và chỉ COMMIT khi cả 2 đều thành công, hoàn thiện chu trình dữ liệu phân tán."*

---

## 📊 KỊCH BẢN 6: THỐNG KÊ QUỸ LƯƠNG (PHÂN TÁN)
**Mục tiêu:** Chứng minh hệ thống có thể thực hiện các truy vấn phức tạp (Group By, Sum) trên dữ liệu bị cắt dọc ở nhiều Server.

1. **Thao tác:** Tại khu vực Thống kê Quỹ Lương Phân Tán, bấm nút **"Làm mới báo cáo"**.
2. **Kết quả:** Hệ thống tính toán và in ra bảng tổng quỹ lương chia theo từng Phòng Ban.
3. **🗣️ Lời thuyết trình:** 
   > *"Thưa Hội đồng, để chứng minh sức mạnh của Federated Engine, em đã tạo chức năng Báo cáo Quỹ Lương. Chức năng này đòi hỏi hệ thống phải gom nhóm (`GROUP BY`) theo Phòng ban nằm ở DB1, đồng thời tính tổng (`SUM`) tiền lương nằm ở DB2. Thông qua View phân tán, MySQL đã tự động giải quyết bài toán JOIN mạng này một cách tối ưu nhất để ra được kết quả tức thì!"*

---

## 🗑️ KỊCH BẢN 7: ĐỒNG BỘ THAO TÁC (XÓA NHÂN SỰ)
**Mục tiêu:** Chứng minh khi xóa 1 nhân sự, dữ liệu ở cả 2 Node vật lý đều bị xóa sạch sẽ cùng lúc[cite: 16].

1. **Thao tác:** Ở ô Xóa nhân sự, nhập số `99` (Mã NV vừa tạo). Bấm **"Thực thi Xóa"**[cite: 16].
2. **Kết quả:** Hệ thống báo xóa thành công. Mã 99 biến mất khỏi danh sách[cite: 16].
3. **🗣️ Lời thuyết trình:** 
   > *"Khi một nhân viên nghỉ việc, Admin chỉ cần gọi 1 hàm duy nhất[cite: 16]. Cơ chế Transaction sẽ đảm bảo nhân viên này bị xóa sạch sẽ ở cả 2 máy chủ vật lý cùng một thời điểm, không để lại dữ liệu mồ côi (tên bị xóa nhưng vẫn còn quỹ lương ở DB2)[cite: 16]."*

---

## 🌩️ KỊCH BẢN 8: XỬ LÝ SỰ CỐ & TÍNH TOÀN VẸN (ROLLBACK)
**Mục tiêu:** Chứng minh nếu có sự cố đứt mạng giữa 2 Node, Transaction sẽ tự động Rollback để bảo vệ tính toàn vẹn[cite: 16].

1. **Thao tác 1:** Mở phần mềm Docker Desktop. Tìm container `mysql-luong` (DB2) và bấm nút **Stop** (Giả lập máy chủ chứa lương bị sập/đứt cáp)[cite: 16].
2. **Thao tác 2:** Quay lại giao diện Web, thử thêm nhân viên mới (Mã 100 - Trần Lỗi Mạng). Bấm **"Lưu Dữ Liệu"**[cite: 16]. Hệ thống hiện thông báo lỗi Sập Server (Toast màu đỏ).
3. **Thao tác kiểm chứng:** Click lại vào menu **"👨‍💼 Nhân viên (DB1)"** để xem danh sách[cite: 16].
4. **Kết quả:** **Hoàn toàn không có** nhân viên mã 100 nào được lưu vào DB1[cite: 16].
5. **🗣️ Lời thuyết trình:** 
   > *"Thưa thầy/cô, em vừa tắt đột ngột máy chủ chứa DB Lương[cite: 16]. Khi cố tình thêm nhân sự mới, do kết nối sang DB2 thất bại, lệnh `ROLLBACK` trong Stored Procedure lập tức kích hoạt để hủy bỏ luôn lệnh thêm tên vào DB1[cite: 16]. Điều này đảm bảo Tính Toàn Vẹn dữ liệu 100%, không bao giờ xảy ra lỗi 'có tên ở DB1 mà lại bị mất lương ở DB2'[cite: 16]."*

---

## 🛡️ KỊCH BẢN 9: TÍNH TỰ TRỊ ĐỊA PHƯƠNG (LOCAL AUTONOMY)
**Mục tiêu:** Khẳng định đặc tính ưu việt: "Một máy chủ sập không được làm chết toàn bộ doanh nghiệp"[cite: 16].

1. **Thao tác chuẩn bị:** Bật lại container `mysql-luong` trên Docker. Sau đó bấm nút **Stop** để tắt container `mysql-hanhchinh` (DB1)[cite: 16].
2. **Thao tác 2:** Lên giao diện Web, bấm nút **"👨‍💼 Nhân viên"** -> Báo Lỗi[cite: 16]. Bấm nút **"👑 Quản trị viên"** -> Báo lỗi[cite: 16].
3. **Thao tác 3:** Bấm nút **"💰 Kế toán (DB2)"**[cite: 16].
4. **Kết quả:** Dữ liệu bảng lương vẫn hiện ra xanh mượt[cite: 16]!
5. **🗣️ Lời thuyết trình:** 
   > *"Thưa thầy/cô, Server Trụ sở chính vừa bị sập hoàn toàn[cite: 16]. Thông thường các hệ thống tập trung sẽ chết đứng[cite: 16]. Nhưng nhờ kiến trúc Phân mảnh vật lý, Server Lương (DB2) vẫn có Tính Tự Trị[cite: 16]. Phòng Kế toán vẫn truy cập DB2 bình thường để tính lương, không gây gián đoạn hoạt động chi trả lương của công ty[cite: 16]."*

---

## 🔐 KỊCH BẢN 10: BẢO MẬT CẤP ĐÁY (BYPASS QUA TERMINAL)
**Mục tiêu:** Chứng minh hệ thống bảo mật ở tận lõi Database Engine, chứ không chỉ rào bằng giao diện Web.

**Bước 1: Mở Terminal và "Đột nhập" vào Server**
*(Nhớ bật lại DB1 trên Docker trước khi thao tác)*
1. Mở Terminal ngay trong VS Code (hoặc Command Prompt).
2. Gõ câu lệnh sau để chui thẳng vào container Hành chính (DB1) bằng quyền của user `nhanvien`:
   ```bash
   docker exec -it do-an-phan-manh-doc-mysql-hanhchinh-1 mysql -u nhanvien -p

3. Terminal sẽ yêu cầu nhập password: Enter password:. 
Bạn gõ nhanvien123 rồi nhấn Enter (Lúc gõ, màn hình sẽ không hiện ký tự nào, cứ gõ đúng và nhấn Enter).


**Bước 2: Chọn Database và bắt đầu dẫn dắt** 

Khi màn hình hiện chữ mysql>, bạn gõ lệnh sau để chọn CSDL:

SQL
USE db_hanhchinh;

   *(Hệ thống sẽ báo: `Database changed`)*
2. **🗣️ Bắt đầu thuyết trình:** 
   > *"Dạ thưa thầy/cô, nhiều hệ thống hiện nay chỉ dùng code ở Web để ẩn các cột nhạy cảm đi. Nếu một người nội bộ có ý đồ xấu, họ hoàn toàn có thể bỏ qua Web, dùng Terminal kết nối thẳng vào lõi Database như em đang làm trên màn hình đây..."*

**Bước 3: Thực hiện truy vấn "vượt rào" (Bypass)**
1. Tiếp tục, bạn gõ câu lệnh cấm kỵ này vào và nhấn Enter:
   ```sql
   USE db_hanhchinh;
   SELECT * FROM vw_HoSoToanDien;
   
**Bước 4: Chốt hạ bằng thông báo lỗi đỏ chót**

1. Kết quả: Ngay lập tức, Terminal sẽ văng ra một dòng lỗi từ chối phũ phàng:
ERROR 1142 (42000): SELECT command denied to user 'nhanvien'@'localhost' for table 'vw_HoSoToanDien'

🗣️ Lời thuyết trình chốt hạ:

"Như thầy cô thấy, MySQL đã lập tức văng lỗi ERROR 1142: Access Denied. Dù Hacker có chui qua mặt giao diện Web, sử dụng giao thức kết nối sâu nhất, họ vẫn bị từ chối truy cập tuyệt đối vì nhóm em đã rào bảo mật bằng lệnh GRANT ngay dưới tầng Database Engine vật lý!"

(Mẹo: Để thoát khỏi màn hình MySQL sau khi demo xong, bạn chỉ cần gõ exit và nhấn Enter).
Bạn chỉ cần in phần này ra hoặc để trên điện thoại lúc cầm mic thuyết trình là quá trơn tru!