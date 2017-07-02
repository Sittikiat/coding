def vat(inputVat):
    result = inputVat * product / 100
    return result


product = eval(input("product: "))
user = eval(input("มากี่คน: "))
inputVat = eval(input("vat: "))
payonly = vat(inputVat) / user


print("สินค้า: ", product, "บาท")
print("ราคา vat ที่ต้องจ่าย: ", vat(inputVat), "บาท")
print("จ่าย vat คนละ: ", payonly, "บาท")
print("จ่ายคนละ: ", (product / user))

