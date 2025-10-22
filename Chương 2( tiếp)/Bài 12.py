import requests
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
if response.status_code == 200:
    posts = response.json()  # Chuyển dữ liệu JSON sang list of dict
    print(f"✅ Kết nối thành công! Có {len(posts)} bài post.\n")
    for post in posts[:5]:  # In thử 5 bài đầu để ngắn gọn
        print(f"User ID: {post['userId']}")
        print(f"Post ID: {post['id']}")
        print(f"Title: {post['title']}")
        print(f"Body: {post['body']}\n")
        print("-" * 50)
else:
    print(" Không thể truy cập API! Mã lỗi:", response.status_code)
