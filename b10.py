import math
#Lop Diem
class Diem:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def hien_thi_toa_do (self):
        print(f"Tọa độ điểm: ({self.x}, {self.y})")

#Lop elip thua ke tu lop diem
class Elip(Diem):
    def __init__(self, x, y, truc_lon, truc_nho):
        super().__init__(x, y)  
        self.truc_lon = truc_lon
        self.truc_nho = truc_nho  
    def dien_tich_elip(self):
        return math.pi * self.truc_lon * self.truc_nho  
    def hien_thi(self):
        print(f"Tọa độ tâm elip: ({self.x}, {self.y})")
        print(f"Trục lớn: {self.truc_lon}")
        print(f"Trục nhỏ: {self.truc_nho}")
        print(f"Diện tích elip: {self.dien_tich_elip()}")

# Lớp Đường tròn kế thừa từ Elip 
class DuongTron(Elip):
    def __init__(self, x, y, ban_kinh):
        super().__init__(x, y, ban_kinh, ban_kinh)  
        self.ban_kinh = ban_kinh
    def dien_tich_htron(self):
        return math.pi * self.ban_kinh ** 2  
    def hien_thi(self):
        print(f"Tọa độ tâm đường tròn: ({self.x}, {self.y})")
        print(f"Bán kính: {self.ban_kinh}")
        print(f"Diện tích đường tròn: {self.dien_tich_htron()}")

# Elip
elip = Elip(4, 6, 5, 3)
print("Elip:")
elip.hien_thi()
print()
# Đường tròn
duong_tron = DuongTron(4, 6, 4)
print("Đường tròn:")
duong_tron.hien_thi()

