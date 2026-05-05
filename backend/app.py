from flask import Flask, jsonify, request
from flask_cors import CORS
import pymysql

app = Flask(__name__)
CORS(app)

# Hàm hỗ trợ kết nối linh hoạt tới các DB với User khác nhau
def get_db_connection(user, password, port, db_name):
    return pymysql.connect(
        host='localhost', # Vì chạy python ở máy host, gọi vào port đã map của docker
        user=user,
        password=password,
        port=port,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=True
    )

# ==========================================
# TEST CASE 1: NHÂN VIÊN CHỈ XEM ĐƯỢC THÔNG TIN CHUNG (Phân quyền DB1)
# ==========================================
@app.route('/api/nhanvien/hoso', methods=['GET'])
def get_hoso_nhanvien():
    try:
        # Đăng nhập vào DB1 (port 3306) bằng tài khoản 'nhanvien'
        conn = get_db_connection('nhanvien', 'nhanvien123', 3306, 'db_hanhchinh')
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM ThongTinChung")
            data = cursor.fetchall()
        conn.close()
        return jsonify({"status": "success", "role": "Nhân viên", "data": data})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 403

# ==========================================
# TEST CASE 2: KẾ TOÁN CHỈ XEM ĐƯỢC LƯƠNG (Phân quyền DB2)
# ==========================================
@app.route('/api/ketoan/luong', methods=['GET'])
def get_luong_ketoan():
    try:
        # Đăng nhập vào DB2 (port 3307) bằng tài khoản 'ketoan'
        conn = get_db_connection('ketoan', 'ketoan123', 3307, 'db_luong')
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM LuongThuong")
            data = cursor.fetchall()
        conn.close()
        return jsonify({"status": "success", "role": "Kế toán", "data": data})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 403

# ==========================================
# TEST CASE 3: TÍNH TRONG SUỐT (Admin xem View gộp 2 nơi)
# ==========================================
@app.route('/api/admin/hoso-toandien', methods=['GET'])
def get_hoso_toandien():
    try:
        # Admin vào DB1, truy vấn View tự động JOIN với Federated Table sang DB2
        conn = get_db_connection('root', 'root', 3306, 'db_hanhchinh')
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM vw_HoSoToanDien")
            data = cursor.fetchall()
        conn.close()
        return jsonify({"status": "success", "role": "Admin", "data": data})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# ==========================================
# TEST CASE 4: ĐỒNG BỘ THÊM DỮ LIỆU VÀO 2 NƠI
# ==========================================
@app.route('/api/admin/them-nhan-vien', methods=['POST'])
def them_nhan_vien():
    try:
        req = request.json
        conn = get_db_connection('root', 'root', 3306, 'db_hanhchinh')
        with conn.cursor() as cursor:
            # Gọi Stored Procedure để nó tự động chèn vào DB1 và DB2
            sql = "CALL sp_ThemNhanVien(%s, %s, %s, %s, %s)"
            cursor.execute(sql, (
                req['MaNV'], req['HoTen'], req['PhongBan'], 
                req['LuongCoBan'], req['HeSo']
            ))
        conn.close()
        return jsonify({"status": "success", "message": "Đã thêm nhân viên vào cả 2 CSDL thành công!"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


  # ==========================================
# TEST CASE 5: XÓA NHÂN SỰ ĐỒNG BỘ
# ==========================================
@app.route('/api/admin/xoa-nhan-vien/<int:ma_nv>', methods=['DELETE', 'OPTIONS'])
def xoa_nhan_vien(ma_nv):
    try:
        conn = get_db_connection('root', 'root', 3306, 'db_hanhchinh')
        with conn.cursor() as cursor:
            cursor.execute("CALL sp_XoaNhanVien(%s)", (ma_nv,))
        conn.close()
        return jsonify({"status": "success", "message": f"Đã xóa hoàn toàn nhân viên mã {ma_nv} khỏi hệ thống!"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
    
    
# ==========================================
# TEST CASE 8: THỐNG KÊ QUỸ LƯƠNG (PHÂN TÁN)
# ==========================================
@app.route('/api/admin/thong-ke', methods=['GET'])
def thong_ke_quy_luong():
    try:
        conn = get_db_connection('root', 'root', 3306, 'db_hanhchinh')
        with conn.cursor(pymysql.cursors.DictCursor) as cursor:
            # Query gộp và tính toán (Group By) trên View phân tán
            sql = """
                SELECT PhongBan, COUNT(MaNV) as SoNhanVien, SUM(LuongCoBan * HeSo) as TongQuyLuong
                FROM vw_HoSoToanDien
                GROUP BY PhongBan
            """
            cursor.execute(sql)
            data = cursor.fetchall()
        conn.close()
        return jsonify({"status": "success", "data": data})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# ==========================================
# TEST CASE 9: SỬA NHÂN VIÊN ĐỒNG BỘ
# ==========================================
@app.route('/api/admin/sua-nhan-vien', methods=['PUT', 'OPTIONS'])
def sua_nhan_vien():
    if request.method == 'OPTIONS':
        return '', 200
    try:
        data = request.json
        conn = get_db_connection('root', 'root', 3306, 'db_hanhchinh')
        with conn.cursor() as cursor:
            cursor.execute("CALL sp_SuaNhanVien(%s, %s, %s, %s, %s)", 
                           (data['maNV'], data['hoTen'], data['phongBan'], data['luongCB'], data['heSo']))
        conn.close()
        return jsonify({"status": "success", "message": f"Đã cập nhật thành công nhân viên mã {data['maNV']}"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
# ------------------------------------------
# TUYỆT ĐỐI ĐỂ DÒNG NÀY Ở DƯỚI CÙNG CỦA FILE:
if __name__ == '__main__':
    print("🚀 Máy chủ Backend Đồ án 1 đang chạy tại http://localhost:5000")
    app.run(host='0.0.0.0', port=5000, debug=True)
