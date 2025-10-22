import requests
import json
import csv

# --- 1) Truy xuất dữ liệu JSON từ API ---
url = "https://api.exchangerate-api.com/v4/latest/USD"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Đã tải dữ liệu JSON thành công!\n")

    # --- 2) Phân tích cú pháp JSON ---
    base_currency = data["base"]
    date = data["date"]
    rates = data["rates"]

    print(f"Tỷ giá {base_currency} ngày {date}:\n")

    # In thử 5 dòng đầu
    for currency, value in list(rates.items())[:5]:
        print(f"  1 {base_currency} = {value} {currency}")

    # --- 3) Ghi dữ liệu ra file CSV ---
    with open("exchange.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Currency", "Value (per 1 USD)"])  # tiêu đề cột

        for currency, value in rates.items():
            writer.writerow([currency, value])

    print("\n✅ Đã lưu dữ liệu vào file exchange.csv")

else:
    print("Không thể truy cập API! Mã lỗi:", response.status_code)
