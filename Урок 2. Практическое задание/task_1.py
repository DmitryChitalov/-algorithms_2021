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

""" Оставила в файле решение с циклом для себя. """


def calculator():
    while True:
        action = input('Введите операцию (+, -, *, / или 0 для выхода): ')
        action_list = ['+', '-', '*', '/']
        if action not in action_list:
            print('Введена некорректная операция')
            continue
        else:
            try:
                operand_1 = int(input('Введите первое число: '))
                operand_2 = int(input('Введите второе число: '))
            except ValueError:
                print('Операнды должны быть числами')
            else:
                if action == '0':
                    print('Работа с калькулятором завершена!')
                    break
                elif action == '+':
                    print('Ваш результат: ', operand_1 + operand_2)
                elif action == '-':
                    print('Ваш результат: ', operand_1 - operand_2)
                elif action == '*':
                    print('Ваш результат: ', operand_1 * operand_2)
                elif action == '/':
                    try:
                        result = operand_1 / operand_2
                    except ZeroDivisionError:
                        print('Деление на ноль недопустимо!')
                    else:
                        print('Ваш результат: ', result)


def calculator_recurs():
    action = input('Введите операцию (+, -, *, / или 0 для выхода): ')
    if action == '0':
        print('Работа с калькулятором завершена!')
    else:
        action_list = ['+', '-', '*', '/']
        if action not in action_list:
            print('Введена некорректная операция')
            return calculator_recurs()
        else:
            try:
                operand_1 = int(input('Введите первое число: '))
                operand_2 = int(input('Введите второе число: '))
            except ValueError:
                print('Операнды должны быть числами')
                return calculator_recurs()
            else:
                if action == '+':
                    print('Ваш результат: ', operand_1 + operand_2)
                    return calculator_recurs()
                elif action == '-':
                    print('Ваш результат: ', operand_1 - operand_2)
                    return calculator_recurs()
                elif action == '*':
                    print('Ваш результат: ', operand_1 * operand_2)
                    return calculator_recurs()
                elif action == '/':
                    try:
                        result = operand_1 / operand_2
                    except ZeroDivisionError:
                        print('Деление на ноль недопустимо!')
                        return calculator_recurs()
                    else:
                        print('Ваш результат: ', result)
                        return calculator_recurs()


# calculator()
calculator_recurs()
