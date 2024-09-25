# Lớp Date được sử dụng để lưu trữ ngày sinh và ngày vào công ty
class Date:
    def __init__(self, day=1, month=1, year=2000):
        self.day = day
        self.month = month
        self.year = year
    def hien_thi(self):
        print(f"{self.day}/{self.month}/{self.year}")
    def __str__(self):
        return f"{self.day}/{self.month}/{self.year}"

# Lớp Employee mô tả thông tin nhân viên
class Employee:
    def __init__(self, name, birth_date, hire_date):
        self.name = name               
        self.birth_date = birth_date   
        self.hire_date = hire_date     
    # Phương thức in thông tin nhân viên
    def hien_thi(self):
        print(f"Họ tên: {self.name}")
        print(f"Ngày sinh: {self.birth_date}")
        print(f"Ngày vào công ty: {self.hire_date}")

# Chương trình quản lý nhân viên
class Company:
    def __init__(self):
        self.nhan_vien = []  
    # Phương thức thêm nhân viên vào danh sách
    def them_nhan_vien(self, employee):
        self.nhan_vien.append(employee)

    # Phương thức hiển thị thông tin của tất cả nhân viên
    def hthi_thong_tin(self):
        for i in self.nhan_vien:
            i.hien_thi()
            print("----------------------------")

# Tạo một số đối tượng nhân viên
birth_date1 = Date(15, 5, 1990)
hire_date1 = Date(1, 6, 2015)
nhan_vien1 = Employee("Nguyen Van An", birth_date1, hire_date1)

birth_date2 = Date(10, 8, 1985)
hire_date2 = Date(15, 7, 2010)
nhan_vien2 = Employee("Tran Thi Binh", birth_date2, hire_date2)

# Tạo đối tượng công ty và thêm nhân viên
company = Company()
company.them_nhan_vien(nhan_vien1)
company.them_nhan_vien(nhan_vien2)

# Hiển thị thông tin của tất cả nhân viên trong công ty
company.hthi_thong_tin()
