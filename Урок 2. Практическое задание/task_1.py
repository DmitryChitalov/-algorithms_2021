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


def calculate():
    operation = input('Введите операцию (+, -, *, / или 0 для выхода): ')
    if operation == '0':  # базовый случай, выход из рекурсии
        return print('Вы вышли из калькулятора')
    if operation not in ['-', '*', '+', '/', '0']:  # Проверка на ввод оператора
        return print('Не верный оператор'), calculate()
    try:  # Проверка на ввод числовых значений
        value1 = int(input('Введите первое число: '))
        value2 = int(input('Введите второе число: '))
    except ValueError:
        return print('Ошибка, необходимо ввести числа'), calculate()

    if operation == '+':
        return print(f'Ваш результат = {value1 + value2}'), calculate()
    elif operation == '-':
        return print(f'Ваш результат = {value1 - value2}'), calculate()
    elif operation == '*':
        return print(f'Ваш результат = {value1 * value2}'), calculate()
    elif operation == '/':
        try:  # Проверка деления на ноль
            return print(f'Ваш результат = {value1 / value2}'), calculate()
        except ZeroDivisionError:
            return print('Ошибка, нельзя делить на ноль'), calculate()


calculate()
