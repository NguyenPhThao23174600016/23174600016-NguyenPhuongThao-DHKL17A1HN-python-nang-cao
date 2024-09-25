class NganXep:
    def __init__(self, suc_chua):
        self.suc_chua = suc_chua  
        self.stack = []           # Mảng để lưu các phần tử (sẽ tự mở rộng khi cần)
        self.dinh = -1            # Đỉnh của ngăn xếp (chỉ số phần tử trên cùng)

    def kiemTraRong(self):
        return self.dinh == -1

    def kiemTraDay(self):
        return self.dinh == self.suc_chua - 1

    def themPhanTu(self, gia_tri):
        if self.kiemTraDay():
            print("Ngăn xếp đã đầy, không thể thêm phần tử!")
        else:
            self.dinh += 1
            self.stack.append(float(gia_tri))  
            print(f"Đã thêm {gia_tri} vào ngăn xếp.")

    def layPhanTu(self):
        if self.kiemTraRong():
            print("Ngăn xếp trống, không thể lấy phần tử!")
            return None
        else:
            gia_tri = self.stack.pop()  # Lấy phần tử trên cùng ra khỏi ngăn xếp
            self.dinh -= 1
            print(f"Đã lấy {gia_tri} ra khỏi ngăn xếp.")
            return gia_tri

    def __del__(self):
        # Hàm hủy ngăn xếp, giải phóng tài nguyên nếu cần
        print("Giải phóng tài nguyên ngăn xếp.")

# Ví dụ sử dụng
ngan_xep = NganXep(5)  # Tạo ngăn xếp với sức chứa 5 phần tử
ngan_xep.themPhanTu(1.2)
ngan_xep.themPhanTu(3.4)
ngan_xep.layPhanTu()
ngan_xep.themPhanTu(5.6)
ngan_xep.themPhanTu(7.8)
ngan_xep.themPhanTu(9.0)
ngan_xep.themPhanTu(10.2)  # Ngăn xếp đầy sẽ báo lỗi
