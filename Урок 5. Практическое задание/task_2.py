"""
2.*  Написать программу сложения и умножения двух шестнадцатиричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)

mul
add

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
    add
    mul

hx = HexNumber
hx + hx
"""

from collections import defaultdict, namedtuple

hex_number = defaultdict(list)


# hex_number = dict()

def calc_defaultdict(x, y):
    hex_number[1] = list(x)
    hex_number[2] = list(y)
    # print(hex_number)
    number_sum = int(''.join(hex_number[1]), 16) + int(''.join(hex_number[2]), 16)
    number_mul = int(''.join(hex_number[1]), 16) * int(''.join(hex_number[2]), 16)
    print(f'defaultdict, Сложение = {list(hex(number_sum))[2:]}, Умножение = {list(hex(number_mul))[2:]}')


calc_defaultdict('A2', 'C4F')


def calc_namedtuple(x, y):
    num = namedtuple('hex_number', 'id number')
    num1 = num(id=1, number=list(x))
    num2 = num(id=1, number=list(y))
    number_sum = int(''.join(num1.number), 16) + int(''.join(num2.number), 16)
    number_mul = int(''.join(num1.number), 16) * int(''.join(num2.number), 16)
    print(f'namedtuple, Сложение = {list(hex(number_sum))[2:]}, Умножение = {list(hex(number_mul))[2:]}')


calc_namedtuple('A2', 'C4F')


class HexCalc:
    def __init__(self, hex_number):
        self.hex_number = list(hex_number)

    def __add__(self, other):
        num1 = int(''.join(self.hex_number), 16)
        num2 = int(''.join(other.hex_number), 16)
        return list(hex(num1 + num2))[2:]

    def __mul__(self, other):
        num1 = int(''.join(self.hex_number), 16)
        num2 = int(''.join(other.hex_number), 16)
        return list(hex(num1 * num2))[2:]


num1 = HexCalc('A2')
num2 = HexCalc('C4F')

print(num1 + num2)
print(num1 * num2)