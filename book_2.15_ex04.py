# assume that we execute the following assigment statements:
# width = 17
# height = 12
# for each of the following expressions, write the value of the expression and the type(of the value of the expression).
# 1. width//2
# 2. width/2.0
# 3. height/3
# 4. 1 + 2 * 5

width = float(input("Enter width: "))
height = float(input("Enter height: "))
a = width//2
b = width/2.0
c = height/3
d = 1 + 2 * 5
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
