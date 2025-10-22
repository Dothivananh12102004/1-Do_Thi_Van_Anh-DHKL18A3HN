import json
from datetime import datetime
def nhap_giao_dich():
    danh_sach = []
    while True:
        loai = input("Nhập loại giao dịch (tiền/vàng/...): ")
        so_tien = float(input("Nhập số tiền: "))
        ghi_chu = input("Nhập ghi chú: ")
        giao_dich = {
            "loai_giao_dich": loai,
            "so_tien": so_tien,
            "ghi_chu": ghi_chu
        }
        danh_sach.append(giao_dich)
        tiep_tuc = input("Nhập thêm giao dịch? (1: Có, 0: Không): ")
        if tiep_tuc == "0":
            break
    return danh_sach
def ghi_file_json(danh_sach):
    now = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    ten_file = f"{now}.json"
    with open(ten_file, "w", encoding="utf-8") as file:
        json.dump(danh_sach, file, ensure_ascii=False, indent=4)
    print(f"\n Đã ghi {len(danh_sach)} giao dịch vào file: {ten_file}")
print("=== GHI DỮ LIỆU GIAO DỊCH VÀO FILE JSON ===")
ds = nhap_giao_dich()
ghi = input("Bạn có muốn ghi vào file không? (1: Có, 0: Không): ")
if ghi == "1":
    ghi_file_json(ds)
else:
    print(" Không ghi dữ liệu.")
