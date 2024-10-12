import requests

# URL của API lấy thông tin các comment với postId = 1
url = "https://jsonplaceholder.typicode.com/comments?postId=1"

# Gửi yêu cầu GET tới API
response = requests.get(url)

# Kiểm tra nếu yêu cầu thành công
if response.status_code == 200:
    comments = response.json()  # Chuyển đổi dữ liệu thành JSON

    # Hiển thị thông báo và giới hạn chỉ 3 comment đầu tiên
    print("Danh sách các bài post nổi bật (giới hạn 3 bài đầu):")
    for comment in comments[:3]:
        print(f"\nID: {comment['id']}")
        print(f"Tên: {comment['name']}")
        print(f"Email: {comment['email']}")
        print(f"Nội dung: {comment['body']}")
else:
    print("Không thể lấy dữ liệu từ API.")
