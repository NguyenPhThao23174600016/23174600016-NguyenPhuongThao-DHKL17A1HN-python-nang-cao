class hinh_chu_nhat:
    def __init__(self,chieu_dai,chieu_rong):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong
    def dien_tich(self):
        return self.chieu_dai * self.chieu_rong
    def chu_vi(self):
        return (self.chieu_dai + self.chieu_rong) * 2
    def thong_tin(self):
        print(f"chieu dai:{self.chieu_dai}")
        print(f"Chieu rong:{self.chieu_rong}")
        print(f"Chu vi: {self.chu_vi()}")
        print(f"Dien tich:{self.dien_tich()}")

chieu_dai = float(input("nhap chieu dai hinh chu nhat la:"))
chieu_rong = float(input("nhap chieu rong hinh chu nhat la:"))
do_dai = hinh_chu_nhat(chieu_rong, chieu_dai)
do_dai.thong_tin()