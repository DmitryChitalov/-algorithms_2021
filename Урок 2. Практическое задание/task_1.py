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

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):
"""


def operand_input(message):
    input_not_finished = True
    while input_not_finished:
        # noinspection PyUnreachableCode
        try:
            return int(input(message))
        except ValueError:
            print('Вы ввели строку вместо числа. Исправьтесь.')
        else:
            input_not_finished = False


def calculator():
    message = 'Ваш результат:'

    input_not_finished = True
    while input_not_finished:
        operation = input('Введите операцию (+, -, *, / или 0 для выхода): ')
        if operation == '0':
            return
        elif operation not in '+-*/':
            print('Введёна неправильная операция')
        else:
            input_not_finished = False

    operand_1 = operand_input('Введите первое число: ')
    operand_2 = operand_input('Введите второе число: ')

    # noinspection PyUnboundLocalVariable
    if operation == '+':
        print(message, operand_1 + operand_2)
    elif operation == '-':
        print(message, operand_1 - operand_2)
    elif operation == '*':
        print(message, operand_1 * operand_2)
    else:
        try:
            print(message, operand_1 / operand_2)
        except ZeroDivisionError:
            print('На ноль делить нельзя.')

    calculator()


calculator()
