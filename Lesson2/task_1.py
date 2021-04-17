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


def math():

    operation = input('\nPlease enter symbol for choosing math operation:\n+ — addition;\n- — subtraction;'
                      '\n* — multiplication;\n/ — division;\n0 — quit from program.\n')

    if operation == '0':
        print('End of calculation.')
        return

    if operation in ['+', '-', '*', '/']:
        try:
            first = input('Enter the first number:')
            if not (first.isnumeric() or (first[1:].isnumeric() and first[0] == '-')):
                raise ValueError

            second = input('Enter the second number:')
            if not (second.isnumeric() or (second[1:].isnumeric() and second[0] == '-')):
                raise ValueError

            result = eval(f'{first}{operation}{second}')

            if int(first) % int(second) != 0 and operation == '/':
                print(f'{first} {operation} {second} = {result:.3f}')

            else:
                print(f'{first} {operation} {second} = {result:.0f}')

        except ZeroDivisionError:
            print('Division by zero, please try again!')
        except ValueError:
            print('Please enter integer numbers!')

    else:
        print('Incorrect operation!')
    math()


math()
