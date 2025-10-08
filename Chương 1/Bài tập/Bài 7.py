class Date:
    # Hàm tạo với giá trị mặc định
    def __init__(self, day=1, month=1, year=2000):
        self.day = day
        self.month = month
        self.year = year

    # Hàm kiểm tra năm nhuận
    def is_leap_year(self):
        return (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)

    # Trả về số ngày trong tháng
    def days_in_month(self):
        if self.month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif self.month in [4, 6, 9, 11]:
            return 30
        elif self.month == 2:
            return 29 if self.is_leap_year() else 28
        else:
            return 0

    # In ngày
    def display(self):
        print(f"{self.day:02d}/{self.month:02d}/{self.year}")

    # Tính ngày tiếp theo
    def next(self):
        self.day += 1
        if self.day > self.days_in_month():
            self.day = 1
            self.month += 1
            if self.month > 12:
                self.month = 1
                self.year += 1
d = Date(28, 2, 2018)
d.display()
d.next()
d.display()
