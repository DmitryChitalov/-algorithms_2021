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

nums = defaultdict(list)

nums['1'] = list(input('Введите первое шестнадцатиричное число: '))
nums['2'] = list(input('Введите второе шестнадцатиричное число: '))

summ = hex(sum([int(''.join(i), 16) for i in nums.values()]))
multip = hex(reduce(lambda x, y: x * y, [int(''.join(i), 16) for i in nums.values()]))

print(f'Сумма чисел: {summ[2:]}\n'
      f'Произведение: {multip[2:]}')


class HexCalculate:
    def __init__(self, hex_first, hex_second):
        self.hex_first = hex_first
        self.hex_second = hex_second

    def __add__(self, other):
        return list(hex(int(''.join(self.hex_first), base=16) + int(''.join(other.hex_second), base=16)))

    def __mul__(self, other):
        return list(hex(int(''.join(self.hex_first), base=16) * int(''.join(other.hex_second), base=16)))


# first_hex_num = list(input('Введите первое шестнадцатиричное число: '))
# second_hex_num = list(input('Введите второе шестнадцатиричное число: '))
#
# hex_sum = HexCalculate(first_hex_num, second_hex_num) + HexCalculate(first_hex_num, second_hex_num)
# hex_mul = HexCalculate(first_hex_num, second_hex_num) * HexCalculate(first_hex_num, second_hex_num)
#
# print(f'Сумма чисел: {hex_sum[2:]}\n'
#       f'Произведение: {hex_mul[2:]}')


'''
Это задание не успел сделать вчера, поэтому не сдал ДЗ во время, выполнил по примеру, хотя идея была немного другая,
с более сложным алгоритмом, идея без использования встроенных исчислений в шестнадцатиричном формате.
'''