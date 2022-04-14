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

first_d = defaultdict(list)
second_d = defaultdict(list)


def numbers_input():
    for i in range(2):
        number = enumerate(input(f'Input the {i + 1} hex number: ').upper())
        for ind, j in number:
            if i == 0:
                first_d[ind] = j
            else:
                second_d[ind] = j


def numbers_add():
    return list(str(hex(int(''.join(first_d.values()), 16) + int(''.join(second_d.values()), 16)))[2:].upper())


def numbers_mult():
    return list(str(hex(int(''.join(first_d.values()), 16) * int(''.join(second_d.values()), 16)))[2:].upper())


numbers_input()
print(first_d.values(), second_d.values())
print(numbers_add())
print(numbers_mult())