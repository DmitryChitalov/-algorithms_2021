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

class HexNumber:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        num = str(hex(int(self.num, 16) + int(other.num, 16)).upper())[2:]
        return num

    def __mul__(self, other):
        num = str(hex(int(self.num, 16) * int(other.num, 16)).upper())[2:]
        return num


num1, num2 = (input('Введите первое число HEX: ').upper(), (input('Введите второе число HEX: ').upper()))
print(HexNumber(num1) + HexNumber(num2))
print(HexNumber(num1) * HexNumber(num2))


hex_dict = defaultdict(list)
hex_dict[num1], hex_dict[num2] = list(num1), list(num2)
print(hex_dict)


int_num_1 = int(''.join(hex_dict[num1]), 16)
sum_hex = list(hex(reduce(lambda x, y: x + y, [int(num1, 16), int(num2, 16)]))[2:].upper())
mul_hex = list(hex(reduce(lambda x, y: x * y, [int(num1, 16), int(num2, 16)]))[2:].upper())
print(sum_hex)
print(mul_hex)
