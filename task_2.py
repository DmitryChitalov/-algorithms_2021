"""
2. Написать программу сложения и умножения двух шестнадцатиричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

# решение задачи через defaultdict из модуля collections
from collections import defaultdict
from functools import reduce


def hex_num():
    hex_numbers = defaultdict(list)
    for i in range(2):
        number = input(f'Введите число {i + 1} в шестнадцатеричном формате: ').upper()
        if number_check(number):
            hex_numbers[number] = list(number)
        else:
            hex_numbers[number].append('0')
    return hex_numbers


def number_check(num):
    try:
        int(num, 16)
        return True
    except ValueError:
        print('Некорректный ввод числа! Будем считать, что вы ввели "0"')
        return False


def hex_add(num_1, num_2):
    return list(hex(num_1 + num_2)[2:].upper())


def hex_mul(num_1, num_2):
    return list(hex(num_1 * num_2)[2:].upper())


numbers = hex_num()
print('Сложение', reduce(hex_add, [int(''.join(value), 16) for value in numbers.values()]))
print('Умножение', reduce(hex_mul, [int(''.join(value), 16) for value in numbers.values()]))


# через ООП


class HexNumber:
    def __init__(self, number):
        self.number = self.number_check(number)

    def number_check(self, number):
        try:
            int(number, 16)
            return number
        except ValueError:
            print('Некорректный ввод числа! Будем считать, что вы ввели "0"')
            return '0'

    def __mul__(self, other):
        try:
            return hex(int(self.number, 16) * int(other.number_1, 16)).upper()[2:]
        except TypeError:
            print('Ошибка вычисления')
            return None

    def __add__(self, other):
        try:
            return hex(int(self.number, 16) + int(other.number_1, 16)).upper()[2:]
        except TypeError:
            print('Ошибка вычисления')
            return None


firs_num = HexNumber(input('Введите число в шестнадцатеричном формате: '))
second_num = HexNumber(input('Введите число в шестнадцатеричном формате: '))

# print(second_num.number_1)
print('Сложение', firs_num + second_num)
print('Умножение', firs_num * second_num)
