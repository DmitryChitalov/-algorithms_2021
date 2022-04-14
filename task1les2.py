def calculator():
    sign = input("Введите операцию (+, -, *, / или 0 для выхода):")
    if sign == "0":
        return "Выход из программы"
    else:
        if sign == "+" or sign == "-" or sign == "*" or sign == "/":
            try:
                number1 = int(input("Введите первое число: "))
                number2 = int(input("Введите второе число: "))
                if sign == "+":
                    print("", number1+number2)
                    return calculator()
                if sign == "-":
                    print("", number1 - number2)
                    return calculator()
                if sign == "*":
                    print("",  number1 * number2)
                    return calculator()
                if sign == "/":
                    if number2 != 0:
                        print("", number1 / number2)
                    else:
                        print("На 0 делить нельзя!")
                    return calculator()
            except ValueError:
                print("Неправильный синтаксис! Вы ввели строку!")
                return calculator()
        else:
            print("Вы ввели неверный символ! Попробуйте снова!")
            return calculator()
calculator()