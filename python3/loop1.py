def loop1():
    for i in range(11): # for(let i=0; i<11; i++)
        print(i)
        print("-----------")

def loop2():
    for i in range(1, 11, 2):
        print(i)

def loop_str():
    s = "over the rainbow"
    for n in s: #loop ทุกตัวของ python เป็น foreach ทั้งหมด คือ ไม่ต้องกำหนดจุดสิ้นสุด หรือ len
        print(n.lower())
        print(n.upper())
    print("Success")

def loop_tuple():
    color = ("red", "green", "blue", "pink", "violet", "purple")
    print(type(color))
    for i in range(1, len(color)):
        print(i, color[i].upper(), sep=". ")

loop_tuple()