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


class HexCalc:
    def __init__(self, number):
        self.number = list(number)
        print(self.number)

    def __add__(self, other):
        return f'Сумма чисел: {list("%X" % (int("".join(self.number), 16) + int("".join(other.number), 16)))}'

    def __mul__(self, other):
        return f'Произведение чисел: {list("%X" % (int("".join(self.number), 16) * int("".join(other.number), 16)))}'


hex_one = HexCalc(input('Введите первое число: '))
hex_two = HexCalc(input('Введите второе число: '))
print(hex_one + hex_two)
print(hex_one * hex_two)


def calc_hex():
    hex_dict = defaultdict(list)
    number_one = input('Введите первое число: ')
    number_two = input('Введите второе число: ')
    hex_dict[number_one] = list(number_one)
    hex_dict[number_two] = list(number_two)
    hex_sum = sum([int(''.join(i), 16) for i in hex_dict.values()])
    hex_mult = reduce(lambda x, y: int(''.join(x), 16) * int(''.join(y), 16), hex_dict.values())
    return f'Сумма: {list("%X" % hex_sum)}\n' \
           f'Произведение: {list("%X" % hex_mult)}'


print(calc_hex())
