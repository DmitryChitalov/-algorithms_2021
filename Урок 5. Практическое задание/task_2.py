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
from operator import mul


# Вариант №1
class Overload:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return f'Сложение:  ' \
               f'{list(self.number)} + {list(other.number)} = ' \
               f'{list(hex(int(self.number, 16) + int(other.number, 16))[2:].upper())}'

    def __mul__(self, other):
        return f'Умножение: ' \
               f'{list(self.number)} * {list(other.number)} = ' \
               f'{list(hex(int(self.number, 16) * int(other.number, 16))[2:].upper())}'


# Вариант №2
def default_d():
    numbers = defaultdict(list)
    numbers[A] = list(A)
    numbers[B] = list(B)

    def_dict_sum = sum([int(''.join(i), 16) for i in numbers.values()])
    def_dict_mul = reduce(mul, [int(''.join(i), 16) for i in numbers.values()], 1)

    print(f'Вариант №2:\n'
          f'Сложение:  {numbers[A]} + {numbers[B]} = {list(hex(def_dict_sum)[2:].upper())}\n'
          f'Умножение: {numbers[A]} * {numbers[B]} = {list(hex(def_dict_mul)[2:].upper())}')


A = 'A2'  # input("Введите первое 16-ричное число))
B = 'C4F'  # input("Введите второе 16-ричное число))

var_1_add = Overload(A) + Overload(B)
var_1_mul = Overload(A) * Overload(B)

print(f'Вариант №1:\n{var_1_add}\n{var_1_mul}\n')

default_d()
