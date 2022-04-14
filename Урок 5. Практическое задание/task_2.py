"""
2. Написать программу сложения и умножения двух шестнадцатиричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)

__mul__
__add__

Пример:
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’]
Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

1. вариант
defaultdict(list)
int(, 16)
reduce

2. вариант
class HexNumber:
    __add__
    __mul__

hx = HexNumber
hx + hx
hex()
"""

from collections import defaultdict
from functools import reduce

# Вариант 1 - с использованием коллекции defaultdict из модуля collections.
# Наверное, не самый красивый код, зато мой собственный от и до, к тому же отлично работает.

hex_num_list = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
hex_num_dict = {x: y for x,y in zip(hex_num_list, list(range(len(hex_num_list))))}
print(hex_num_dict)

print('Вариант 1 - с использованием коллекции defaultdict из модуля collections:')

hex_num1 = list(input('введите первое шестнадцатиричное число: '))
hex_num2 = list(input('введите второе шестнадцатиричное число: '))

def get_hex_nums_prepared(hex_num1, hex_num2):
    d1 = defaultdict(int)  # когда прописывала list, class у defaultdict был list,
    # и значение по умолчанию присваивалось [] - пустой список, а не ноль!!!!!!
    # попробовала d1 = defaultdict(int) вместо d = defaultdict(list), и все получилось.
    d2 = defaultdict(int)
    max_len = (len(hex_num1) if len(hex_num1) >= len(hex_num2) else len(hex_num2))
    hex_num1 = hex_num1[::-1]
    hex_num2 = hex_num2[::-1]
    for i in range(max_len):
        if i >= len(hex_num1):
            d1[i]
            d2[i] = int(hex_num_dict[hex_num2[i]])
        elif i >= len(hex_num2):
            d2[i]
            d1[i] = int(hex_num_dict[hex_num1[i]])
        else:
            d1[i] = hex_num_dict[hex_num1[i]]
            d2[i] = hex_num_dict[hex_num2[i]]
    return d1, d2, max_len
print(get_hex_nums_prepared(hex_num1, hex_num2))


def get_hex_nums_sum_1(hex_num1, hex_num2):
    d1, d2, max_len = get_hex_nums_prepared(hex_num1, hex_num2)
    new_num = 0
    for i in range(0, max_len):
        new_num += (d1[i] + d2[i]) * (16 ** i)
    return f'Сумма двух шестнадцатеричных чисел: {list(str(hex(new_num))[2::].upper())}'

print(get_hex_nums_sum_1(hex_num1, hex_num2))


def get_hex_nums_product(hex_num1, hex_num2):
    d1, d2, max_len = get_hex_nums_prepared(hex_num1, hex_num2)
    decimal_num1 = 0
    decimal_num2 = 0
    for i in range(0, max_len):
        decimal_num1 += d1[i] * (16 ** i)
        decimal_num2 += d2[i] * (16 ** i)
    print(decimal_num2 * decimal_num1)
    return f'Произведение двух шестнадцатеричных чисел: {list(str(hex(decimal_num1 * decimal_num2))[2::].upper())}'

print(get_hex_nums_product(hex_num1, hex_num2))

# Вариант 2:
class HexNumber:
    def __init__(self, hex_num):
        self.hex_num = hex_num

    def __add__(self, other):
        new_hex_num1 = list(str(hex(int(self.hex_num, 16) + int(other.hex_num, 16)))[2:].upper())
        return f'Сумма двух шестнадцатеричных чисел: {new_hex_num1}'

    def __mul__(self, other):
        new_hex_num2 = list(str(hex(int(self.hex_num, 16) * int(other.hex_num, 16)))[2:].upper())
        return f'Произведение двух шестнадцатеричных чисел: {new_hex_num2}'


print('Вариант 2  - ООП:')
hex_num_1 = HexNumber(input('введите первое шестнадцатиричное число: '))
hex_num_2 = HexNumber(input('введите второе шестнадцатиричное число: '))
print(hex_num_1 + hex_num_2)
print(hex_num_1 * hex_num_2)
print()


# вариант 3

def sum_hex_nums(hex_num1, hex_num2):
    hex_num1 = hex_num1[::-1]
    hex_num2 = hex_num2[::-1]
    new_num = 0
    max_len = (len(hex_num1) if len(hex_num1) > len(hex_num2) else len(hex_num2))
    for i in range(0, max_len):
        if i >= len(hex_num1):
            new_num += (int(hex_num2[i], 16)) * (16 ** i)
        elif i >= len(hex_num2):
            new_num += (int(hex_num1[i], 16)) * (16 ** i)
        else:
            new_num += (int(hex_num1[i], 16) + int(hex_num2[i], 16)) * (16 ** i)
    return f'Сумма двух шестнадцатеричных чисел: {list(str(hex(new_num))[2::].upper())}'


def prod_hex_nums(hex_num1, hex_num2):
    hex_num1 = hex_num1[::-1]
    hex_num2 = hex_num2[::-1]
    decimal_num1 = 0
    decimal_num2 = 0
    max_len = (len(hex_num1) if len(hex_num1) >= len(hex_num2) else len(hex_num2))
    for i in range(0, max_len):
        if i >= len(hex_num1):
            decimal_num2 += (int(hex_num2[i], 16)) * (16 ** i)
            decimal_num1 += 0
        elif i >= len(hex_num2):
            decimal_num1 += (int(hex_num1[i], 16)) * (16 ** i)
            decimal_num2 += 0
        else:
            decimal_num1 += (int(hex_num1[i], base=16)) * (16 ** i)
            decimal_num2 += (int(hex_num2[i], base=16)) * (16 ** i)
    # print(decimal_num1, decimal_num2)
    return f'Произведение двух шестнадцатеричных чисел: {list(str(hex(decimal_num1 * decimal_num2))[2::].upper())}'


print('Вариант 3 - функции без использования коллекций и ООП:')
hex_num3 = list(input('введите первое шестнадцатиричное число: '))
hex_num4 = list(input('введите второе шестнадцатиричное число: '))

print(sum_hex_nums(hex_num3, hex_num4))
print(prod_hex_nums(hex_num3, hex_num4))
