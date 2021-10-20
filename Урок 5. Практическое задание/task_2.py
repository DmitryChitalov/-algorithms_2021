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

# 1 вариант defaultdict
from collections import defaultdict, deque
from functools import reduce

num_dict = defaultdict(list)
num_dict[1] = list(input().upper())
num_dict[2] = list(input().upper())

add_nums = reduce(lambda x, y,: int(''.join(x), 16) + int(''.join(y), 16), [num_dict[1], num_dict[2]])
mul_nums = reduce(lambda x, y,: int(''.join(x), 16) * int(''.join(y), 16), [num_dict[1], num_dict[2]])

print(f'Сумма чисел из примера: {list(hex(add_nums)[2:].upper())}')
print(f'Произведение - {list(hex(mul_nums)[2:].upper())}')


# 2 варианты deque
num_1 = deque('a2'.upper())
num_2 = deque('c4f'.upper())

add_nums_2 = reduce(lambda x, y,: int(''.join(x), 16) + int(''.join(y), 16), [num_1, num_2])
mul_nums_2 = reduce(lambda x, y,: int(''.join(x), 16) * int(''.join(y), 16), [num_1, num_2])

print(f'Сумма чисел из примера: {deque(hex(add_nums_2)[2:].upper())}')
print(f'Произведение - {deque(hex(mul_nums_2)[2:].upper())}')


# 3 варианты ООП(перезагрузка методов)
class HexNumber:
    def __init__(self, num):
        self.num = int(num.upper(), 16)

    def __add__(self, other):
        add_nums = self.num + other.num
        return list(hex(add_nums)[2:].upper())

    def __mul__(self, other):
        add_nums = self.num * other.num
        return list(hex(add_nums)[2:].upper())

hx1 = HexNumber('A2')
hx2 = HexNumber('C4F')
print(hx1 + hx2)
print(hx1 * hx2)