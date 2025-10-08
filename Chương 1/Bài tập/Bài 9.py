class DaGiac:
    def __init__(self, sides):
        self.sides = sides
    def chu_vi(self):
        return sum(self.sides)
    def display(self):
        print("Các cạnh:", self.sides)
        print("Chu vi:", self.chu_vi())
class HinhBinhHanh(DaGiac):
    def __init__(self, a, b, h):
        super().__init__([a, b, a, b])
        self.a = a
        self.b = b
        self.h = h
    def dien_tich(self):
        return self.a * self.h
    def display(self):
        super().display()
        print("Diện tích hình bình hành:", self.dien_tich())
class HinhChuNhat(HinhBinhHanh):
    def __init__(self, a, b):
        super().__init__(a, b, h=b)
        self.a = a
        self.b = b
    def dien_tich(self):
        return self.a * self.b
    def display(self):
        print("Hình chữ nhật:")
        super(HinhBinhHanh, self).display()
        print("Diện tích hình chữ nhật:", self.dien_tich())
class HinhVuong(HinhChuNhat):
    def __init__(self, a):
        super().__init__(a, a)
        self.a = a
    def dien_tich(self):
        return self.a * self.a
    def display(self):
        print("Hình vuông:")
        super(HinhChuNhat, self).display()
        print("Diện tích hình vuông:", self.dien_tich())
print("=== Hình bình hành ===")
hb = HinhBinhHanh(6, 4, 3)
hb.display()
print("\n=== Hình chữ nhật ===")
hcn = HinhChuNhat(5, 3)
hcn.display()
print("\n=== Hình vuông ===")
hv = HinhVuong(4)
hv.display()
