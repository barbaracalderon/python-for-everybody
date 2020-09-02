value = float(input("Enter a number: "))
soma = 0
qtde = 0

while True:
    try:
        while (value != 'done'):
            if value >= soma:
                soma = value + soma
                qtde = qtde + 1
                value = float(input("Enter a number: "))
            else:
                soma = soma + value
                qtde = qtde +1
                average = soma/qtde
                value = float(input("Enter a number: "))
        else:
            print(soma, qtde, average)
    except:
        value = print("Invalid input")
        value = 0
        value = float(input("Enter a number: "))
        while (value != 'done'):
            if value > soma:
                soma = value
                qtde = 1
                value = input("Enter a number: ")
            else:
                soma = soma + value
                qtde = qtde +1
                average = soma/qtde
                value = input("Enter a number: ")
        else:
            print(soma, qtde, average)
            break