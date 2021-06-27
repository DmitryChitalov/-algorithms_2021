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
    operator = input("Enter an operation sign (+, -, /, *) or 0 to exit: ")
    if operator == '0':
        return f"Exiting"
    else:
        if operator in '+-/*':
            try:
                _f_num = float(input("Enter first number: "))
                _s_num = float(input("Enter second number: "))
            except ValueError:
                print("Please, enter the numbers!")
                return calculator()
            try:
                _f_num / _s_num
            except ZeroDivisionError:
                print("Fatal error! Division by 0 is prohibited")
                return calculator()
            else:
                if operator == '+':
                    print(f"Result: ", _f_num + _s_num)
                elif operator == '-':
                    print(f"Result: ", _f_num - _s_num)
                elif operator == '*':
                    print(f"Result: ", _f_num * _s_num)
                else:
                    print(f"Result: ", _f_num / _s_num)
        else:
            print("The sign was entered incorrectly. Try again")

    return calculator()


if __name__ == '__main__':
    calculator()
