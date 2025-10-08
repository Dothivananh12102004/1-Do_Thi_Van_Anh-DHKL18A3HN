class ThiSinh:
    def __init__(self, hoten, toan, ly, hoa):
        self.hoten = hoten
        self.toan = toan
        self.ly = ly
        self.hoa = hoa
    def tong_diem(self):
        return self.toan + self.ly + self.hoa
    def hien_thi(self):
        print(f"Họ tên: {self.hoten}, Toán: {self.toan}, Lý: {self.ly}, Hóa: {self.hoa}, Tổng: {self.tong_diem()}")
ds_thisinh = []
n = int(input("Nhập số lượng thí sinh: "))
for i in range(n):
    hoten = input("Nhập họ tên: ")
    toan = float(input("Nhập điểm Toán: "))
    ly = float(input("Nhập điểm Lý: "))
    hoa = float(input("Nhập điểm Hóa: "))
    ts = ThiSinh(hoten, toan, ly, hoa)
    ds_thisinh.append(ts)
print("\nDanh sách thí sinh:")
for ts in ds_thisinh:
    ts.hien_thi()
diem_chuan = 20
print(f"\nDanh sách thí sinh trúng tuyển (điểm chuẩn = {diem_chuan}), sắp xếp từ cao xuống thấp:")
trung_tuyen = [ts for ts in ds_thisinh if ts.tong_diem() >= diem_chuan]
trung_tuyen.sort(key=lambda x: x.tong_diem(), reverse=True)
for ts in trung_tuyen:
    ts.hien_thi()
