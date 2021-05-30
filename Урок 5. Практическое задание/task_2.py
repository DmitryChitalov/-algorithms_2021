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


def check_hex(num):
    sign = '0123456789ABCDEFabcdef'
    for el in num:
        if el not in sign:
            return 0
    return 1


def sum_hex(defdict_num_1, defdict_num_2):
    hex_sum = hex((int(''.join(defdict_num_1.values()), 16)) + (int(''.join(defdict_num_2.values()), 16)))
    return list(hex_sum)[2:]


def mul_hex(defdict_num_1, defdict_num_2):
    hex_mul = hex((int(''.join(defdict_num_1.values()), 16)) * (int(''.join(defdict_num_2.values()), 16)))
    return list(hex_mul)[2:]


num_1 = list(input('Введите первое число в шестнадцатеричной системе: '))
num_2 = list(input('Введите второе число в шестнадцатеричной системе: '))
if check_hex(num_1) == 0 or check_hex(num_2) == 0:
    print('Вы ввели не шестнадцетеричное число!!!')
    exit()
defdict_num_1 = defaultdict(list)
defdict_num_2 = defaultdict(list)
for idx, el in enumerate(num_1):
    defdict_num_1[idx] = el
for idx, el in enumerate(num_2):
    defdict_num_2[idx] = el
print(f'Сумма чисел из примера:{sum_hex(defdict_num_1, defdict_num_2)}')
print(f'Произведение чисел из примера:{mul_hex(defdict_num_1, defdict_num_2)}')


''' Вариант с ООП '''


class HexNumber:
    def __init__(self, num_list):
        self.num = num_list

    def __add__(self, other):
        hex_sum = hex((int(''.join(self.num), 16)) + (int(''.join(other.num), 16)))
        return list(hex_sum)[2:]

    def __mul__(self, other):
        mul_hex = hex((int(''.join(self.num), 16)) * (int(''.join(other.num), 16)))
        return list(mul_hex)[2:]


hx_1 = HexNumber(num_1)
hx_2 = HexNumber(num_2)
print(f'Сумма чисел из примера вторым способом:{hx_1 + hx_2}')
print(f'Произведение чисел из примера вторым способом::{hx_1 * hx_2}')

