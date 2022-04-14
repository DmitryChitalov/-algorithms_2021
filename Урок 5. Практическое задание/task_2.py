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

class Hexnumber:
    def __init__(self, number):
        self.num = number

    def __add__(self, other):
        return list(hex(int(self.num, 16) + int(other.num, 16))[2:].upper())

    def __mul__(self, other):
        return list(hex(int(self.num, 16) * int(other.num, 16))[2:].upper())

def get_numbers():
    first_num = '0x' + input('Введите первое число')
    second_num = '0x' + input('Введите второе число')
    return first_num, second_num


def add_hex_dict(hex_num):
    hex_dict[hex_num] = list(hex_num[2:].upper())


def calculate(first_hex_num, second_hex_num):
    add_hex_dict(first_hex_num)
    add_hex_dict(second_hex_num)
    sum_hex_num = hex(int(first_hex_num, 16) + int(second_hex_num, 16))
    mul_hex_num = hex(int(first_hex_num, 16) * int(second_hex_num, 16))
    add_hex_dict(sum_hex_num)
    add_hex_dict(mul_hex_num)
    print(f'Сумма чисел равна: {hex_dict[sum_hex_num]}')
    print(f'Произведение чисел равно: {hex_dict[mul_hex_num]}')


hex_dict = defaultdict(list)
first_number, second_number = get_numbers()
add_hex_dict(first_number)
add_hex_dict(second_number)
calculate(first_number, second_number)
print(f'Сумма чисел с использованием класса Hexnumber: {Hexnumber(first_number) + Hexnumber(second_number)}')
print(f'Произведение чисел с использованием класса Hexnumber: {Hexnumber(first_number) * Hexnumber(second_number)}')


