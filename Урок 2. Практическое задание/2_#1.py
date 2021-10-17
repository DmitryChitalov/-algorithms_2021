def calculator():
    symbol = input('Введите операцию "+", "-", "*", "/", для выхода "0": ')
    if symbol == '0':
        return 'exit'
    else:
        if symbol in "+-*/":
            one_number = int(input('Введите первое число: '))
            two_number = int(input('Введите второе число: '))

            if symbol == '+':
                decision = one_number + two_number
                print(decision)
                return calculator()
            elif symbol == '-':
                decision = one_number - two_number
                print(decision)
                return calculator()
            elif symbol == '/' and two_number != 0:
                decision = one_number / two_number
                print(decision)
                return calculator()
            elif symbol == '/' and two_number == 0:
                try:
                    one_number / 0
                except ZeroDivisionError:
                    print('На 0 делить нельзя! Повторите ввод!')
                    return calculator()
            elif symbol == '*':
                decision = one_number * two_number
                print(decision)
                return calculator()
        else:
            print('Неправильный ввод символа! Повторите ввод!')
            return calculator()


print(calculator())
