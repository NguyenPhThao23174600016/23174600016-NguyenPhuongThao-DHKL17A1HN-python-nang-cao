import json

python_object = '''{
    "name": "Nguyen Phuong Thao",
    "age": 19,
    "address": {
        "city": "Bac Giang",
        "country": "Vietnam"
    },
    "hobbies": ["reading", "listening", "coding"]
}'''

# Chuyển đổi đối tượng Python sang JSON
json_data = json.dumps(python_object,indent = 4)

# In đối tượng Python
print("Chuỗi JSON:\n", json_data)

