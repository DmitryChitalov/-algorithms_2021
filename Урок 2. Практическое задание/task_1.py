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

def calculation():
    operation = input("Input your operation>>> ")
    if operation == "0":

        return "--- Stop Calculations ---"
    try:
        a = int(input("Input first number>>> "))
    except ValueError:
        print("String is not allowed, only numbers are required. Fix it!!!")
        return calculation()
    try:
        b = int(input("Input second number>>> "))
    except ValueError:
        print("String is not allowed, only numbers are required. Fix it!!!")
        return calculation()
    if b == 0 and operation == "/":
        print("b == 0 => Operation is impossible, Fix it!!!")
        return calculation()
    operations = ['+',"-","*","/"]
    if operation in operations:
        do_it = {
            "+": a + b,
            "-": a - b,
            "*": a * b,
            "/": a / b
        }
        print(do_it[operation])

    else:
        print(f"There is not such operation like {operation}, only {operations} are required")

    return calculation()

print(calculation())

