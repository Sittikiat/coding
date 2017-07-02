def ticket(age, is_local):
    if (age <= 5 or age >= 60) and is_local == True:
        print("Free")
    else:
        print("Pay money")

ticket(5, True)