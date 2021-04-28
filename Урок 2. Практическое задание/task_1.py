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


def validation(number):
    try:
        float(number)
        return True
    except ValueError:
        print('This is not a number')
        return False


def calculator():
    operation = input("select operation +, -, *, / or 0 to exit: ")
    if operation == '0':
        return print('You entered "0". Termination of the function.')
    if operation not in ('+', '-', '*', '/'):
        print('incorrect input')
        return calculator()

    first_number = input("Enter the first number: ")
    if not validation(first_number):
        return calculator()
    first_number = float(first_number)
    second_number = input("Enter the second number:")
    if not validation(second_number):
        return calculator()
    second_number = float(second_number)

    if operation == '+':
        print(f'Result:  {first_number + second_number}')
    elif operation == '-':
        print(f'Result:  {first_number - second_number}')
    elif operation == '*':
        print(f'Result:  {first_number * second_number}')
    elif operation == '/' and second_number:
        print(f'Result:  {first_number / second_number}')
    else:
        print(f'The divisor must be nonzero)')

    return calculator()


calculator()
