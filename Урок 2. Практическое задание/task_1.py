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

operation = {"+": (lambda x, y: x + y),
             "-": (lambda x, y: x - y),
             "*": (lambda x, y: x * y),
             "/": (lambda x, y: x / y)}


class User_raise(Exception):
    def __init__(self, text):
        self.text = text


def calculator():
    try:
        op = input("Введите операцию (+, -, *, / или 0 для выхода): ")
        if op not in ["+", "-", "*", "/", "0"]:
            raise User_raise("Вы ввели неправильную операцию!")
    except User_raise as err:
        print(err)
        return calculator()
    else:
        if op != "0":
            try:
                val_1 = int(input("Введите первое трехзначное число: "))
                val_2 = int(input("Введите второе трехзначное число: "))
                if op == "/" and val_2 == 0:
                    raise User_raise("Делить на 0 нельзя!")
            except User_raise as err:
                print(err)
                return calculator()
            except ValueError:
                print("Вы вместо трехзначного числа ввели строку (((. Исправьтесь")
                return calculator()
            else:
                print(f"Ваш результат: {operation[op](val_1, val_2)}")
                return calculator()
        else:
            return "Пока!"


print(calculator())
