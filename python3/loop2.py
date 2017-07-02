def temperature_table():
    for c in range(0, 101):
        f = (c * 9 / 5) + 32
        print("{}C = {}F".format(c, f))

def mult_table(form_n, to_n):
    #nested loop คือ loop ซ้อน loop
    for i in range(form_n, to_n + 1):
        for j in range(1, 13): #nested loop
            print("{} x {} = {}".format(i, j, i * j))
        print("-" * 40)
mult_table(2,4)