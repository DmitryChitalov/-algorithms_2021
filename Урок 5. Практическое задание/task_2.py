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
from functools import reduce


class HexNumbers:
    def __init__(self, hex_number):
        self.hex_number = hex_number

    def __add__(self, other):
        return list(hex(int(self.hex_number, 16) + int(other.hex_number, 16)))[2:]

    def __mul__(self, other):
        return list(hex(int(self.hex_number, 16) * int(other.hex_number, 16)))[2:]


num_1 = input("Введите первое шестнадцатиричное число:")
num_2 = input("Введите второе шестнадцатиричное число:")
first_num = HexNumbers(num_1)
second_num = HexNumbers(num_2)
print("Решение с помощь ООП:")
print(f"Сумма чисел равна: {first_num + second_num}")
print(f"произведение чисел равно: {first_num * second_num}")
print("*" * 100)
print("Решение с помощь defaultdict:")

def_dict = defaultdict(list)

def_dict.update({"1": list(num_1)})
def_dict.update({"2": list(num_2)})

print(f"Сумма чисел равна: {hex(sum([int(''.join(elem), 16) for elem in def_dict.values()]))[2:]}")
print(
    f"Произведение чисел равно: "
    f"{hex(reduce(lambda n_1, n_2: n_1 * n_2, [int(''.join(elem), 16) for elem in def_dict.values()]))[2:]}")
print(def_dict)
