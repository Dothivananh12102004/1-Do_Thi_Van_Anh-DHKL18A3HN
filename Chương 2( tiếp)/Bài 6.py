import requests
import xml.etree.ElementTree as ET
import csv
url = "https://www.hindustantimes.com/rss/topnews/rssfeed.xml"
response = requests.get(url)
with open("rssfeed.xml", "wb") as f:
    f.write(response.content)
print("Đã tải xong RSS feed và lưu vào rssfeed.xml")
tree = ET.parse("rssfeed.xml")
root = tree.getroot()
items = root.findall(".//item")
news_list = []
for item in items:
    title = item.find("title").text if item.find("title") is not None else ""
    link = item.find("link").text if item.find("link") is not None else ""
    pubDate = item.find("pubDate").text if item.find("pubDate") is not None else ""
    description = item.find("description").text if item.find("description") is not None else ""
    news_list.append({
        "Title": title,
        "Link": link,
        "PubDate": pubDate,
        "Description": description
    })
print(f"Đã đọc {len(news_list)} bản tin từ RSS feed.")
with open("news.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv
