"""
2.*	Написать программу сложения и умножения двух шестнадцатеричных чисел.
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
"""

from collections import defaultdict
from functools import reduce

dict_list = defaultdict(list)


def add_num(i, num, dct):
    for let in num:
        dct[i].append(let)


def concat(first, second):
    return first + second


def sum_nums(dct):
    num_1 = reduce(concat, dct[1])
    num_2 = reduce(concat, dct[2])
    result = int(num_1, 16) + int(num_2, 16)
    return hex(result)[2:]


def mul_nums(dct):
    num_1 = reduce(concat, dct[1])
    num_2 = reduce(concat, dct[2])
    result = int(num_1, 16) * int(num_2, 16)
    return hex(result)[2:]    


print('Программа для умножения и сложения двух шеснадцетиричных чисел.')
num_16 = input('Ведите первое число: ')
add_num(1, num_16, dict_list)
num_16 = input('Ведите второе число: ')
add_num(2, num_16, dict_list)

sum_n = sum_nums(dict_list)
add_num('sum_n', sum_n, dict_list)
print()
print('Сумма двух шестнадцатеричных чисел:')
print(f'В десятичной системе - {int(sum_n, 16)}')
print(f'В шестнадцатеричной системе - {"0x" + sum_n}')
print(f'Хранится в defaultdict - {dict_list["sum_n"]}')
print()
mul_n = mul_nums(dict_list)
add_num('mul_n', mul_n, dict_list)
print(f'Произведение двух шестнадцатеричных чисел:')
print(f'В десятичной системе - {int(mul_n, 16)}')
print(f'В шестнадцатеричной системе - {"0x" + mul_n}')
print(f'Хранится в defaultdict - {dict_list["mul_n"]}')
print()
print(dict_list)
