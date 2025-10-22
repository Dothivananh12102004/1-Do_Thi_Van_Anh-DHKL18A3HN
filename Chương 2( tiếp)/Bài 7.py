import json
with open("sinhvien.json", "r", encoding="utf-8") as f:
    data = json.load(f)
print("Danh sách sinh viên hiện có:\n")
for sv in data["Students"]:
    print(f"{sv['id']} - {sv['name']} - {sv['class']} - {sv['gender']}")
new_sv = {
    "id": "SV003",
    "name": "Phạm Văn C",
    "class": "DHKL18A3HN",
    "gender": "Nam"
}
data["Students"].append(new_sv)
print("\nĐã thêm sinh viên mới!")
with open("sinhvien.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
print("Dữ liệu đã được lưu lại vào sinhvien.json")
