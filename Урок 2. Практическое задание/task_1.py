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


class OwnError (Exception):
    def __init__(self, txt):
        self.txt = txt


def my_calc(num_1, num_2, operation):

    try:
        if operation == '+':
            return num_1+num_2
        elif operation == '-':
            return num_1-num_2
        elif operation == '*':
            return num_1*num_2
        elif operation == '/':
            return num_1/num_2
    except ZeroDivisionError:
        return 'Ошибка деление на ноль!'


def req_calc():
    while True:
        try:
            operation = input("Введите операцию (+, -, *, / или 0 для выхода):")
            if operation not in ['+', '-', '*', '/', '0']:
                raise OwnError("Не знаю такой операции!\n")
            elif operation == '0':
                return 'Было приятно с Вами работать! До свидания!'  # Базовое условие, выходим
            else:
                # Если операция валидна и не было ретурна из-за 0
                user_number = []
                for i in range(1, 3):
                    while True:
                        try:
                            user_number.append(float(input(f"Введите {i}-е число:")))
                            break
                        except ValueError:
                            print('Введено не число!\n')
                # Если числа успешно введены,выводим результат и запускаем себя
                print(f'Результат {my_calc(user_number[0], user_number[1], operation)}')
                req_calc()
                break
        except OwnError as err:
            print(err)


print(req_calc())
