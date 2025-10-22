import requests
print("=== ĐỌC DANH SÁCH SÁCH NỔI BẬT TỪ API ===")
url = "https://openlibrary.org/subjects/popular.json?limit=5"
try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    books = data.get("works", [])
    print(f"Tổng số sách nổi bật: {len(books)}\n")
    for i, book in enumerate(books, start=1):
        title = book.get("title", "Không có tiêu đề")
        authors = ", ".join(a["name"] for a in book.get("authors", []))
        print(f"{i}. Tên sách: {title}")
        print(f"   Tác giả: {authors}")
        print(f"   Năm xuất bản: {book.get('first_publish_year', 'Không rõ')}")
        print("-" * 40)
except requests.exceptions.RequestException as e:
    print(" Lỗi khi truy cập API:", e)
