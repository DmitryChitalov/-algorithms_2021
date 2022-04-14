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

hex_nums = defaultdict(list)


def add_to_dict(hex_num):
    hex_nums[hex_num].extend(list(hex_num[2:].upper()))


def get_nums():
    a, b = [
        '0x' + input('Введите {} шестнадцатиричное число: '.format('первое' if not i else 'второе')) for i
        in range(2)]
    return a, b


def default_dict_main(a, b):
    print('Default Dict')
    add_to_dict(a)
    add_to_dict(b)
    a, b = int(a, 16), int(b, 16)
    add, mul = hex(a + b), hex(a * b)
    add_to_dict(add)
    add_to_dict(mul)
    print(f'Сумма чисел: {hex_nums[add]}')
    print(f'Произведение чисел: {hex_nums[mul]}')


class HexNumber:
    def __init__(self, str_num):
        self.name = str_num
        self.value = list(str_num.upper())

    def __str__(self):
        return str(self.value)

    def __add__(self, other):
        if isinstance(other, HexNumber):
            name = str(hex(int(self.name, 16) + int(other.name, 16)))[2:]
            return HexNumber(name)

    def __mul__(self, other):
        if isinstance(other, HexNumber):
            name = str(hex(int(self.name, 16) * int(other.name, 16)))[2:]
            return HexNumber(name)


def test_class(a, b):
    print('HexNumber class')
    a = HexNumber(a)
    b = HexNumber(b)
    print('Сумма чисел: ', a + b)
    print('Произведение чисел: ', a * b)


if __name__ == '__main__':
    first_num, second_num = get_nums()
    default_dict_main(first_num, second_num)
    test_class(first_num, second_num)
