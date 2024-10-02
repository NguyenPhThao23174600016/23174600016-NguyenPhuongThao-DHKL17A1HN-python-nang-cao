import xml.dom.minidom

# Tải và phân tích file sample.xml
def parse_and_print_elements():
    # Load file XML
    doc = xml.dom.minidom.parse("sample.xml")
    
    # Lấy danh sách tất cả các phần tử có thẻ <staff>
    staff_elements = doc.getElementsByTagName("staff")
    
    # Duyệt qua từng phần tử và in ra tên của nhân viên
    for staff in staff_elements:
        # Lấy tên của nhân viên (nằm trong thẻ <name>)
        name = staff.getElementsByTagName("name")[0].childNodes[0].data
        print(f"Staff Name: {name}")

# Gọi hàm parse_and_print_elements để in ra danh sách tên của nhân viên
parse_and_print_elements()
