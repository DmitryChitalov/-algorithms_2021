def calculator():
    operator = input('Выберите операцию (+-*/ или 0 для выхода): ')

    if operator == '0':
        return 'Bye'

    elif operator in '+-/*':
        try:
            fnum = int(input('Введите первое число: '))
            snum = int(input('Введите второе число'))
            if operator == '+':
                res = fnum + snum
                print(f'Ваш результат {res} ')
                return calculator()
            if operator == '-':
                res = fnum - snum
                print(f'Ваш результат {res} ')
                return calculator()
            if operator == '*':
                res = fnum * snum
                print(f'Ваш результат {res} ')
                return calculator()
            if operator == '/':
                if snum == 0:
                    print('Деление на 0 невозможно')
                else:
                    res = fnum / snum
                    print(f'Ваш результат {res} ')
                return calculator()
        except ValueError:
            print('Это не число, попробуй еще раз')
            return calculator()
    else:
        print('Неверный знак, попробуй еще раз')
        return calculator()


print(calculator())
