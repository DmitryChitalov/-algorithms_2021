def calculate(operation, number1, number2):
    if operation == "+":
        return number1 + number2
    elif operation == "-":
        return number1 - number2
    elif operation == "*":
        return number1 * number2
    elif operation == "/":
        if number2 != 0:
            return number1 / number2
        else:
            return "ZeroDivivsionError"

def calculate_recursion():
    operation = input("Input operation ")
    if operation == '0':
        print("stop")
    else:
        number1 = int(input("input first number "))
        number2 = int(input("input second number "))
        print(calculate(operation, number1, number2))
        calculate_recursion()


calculate_recursion()
