hours = float(input("Enter hours: "))
rate = float(input("Enter rate: "))

def computepay(hours, rate):
    if hours <= 40:
        pay = hours * rate
    else:
            pay_1 = 40 * rate
            pay_2 = (hours - 40) * rate * 1.5
            pay = pay_1 + pay_2
    return pay

pay = computepay(hours, rate)
print("Pay", pay)