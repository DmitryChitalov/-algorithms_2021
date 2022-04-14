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


def var_1():
    numbers = defaultdict(list)

    for i in range(2):
        number = input(f'Введите {i + 1} число в шестнадцатиричном формате: ')
        numbers[f'{i + 1}-{number}'] = list(number)

    summa = hex(sum([int(''.join(number), 16) for number in numbers.values()]))[2:].upper()
    mul = hex(reduce(lambda a, b: a * b, [int(''.join(number), 16) for number in numbers.values()]))[2:].upper()

    print(f'Сумма чисел составляет: {list(summa)}')
    print(f'Произведение чисел: {list(mul)}')


def var_2():
    class HexOperation:
        def __init__(self, a, b):
            self.a = list(a)
            self.b = list(b)

        def __add__(self, other):
            return list(hex(int(''.join(self.a), 16) + int(''.join(other.b), 16)))[2:]

        def __mul__(self, other):
            return list(hex(int(''.join(self.a), 16) * int(''.join(other.b), 16)))[2:]

    num_1 = input('Введите первое число в шестнадцатиричном формате: ')
    num_2 = input('Введите второе число в шестнадцатиричном формате: ')

    summa = HexOperation(num_1, num_2) + HexOperation(num_1, num_2)
    mul = HexOperation(num_1, num_2) * HexOperation(num_1, num_2)

    print(f'Сумма чисел составляет: {summa}')
    print(f'Произведение чисел: {mul}')


var_1()
var_2()
