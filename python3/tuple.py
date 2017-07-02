# tuple เป็น แบบ immutable คือ ไม่สามารถเปลี่ยนค่าได้

# a = (1,2,3,4,5,6)
#
# print(a[2] - a[0])


def distance(pointA, pointB):
    return ((pointA[0] - pointB[0]) ** 2 + (pointA[1] - pointB[1]) ** 2) ** 0.5

pointA = (1, 7)
pointB = (5, 10)

d = distance(pointA, pointB)
print(d)

# OR

# def distance2(x1, y1, x2, y2):
#     return ((x1 - y1) ** 2 + (x2 - y2) ** 2) ** 0.5
#
# d = distance2(1,5,7,10)
# print(d)
