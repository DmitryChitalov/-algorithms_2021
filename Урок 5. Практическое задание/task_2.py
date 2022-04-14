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
    def __init__(self, hex_num):
        self.hex_num = hex_num

    def __add__(self, other):
        return list(hex(int(self.hex_num, 16) + int(other.hex_num, 16))[2:].upper())

    def __mul__(self, other):
        return list(hex(int(self.hex_num, 16) * int(other.hex_num, 16))[2:].upper())


def from_dict(num_1, num_2):
    hex_numbers = defaultdict(list)
    hex_numbers[1] = list(num_1)
    hex_numbers[2] = list(num_2)

    add_nums = reduce(lambda i, j: int("".join(i), 16) + int("".join(j), 16), hex_numbers.values())
    mul_nums = reduce(lambda i, j: int("".join(i), 16) * int("".join(j), 16), hex_numbers.values())

    return f'Add: {hex(add_nums).upper()[2:]}\nMull: {hex(mul_nums).upper()[2:]}'


numb_1 = 'A2'
numb_2 = 'C4F'

add_hex_num = HexNumber(numb_1) + HexNumber(numb_2)
mul_hex_num = HexNumber(numb_1) * HexNumber(numb_2)

print(f'Add: {"".join(add_hex_num)}\nMul: {"".join(mul_hex_num)}'
      f'\n\nWith defaultdict:\n{from_dict(numb_1, numb_2)}')

"""
Смысла в использовании коллекций не увидел. Плюс ко всему начали сыпаться предупреждения на hex_numbers.values()
Expected type 'Iterable[int]' (matched generic type 'Iterable[_T]'), got 'ValuesView[list]' instead
Решение через перегрузку более питоническое. 
"""
