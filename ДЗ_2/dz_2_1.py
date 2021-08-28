'''
    Калькулятор.
    Для операций используем операторы +, -, *, /.
    Для выхода 0.
'''
def calculator():
    # Получаем знак операции от пользователя
    operation = input('Введите операцию (+, -, *, / или 0 для выхода): ')

    # Проверка знака операции
    if not (operation.strip() == "+" or operation.strip() == "-"
            or operation.strip() == "*" or operation.strip() == "/"):
        print('Введена неверная операция! Попробуйте еще раз.')
        return calculator()

    # Выход из функции если введен 0
    if operation == '0':
        return

    # Пытаемся сложить введенные числа
    try:
        digit_1 = int(input('Введите первое число: '))
        digit_2 = int(input('Введите второе число: '))

        if operation == '+':
            print(digit_1 + digit_2)
        elif operation == '-':
            print(digit_1 - digit_2)
        elif operation == '*':
            print(digit_1 * digit_2)
        elif operation == '/':
            if digit_2 != 0:
                print(digit_1 / digit_2)
            else:
                print('Ошибка! Деление на ноль.')
    except ValueError:
        print('Введено не число!')

    return calculator()


calculator()
