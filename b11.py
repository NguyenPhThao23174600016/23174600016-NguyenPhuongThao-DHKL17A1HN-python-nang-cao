import math
# Lớp Tam giác 
class TamGiac:
    def __init__(self, canh_a, canh_b, canh_c):
        self.canh_a = canh_a
        self.canh_b = canh_b
        self.canh_c = canh_c
    def chu_vi_tg(self):
        return self.canh_a + self.canh_b + self.canh_c
    def dien_tich_tg(self):
        p = self.chu_vi_tg() / 2  
        return math.sqrt(p * (p - self.canh_a) * (p - self.canh_b) * (p - self.canh_c))  

    def hien_thi(self):
        print(f"Các cạnh của tam giác: {self.canh_a}, {self.canh_b}, {self.canh_c}")
        print(f"Chu vi: {self.chu_vi_tg()}")
        print(f"Diện tích: {self.dien_tich_tg()}")

# Lớp Tam giác Vuông kế thừa từ lớp Tam giác
class TamGiacVuong(TamGiac):
    def __init__(self, canh_a, canh_b):
        canh_c = math.sqrt(canh_a ** 2 + canh_b ** 2)  
        super().__init__(canh_a, canh_b, canh_c)
    def hien_thi(self):
        print(f"Tam giác vuông với cạnh góc vuông {self.canh_a} và {self.canh_b}, cạnh huyền {self.canh_c}")
        print(f"Chu vi: {self.chu_vi_tg()}")
        print(f"Diện tích: {self.dien_tich_tg()}")

# Lớp Tam giác Cân  kế thừa từ lớp Tam giác
class TamGiacCan(TamGiac):
    def __init__(self, canh_bang, canh_day):
        super().__init__(canh_bang, canh_bang, canh_day)
    def hien_thi(self):
        print(f"Tam giác cân với hai cạnh bằng nhau: {self.canh_a} và cạnh đáy: {self.canh_c}")
        print(f"Chu vi: {self.chu_vi_tg()}")
        print(f"Diện tích: {self.dien_tich_tg()}")

# Lớp Tam giác Đều kế thừa từ lớp Tam giác Cân
class TamGiacDeu(TamGiacCan):
    def __init__(self, canh):
        super().__init__(canh, canh) 
    def hien_thi(self):
        print(f"Tam giác đều với 3 cạnh bằng nhau: {self.canh_a}")
        print(f"Chu vi: {self.chu_vi_tg()}")
        print(f"Diện tích: {self.dien_tich_tg()}")

# Tam giác thường
tam_giac = TamGiac(3, 4, 5)
print("Tam giác thường:")
tam_giac.hien_thi()
print()
# Tam giác vuông
tam_giac_vuong = TamGiacVuong(3, 4)
print("Tam giác vuông:")
tam_giac_vuong.hien_thi()
print()
# Tam giác cân
tam_giac_can = TamGiacCan(5, 6)
print("Tam giác cân:")
tam_giac_can.hien_thi()
print()
# Tam giác đều
tam_giac_deu = TamGiacDeu(5)
print("Tam giác đều:")
tam_giac_deu.hien_thi()
