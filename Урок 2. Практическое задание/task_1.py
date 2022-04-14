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

while True:
    s = input("Введите операцию (+, -, *, / или 0 для выхода):")
    if s == '0':
        break
    if s in ('+', '-', '*', '/'):
        try:
            x = float(input("x="))
            y = float(input("y="))
            if s == '+':
                print("%.2f" % (x+y))
            elif s == '-':
                print("%.2f" % (x-y))
            elif s == '*':
                print("%.2f" % (x*y))
            elif s == '/':
                if y != 0:
                    print("%.2f" % (x/y))
                else:
                    print("Деление на ноль!")
        except ValueError:
            print('Вы вместо числа ввели строку. Исправьтесь')
            continue
    else:
        print("Неверный знак операции!")