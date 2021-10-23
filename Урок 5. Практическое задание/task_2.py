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
(в частности по перегрузке методов).

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
import collections
import numpy


# Вариант №2
class HexNumber:
    def __init__(self):
        self.hex_number = input(f"Enter the number please: ")
        self.number = int(self.hex_number, 16)

    def __add__(self, other):
        return list(hex(self.number + other.number))[2:]
        # print(f'The summa of the numbers is: {list(hex(self.number + other.number ))[2:]}')

    def __mul__(self, other):
        return list(hex(self.number * other.number))[2:]

    def __str__(self):
        return self


# Вариант №1

def my_function():
    numbers = collections.defaultdict(list)
    for i in range(2):
        z = input(f"Please enter the {i + 1} number: ")
        numbers[f'{i}_{z}'] = list(z)

    numbers_on_list = [int("".join(i), 16) for i in numbers.values()]
    print(f'The summa of the numbers is: {list(hex(sum(numbers_on_list)))[2:]}')
    print(f'The multiplication of the numbers is: {list(hex(numpy.prod(numbers_on_list)))[2:]}')


# for first variant
my_function()
# for second one
x = HexNumber()
y = HexNumber()
print(f'The summa of the numbers is: {x + y}')
print(f'The multiplication of the numbers is: {x * y}')
