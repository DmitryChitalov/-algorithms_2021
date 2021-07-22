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

ddict = defaultdict(list)

ddict[1] = list(input('Введите первое число: '))
ddict[2] = list(input('Введите второе число: '))
print(ddict)

c = hex(int(''.join(str(i) for i in ddict[1]), 16) * int(''.join(str(i) for i in ddict[2]), 16))
d = hex(int(''.join(str(i) for i in ddict[1]), 16) + int(''.join(str(i) for i in ddict[2]), 16))
print(f'Сумма: {list(c[2:].upper())}')
print(f'Произведение: {list(d[2:].upper())}')


class HexNumber:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return hex(int(self.num, 16) + int(other.num, 16)).upper()[2:]

    def __mul__(self,other):
        return hex(int(self.num, 16) * int(other.num, 16)).upper()[2:]

a = input('Введите первое число: ')
b = input('Введите второе число: ')
a = HexNumber(a)
b = HexNumber(b)
c = a + b
d = a * b

print(f'Сумма: {list(c)}')
print(f'Произведение: {list(d)}')
