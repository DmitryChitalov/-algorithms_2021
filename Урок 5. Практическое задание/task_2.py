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

from collections import namedtuple


class HexOp:
    def __init__(self, first_num, second_num):
        self.first_num = first_num
        self.second_num = second_num

    def __add__(self, other):
        return list(hex(int(''.join(self.first_num), 16) + int(''.join(other.second_num), 16)))[2:]

    def __mul__(self, other):
        return list(hex(int(''.join(self.first_num), 16) * int(''.join(other.second_num), 16)))[2:]


def get_calc(first_num, second_num):
    print(f'Первое натуральное шестнадцатиричное число: {first_num}')
    print(f'Второе натуральное шестнадцатиричное число: {second_num}')
    nums = namedtuple("nums", "first_num_dec second_num_dec")
    nums.first_num_dec = int(''.join(first_num), 16)
    nums.second_num_dec = int(''.join(second_num), 16)
    print(f'Сумма чисел: {list(hex(nums.first_num_dec + nums.second_num_dec))[2:]}')
    print(f'Произведение чисел: {list(hex(nums.first_num_dec * nums.second_num_dec))[2:]}')


if __name__ == '__main__':
    first_num_hex = list(input('Введите первое шестнадцатиричное число: '))
    second_num_hex = list(input('Введите второе шестнадцатиричное число: '))

    get_calc(first_num_hex, second_num_hex)

    print(f'Сумма чисел:{HexOp(first_num_hex, second_num_hex) + HexOp(first_num_hex, second_num_hex)}')
    print(
        f'Произведение чисел:{HexOp(first_num_hex, second_num_hex) * HexOp(first_num_hex, second_num_hex)}')
