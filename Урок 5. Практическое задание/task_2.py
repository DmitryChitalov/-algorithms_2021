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
from functools import reduce
from collections import defaultdict

# Option 1


def hex_to_int(hex_list):
    return int(''.join(hex_list), 16)


def int_to_hex(int_num):
    return list(str(hex(int_num)))[2:]


def mult_hex_lists(hex_dict):
    int_list = list(map(str_to_int, list(hex_dict.keys())))
    return int_to_hex(reduce(lambda x, y: x * y, int_list))


def sum_hex_lists(hex_dict):
    int_list = list(map(str_to_int, list(hex_dict.keys())))
    return int_to_hex(sum(int_list))


def str_to_int(str_num):
    return int(str_num, 16)


class HexNumber:
    def __init__(self, str_hex_number):
        self.str_hex = str_hex_number
        self.hex_list = list(self.str_hex)
        self.hex_int = hex_to_int(self.str_hex)

    def __str__(self):
        return str(self.hex_list)

    def __mul__(self, other):
        return HexNumber(int_to_hex(self.hex_int * other.hex_int))

    def __add__(self, other):
        return HexNumber(int_to_hex(self.hex_int + other.hex_int))


hex_dict = defaultdict(list)
new_number = input("Введите первое шестнадцатиричное число: ")
hex_dict[new_number] = list(new_number)
hexNum1 = HexNumber(new_number)
new_number = input("Введите второе шестнадцатиричное число: ")
hex_dict[new_number] = list(new_number)
hexNum2 = HexNumber(new_number)


print("Первое число: ", list(hex_dict.values())[0])
print("Второе число: ", list(hex_dict.values())[1])
print("\nOption 1")
print("Сумма чисел: ", sum_hex_lists(hex_dict))
print("Произведение: ", mult_hex_lists(hex_dict))

print("\nOption 2")
print("Сумма чисел: ", hexNum1 + hexNum2)
print("Произведение: ", hexNum1 * hexNum2)