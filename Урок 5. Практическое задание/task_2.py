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

################# класс для hex чисел ###############
class hex_class():
    def __init__(self, hex_val):
        self.__hex_val = hex_val

    def get_val(self):
        return self.__hex_val

    def __add__(self, other):
        return list(hex(int(self.__hex_val, 16) + int(other.get_val(), 16))[2:].upper())

    def __mul__(self, other):
        return list(hex(int(self.__hex_val, 16) * int(other.get_val(), 16))[2:].upper())

################# функции сложениея и умножения ###############
def hex_add(def_dict):
    hex_val = 0
    for i in def_dict:
        hex_val += int(''.join(def_dict[i]), 16)
    return list(hex(hex_val)[2:].upper())


def hex_mul(def_dict):
    hex_val = 1
    for i in def_dict:
        hex_val *= int(''.join(def_dict[i]), 16)
    return list(hex(hex_val)[2:].upper())


def_dict = defaultdict(list)

numb_hex = "A2"
def_dict[0] = list(numb_hex)
numb_hex = "C4F"
def_dict[1] = list(numb_hex)

print(f"Сумма {hex_add(def_dict)}")
print(f"Произведение {hex_mul(def_dict)}")

hex_val_1 = hex_class("A2")
hex_val_2 = hex_class("C4F")
print("#" * 100)
print(f"Умножение классов {hex_val_1 * hex_val_2}")
print(f"Сложение классов {hex_val_1 + hex_val_2}")
print("#" * 100)
