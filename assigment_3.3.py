number = float(input("Enter your score: "))
if (number >= 0) and (number <= 1):
    if number >= 0.9:
        print("A")
    elif number >= 0.8:
        print("B")
    elif number >= 0.7:
        print("C")
    elif number >= 0.6:
        print("D")
    else: print("F")
else:
    print("Error. Enter a valid score between 0.0 and 1.0")
    quit()