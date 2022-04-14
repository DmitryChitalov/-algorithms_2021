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


class SignError(Exception):
    pass


def calculator():
    try:
        s = str(input("Введите операцию (*, +, -, / или 0 для выхода): "))
        if (s != '*') and (s != '-') and (s != '+') and (s != '/') and (s != '0'):
            raise SignError
    except SignError:
        print("Введена неверная операция, введите снова")
        calculator()
    else:
        if s == '0':
            return
        else:
            try:
                val_1 = int(input("Введите первое число: "))
                val_2 = int(input("Введите второе число: "))
            except ValueError:
                print('Введено не число, повторите ввод')
                calculator()
            else:
                if s == '+':
                    print('Результат: ', val_1 + val_2)
                    calculator()
                elif s == '-':
                    print('Результат: ', val_1 - val_2)
                    calculator()
                elif s == '*':
                    print('Результат: ', val_1 * val_2)
                    calculator()
                else:
                    try:
                        print('Результат: ', val_1 / val_2)
                    except ZeroDivisionError:
                        print('Невозможно деление на нуль')
                        calculator()
                    calculator()


calculator()
