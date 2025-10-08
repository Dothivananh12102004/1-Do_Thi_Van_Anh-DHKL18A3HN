class Date:
    def __init__(self, day=1, month=1, year=2000):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"{self.day:02d}/{self.month:02d}/{self.year}"
class Employee:
    def __init__(self, name, birth: Date, join: Date):
        self.name = name
        self.birth = birth
        self.join = join
    def display(self):
        print(f"Họ tên: {self.name}")
        print(f"Ngày sinh: {self.birth}")
        print(f"Ngày vào công ty: {self.join}")
ds_nv = []
n = int(input("Nhập số lượng nhân viên: "))
for i in range(n):
    print(f"\nNhân viên {i+1}:")
    name = input("Họ tên: ")
    d1, m1, y1 = map(int, input("Ngày sinh (dd mm yyyy): ").split())
    birth = Date(d1, m1, y1)
    d2, m2, y2 = map(int, input("Ngày vào công ty (dd mm yyyy): ").split())
    join = Date(d2, m2, y2)
    nv = Employee(name, birth, join)
    ds_nv.append(nv)
print("\n--- Danh sách nhân viên ---")
for nv in ds_nv:
    nv.display()
