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


def calc():
    operand = input('Введите операцию (+, -, *, / или 0 для выхода): ')
    if operand == "0":
        return print(f'Программа завершена')
    elif operand not in ('+', '-', '*', '/'):
        print(f'Вы ввели неверный операнд!')
        return calc()
    else:
        first_num = input('Введите первое число: ')
        if not first_num.isdigit():
            print(f'Вы ввели не численное значение!')
            return calc()
        second_num = input('Введите второе число: ')
        if not second_num.isdigit():
            print(f'Вы ввели не численное значение!')
            return calc()
        first_num = int(first_num)
        second_num = int(second_num)
        if operand == '+':
            print(second_num + first_num)
            return calc()
        elif operand == '-':
            print(first_num - second_num)
            return calc()
        elif operand == '*':
            print(first_num * second_num)
            return calc()
        elif operand == '/' and second_num != 0:
            print(first_num / second_num)
            return calc()
        else:
            print('На ноль делить нельзя')
            return calc()


calc()
