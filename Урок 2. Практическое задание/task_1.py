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


class MyZeroDivisionError(Exception):
    def __str__(self):
        return "Попытка деления на ноль."


class ActError(Exception):
    def __str__(self):
        return "Необходимо ввести предложенный знак или 0 для выхода."


def my_calc():
    try:
        act = input('Введите операцию (+, -, *, / или 0 для выхода): ')
        if act not in '+-*/0' or len(act) != 1:
            raise ActError
    except ActError as error:
        print(error, 'Ещё попытка.')
        return my_calc()
    if act == '0':
        print('Выход')
        return
    try:
        a = int(input('Введите первое число: '))
        b = int(input('Введите второе число: '))
        if b == 0:
            raise MyZeroDivisionError
    except MyZeroDivisionError as error:
        print(error)
        return my_calc()
    except ValueError:
        print('Необходимо ввести число. Попробуйте ещё раз.')
        return my_calc()
    if act == '+':
        print(f'{a} {act} {b} = {a + b}')
    elif act == '-':
        print(f'{a} {act} {b} = {a - b}')
    elif act == '*':
        print(f'{a} {act} {b} = {a * b}')
    else:
        print(f'{a} {act} {b} = {a / b}')
    return my_calc()


my_calc()
