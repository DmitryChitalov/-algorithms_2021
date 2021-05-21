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
from functools import reduce
from collections import defaultdict


num = input("Введите два шестнадцатиричных числа через пробел: ").split(" ")  # 'A2 C4F'
dd = defaultdict(list)
for el in num:
    dd[el] = [i for i in el]
sum = reduce(lambda a, b: a + b, [int(''.join(i), 16) for i in dd.values()])
print('Сумма равна: ', list('%X' % sum))
prod = reduce(lambda a, b: a * b, [int(''.join(i), 16) for i in dd.values()])
print('Произведение равно: ', list('%X' % prod))


"------------------------------------------------------------"
print('Вариант с ООП: ')


class HexNumber:
    def __init__(self, num_str):  # 'A2'
        self.num_str = [i for i in num_str]  # ['A', '2']

    def __add__(self, other):
        sum = int(''.join(self.num_str), 16) + int(''.join(other.num_str), 16)
        return 'Произведение равно: ', list('%X' % sum)

    def __mul__(self, other):
        prod = int(''.join(self.num_str), 16) * int(''.join(other.num_str), 16)
        return 'Сумма равна: ', list('%X' % prod)


hx_1 = HexNumber(input('Введите первое шестнадцатиричное число: '))  # 'A2'
hx_2 = HexNumber(input('Введите второе шестнадцатиричное число: '))  # 'C4F'
print(hx_1 + hx_2)
print(hx_1 * hx_2)

