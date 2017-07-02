"""
    แสดงว่าเป็น เลคี่ หรือ คู่
"""

def is_even(n):
    if (n % 2 == 0):
        print("เป็นเลขคู่")
        return True
    else:
        print("เป็นเลขคี่")
        return False
print(is_even(2))
print(is_even(3))
print(is_even(13))