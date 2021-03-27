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


def my_calculator():
    act = input("введите: + - * / или 0 для выхода: ")
    if act == "0":
        print("досвидания")
        return "выход"
    else:
        try:
            num_1 = int(input("введите первое число: "))
            num_2 = int(input("введите второе число: "))
            if act == "+":
                result = num_1 + num_2
                print(num_1, " + ", num_2, "= ", result)
                return my_calculator()
            elif act == "-":
                result = num_1 - num_2
                print(num_1, " - ", num_2, "= ", result)
                return my_calculator()
            elif act == "*":
                result = num_1 + num_2
                print(num_1, " * ", num_2, "= ", result)
                return my_calculator()
            elif act == "/" and num_2 != 0 and num_1 != 0:
                result = num_1 / num_2
                print(num_1, " / ", num_2, "= ", result)
                return my_calculator()
            else:
                print("выбрана недопустимая операция с числами")
                return my_calculator()
        except ValueError:
            print("неверно заданное число")
            return my_calculator()


my_calculator()
