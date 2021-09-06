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


a = 'A2'
b = 'C4F'
def_dict = defaultdict(list)
def_dict[a] = list(a)
def_dict[b] = list(b)
x = int(''.join((str(i) for i in def_dict[a])), 16) + int(''.join((str(i) for i in def_dict[b])), 16)
y = int(''.join((str(i) for i in def_dict[a])), 16) * int(''.join((str(i) for i in def_dict[b])), 16)
def_dict['sum'] = list(hex(x).upper())[2:]
def_dict['mul'] = list(hex(y).upper())[2:]
print(def_dict)


class HexNumber:
    def __init__(self, vol):
        self.vol = vol

    def __add__(self, other):
        return hex(int(self.vol, 16) + int(other.vol, 16)).upper()[2:]

    def __mul__(self, other):
        return hex(int(self.vol, 16) * int(other.vol, 16)).upper()[2:]


vol_1 = HexNumber('A2')
vol_2 = HexNumber('C4F')
print(f'sum = {vol_1 + vol_2}')
print(f'mul = {vol_1 * vol_2}')
