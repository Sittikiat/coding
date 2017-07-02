def rectangle(w, h):
    area = w * h
    return(area)

# main entry point
w = eval(input("width = "))
h = eval(input("height = "))

print("area = ", rectangle(w, h))