
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
z = input("Choose operator (+, -, *, /): ")

if z == "+":
    print(x + y)
elif z == "-":
    print(x - y)
elif z == "*":
    print(x * y)
elif z == "/":
    print(x / y)
else:
    print("Invalid operator")
