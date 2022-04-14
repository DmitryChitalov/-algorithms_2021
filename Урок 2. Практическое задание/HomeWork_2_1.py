def calculator():
    print('Какую операцию совершаем?')
    action = input()
    if action == '0':
        return 'Программа завершена'
    else:
        if action in '+-*/':
            try:
                print('Введите первое число')
                numb_1 = int(input())
                print('Введите второе число')
                numb_2 = int(input())
                if action == '+':
                    result = numb_1 + numb_2
                    print(f'Результат операции {result}')
                elif action == '-':
                    result = numb_1 - numb_2
                    print(f'Результат операции {result}')
                elif action == '*':
                    result = numb_1 * numb_2
                    print(f'Результат операции {result}')
                elif action == '/':
                    try:
                        result = numb_1 / numb_2
                        print(f'Результат операции {result}')
                    except ZeroDivisionError:
                        print('Деление на ноль!')
                        return calculator()
                return calculator()
            except ValueError:
                print('Вы ввели некорректное число!')
                return calculator()
        else:
            print('Вы ввели некоректное действие!')
            return calculator()

print(calculator())