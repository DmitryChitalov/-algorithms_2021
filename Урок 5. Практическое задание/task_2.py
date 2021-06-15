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
"""
from collections import defaultdict
from functools import reduce

def get_hex_dict(*args):
    hex_dict = defaultdict(list)
    for i in args:
        hex_dict[i] = list(i)
    return hex_dict


def sum(x, y, hex_dict):
    return reduce(lambda x, y: int(f'0x{x}', 16) + int(f'0x{y}', 16), hex_dict.keys())


def mul(x, y, hex_dict):
    return reduce(lambda x, y: int(f'0x{x}', 16) * int(f'0x{y}', 16), hex_dict.keys())


def computation():
    x = input('Введите 1-ое шестнадцати-ое число: ')
    y = input('Введите 2-ое шестнадцати-ое число: ')
    hex_dict = get_hex_dict(x, y)
    res1 = sum(x, y, hex_dict)
    res2 = mul(x, y, hex_dict)
    return f'Введены два числа {get_hex_dict(x)} и {get_hex_dict(y)}\n' \
           f'Их сумма равна - {get_hex_dict(hex(res1).split("x")[1])}\n' \
           f'Произведение - {get_hex_dict(hex(res2).split("x")[1])}'

print(computation())