largest = 0
smallest = None

while True:
    string_value = input("Enter a number: ")
    if string_value == 'done':
        break
    try:
        float_value = float(string_value)
    except:
        print("Invalid input")
        continue
    if smallest is None:
        smallest = float_value
        largest = float_value
    elif float_value > largest:
        largest = float_value
    elif float_value < smallest:
        smallest = float_value

print("Maximum is {}".format(largest))
print("Minimum is {}".format(smallest))
