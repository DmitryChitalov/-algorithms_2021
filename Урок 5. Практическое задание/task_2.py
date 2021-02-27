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

# Через defaultdict:
from collections import defaultdict


def add_to_dict(num, add_dict):
    for i in num:
        add_dict[num].append(i)


def to_sixteen(num):
    num_str = '0123456789ABCDEF'
    if num // 16 == 0:
        return num_str[num]
    else:
        return to_sixteen(num // 16) + num_str[num % 16]


num_dict = defaultdict(list)

num_1 = input('Введите первое число шестнадцатиричной системы: ')
num_2 = input('Введите второе число шестнадцатиричной системы: ')

add_to_dict(num_1, num_dict)
add_to_dict(num_2, num_dict)

num_sum = to_sixteen(int(num_1, 16) + int(num_2, 16))
num_mul = to_sixteen(int(num_1, 16) * int(num_2, 16))

add_to_dict(num_sum, num_dict)
add_to_dict(num_mul, num_dict)

print(f'{num_dict[num_1]} + {num_dict[num_2]} = {num_dict[num_sum]}')
print(f'{num_dict[num_1]} * {num_dict[num_2]} = {num_dict[num_mul]}')

'''
Не совсем понял, нужно ли было взаимодействовать именно со списками из словаря или же
словарь здесь исключительно для хранения чисел в виде списков, но сделал вот так
'''

print('-' * 200)


# Через ООП:
class SNum:
    def __init__(self, num):
        self.num = num
        self.list_num = list(self.num)

    def __str__(self):
        return f'{self.list_num}'

    # Если бы до этого не вводил функцию to_sixteen, добавил бы здесь статический метод
    def __mul__(self, other):
        return list(to_sixteen(int(self.num, 16) * int(other.num, 16)))

    def __add__(self, other):
        return list(to_sixteen(int(self.num, 16) + int(other.num, 16)))


num_1 = SNum(num_1)
num_2 = SNum(num_2)

print(f'{num_1} + {num_2} = {num_1 + num_2}')
print(f'{num_1} * {num_2} = {num_1 * num_2}')
