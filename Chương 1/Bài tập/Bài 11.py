import math
class PhanSo:
    def __init__(self, tu=0, mau=1):
        if mau == 0:
            raise ValueError("Mẫu số không thể bằng 0!")
        self.tu = tu
        self.mau = mau
    def __str__(self):
        return f"{self.tu}/{self.mau}"
    def __add__(self, other):
        tu = self.tu * other.mau + other.tu * self.mau
        mau = self.mau * other.mau
        return PhanSo(tu, mau)
    def __sub__(self, other):
        tu = self.tu * other.mau - other.tu * self.mau
        mau = self.mau * other.mau
        return PhanSo(tu, mau)
    def __mul__(self, other):
        tu = self.tu * other.tu
        mau = self.mau * other.mau
        return PhanSo(tu, mau)
    def __truediv__(self, other):
        if other.tu == 0:
            raise ZeroDivisionError("Không thể chia cho phân số 0!")
        tu = self.tu * other.mau
        mau = self.mau * other.tu
        return PhanSo(tu, mau)
ps1 = PhanSo(2, 3)
ps2 = PhanSo(4, 5)
print("ps1 =", ps1)
print("ps2 =", ps2)
print("Cộng:", ps1 + ps2)
print("Trừ:", ps1 - ps2)
print("Nhân:", ps1 * ps2)
print("Chia:", ps1 / ps2)
