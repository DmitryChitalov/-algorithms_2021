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


# Решение через рекурсию:
def calc():
    operators = ['+', '-', '*', '/']
    operator = input('Выберите арифметическое действие.\nДля выхода из программы введите "0": ')
    if operator != '0':  # шаг рекурсии
        if operator in operators:
            try:
                operand_one = float(input('Введите первое число: '))
                operand_two = float(input('Введите второе число: '))
                if operator == '+':
                    print(f'{operand_one} {operator} {operand_two} = {round(operand_one + operand_two, 3)}')
                elif operator == '-':
                    print(f'{operand_one} {operator} {operand_two} = {round(operand_one - operand_two, 3)}')
                elif operator == '*':
                    print(f'{operand_one} {operator} {operand_two} = {round(operand_one * operand_two, 3)}')
                else:
                    print(f'{operand_one} {operator} {operand_two} = {round(operand_one / operand_two, 3)}')
            except ZeroDivisionError:
                print('На ноль делить нельзя!')
            except ValueError:
                print('Число введено неправильно!')
        else:
            print(f'{operator} не является арифметическим действием.\nПопробуйте еще раз:')
        calc()
    else:
        print('Завершение работы')  # базовый случай


calc()

"""
#Решение с помощью цикла

operators = ['+', '-', '*', '/']
operator = ''
while operator != 0:
    operator = input('Выберите арифметическое действие.\nДля выхода из программы введите "0": ')
    if operator in operators:
        try:
            operand_one = float(input('Введите первое число: '))
            operand_two = float(input('Введите второе число: '))
            if operator == '+':
                print(f'{operand_one} {operator} {operand_two} = {round(operand_one + operand_two, 3)}')
            elif operator == '-':
                print(f'{operand_one} {operator} {operand_two} = {round(operand_one - operand_two, 3)}')
            elif operator == '*':
                print(f'{operand_one} {operator} {operand_two} = {round(operand_one * operand_two, 3)}')
            else:
                print(f'{operand_one} {operator} {operand_two} = {round(operand_one / operand_two, 3)}')
        except ZeroDivisionError:
            print('На ноль делить нельзя!')
        except ValueError:
            print('Число введено неправильно!')
    elif operator == '0':
        print('Завершение работы')
        break
    else:
        print(f'{operator} не является арифметическим действием.\nПопробуйте еще раз:')
"""
