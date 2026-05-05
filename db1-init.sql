-- Ép hệ thống dùng chuẩn tiếng Việt ngay từ đầu
SET NAMES utf8mb4;

CREATE DATABASE IF NOT EXISTS db_hanhchinh CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE db_hanhchinh;

-- 1. Bảng Thông tin công khai
CREATE TABLE ThongTinChung (
    MaNV INT PRIMARY KEY,
    HoTen VARCHAR(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
    PhongBan VARCHAR(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL
);

-- 2. Bảng Ảo (Federated)
CREATE TABLE Remote_LuongThuong (
    MaNV INT PRIMARY KEY,
    LuongCoBan DECIMAL(15, 2),
    HeSo DECIMAL(4, 2)
) ENGINE=FEDERATED CONNECTION='mysql://link_user:link123@mysql-luong:3306/db_luong/LuongThuong';

-- 3. View gộp
CREATE VIEW vw_HoSoToanDien AS
SELECT a.MaNV, a.HoTen, a.PhongBan, b.LuongCoBan, b.HeSo
FROM ThongTinChung a
LEFT JOIN Remote_LuongThuong b ON a.MaNV = b.MaNV;

-- 4. Stored Procedure
DELIMITER //
CREATE PROCEDURE sp_ThemNhanVien(
    IN p_MaNV INT, IN p_HoTen VARCHAR(100), IN p_PhongBan VARCHAR(50), 
    IN p_LuongCoBan DECIMAL(15,2), IN p_HeSo DECIMAL(4,2)
)
BEGIN
    DECLARE exit handler for sqlexception
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;

    START TRANSACTION;
        INSERT INTO ThongTinChung (MaNV, HoTen, PhongBan) VALUES (p_MaNV, p_HoTen, p_PhongBan);
        INSERT INTO Remote_LuongThuong (MaNV, LuongCoBan, HeSo) VALUES (p_MaNV, p_LuongCoBan, p_HeSo);
    COMMIT;
END //
DELIMITER ;

-- 5. User Phân quyền
CREATE USER 'nhanvien'@'%' IDENTIFIED BY 'nhanvien123';
GRANT SELECT ON db_hanhchinh.ThongTinChung TO 'nhanvien'@'%';

-- Thêm dữ liệu mẫu chuẩn Tiếng Việt
INSERT INTO ThongTinChung VALUES 
(1, 'Nguyễn Văn A', 'IT'), 
(2, 'Trần Thị B', 'Nhân sự');


-- Thêm Stored Procedure Xóa Nhân Viên (Đồng bộ 2 bên)
DELIMITER //
CREATE PROCEDURE sp_XoaNhanVien(IN p_MaNV INT)
BEGIN
    DECLARE exit handler for sqlexception
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;

    START TRANSACTION;
        -- Xóa thông tin hành chính ở DB1
        DELETE FROM ThongTinChung WHERE MaNV = p_MaNV;
        -- Xóa thông tin lương ở DB2 (thông qua bảng Federated)
        DELETE FROM Remote_LuongThuong WHERE MaNV = p_MaNV;
    COMMIT;
END //
DELIMITER ;