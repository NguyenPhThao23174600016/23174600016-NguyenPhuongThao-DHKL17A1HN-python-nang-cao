import xml.dom.minidom

# Tải và phân tích file sample.xml
def parse_xml():
    # Load file XML
    doc = xml.dom.minidom.parse("sample.xml")
    
    # In ra toàn bộ nội dung XML dưới dạng chuỗi
    print(doc.toprettyxml())

# Gọi hàm parse_xml để phân tích file XML
parse_xml()
