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


def hex_mul(num1, num2):
    hex_list = defaultdict(list)
    hex_list[int(num1, 16)] = ' '.join(num1).split()
    hex_list[int(num2, 16)] = ' '.join(num2).split()
    print(hex_list)
    print("Произведение 2-х ваших 16-ричных чисел: ")
    return reduce(lambda k, n: ('%X' % (k * n)), [int(''.join(value), 16) for value in hex_list.values()])


def hex_add(num1, num2):
    hex_list = defaultdict(list)
    hex_list[int(num1, 16)] = ' '.join(num1).split()
    hex_list[int(num2, 16)] = ' '.join(num2).split()
    print(hex_list)
    print("Сумма 2-х ваших 16-ричных чисел: ")
    return reduce(lambda k, n: ('%X' % (k + n)), [int(''.join(value), 16) for value in hex_list.values()])


hex_1 = input('Введите первое 16-ричное число: ')
hex_2 = input('Введите второе 16-ричное число: ')
print(hex_mul(hex_1, hex_2))
print(hex_add(hex_1, hex_2))

