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
from functools import reduce


def func_reduce(prev_value, value):
    s_value = hex(int(''.join(map(str, prev_value)), 16) + int(''.join(map(str, value)), 16))
    m_value = hex(int(''.join(map(str, prev_value)), 16) * int(''.join(map(str, value)), 16))
    sum_value = [s_value[el] for el in range(2, len(s_value))]
    mul_value = [m_value[el] for el in range(2, len(m_value))]
    return f'Сложение 16-ых чисел {sum_value}\nУмножение 16-ых чисел {mul_value}'


def func_1(num_1, num_2):
    x_num = [num_1[el] for el in range(len(num_1))]
    y_num = [num_2[el] for el in range(len(num_2))]
    def_dict = defaultdict(list)
    for el in range(1):
        def_dict[el].append(x_num)
        def_dict[el].append(y_num)
        for value in def_dict.values():
            return reduce(func_reduce, value)


print(func_1(num_1=input('Введите первое число: '), num_2=input('Введите первое число:')))
