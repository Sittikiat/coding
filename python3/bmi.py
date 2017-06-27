weight = eval(input("น้ำหนักของคุณ: "))
height = eval(input("ความสูงของคุณ: "))

height = height / 100

bmi = weight / (height * height)
if (bmi >= 30.0):
    print("bmi = ", bmi)
    print("Obese")
elif (bmi <= 29.9 and bmi >= 25.0):
    print("bmi = ", bmi)
    print("Overeight")
elif (bmi <= 24.9 and bmi >= 18.5):
    print("bmi = ", bmi)
    print("Normal")
elif (bmi < 18.5):
    print("bmi = ", bmi)
    print("Underweight")
else:
    print("error")
