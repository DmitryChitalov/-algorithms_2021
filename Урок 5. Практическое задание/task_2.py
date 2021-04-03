"""
2.*	Написать программу сложения и умножения двух шестнадцатиричных чисел.
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


def hex_oper(x, y):
    def_dict = defaultdict(list)
    for i in x, y:
        def_dict[i] = (list(i))
    return (f'{def_dict[x]} + {def_dict[y]} = {list(hex(int(x, 16) + int(y, 16)).upper())[2:]}\n'
            f'{def_dict[x]} * {def_dict[y]} = {list(hex(int(x, 16) * int(y, 16)).upper())[2:]}')


print(hex_oper('A2', 'C4F'))

"""Может я как-то неправильно понял задание, но не понятно, зачем тут defaultdict"""


class HexNumber:

    def __init__(self, num):
        self.num = num
        self.num_list = list(num)
        self.oper = 0

    def __add__(self, other):
        self.oper = list(hex(int(self.num, 16) + int(other.num, 16)).upper())[2:]
        return self.oper

    def __mul__(self, other):
        self.oper = list(hex(int(self.num, 16) * int(other.num, 16)).upper())[2:]
        return self.oper

    def __str__(self):
        return f'{self.num_list}'


a1 = HexNumber('A2')
a2 = HexNumber('C4F')
print(f'{a1} + {a2} = {a1 + a2}')
print(f'{a1} * {a2} = {a1 * a2}')
