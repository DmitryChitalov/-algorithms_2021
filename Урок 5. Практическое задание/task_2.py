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


def add_hex_numbers_req(hex_num_1, hex_num_2):
    print('hex_num_1', hex_num_1)
    print('hex_num_2', hex_num_2)
    if len(hex_num_1) < 2:
        answer = hex(int(hex_num_1[0], 16) + int(hex_num_2[0], 16))
        print('answer', str(answer)[2:])
        return str(answer)[2:]

    num_1 = hex_num_1.pop()
    num_2 = hex_num_2.pop()
    cur_sum = add_hex_numbers_req(hex_num_1, hex_num_2) + str(hex(int(num_1, 16) + int(num_2, 16)))[2:]
    return cur_sum.upper()


def add_hex_num(hex_num_1, hex_num_2):
    hex_sum = hex(int(''.join(hex_num_1), 16) + int(''.join(hex_num_2), 16))
    return list(str(hex_sum)[2:])


def add_hex_num_2(_hex_num):
    hex_sum = hex(int(''.join(_hex_num[0]), 16) + int(''.join(_hex_num[1]), 16))
    return list(str(hex_sum)[2:])


def mul_hex_num_2(_hex_num):
    hex_mul = hex(int(''.join(_hex_num[0]), 16) * int(''.join(_hex_num[1]), 16))
    return list(str(hex_mul)[2:])


def mul_hex_num(hex_num_1, hex_num_2):
    hex_sum = hex(int(''.join(hex_num_1), 16) * int(''.join(hex_num_2), 16))
    return list(str(hex_sum)[2:])


def add_hex_num_oop(hex_num_1, hex_num_2):
    hex_sum = hex(int(hex_num_1, 16) + int(hex_num_2, 16))
    return list(str(hex_sum)[2:])


def mul_hex_num_oop(hex_num_1, hex_num_2):
    hex_mul = hex(int(hex_num_1, 16) * int(hex_num_2, 16))
    return list(str(hex_mul)[2:])


hex_nums = defaultdict(list)

# ввод строки с числами через пробел
hex_str = 'A2 C4F'

for i, num in enumerate(hex_str.split(' ')):
    hex_nums[i] = list(num)

hex_1 = 'A2'
hex_2 = 'C4F'

print(add_hex_num_oop(hex_1, hex_2))
print(mul_hex_num_oop(hex_1, hex_2))

print(add_hex_num_2(hex_nums))
print(mul_hex_num_2(hex_nums))
