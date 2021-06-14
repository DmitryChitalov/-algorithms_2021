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
#Вариант 1

from collections import defaultdict
from functools import reduce

user_numbers_dict = defaultdict(list)

user_numbers_dict.update({'first_num': list(input("Введите первое шестнадцатиричное число: "))})
user_numbers_dict.update({'second_num': list(input("Введите второе шестнадцатиричное число: "))})

hex_add = list(hex(sum([int(''.join(i), 16) for i in user_numbers_dict.values()])).upper()[2:])
hex_mul = list(hex(reduce((lambda first_num, second_num: first_num * second_num),
                          [int(''.join(i), 16) for i in user_numbers_dict.values()])).upper()[2:])
print(hex_add)
print(hex_mul)
print(user_numbers_dict)