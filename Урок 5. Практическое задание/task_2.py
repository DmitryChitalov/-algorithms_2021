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


# 1. вариант
def int16(num):
    my_str = ''
    for el in range(len(num)):
        my_str = my_str + num[el]
    return int(my_str, 16)

def number16(num):
    num_list = []
    my_dict = defaultdict(list)
    for n in range(len(num)):
        my_dict[n] = num[n]
        num_list.append(my_dict.get(n))
    return num_list


N1 = input('Введите первое число: ')
N2 = input('Введите второе число: ')
print('ПЕРВЫЙ ВАРИАНТ (collections)')
number_1 = number16(list(N1))
number_2 = number16(list(N2))
print(f'Представление чисел => {number_1} и {number_2}')

my_list = [int16(number_1), int16(number_2)]
sum_all = [el for el in format((reduce(lambda x, y: x + y, my_list)), 'X')]
mul_all = [el for el in format((reduce(lambda x, y: x * y, my_list)), 'X')]
print(f'Сумма чисел         => {sum_all}')
print(f'Произведение чисел  => {mul_all}')


# 2. вариант
class MyClass:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return MyClass(format((self.num + other.num), 'X'))

    def __mul__(self, other):
        return MyClass(format((self.num * other.num), 'X'))

    def __str__(self):
        return f'{list(self.num)}'


print('ВТОРОЙ ВАРИАНТ (ООП - перегрузка методов)')
N_1 = MyClass(int(N1, 16))
N_2 = MyClass(int(N2, 16))
print(f'Сумма чисел         => {N_1+N_2}')
print(f'Произведение чисел  => {N_1*N_2}')
