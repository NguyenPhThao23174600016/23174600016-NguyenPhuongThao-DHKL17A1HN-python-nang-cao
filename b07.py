class Date:
    def __init__(self, day=1, month=1, year=2000):
        self.day = day
        self.month = month
        self.year = year
    # Phương thức hiển thị thông tin ngày tháng năm
    def hien_thi(self):
        print(f"Ngày {self.day}/{self.month}/{self.year}")
    # Phương thức tính ngày tiếp theo
    def ngay_tiep_theo(self):
        # Số ngày trong mỗi tháng
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        # Kiểm tra năm nhuận
        if (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0):
            days_in_month[1] = 29  # Tháng 2 có 29 ngày trong năm nhuận
        # Tăng ngày lên 1
        self.day += 1
        # Kiểm tra nếu ngày vượt quá số ngày trong tháng
        if self.day > days_in_month[self.month - 1]:
            self.day = 1  # Chuyển ngày về 1
            self.month += 1  # Tăng tháng lên 1
            # Nếu tháng vượt quá 12, chuyển về tháng 1 và tăng năm lên 1
            if self.month > 12:
                self.month = 1
                self.year += 1

d = Date(25, 9, 2024)  
d.hien_thi()  
d.ngay_tiep_theo()
d.hien_thi()  
d.ngay_tiep_theo()
d.hien_thi() 
