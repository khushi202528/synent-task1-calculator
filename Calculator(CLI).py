# simple calculator

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
op = input("Enter operation (+, -, *, /): ")

try:
    num1 = float(num1)
    num2 = float(num2)

    if op == "+":
        result = num1 + num2
        print("Result is:", result)

    elif op == "-":
        result = num1 - num2
        print("Result is:", result)

    elif op == "*":
        result = num1 * num2
        print("Result is:", result)

    elif op == "/":
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            result = num1 / num2
            print("Result is:", result)

    else:
        print("Invalid operation")

except:
    print("Invalid input")