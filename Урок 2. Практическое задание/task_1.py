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

'''
==================================================================================================
Вариант решения не очень рекуривный
'''
def input_operation():
    operation_list = ['+', '-', '*', '/', '0']
    while True:
        operation = input('Введите операцию (+, -, *, / или 0 для выхода): ')
        operation = operation.replace(' ', '')
        if operation in operation_list:
            break
        print('Вы ввели операцию не из списка или ошиблись. Исправьтесь')
    return operation


def validate_number(number):
    if type(int(number)) == int:
        return True


def input_number(element: str):
    while True:
        number = input(f'Введите {element} число: ')
        if validate_number(number):
            number = int(number)
            break
        print(f'Вместо целого числа вы ввели {number}. Исправьтесь')
    return number


def calculator_recur(operation):
    if operation == '0':
        return
    number_1 = input_number('первое')
    number_2 = input_number('второе')
    if operation == '+':
        print(f'Ваш результат {number_1 + number_2}')
        calculator_recur(input_operation())
    if operation == '-':
        print(f'Ваш результат {number_1 - number_2}')
        calculator_recur(input_operation())
    if operation == '*':
        print(f'Ваш результат {number_1 * number_2}')
        calculator_recur(input_operation())
    if operation == '/':
        if number_2 == 0 and operation == '/':
            print('На ноль делить нельзя!')
            calculator_recur(input_operation())
        else:
            print(f'Ваш результат {number_1 / number_2}')
            calculator_recur(input_operation())


calculator_recur(operation=input_operation())
