
def get_result():
    operation = input('Введите операцию (+, -, *, / или 0 для выхода): ')
    if operation == '0':                                                        # Базовый случай, выход из рекурсии
        return print('Завершение программы')
    if operation not in ['-', '*', '+', '/', '0']:
        print('Повторите ввод операции')
        return get_result()
    try:                                                                        # Проверка на ввод числа
        num_1 = int(input('Введите первое число: '))
        num_2 = int(input('Введите второе число: '))
    except ValueError:
        print('Вы вместо числа ввели строку (((. Исправьтесь'), get_result()
    if operation == '+':                                                        # Блок операций, если все хорошо
        print (f'Ваш результат = {int(num_1) + num_2}')
        return get_result()
    elif operation == '-':
        print (f'Ваш результат = {num_1 - num_2}')
        return get_result()
    elif operation == '*':
        print (f'Ваш результат = {num_1 * num_2}')
        return get_result()
    elif operation == '/':
        try:                                                                      # Проверка деления на ноль
            print (f'Ваш результат = {num_1 / num_2}')
            return get_result()
        except ZeroDivisionError:
            print('Деление на ноль (((. Исправьтесь')
            return get_result()


get_result()