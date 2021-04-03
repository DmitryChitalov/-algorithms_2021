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


class MyDictClass:
    def __init__(self, f_op):
        self.result_val = f_op

    def __add__(self, s_op):
        return list(hex(int(self.result_val, 16) + int(''.join(s_op), 16))[2:].upper())

    def __mul__(self, s_op):
        return list(hex(int(self.result_val, 16) * int(''.join(s_op), 16))[2:].upper())


def default_dict_sum(d_dict):  # Сумма
    result_val = 0
    for i in d_dict:
        result_val += int(''.join(d_dict[i]), 16)
    return list(hex(result_val)[2:].upper())


def default_dict_product(d_dict):  # Произведение
    result_val = 1
    for i in d_dict:
        result_val *= int(''.join(d_dict[i]), 16)
    return list(hex(result_val)[2:].upper())


default_dict = defaultdict(list)

first_op = input("Input first operand: ")
second_op = input("Input second operand: ")

default_dict[0] = list(first_op)
default_dict[1] = list(second_op)

print(f"Sum {default_dict_sum(default_dict)}")
print(f"Product {default_dict_product(default_dict)}")

# Вариант с ООП
new_obj = MyDictClass(first_op)
print(f"Sum {new_obj + second_op}")
print(f"Product {new_obj * second_op}")
