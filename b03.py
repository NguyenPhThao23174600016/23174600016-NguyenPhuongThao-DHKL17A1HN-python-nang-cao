class phan_so:
    def __init__(self,tu_so,mau_so):
        self.tu_so = tu_so
        self.mau_so = mau_so
        if mau_so == 0:
            print("Mau so vua nhap ko hop le !!!")
        elif tu_so == 0:
            print("Phan so bang: 0")
        elif tu_so == 0 and mau_so == 0:
            print("Phan so khong xac dinh !!!")
        elif mau_so != 0:
            print(f"Phan so vua nhap co dang:{tu_so}/{mau_so}")

tu_so = int(input("Nhap tu so la:"))
mau_so = int(input("Nhap mau so la:"))
phan_so_sau_ktra = phan_so(tu_so,mau_so)