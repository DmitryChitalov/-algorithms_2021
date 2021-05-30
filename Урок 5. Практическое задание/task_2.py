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


# Первое решение
from collections import defaultdict
from functools import reduce

test_dict = defaultdict(list)

test_dict.update({'first_num': list('A2')})
test_dict.update({'second_num': list('C4F')})

hex_add = list(hex(sum([int(''.join(i), 16) for i in test_dict.values()])).upper()[2:])
hex_mul = list(hex(reduce((lambda first_num, second_num: first_num * second_num),
                          [int(''.join(i), 16) for i in test_dict.values()])).upper()[2:])
print('Первое решение')
print(hex_add)
print(hex_mul)
print(test_dict)


# Второе решение
class Hexadecimal:
    def __init__(self, number):
        self.number = list(number)

    def __add__(self, other):
        result = self.decfunc() + other.decfunc()
        return Hexadecimal(self.hexfunc(result))

    def __mul__(self, other):
        result = self.decfunc() * other.decfunc()
        return Hexadecimal(self.hexfunc(result))

    def __str__(self):
        return f'{self.number}'

    def decfunc(self):
        list_to_string = ''.join(self.number)
        result = int(list_to_string, 16)
        return result

    @staticmethod
    def hexfunc(in_number):
        result = hex(in_number)
        return result.upper()[2:]


a = Hexadecimal('A2')
b = Hexadecimal('C4F')
c = a + b
d = a * b
print('Второе решение')
print(a)
print(b)
print(c)
print(d)
