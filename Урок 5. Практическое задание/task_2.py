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


def multiplication_and_sum():
    numbers = defaultdict(list)
    first_num, second_num = input('Введите два шестнадцатиричных числа: ').split()
    numbers[first_num] = list(first_num)
    numbers[second_num] = list(second_num)
    my_sum = 0
    my_multiplication = 1

    for i in numbers.values():
        my_sum += (int(''.join(i), 16))
        my_multiplication *= int(''.join(i), 16)

    print(f'Сумма введенных чисел: {list(str(hex(my_sum)).upper()[2:])}')
    print(f'Произведение введенных чисел: {list(str(hex(my_multiplication)).upper()[2:])}')


multiplication_and_sum()
