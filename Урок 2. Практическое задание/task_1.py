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


def arithmetic_operation():
    operation = input('Please enter operation +, -, *, / or 0 - for out: ')
    if operation not in '+-*/0':
        print('operation error')
        return arithmetic_operation()
    elif operation == '0':
        return 'by'
    number_1 = input('Please enter number one: ')
    number_2 = input('Please enter number two: ')
    try:
        if number_1.replace('.', '').isdigit() == False or number_2.replace('.', '').isdigit() == False:
            print('you entered not a number')
            return arithmetic_operation()
        if operation == '+':
            result = float(number_1) + float(number_2)
            print(result)
            return arithmetic_operation()
        elif operation == '-':
            result = float(number_1) - float(number_2)
            print(f'{result}')
            return arithmetic_operation()
        elif operation == '*':
            result = float(number_1) * float(number_2)
            print(result)
            return arithmetic_operation()
        else:
            result = float(number_1) / float(number_2)
            print(round(result, 3))
            return arithmetic_operation()
    except ZeroDivisionError:
        print('you divide by zero')
        return arithmetic_operation()


if __name__ == '__main__':
    arithmetic_operation()