"""
2. Написать программу сложения и умножения двух шестнадцатиричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля
collections Для лучшее освоения материала можете даже сделать несколько решений
этого задания, применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши
знания по ООП
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
# вариант №1
nums = defaultdict(list)
nums[1] = list(input('Введите первое число: \n'))
nums[2] = list(input('Введите второе число: \n'))

num_sum = reduce(lambda x, y: int(''.join(x), 16) + int(''.join(y), 16),
                 nums.values())
num_mul = reduce(lambda x, y: int(''.join(x), 16) * int(''.join(y), 16),
                 nums.values())
print(f'Сумма чисел {"".join(nums[1]).upper()} и {"".join(nums[2]).upper()} '
      f'равна: {"".join(list(hex(num_sum)[2:].upper()))}')
print(f'Произведение чисел {"".join(nums[1]).upper()} и '
      f'{"".join(nums[2]).upper()} равно: '
      f'{"".join(list(hex(num_mul)[2:].upper()))}')

# вариант №2


class HexNumber:
    def __init__(self, num):
        self.num = list(num)

    def __add__(self, other):
        return ''.join(list(hex(int(''.join(self.num), 16) +
                                int(''.join(other.num), 16)))[2:]).upper()

    def __mul__(self, other):
        return ''.join(list(hex(int(''.join(self.num), 16) *
                                int(''.join(other.num), 16)))[2:]).upper()


hx = HexNumber('a2')
hy = HexNumber('c4f')
print('\nСумма и произведение чисел из примера через ООП')
print(hx + hy)
print(hx * hy)
