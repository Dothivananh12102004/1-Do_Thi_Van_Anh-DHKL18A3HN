import math
class PhanSo:
    def __init__(self, tu=0, mau=1):
        self.tu = tu
        self.mau = mau
    def nhap(self):
        self.tu = int(input("Nhập tử số: "))
        self.mau = int(input("Nhập mẫu số: "))
        if self.mau == 0:
            print("Mẫu số không được bằng 0")
    def hien_thi(self):
        if self.mau == 1:
            print(f"Phân số: {self.tu}")
        else:
            print(f"Phân số: {self.tu}/{self.mau}")
ps = PhanSo()
ps.nhap()
ps.hien_thi()

