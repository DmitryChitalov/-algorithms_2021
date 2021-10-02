#!/usr/bin/env python3


from collections import defaultdict
from functools import reduce

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


def get_hex_value(i):
    try:
        int(value := input(f'Введите значение {i}: '), 16)
        return value
    except ValueError:
        print(f'{value}: Неверное значение!')
        return get_hex_value(i)


def variant_1():
    data = defaultdict(list)

    for i in [1, 2]:
        value = get_hex_value(i)
        data[int(value, 16)] = list(value)

    print(f'Сумма чисел из примера: {list(hex(reduce(lambda x, y: x[0] + y[0], data.items())).split("x")[1])}')
    print(f'Произведение чисел из примера: {list(hex(reduce(lambda x, y: x[0] * y[0], data.items())).split("x")[1])}')


def variant_2():
    class HexNumber:
        def __init__(self, value: str):
            self.__value = value

        def __add__(self, other_value):
            return HexNumber(hex(int(other_value.__value, 16) + int(self.__value, 16)).split('x')[1])

        def __mul__(self, other_value):
            return HexNumber(hex(int(other_value.__value, 16) * int(self.__value, 16)).split('x')[1])

        def __str__(self):
            return str(list(self.__value))

    value1 = HexNumber(get_hex_value(1))
    value2 = HexNumber(get_hex_value(2))
    print(f'Сумма чисел из примера: {value1 + value2}')
    print(f'Произведение чисел из примера: {value1 * value2}')


def main():
    variant_1()
    variant_2()


if __name__ == '__main__':
    main()
