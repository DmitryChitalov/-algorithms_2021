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

""" 
Домашнее задание к уроку №2. Алгоритмы и структуры данных на Python.
Студент: Максим Сапунов. Jenny6199@yandex.ru 04.06.2021
"""


class Calculator:
    """ Учебное представление калькулятора """

    operand_list = ['+', '-', '*', '/']
    flag = True

    def __init__(self):
        """ Конструктор класса."""
        self.input_log = []
        self.calculate_log = []
        self.formula = ''
        self.digit_1 = None
        self.digit_2 = None
        self.operator = None
        print('Запущена программа - калькулятор v.01 от 05.06.2021.')

    def insert_operator(self):
        """ Пользователь вводит оператор."""
        while self.flag:
            operator = input('Выберете операцию +, -, *, / и нажмите Enter:')
            self.input_log.append(operator)
            if operator in self.operand_list:
                return operator
            elif operator == 'q' or operator == 'Q':
                print('\033[031mОперация прервана пользователем.\033[0m')
                self.flag = False
                break
            else:
                print('\033[031m  Ошибка! Неверный ввод.\033[0m')
                print('\033[96m  Попробуйте еще раз, можно вводить операторы +. -. *. /\033[0m')

    def insert_digit(self):
        """ Пользователь вводит число."""
        digit = None
        while self.flag and type(digit) != float:
            digit = input('Введите число и нажмите Enter: ')
            if digit == 'q' or digit == 'Q':
                self.flag = False
                break
            try:
                digit = float(digit)
            except ValueError:
                print('\033[031m  Ошибка! Вы ввели не число.\033[0m')
                print('\033[96m  Попробуйте еще раз - можно вводить целые и дробные числа:\033[0m')
        return digit

    def show_input_log(self):
        """ Просмотр журнала ввода данных пользователем."""
        print('Input log:')
        for el in self.input_log:
            print(el)

    def get_result(self):
        """ Подсчет финального результата."""
        if self.flag:
            if self.operator == '+':
                return self.digit_1 + self.digit_2
            elif self.operator == '-':
                return self.digit_1 - self.digit_2
            elif self.operator == '/':
                try:
                    result = self.digit_1 / self.digit_2
                    return result
                except ZeroDivisionError:
                    print('\033[031m Ошибка! Делить на ноль нельзя!\033[0m')
            elif self.operator == '*':
                return self.digit_1 * self.digit_2
        else:
            return str('Программа завершает работу по запросу пользователя.')

    def create_formula(self):
        """ Конкатенация формулы из введенных пользователем значений. """
        if self.flag:
            print(f'Выполняется расчет: {self.digit_1} {self.operator} {self.digit_2} :')

    def new_calculate(self):
        """ Запуск расчета."""
        self.digit_1 = self.insert_digit()
        self.operator = self.insert_operator()
        self.digit_2 = self.insert_digit()
        self.create_formula()
        print(self.get_result())
        if self.flag:                   # Здесь реализован рекурсивный запуск функции.
            print('Новый расчет:')
            self.new_calculate()


if __name__ == '__main__':
    v1 = Calculator()
    v1.new_calculate()

    # v1.show_input_log()
