CREATE DATABASE db_luong;
USE db_luong;

-- 1. Bảng lưu trữ lương
CREATE TABLE LuongThuong (
    MaNV INT PRIMARY KEY,
    LuongCoBan DECIMAL(15, 2) NOT NULL,
    HeSo DECIMAL(4, 2) NOT NULL
);

-- 2. Tạo User cho Kế toán (Chỉ truy cập DB này)
CREATE USER 'ketoan'@'%' IDENTIFIED BY 'ketoan123';
GRANT SELECT, INSERT, UPDATE, DELETE ON db_luong.LuongThuong TO 'ketoan'@'%';

-- 3. Tạo User hệ thống để DB1 có thể remote sang
CREATE USER 'link_user'@'%' IDENTIFIED BY 'link123';
GRANT SELECT, INSERT, UPDATE, DELETE ON db_luong.LuongThuong TO 'link_user'@'%';

-- Thêm dữ liệu mẫu
INSERT INTO LuongThuong VALUES (1, 15000000, 1.2), (2, 20000000, 1.5);