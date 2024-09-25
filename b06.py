class Stack:
    def __init__(self):
        self.stack = []
    # Phương thức thêm phần tử vào ngăn xếp
    def them(self, ptu):
        self.stack.append(ptu)
    # Phương thức lấy phần tử khỏi ngăn xếp
    def lay(self):
        if not self.kiem_tra():
            return self.stack.lay()
        else:
            return None
    # Phương thức kiểm tra ngăn xếp có rỗng hay không
    def kiem_tra(self):
        return len(self.stack) == 0
    # Phương thức trả về số phần tử trong ngăn xếp
    def tra(self):
        return len(self.stack)
    # Phương thức in nội dung của ngăn xếp
    def print_stack(self):
        if self.kiem_tra():
            print("Ngăn xếp trống.")
        else:
            print("Nội dung ngăn xếp:", self.stack)

s = Stack()
s.them(1)
s.them(2)
s.them(3)
s.print_stack()  