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


# Решение с помощью ООП:
class HexNumber:
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return str(self.val)[2:]

    def __add__(self, other):
        return HexNumber(hex(int(self.val, 16) + int(other.val, 16)))

    def __mul__(self, other):
        return HexNumber(hex(int(self.val, 16) * int(other.val, 16)))


num_1 = HexNumber(input("Введите 1-е шестнадцатиричное число: "))
num_2 = HexNumber(input("Введите 2-е шестнадцатиричное число: "))
print(f'Сумма чисел из примера: {list(str(num_1 + num_2).upper())}')
print(f'Произведение - {list(str(num_1 * num_2).upper())}')

# Решение с помощью коллекций:
from collections import defaultdict


def hexsumm(dic):
    res = 0
    for key in dic.keys():
        res += int(key, 16)
    return hex(res)[2:]


def hexmul(dic):
    res = 1
    for key in dic.keys():
        res *= int(key, 16)
    return hex(res)[2:]


num_1 = input("Введите 1-е шестнадцатиричное число: ")
num_2 = input("Введите 2-е шестнадцатиричное число: ")
nums = defaultdict(list)
nums[num_1] = list(num_1)
nums[num_2] = list(num_2)
print(f'Сумма чисел из примера: {list(hexsumm(nums).upper())}')
print(f'Произведение - {list(hexmul(nums).upper())}')
