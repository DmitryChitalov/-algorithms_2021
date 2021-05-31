def calculator():
    operation = input('Введите операцию (+, -, *, / или 0 для выхода): ')
    if operation == '0':
        quit()
    if operation not in ['+', '-', '/', '*']:
        print('Вы ввели неверную операцию. Исправьтесь(')
        calculator()
    first_val = input('Введите первое число: ')
    sec_val = input('Введите второе число: ')
    if operation == '+':
        try:
            print(f'Ваш результат: {round(int(first_val) + int(sec_val), 2)}')
        except ValueError:
            print('Вы ввели не число. Исправьтесь(')
    elif operation == '-':
        try:
            print(f'Ваш результат: {round(int(first_val) - int(sec_val), 2)}')
        except ValueError:
            print('Вы ввели не число. Исправьтесь(')
    elif operation == '*':
        try:
            print(f'Ваш результат: {round(int(first_val) * int(sec_val), 2)}')
        except ValueError:
            print('Вы ввели не число. Исправьтесь(')
    elif operation == '/':
        if sec_val != '0':
            try:
                print(f'Ваш результат: {round(int(first_val) / int(sec_val), 2)}')
            except ValueError:
                print('Вы ввели не число. Исправьтесь(')
        else:
            print('На "0" делить нельзя!')
    calculator()


calculator()