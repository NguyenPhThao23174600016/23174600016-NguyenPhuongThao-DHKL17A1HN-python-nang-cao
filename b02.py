class qlydiem:
    def __init__(self,ho_ten,diem_toan,diem_ly,diem_hoa):
        self.ho_ten = ho_ten
        self.diem_toan = diem_toan
        self.diem_ly = diem_ly
        self.diem_hoa = diem_hoa
    def tinh_tong_diem(self):
        return self.diem_toan + self.diem_hoa + self.diem_ly
    def in_thong_tin(self):
        return f"Họ tên: {self.ho_ten}, Toán: {self.diem_toan}, Lý: {self.diem_ly}, Hóa: {self.diem_hoa}, Tổng điểm: {self.tinh_tong_diem()}"

# Hàm in danh sách thí sinh trúng tuyển theo thứ tự điểm từ cao đến thấp
def in_ds_trung_tuyen(danh_sach, diem_chuan=20):
    ds_trung_tuyen = [thi_sinh for thi_sinh in danh_sach if thi_sinh.tinh_tong_diem() >= diem_chuan]
    ds_trung_tuyen.sort(key=lambda ts: ts.tinh_tong_diem(), reverse=True)
    
    if ds_trung_tuyen:
        print("Danh sách thí sinh trúng tuyển:")
        for ts in ds_trung_tuyen:
            print(ts.in_thong_tin())
    else:
        print("Không có thí sinh nào trúng tuyển.")

# Test thử chương trình với dữ liệu đầu vào
danh_sach_thi_sinh = [
    qlydiem("Nguyen Van An", 7.8, 7, 6),
    qlydiem("Le Thi Bich", 9, 8.8, 7),
    qlydiem("Tran Van Chung", 5.8, 4.4, 6),
    qlydiem("Pham Thi Dieu Chi", 7, 6, 8),
    qlydiem("Ha Thi Lan", 8.4, 5.8, 9.5)
]

in_ds_trung_tuyen(danh_sach_thi_sinh)