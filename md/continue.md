A. Viết Báo cáo kỹ thuật (File Word/PDF)
Báo cáo không cần quá dài, nhưng phải giải thích được Kiến trúc hệ thống. Bạn cần đưa các ý sau vào báo cáo:

Lý do chọn giải pháp: Trình bày việc chọn MySQL làm CSDL phân mảnh và sử dụng FEDERATED Engine để cấu hình phân tán.

Sơ đồ kiến trúc (Mô hình vật lý): Vẽ sơ đồ gồm 2 Node (DB1: Hành chính chứa bảng ThongTinChung, DB2: Lương chứa bảng LuongThuong).

Cách giải quyết Tính trong suốt: Trình bày mã SQL tạo VIEW vw_HoSoToanDien kết hợp với bảng Federated để JOIN dữ liệu xuyên Server.  

Cách giải quyết Đồng bộ & Toàn vẹn: Trình bày mã SQL của Stored Procedure sp_ThemNhanVien với cơ chế START TRANSACTION và ROLLBACK để đảm bảo Insert luôn vào đúng 2 nơi.  

Cơ chế Phân quyền bảo mật: Chụp ảnh mã lệnh GRANT SELECT giới hạn quyền của user nhanvien và ketoan trên từng Database vật lý.  

B. Kịch bản Demo thực tế (Khi ra Hội đồng)
Bạn mở giao diện web vừa làm lên, và thuyết trình theo đúng 4 bước sau (Vừa nói vừa click):

Bước 1 - Demo Phân quyền DB1 (Click nút Nhân viên): "Dạ thưa thầy/cô, khi user Nhân viên đăng nhập, hệ thống kết nối thẳng vào DB1. CSDL chỉ trả về Tên và Phòng ban. Dữ liệu lương hoàn toàn vô hình."

  

Bước 2 - Demo Phân quyền DB2 (Click nút Kế toán): "Tương tự, user Kế toán kết nối vào DB2, chỉ thấy Mã NV và Lương. Không hề biết tên ai. Điều này đảm bảo tách biệt dữ liệu nhạy cảm."

  

Bước 3 - Demo Tính trong suốt (Click nút Admin): "Dưới góc độ Admin, dù dữ liệu bị cắt dọc làm 2 DB khác nhau, nhưng nhờ em dùng View và Federated Engine, Admin vẫn nhìn thấy 1 bảng hợp nhất hoàn chỉnh mà không cần biết dữ liệu thực sự nằm ở đâu."

  

Bước 4 - Demo Tính toàn vẹn (Thêm nhân viên): Bạn nhập liệu vào Form rồi bấm Lưu. Sau đó mở Terminal của Docker lên (hoặc dùng DBeaver/Navicat) query trực tiếp vào 2 DB để thầy cô thấy dữ liệu đã thực sự được "chẻ đôi" và nằm ở 2 server vật lý khác nhau.