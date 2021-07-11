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


def check_input(input_string, is_operation=False):
    if input_string == "0" and is_operation:
        exit()
    elif input_string == "+" or input_string == "-" or input_string == "*" or input_string == "/":
        return True if is_operation else False
    elif input_string.isdigit():
        return True if is_operation is False else False
    else:
        print("Вы ввели что-то не то!\n")
        return False


def calc(operation, first_number, second_number):
    if operation == "+":
        return first_number + second_number
    elif operation == "-":
        return first_number - second_number
    elif operation == "*":
        return first_number * second_number
    elif operation == "/":
        #  Skip ZeroDivisionError.
        if second_number != 0:
            return first_number / second_number
        else:
            return 0


def main_calc():
    operation = (input("Введите операцию (+, -, *, / или 0 для выхода): \n")).lower()
    if check_input(operation, True):
        first_number = input("Введите первое число: \n")
        if check_input(first_number):
            first_number = int(first_number)
            second_number = input("Введите второе число: \n")
            if check_input(second_number):
                second_number = int(second_number)

                print(f"{first_number} {operation} {second_number} = {calc(operation, first_number, second_number)};\n")
                return main_calc()

            else:
                return main_calc()
        else:
            return main_calc()
    else:
        return main_calc()


main_calc()
