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

dic = defaultdict(list)
first = input('Enter the first number: ')
second = input('Enter the second number: ')

dic[first] = list(first)
dic[second] = list(second)


def hex_calc(first, second):
    res_summ = hex(int(first, 16) + int(second, 16)).replace('0x', '').upper()
    res_prod = hex(int(first, 16) * int(second, 16)).replace('0x', '').upper()
    dic[res_summ] = list(res_summ)
    dic[res_prod] = list(res_prod)
    return f'The sum of the numbers: {dic[res_summ]}\nThe product of the numbers: {dic[res_prod]}'


print(reduce(hex_calc, [first, second]))


class HexNumber:
    def __init__(self, value):
        self.value = int(value, 16)

    def __add__(self, other):
        return hex(self.value + other.value).replace('0x', '').upper()

    def __mul__(self, other):
        return hex(self.value * other.value).replace('0x', '').upper()


a = HexNumber(first)
b = HexNumber(second)

print(f'The sum of the numbers: {a + b}\nThe product of the numbers: {a * b}')
