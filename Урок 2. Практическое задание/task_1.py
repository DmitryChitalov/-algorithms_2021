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


def addition(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1 - num2


def multiplication(num1, num2):
    return num1 * num2


def division(num1, num2):
    return num1 / num2


class Calculator():
    available_operation = {'+': addition,
                           '-': subtraction,
                           '*': multiplication,
                           '/': division,
                           '0': 'exit'}

    exit_symbol = '0'

    def __init__(self):
        self.num1 = ''
        self.num2 = ''
        self.operator = ''

    @staticmethod
    def num_check(num):
        try:
            int(num)
            return True
        except ValueError:
            return False

    def operator_check(self, operator):
        return operator in self.available_operation

    def get_operation_func(self, operator):
        return self.available_operation[operator]

    def data_input(self):
        while not self.num_check(self.num1):
            num1 = input("Введите первое число: ")
            if self.num_check(num1):
                self.num1 = int(num1)

        while not self.num_check(self.num2):
            num2 = input("Введите второе число: ")
            if self.num_check(num2):
                self.num2 = int(num2)

        while not self.operator_check(self.operator):
            operator = input("Введите операцию (+, -, *, / или 0 для выхода): ")
            if self.operator_check(operator):
                self.operator = operator

    def calculation(self):
        self.data_input()

        if self.operator == self.exit_symbol:
            return
        else:
            func = self.get_operation_func(self.operator)
            try:
                res = func(self.num1, self.num2)
                print(res)
            except ZeroDivisionError:
                print("На ноль делить нельзя")

            self.num1 = ''
            self.num2 = ''
            self.operator = ''
            return self.calculation()


calc = Calculator()
calc.calculation()
