hours = input("Enter hours: ")
rate = input("Enter rate: ")

try:
    hours_float = float(hours)
    rate_float = float(rate)
    if hours <= 40:
        pay = hours_float * rate_float
    else:
            pay_1 = 40 * rate_float
            pay_2 = (hours_float - 40) * rate_float * 1.5
            pay = pay_1 + pay_2
    print("Pay: ", pay)
except:
    print("Error, please enter a numeric input")