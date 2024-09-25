class Stark:
    def __init__(self):
        self.stark = []
    #Them phan tu vao ngan xep
    def them_ptu (self,them):
        self.stark.append(them)
    #Lay phan tu ra khoi ngan xep
    def lay_ptu (self):
        if not self.ktra():
            return self.stark.lay_ptu()
        else:
            return None
    #Ktra ngan xep co rong hay ko
    def ktra(self):
        return len(self.stark)
    #Tra ve so ptu trong ngan xep
    def tra_ve(self):
        return len(self.stark)

S = Stark()
S.them_ptu(1)
S.them_ptu(2)
S.them_ptu(3)
print(S.tra_ve())
S.lay_ptu()
print(S.tra_ve())