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


class HexNumber2:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return f'{list(self.num)} + {list(other.num)} = ' \
               f'{list(hex(int(self.num, 16) + int(other.num, 16))[2:].upper())}'

    def __mul__(self, other):
        return f'{list(self.num)} * {list(other.num)} = ' \
               f'{list(hex(int(self.num, 16) * int(other.num, 16))[2:].upper())}'


number1 = input('Введите первое число: ')
number2 = input('Введите второе число: ')

two_numbers = defaultdict(list)
two_numbers[0] = list(number1)
two_numbers[1] = list(number2)
two = [int(''.join(i), 16) for i in two_numbers.values()]
add_hex = sum(two)
mul_hex = reduce(mul, two, 1)

print('1. вариант')
print(f'Сохраняю два числа {list(number1)} и {list(number2)}')
print(f'Сумма чисел: {list(hex(add_hex)[2:].upper())}')
print(f'Произведение: {list(hex(mul_hex)[2:].upper())}')
print('2. вариант')
print(f'Сумма чисел: {HexNumber2(number1) + HexNumber2(number2)}')
print(f'Произведение: {HexNumber2(number1) * HexNumber2(number2)}')
