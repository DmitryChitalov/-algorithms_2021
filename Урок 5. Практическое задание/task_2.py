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


import collections
import functools


class HexNumber:
    def __init__(self, first_number, second_number):
        self.first_number = first_number
        self.second_number = second_number

    def __add__(self, other):
        return list(format(int(''.join(self.first_number), 16) + int(''.join(self.second_number), 16), 'X'))

    def __mul__(self, other):
        return list(format(int(''.join(self.first_number), 16) * int(''.join(self.second_number), 16), 'X'))


hx = HexNumber(input('Введите число в 16-ричном формате.\n'), input('Введите число в 16-ричном формате.\n'))
print(f'Сумма равна {hx + hx}')
print(f'Произведение равно {hx * hx}')


nums = collections.defaultdict(list)
for i in range(2):
    n = input('Введите число в 16-ричном формате.\n')
    nums[n] = list(n)
print(nums)

sum_res = sum([int(''.join(val), 16) for val in nums.values()])
print(hex(sum_res))
print(f'Сумма = {list(format(sum_res, "X"))}')

mul_res = functools.reduce(lambda n_1, n_2: n_1 * n_2, [int(''.join(val), 16) for val in nums.values()])
print(f'Произведение = {list(format(mul_res, "X"))}')



