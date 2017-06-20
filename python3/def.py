# ไม่คืนค่า ให้แสดงอย่างเดียว จบในตัวมันเอง
def get_triangle (width, height):
    area = width * height / 2
    print("Area =", area)
    print("Type =", type(area))

# return ค่าเพื่อส่งไปใช้ประโยชน์ต่อ   
"""
def get_name (name):
    return(name)

name = get_name("mike")
print(name)
"""

def get_square_area (width=30, height=5):
    return(width * height)

#default parameter
result1 = get_square_area()
print(result1)
result2 = get_square_area(10)
print(result2)
result3 = get_square_area(12, 15)
print(result3)
