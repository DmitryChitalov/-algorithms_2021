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

# 1. вариант
from collections import defaultdict


def hexnum(num_1, num_2):
    """
    Возвращает арифметические операции + и * с шестнадцатиричными числами
    :param num_1: первое число
    :param num_2: второе число
    :return: ответ в виде массива
    """
    d = defaultdict(list)
    d[num_1] = list(num_1)
    d[num_2] = list(num_2)
    d['add'] = list(hex(int(num_1, 16) + int(num_2, 16))[2:])
    d['mul'] = list(hex(int(num_1, 16) * int(num_2, 16))[2:])
    return f'{num_1} + {num_2} = {d["add"]}\n {num_1} * {num_2} = {d["mul"]}'


print(f'def hexnum:\n{hexnum("a2", "c4f")}')

# 2. вариант
class HexNumber:
    """
    Возвращает арифметические операции + и * с шестнадцатиричными числами
    """
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


hex_num_1 = HexNumber('a2')
hex_num_2 = HexNumber('c4f')
print('HexNumber __add__: ', hex_num_1 + hex_num_2)
print('HexNumber __mul__:', hex_num_1 * hex_num_2)