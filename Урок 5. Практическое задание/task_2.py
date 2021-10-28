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


def mult_and_sum():
    nums_dict = defaultdict(list)
    calc_sum = 0
    calc_mult = 1
    num1 = input('Введите число 1 в шестнадцатиричной системе счисления: ')
    num2 = input('Введите число 1 в шестнадцатиричной системе счисления: ')
    nums_dict[num1] = list(num1)
    nums_dict[num2] = list(num2)
    print(nums_dict)

    for i in nums_dict.values():
        calc_sum += (int(''.join(i), 16))
        calc_mult *= int(''.join(i), 16)
    result_sum = list(str(hex(calc_sum))[2:])
    result_mult = list(str(hex(calc_mult))[2:])

    print(f'Сумма чисел: {result_sum}')
    print(f'Произведение чисел: {result_mult}')


mult_and_sum()