def calculator():
    operation = input("Введите операцию (+, -, *, / или 0 (ноль) для выхода): ")
    symbol = ('+', '-', '*', '/')
    if operation == '0':
        return "Выход"

    if operation not in symbol:
        print("Символ операции введен не корректно")
        return calculator()
    else:
        try:
            number_1 = int(input("Введите число - "))
            number_2 = int(input("Введите второе число - "))
        except ValueError:
            print("Вводить можно только числа")
            return calculator()

        if operation == '+':
            res = number_1 + number_2
            print(f"{number_1} + {number_2} = {res}")
            return calculator()

        if operation == '-':
            res = number_1 - number_2
            print(f"{number_1} - {number_2} = {res}")
            return calculator()

        if operation == '*':
            res = number_1 * number_2
            print(f"{number_1} * {number_2} = {res}")
            return calculator()

        if operation == '/':
            try:
                res = number_1 / number_2
            except ZeroDivisionError:
                print("Делить на 0 нельзя")
            else:
                print(f"{number_1} / {number_2} = {res}")
            finally:
                return calculator()


calculator()
