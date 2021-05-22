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
    user_input = input('Какую операцию будем выполнять? ("+", "-", "/", "*", а так же "0" для выхода)')
    if user_input == '0':
        return 'Вы выбрали выход'
    else:
        if user_input in '+-/*':
            try:
                first = int(input('Введите первое значение: '))
                second = int(input('Введите второе значение: '))

                if user_input == '+':
                    result = first + second
                    print(f'Ваш результат: {result}')
                    return calculator()

                elif user_input == '-':
                    result = first - second
                    print(f'Ваш результат: {result}')
                    return calculator()

                elif user_input == '/':
                    try:
                        result = first / second
                    except ZeroDivisionError:
                        print('На ноль делить нельзя!!')
                    else:
                        print(f'Ваш результат: {result}')
                    finally:
                        return calculator()

                elif user_input == '*':
                    result = first * second
                    print(f'Ваш результат: {result}')
                    return calculator()

            except Exception:
                print('Упс ошибка')
        else:
            print('Введите значение из предложенного!')
            return calculator()


calculator()







