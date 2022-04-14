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
def calculator():
    type_operation = input("Input operation (+, -, *, / or 0 for exit)")
    if type_operation == 0:
        return "Exit"
    else:
        if type_operation in "=, -, *, /":
            try:
                num_1 = int(input("Input first number:"))
                num_2 = int(input("Input first number:"))

                if type_operation == "+":
                     res = num_1 + num_2
                     print(f'You result {res}')
                     return calculator()
                elif type_operation == "-":
                    res = num_1 - num_2
                    print(f'You result {res}')
                    return calculator()
                elif type_operation == "*":
                    res = num_1 * num_2
                    print(f'You result {res}')
                    return calculator()
                elif type_operation == "/":
                    try:
                        res = num_1 / num_2
                    except ZeroDivisionError:
                        print("Not null")
                    else:
                        print(f'You result {res}')
                    finally:
                        return calculator()
            except ValueError:
                print("You input string")
                return calculator()
        else:
            print("You input error symbol")
