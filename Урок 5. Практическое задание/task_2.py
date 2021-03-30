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


from collections import defaultdict


def get_hex_defaultdict():
    hex_dict = defaultdict(int)
    for i in range(16):
        hex_dict[hex(i)[2:].upper()] = i
    return hex_dict


class Calc:

    def __init__(self, number):
        self.number = list(number)
        self.summa = 0
        self.mult = 0
        self.result = 0
        self.hex_dict = get_hex_defaultdict()

    def __add__(self, other):
        for i in range(len(self.number)):
            self.summa += self.hex_dict[self.number[-i - 1]] * 16 ** i
        for j in range(len(other.number)):
            self.summa += self.hex_dict[other.number[-j - 1]] * 16 ** j
        self.result = list(hex(self.summa).upper())[2:]
        return self.result

    def __mul__(self, other):
        for i in range(len(self.number)):
            self.mult += self.hex_dict[self.number[-i - 1]] * 16 ** i
        for j in range(len(other.number)):
            other.mult += self.hex_dict[other.number[-j - 1]] * 16 ** j
        self.result = list(hex(self.mult * other.mult).upper())[2:]
        return self.result

    def __str__(self):
        return f'{self.number}'


x = Calc('A2')
y = Calc('C4F')

print(f'{x} + {y} = {x + y}')
print(f'{x} * {y} = {x * y}')
