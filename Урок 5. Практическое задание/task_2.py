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
import functools
from collections import defaultdict


def func():
    numbers = input('Введите 2 числа в 16-ричном формате например(1AF 2B) через пробел ').split()
    num_dict = defaultdict()
    for i in numbers:
        num_dict[i] = list(i)

    sum_x = sum([int(''.join(i), 16) for i in num_dict.values()])
    mul_x = functools.reduce(lambda x, y: x*y, [int(''.join(i), 16) for i in num_dict.values()])
    print(list('%x' % sum_x))
    print(list('%x' % mul_x))


class HexNumber:
    def __init__(self):
        self.num = list(input('Введите число в 16-ричном формате: '))

    def __add__(self, other):
        return list('%x' % (int(''.join(self.num), 16) + int(''.join(other.num), 16)))

    def __mul__(self, other):
        return list('%x' % (functools.reduce(lambda x, y: x*y, [int(''.join(self.num), 16),
                                                                int(''.join(self.num), 16)])))


x = HexNumber()
print(x + x, x * x)
