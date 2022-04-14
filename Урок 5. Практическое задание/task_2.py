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

# Вариант 1
from collections import defaultdict

res = defaultdict(int)
a, b = [format(int(i, 16), 'X') for i in input(f'Введите числа через пробел: ').split(' ')]
res[a] = list(a)
res[b] = list(b)
res['Сумма'] = list(format(int(a, 16) + int(b, 16), 'X'))
res['Произведение'] = list(format(int(a, 16) * int(b, 16), 'X'))
print(res)


# Вариант 2
class HexNumber:

    def __init__(self, num1):
        self.a = num1

    def value(self):
        return list(str(self.a))

    def __add__(self, other):
        return list(format((int("".join(self.value()), 16) + int("".join(other.value()), 16)), 'X'))

    def __mul__(self, other):
        return list(format((int("".join(self.value()), 16) * int("".join(other.value()), 16)), 'X'))


hx1 = HexNumber(input(f'Введите первое число: '))
hx2 = HexNumber(input(f'Введите первое число: '))
print(f'Число #1: {hx1.value()}')
print(f'Число #1: {hx2.value()}')
print(f'Сумма: {hx1+hx2}')
print(f'Произведение: {hx1*hx2}')
