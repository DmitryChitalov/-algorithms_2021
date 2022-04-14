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

my_dct = defaultdict(int)

hex_1 = 'A2'
hex_2 = 'C4F'
my_dct['num_1'] = list(hex_1)
my_dct['num_2'] = list(hex_2)
my_dct['sum'] = list(hex(int(hex_1, 16) + int(hex_2, 16)).strip('0x').upper())
my_dct['mul'] = list(hex(int(hex_1, 16) * int(hex_2, 16)).strip('0x').upper())
print('Решение через defaultdict')
print(f'Сложение: {my_dct["sum"]}')
print(f'Умножение: {my_dct["mul"]}')

"""
Решение с ООП
"""


class HexNum:
    def __init__(self, number):
        self.number = ''.join(number)

    def __add__(self, other):
        return list(f'{(int(self.number, 16) + int(other.number, 16)):X}')

    def __mul__(self, other):
        return list(f'{(int(self.number, 16) * int(other.number, 16)):X}')


hex_1 = HexNum(list(hex_1))
hex_2 = HexNum(list(hex_2))
print('Решение через ООП')
print(f'Сложение: {hex_1 + hex_2}')
print(f'Умножение: {hex_1 * hex_2}')

