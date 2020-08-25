hours = input("Enter hours: ")
rate = input("Enter rate: ")
try:
    float_hours = float(hours)
    float_rate = float(rate)
except:
    print("Error, please enter a numeric input.")
    quit()
print("Pay: ", float_hours*float_rate)