import json

json_data = '''{
    "name": "Nguyen Phuong Thao",
    "age": 19,
    "address": {
        "city": "Bac Giang",
        "country": "Vietnam"
    },
    "hobbies": ["reading", "listening", "coding"]
}'''

# Chuyển đổi từ JSON sang đối tượng Python (dictionary)
python_object = json.loads(json_data)

# In đối tượng Python
print(python_object)

# Truy cập các phần tử trong đối tượng
print("Name:", python_object["name"])
print("Age:",python_object["age"])
print("City:", python_object["address"]["city"])
print("Hobbies:", python_object["hobbies"])

