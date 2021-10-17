"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.

Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.

Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, / - ШАГ РЕКУРСИИ
- условие завершения рекурсии - введена операция 0 - БАЗОВЫЙ СЛУЧАЙ

Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""

# enter = input('Введите операцию (+, -, *, / или 0 для выхода): ')
# while enter != '0':
#     first_number = int(input('Введите первое число: '))
#     second_number = int(input('Введите второе число: '))
#     if enter == '+':
#         result = first_number + second_number
#     elif enter == '-':
#         result = first_number - second_number
#     elif enter == '*':
#         result = first_number * second_number
#     elif enter == '/':
#         result = first_number / second_number
#     print(result)
#     enter = input('Введите операцию (+, -, *, / или 0 для выхода): ')


def calculator():
    enter = input('Введите операцию (+, -, *, / или 0 для выхода): ')
    if enter == '0':
        return 'Exit'
    elif enter in ['+', '-', '*', '/']:
        try:
            first_number = int(input('Введите первое число: '))
        except ValueError:
            print('Введено не число. Начнём сначала')
            return calculator()
        try:
            second_number = int(input('Введите второе число: '))
        except ValueError:
            print('Введено не число. Начнём сначала')
            return calculator()
        if enter == '+':
            result = first_number + second_number
        elif enter == '-':
            result = first_number - second_number
        elif enter == '*':
            result = first_number * second_number
        elif enter == '/':
            try:
                result = first_number / second_number
            except ZeroDivisionError:
                print('Делить на 0 нельзя. Попробуйте снова.')
                return calculator()
        print('Ваш результат: ', result)
    else:
        return calculator()
    return calculator()


print(calculator())
