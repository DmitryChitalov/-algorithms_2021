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


# вариант 1
def sum_16(first, second):
    return list(hex(int(''.join(first), 16) + int(''.join(second), 16)).upper())[2:]


def mul_16(first, second):
    return list(hex(int(''.join(first), 16) * int(''.join(second), 16)).upper())[2:]


numbers = defaultdict(list)
numbers['first'] = list(input('Введите первое число в 16-ричной системе: ').upper())
numbers['second'] = list(input('Введите второе число в 16-ричной системе: ').upper())
numbers['addition'] = sum_16(numbers['first'], numbers['second'])
numbers['multiplication'] = mul_16(numbers['first'], numbers['second'])
for key, values in numbers.items():
    print(key, values)


# вариант 2

class HexNumber():

    def __init__(self, number):
        self.number = list(number.upper())

    def __add__(self, other):
        addition = hex(int(''.join(self.number), 16) + int(''.join(other.number), 16)).upper()[2:]
        return HexNumber(addition)

    def __mul__(self, other):
        multiplication = hex(int(''.join(self.number), 16) * int(''.join(other.number), 16)).upper()[2:]
        return HexNumber(multiplication)


a1 = HexNumber(input('Введите первое число в 16-ричной системе: '))
a2 = HexNumber(input('Введите второе число в 16-ричной системе: '))
print((a1 + a2).number)
print((a1 * a2).number)
