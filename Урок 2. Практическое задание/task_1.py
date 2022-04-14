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
    sign = str(input('Введите операцию: +, -, *, / или 0 для выхода: '))
    if sign == '0':
        return f'Выходим из приложения'
    elif sign != '+' and sign != '-' and sign != '*' and sign != '/' and sign != 0:
        print('Веведена неправильная операция')
        return calc()
    try:
        first_num = int(input('Введите первое число: '))
    except ValueError:
        print('Необходимо ввести число')
        return calc()
    try:
        second_num = int(input('Введите второе число: '))
    except ValueError:
        print('Необходимо ввести число')
        return calc()
    if sign == '/' and second_num == 0:
        print('На ноль делить нельзя')
        return calc()
    if sign == '+':
        print(first_num.__add__(second_num))
        return calc()
    if sign == '-':
        print(first_num.__sub__(second_num))
        return calc()
    if sign == '*':
        print(first_num.__mul__(second_num))
        return calc()
    if sign == '/':
        print(first_num.__truediv__(second_num))
        return calc()


print(calc())
