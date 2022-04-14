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

def count_hex(list_dict):
    arr_list_hex = [int(''.join(x), 16) for x in list_dict.values()]
    sum_hex = list(hex(sum(arr_list_hex)))[2:]
    multi_hex = list(hex(reduce(lambda x, y: x * y, arr_list_hex)))[2:]

    print('Сумма чисел: ', sum_hex) #[‘C’, ‘F’, ‘1’]
    print('Произведение чисел: ', multi_hex) #[‘7’, ‘C’, ‘9’, ‘F’, ‘E’]

list_hex = defaultdict(dict)
number_1 = input("Введите первое hex число: ")
list_hex[number_1] = list(number_1)
print(list_hex[number_1])

number_2 = input("Введите второе hex число: ")
list_hex[number_2] = list(number_2)
print(list_hex[number_2])

count_hex(list_hex)

#---------------
class hex_number:
    def __init__(self, a):
        self.a = list(a)

    def __add__(self, other):
        return list(hex(int(''.join(self.a), 16) + int(''.join(other.a), 16)))[2:]

    def __mul__(self, other):
        return list(hex(int(''.join(self.a), 16) * int(''.join(other.a), 16)))[2:]

hex_num_1 = hex_number(number_1)
hex_num_2 = hex_number(number_2)

print('--------')
print('Сделали через класс:')
print('Сумма чисел: ', hex_num_1 + hex_num_2)
print('Произведение чисел: ', hex_num_1 * hex_num_2)

