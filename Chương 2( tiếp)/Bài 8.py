import requests
import json
url = "https://api.open-meteo.com/v1/forecast?latitude=21.0285&longitude=105.8542&current_weather=true"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()   # Phân tích JSON thành dict Python
    print("Dữ liệu JSON nhận được:\n")
    current = data["current_weather"]
    temperature = current["temperature"]
    windspeed = current["windspeed"]
    time = current["time"]
    print("\n Thời tiết hiện tại tại Hà Nội:")
    print(f"  Nhiệt độ: {temperature}°C")
    print(f"  Tốc độ gió: {windspeed} km/h")
    print(f"  Thời gian cập nhật: {time}")
else:
    print("Không thể truy xuất dữ liệu! Mã lỗi:", response.status_code)
