"""
2.*	Написать программу сложения и умножения двух шестнадцатиричных чисел.
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
"""
from collections import defaultdict


class HexNumber:

    def __init__(self, number):
        def is_hex(s):
            try:
                int(s, 16)
                return True
            except ValueError:
                return False

        while is_hex(number) is not True:
            print(f'Введённые данные не являются числом из 16-ой системы счисления!')
            number = input(f'Введённые число, принадлежащее 16-ой системе счисления: ')

        self.number = int(number, 16)

    def __str__(self):
        return str([x for x in hex(self.number)[2:]]).upper()

    def __add__(self, other):
        result = hex(self.number + other.number)
        return HexNumber(result)

    def __mul__(self, other):
        result = hex(self.number * other.number)
        return HexNumber(result)


print(HexNumber('A2') + HexNumber('C4F'))
print(HexNumber('A2') * HexNumber('C4F'))


def hex_num(num1, num2):

    hex_dict = defaultdict(list, num1=[x for x in num1], num2=[x for x in num2])

    addition = [x for x in hex(int(num1, 16) + int(num2, 16))[2:].upper()]
    multi = [x for x in hex(int(num1, 16) * int(num2, 16))[2:].upper()]
    print(f'Сумма числа {hex_dict["num1"]} и числа {hex_dict["num2"]} равно {addition}\n'
          f'Произведение числа {hex_dict["num1"]} и числа {hex_dict["num2"]} равно {multi}')


hex_num('A2', 'C4F')
