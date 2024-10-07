import json

python_dict = '''{
    "name": "Nguyen Phuong Thao",
    "age": 19,
    "address": {
        "city": "Bac Giang",
        "country": "Vietnam"
    },
    "hobbies": ["reading", "listening", "coding"]
}'''
#Chuyen doi tu dien Python sang chuoi JSON voi khoa duoc sap xep va thut le 4 khoang trang
json_data = json.dumps(python_dict, indent=4, sort_keys=True, ensure_ascii=False)

# In chuoi JSON ra man hinh
print("Chuỗi JSON với khóa được sắp xếp:\n", json_data)