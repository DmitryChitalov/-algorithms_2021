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

PERM_OP = ('+', '-', '*', '/')


def rec_calc(result=None):
    if result:
        print(f"Результат вычислений: {int(result) if result % 1 == 0 else result}")
    op = input('Введите операцию (+, -, *, / или 0 для выхода): ')
    if op in PERM_OP:
        try:
            first_n, second_n = float(input('Введите первое число: ')), float(input('Введите второе число: '))
        except ValueError:
            print('Необходимо вводить только числа!')
            rec_calc()
        else:
            if op == '+':
                rec_calc(first_n + second_n)
            elif op == '-':
                rec_calc(first_n - second_n)
            elif op == '*':
                rec_calc(first_n * second_n)
            elif op == '/':
                try:
                    rec_calc(first_n / second_n)
                except ZeroDivisionError:
                    print('Делить на ноль нельзя!')
                rec_calc()
    elif op == '0':
        print('Программа завершена!')
    else:
        rec_calc()


rec_calc()
