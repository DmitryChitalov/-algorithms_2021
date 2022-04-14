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


# 1
def counting(n):
    listed = defaultdict(dict)
    for i in range(n):
        number = input("Введите чило: ")
        listed[number] = list(number)
    arr = [int(''.join(x), 16) for x in listed.values()]
    summa = list(hex(sum(arr)))[2:]
    multi = list(hex(reduce(lambda x, y: x * y, arr)))[2:]
    return f"""Сохраняю: {[x for x in listed.values()]}
Сумма из примера: {summa}
Произведение: {multi}
"""


print(counting(2))


# 2
class HexNumber:
    def __init__(self, a):
        self.a = list(a)

    def __add__(self, other):
        return list(hex(int(''.join(self.a), 16) + int(''.join(other.a), 16)))[2:]

    def __mul__(self, other):
        return list(hex(int(''.join(self.a), 16) * int(''.join(other.a), 16)))[2:]


hx = HexNumber("A")
hy = HexNumber("A")
print(hx + hy)
print(hx * hy)
