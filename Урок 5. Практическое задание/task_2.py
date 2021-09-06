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


def hex_sum(numbers):
    my_sum = 0
    for val in numbers.values():
        my_sum += int(''.join(val), 16)
    return str(hex(my_sum))[2:]


def hex_mult(numbers):
    my_mult = 1
    for val in numbers.values():
        my_mult *= int(''.join(val), 16)
    return str(hex(my_mult))[2:]


numbers = defaultdict(list)
fst_num, sec_num = input("Введите два шестнадцатиричных числа через пробел: ").split()
numbers[fst_num] = list(fst_num)
numbers[sec_num] = list(sec_num)

print(f'Сумма введённых чисел равна {list(hex_sum(numbers))}')
print(f'Произведение введённых чисел равно {list(hex_mult(numbers))}')
