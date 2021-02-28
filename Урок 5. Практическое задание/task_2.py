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
# Вариант 1
from collections import defaultdict


def hexnum(num1, num2):
    d = defaultdict(list)
    d[num1] = list(num1)
    d[num2] = list(num2)
    d['summa'] = list(hex(int(num1, 16) + int(num2, 16))[2:])
    d['mult'] = list(hex(int(num1, 16) * int(num2, 16))[2:])
    return f"Введены числа {num1} и {num2}.\nИх сумма равна {d['summa']}\nИх произведение равно {d['mult']}."


print(hexnum('a2', 'c4f'))
print()


# Вариант 2
class HexNumber:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        result = hex(int(self.number, 16) + int(other.number, 16))
        return list(result[2:])

    def __mul__(self, other):
        result = hex(int(self.number, 16) * int(other.number, 16))
        return list(result[2:])

    def __str__(self):
        return f'Полученное число: {list(self.number)}'


hx1 = HexNumber('a2')
print(hx1)

hx2 = HexNumber('c4f')
print('Сумма чисел:', hx1 + hx2)
print('Произведение чисел:', hx1 * hx2)
