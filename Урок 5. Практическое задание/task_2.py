"""
2.*	Написать программу сложения и умножения двух шестнадцатеричных чисел.
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
hex_digit = defaultdict(list)
first_num = input('Введите первое число в шестнадцатеричном формате: ')
second_num = input('Введите второе число в шестнадцатеричном формате: ')
hex_digit[int(first_num, 16)] = ' '.join(first_num).split()
hex_digit[int(second_num, 16)] = ' '.join(second_num).split()
print(hex_digit)


def reduce_func(f_num, s_num):
    return '%X' % (f_num * s_num), '%X' % (f_num + s_num)


print(reduce(reduce_func, [int(''.join(value), 16) for value in hex_digit.values()]))
print(reduce(lambda f_num, s_num: ('%X' % (f_num * s_num), ('%X' % (f_num + s_num))),
             [int(''.join(value), 16) for value in hex_digit.values()]))


class HexNum():
    def __init__(self):
        num_1 = input('Введите первое число в шестнадцатеричном формате: ')
        num_2 = input('Введите второе число в шестнадцатеричном формате: ')
    # def math_operation(self):
