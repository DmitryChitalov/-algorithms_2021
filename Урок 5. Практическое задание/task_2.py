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


def hex_calc():
    num_dct = defaultdict(list)
    first_num = input('Введите первое число:')
    second_num = input('Введите второе число:')

    num_dct[first_num].extend(hex(int(first_num, 16)))
    num_dct[second_num].extend(hex(int(second_num, 16)))

    num_dct[hex(int(first_num, 16) + int(second_num, 16))].extend(hex(int(first_num, 16) + int(second_num, 16)))
    num_dct[hex(int(first_num, 16) * int(second_num, 16))].extend(hex(int(first_num, 16) * int(second_num, 16)))

    return f'Сумма чисел - {num_dct[hex(int(first_num, 16) + int(second_num, 16))]} \n' \
           f'Произведение - {num_dct[hex(int(first_num, 16) * int(second_num, 16))]}'


class HexNumber:
    def __init__(self, num: str):
        self.number = int(num, 16)

    def __add__(self, other):
        return list(hex(self.number + other.number))

    def __mul__(self, other):
        return list(hex(self.number * other.number))

if __name__ == '__main__':
    #print(hex_calc())

    a1 = HexNumber('A2')
    a2 = HexNumber('C4F')
    print(a1 + a2)
    print(a1 * a2)
