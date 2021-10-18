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


def summ_sixteen():
    number_1 = input('Введите число: ')
    number_2 = input('Введите число: ')
    d = defaultdict(list)
    for el in number_1:
        d[number_1].append(el)
    for el in number_2:
        d[number_2].append(el)
    sum_all = reduce(lambda x, y: hex(int(x, 16) + int(y, 16)).upper()[2:], d)
    mul_all = reduce(lambda x, y: hex(int(x, 16) * int(y, 16)).upper()[2:], d)
    for el in sum_all:
        d[sum_all].append(el)
    for el in mul_all:
        d[mul_all].append(el)
    # print(d)
    print(f'Сумма равна: {d[sum_all]}\n', f'Произведение равно: {d[mul_all]}')


summ_sixteen()