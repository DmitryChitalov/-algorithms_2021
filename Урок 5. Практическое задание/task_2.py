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


from collections import defaultdict, namedtuple
from functools import reduce


# "defaultdict"
def hex_result(n_1, n_2):
    collect = defaultdict(list)
    collect['summ'] = list(hex(int(n_1, 16) + int(n_2, 16))[2:].upper())
    collect['mult'] = list(hex(int(n_1, 16) * int(n_2, 16))[2:].upper())
    return f'Sum of numbers {list(n_1.upper())} and {list(n_2.upper())} = {collect["summ"]}\n' \
           f'Product of numbers {list(n_1.upper())} and {list(n_2.upper())} = {collect["mult"]}'


# "class HexNumber"
class HexNumber:
    def __init__(self, number):
        self.number = number

    def __add__(self, second):
        return hex(int(self.number, 16) + int(second.number, 16)).upper()[2:]

    def __mul__(self, second):
        return hex(int(self.number, 16) * int(second.number, 16)).upper()[2:]


if __name__ == '__main__':
    input_number_1 = input(f'Enter the first hexadecimal number: ')
    input_number_2 = input(f'Enter the second hexadecimal number: ')
    print(f'{"*" * 25} "defaultdict" {"*" * 25}')
    print(hex_result(input_number_1, input_number_2))
    print(f'{"*" * 35} "class HexNumber" {"*" * 35}')
    print(f"Sum of numbers {list(CalcHex(input_number_1) + CalcHex(input_number_2))}")
    print(f"Product of numbers  {list(CalcHex(input_number_1) * CalcHex(input_number_2))}")
