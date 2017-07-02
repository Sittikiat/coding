s = "Hello, world";
print(len(s))
print(s[:7]) #sub string
print(s[7:]) #sub string




# find()
#string1.find(string2, beg = 0, end = len(string1))

text = "This is my world, Hello world"
word = "world"

result = text.find(word, 0, len(text))

if result == -1:
    print("ไม่มีคำนี้อยู่ในระบบ")
else:
    print("ยีนดีด้วยคุณเจอคำที่ต้องการ คือ ", result)