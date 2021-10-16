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

some_dict = defaultdict(list)
first_number = input('Введите первое шестнадцатеричное число: ')
second_number = input('Введите второе шестнадцатеричное число: ')

some_dict[first_number] = list(first_number)
some_dict[second_number] = list(second_number)


def operations_hex(first, second):
    res_summ = hex(int(first, 16) + int(second, 16)).replace('0x', '').upper()
    res_mul = hex(int(first, 16) * int(second, 16)).replace('0x', '').upper()
    some_dict[res_summ] = list(res_summ)
    some_dict[res_mul] = list(res_mul)
    return f'Сумма чисел из примера: {some_dict[res_summ]}, ' \
           f'Произведение - {some_dict[res_mul]}'


print(reduce(operations_hex, [first_number, second_number]))


class HexNumber:
    def __init__(self, value):
        self.value = int(value, 16)

    def __add__(self, other):
        return hex(self.value + other.value).replace('0x', '').upper()

    def __mul__(self, other):
        return hex(self.value * other.value).replace('0x', '').upper()


a = HexNumber(first_number)
b = HexNumber(second_number)

print(f'Сумма чисел из примера: {a + b}')
print(f'Произведение - {a * b}')
