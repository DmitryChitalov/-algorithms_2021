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

# 1. вариант
from collections import deque


def hex_present(a):
    d1 = deque(a)
    print(f'Введенное число: {d1}')
    int_d1 = deque()
    n = 0
    for i in reversed(deque(map(lambda x: int(x, 16), d1))):
        int_d1.appendleft(i * 16 ** n)
        n += 1
    return int_d1


def hex_sum(a, b):
    d1 = hex_present(a)
    d2 = hex_present(b)
    res = deque((hex(sum(d1) + sum(d2)).upper())[2:])
    return f'Сумма: {res}'


def hex_mul(a, b):
    d1 = hex_present(a)
    d2 = hex_present(b)
    res = deque((hex(sum(d1) * sum(d2)).upper())[2:])
    return f'Произведение: {res}'


# 2. вариант
class HexNumber:
    def __init__(self, a):
        self.lst = list(a)

    def __str__(self):
        return f'{self.lst}'

    def int_lst(self):
        d1 = []
        n = 0
        for d in reversed(list(map(lambda x: int(x, 16), self.lst))):
            d1.insert(0, d * 16 ** n)
            n += 1
        return d1

    def __add__(self, other):
        d1 = sum(self.int_lst())
        d2 = sum(other.int_lst())
        res = (hex(d1 + d2).upper())[2:]
        return HexNumber(res)

    def __mul__(self, other):
        d1 = sum(self.int_lst())
        d2 = sum(other.int_lst())
        res = (hex(d1 * d2).upper())[2:]
        return HexNumber(res)


a = input('Введите число: ')
b = input('Введите число: ')
print('Вариант 1:')
print(hex_sum(a, b))
print(hex_mul(a, b))
print('###################################################################\nВариант 2:')
c1 = HexNumber(a)
c2 = HexNumber(b)
c3 = c1 + c2
c4 = c1 * c2
print(f'c1 + c2 = {c1} + {c2} = {c3}, \n c3 -> {type(c3)}')
print(f'c1 * c2 = {c1} * {c2} = {c4}, \n c3 -> {type(c3)}')

# Введите число: A2
# Введите число: C4F
# Вариант 1:
# Введенное число: deque(['A', '2'])
# Введенное число: deque(['C', '4', 'F'])
# Сумма: deque(['C', 'F', '1'])
# Введенное число: deque(['A', '2'])
# Введенное число: deque(['C', '4', 'F'])
# Произведение: deque(['7', 'C', '9', 'F', 'E'])
# ###################################################################
# Вариант 2:
# c1 + c2 = ['A', '2'] + ['C', '4', 'F'] = ['C', 'F', '1'],
#  c3 -> <class '__main__.HexNumber'>
# c1 * c2 = ['A', '2'] * ['C', '4', 'F'] = ['7', 'C', '9', 'F', 'E'],
#  c3 -> <class '__main__.HexNumber'>
