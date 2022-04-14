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
print('Решение 1 вариантом')
nums[1] = list(input('Введите первое число: '))
nums[2] = list(input('Введите второе число: '))
num_sum = reduce(lambda x1, y1: int(''.join(x1), 16) + int(''.join(y1), 16), nums.values())
num_mul = reduce(lambda x1, y1: int(''.join(x1), 16) * int(''.join(y1), 16), nums.values())
print(f'Сумма чисел равна: {"".join(list(hex(num_sum)[2:].upper()))}')
print(f'Произведение чисел равно: {"".join(list(hex(num_mul)[2:].upper()))}')


class HexNumber:
    def __init__(self, num):
        self.num = list(num)

    def __add__(self, other):
        return ''.join(list(hex(int(''.join(self.num), 16) + int(''.join(other.num), 16)))[2:]).upper()

    def __mul__(self, other):
        return ''.join(list(hex(int(''.join(self.num), 16) * int(''.join(other.num), 16)))[2:]).upper()


print('Решение 2 вариантом')
x = HexNumber(input('Введите первое число: '))
y = HexNumber(input('Введите второе число: '))
print(f'Сумма чисел: {x+y}\nПроизведение чисел: {x*y}')
