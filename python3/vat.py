product = eval(input("product: "))
vat = eval(input("vat: "))
result = (vat * product) / 100

print("vat: ", vat);
print("เงิน: ", product)
print("ราคา vat ที่ต้องจ่าย: ", result)
