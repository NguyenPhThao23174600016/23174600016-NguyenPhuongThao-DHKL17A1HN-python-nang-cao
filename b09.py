# Lớp Đa giác 
class DaGiac:
    def __init__(self, so_canh):
        self.so_canh = so_canh  
    def hien_thi_so_canh(self):
        print(f"Số cạnh của đa giác: {self.so_canh}")

# Lớp Hình bình hành kế thừa từ Đa giác
class HinhBinhHanh(DaGiac):
    def __init__(self, day, chieu_cao, do_dai_canh):
        super().__init__(4)  
        self.day = day       
        self.chieu_cao = chieu_cao      
        self.do_dai_canh = do_dai_canh  
    def chu_vi_hbh(self):
        return 2 * (self.day + self.do_dai_canh)  
    def dien_tich_hbh(self):
        return self.day * self.chieu_cao  

# Lớp Hình chữ nhật kế thừa từ Hình bình hành
class HinhChuNhat(HinhBinhHanh):
    def __init__(self, chieu_dai, chieu_rong):
        super().__init__(chieu_dai, chieu_rong, chieu_rong)  
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong
    def chu_vi_hcn(self):
        return 2 * (self.chieu_dai + self.chieu_rong)  
    def dien_tich_hcn(self):
        return self.chieu_dai * self.chieu_rong  

# Lớp Hình vuông kế thừa từ Hình chữ nhật
class HinhVuong(HinhChuNhat):
    def __init__(self, canh):
        super().__init__(canh, canh)  
        self.canh = canh
    def chu_vi_hv(self):
        return 4 * self.canh 
    def dien_tich_hv(self):
        return self.canh ** 2 
    
# Hình bình hành
hinh_binh_hanh = HinhBinhHanh(10, 5, 6)
print("Hình bình hành:")
hinh_binh_hanh.hien_thi_so_canh()
print(f"Chu vi: {hinh_binh_hanh.chu_vi_hbh()}")
print(f"Diện tích: {hinh_binh_hanh.dien_tich_hbh()}\n")

# Hình chữ nhật
hinh_chu_nhat = HinhChuNhat(8, 5)
print("Hình chữ nhật:")
hinh_chu_nhat.hien_thi_so_canh()
print(f"Chu vi: {hinh_chu_nhat.chu_vi_hcn()}")
print(f"Diện tích: {hinh_chu_nhat.dien_tich_hcn()}\n")

# Hình vuông
hinh_vuong = HinhVuong(4)
print("Hình vuông:")
hinh_vuong.hien_thi_so_canh()
print(f"Chu vi: {hinh_vuong.chu_vi_hv()}")
print(f"Diện tích: {hinh_vuong.dien_tich_hv()}")
