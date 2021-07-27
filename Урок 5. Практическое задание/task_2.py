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
# 1 вариант
from collections import defaultdict
from functools import reduce

x = input('Введите первое шестнадцатеричное число: ')
y = input('Введите второе шестнадцатеричное число: ')
numbers = defaultdict(list)
numbers[x] = list(x)
numbers[y] = list(y)
add_number = sum([int(''.join(value), 16) for value in numbers.values()])
add_result = list('{:x}'.format(int(add_number)).upper())
mul_number = reduce(lambda a, b: a * b, [int(''.join(value), 16) for value in numbers.values()])
mul_result = list('{:x}'.format(int(mul_number)).upper())
print(f'Сумма чисел - {add_result}, произведение - {mul_result}')


# 2 вариант
class HexNumber:
    def __init__(self, first_num, second_num):
        self.first_num = first_num
        self.second_num = second_num

    def __add__(self, other):
        res = list(hex(int(''.join(self.first_num), 16) + int(''.join(other.second_num), 16)))[2:]
        return f'Сумма чисел - {[i.upper() for i in res]}'

    def __mul__(self, other):
        res = list(hex(int(''.join(self.first_num), 16) * int(''.join(other.second_num), 16)))[2:]
        return f'Произведение чисел - {[i.upper() for i in res]}'


first_number = list(input('Введите первое шестнадцатеричное число: '))
second_number = list(input('Введите второе шестнадцатеричное число: '))
print(HexNumber(first_number, second_number) + HexNumber(first_number, second_number))
print(HexNumber(first_number, second_number) * HexNumber(first_number, second_number))
