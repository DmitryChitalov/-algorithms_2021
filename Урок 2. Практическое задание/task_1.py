def calculator():
    what_to_do = input('\nЧто будем делать? +, -, *, /, \n'
                       'если устал введи "0" для выхода из программы.\n')

    if what_to_do == '0':
        print('Ну чтож бывает, меня уже не раз выключали :(')
        exit()

    elif what_to_do in '+-*/':
        try:
            num1 = int(input('введите первое число: \n'))
            num2 = int(input('введите второе число: \n'))

            if what_to_do == '+':
                print('Сумма чисел равна ', num1 + num2)
                return calculator()

            elif what_to_do == '-':
                print('Разность чисел равна ', num1 - num2)
                return calculator()

            elif what_to_do == '*':
                print('Произведение чисел ', num1 * num2)
                return calculator()

            elif what_to_do == '/':
                try:
                    print('Частное от деления чисел ', num1 / num2)
                    return calculator()

                except ZeroDivisionError:
                    print('Делить на ноль?! Ай-яай-яай')
                    return calculator()

        except ValueError:
            print('Непохоже это на число. Попробуй ещё раз.')
            return calculator()
    else:
        print('Что это за знаки? каракули какие-то. ты давай определись. '
              'Решаем или выходим')
        return calculator()


calculator()
