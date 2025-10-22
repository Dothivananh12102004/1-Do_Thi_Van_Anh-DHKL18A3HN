import json
with open("company.json", "r", encoding="utf-8") as file:
    data = json.load(file)
company_name = data["company"]
address = data["address"]
departments = data["departments"]
total_employees = sum(d["employees"] for d in departments)
print(f"Tên công ty: {company_name}")
print(f"Địa chỉ: {address}")
print("----- Thống kê nhân viên theo đơn vị -----")
for i, dept in enumerate(departments, start=1):
    name = dept["name"]
    num = dept["employees"]
    percent = (num / total_employees) * 100
    print(f"{i}. Tên đơn vị: {name}")
    print(f" - Số nhân viên: {num}")
    print(f" - Tỷ lệ: {percent:.2f}%")
