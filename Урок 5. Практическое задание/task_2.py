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

dict_hex = defaultdict(str)


def save_dict(el):
    dict_hex[el] = int(el, 16)


def sum_option1(el_1, el_2):
    result = dict_hex[el_1] + dict_hex[el_2]
    return hex(result).replace('0x', '')


def mull_option1(el_1, el_2):
    result = dict_hex[el_1] * dict_hex[el_2]
    return hex(result).replace('0x', '')


# if __name__ == '__main__':
#     param_1 = input('Please enter number one: ')
#     param_2 = input('Please enter number two: ')
#     save_dict(param_1)
#     save_dict(param_2)
#     print(sum_option1(param_1, param_2))
#     print(mull_option1(param_1, param_2))
#     print(dict_hex)


class HexNumber:
    def __init__(self):
        self.el = input('Please enter number: ')

    def __add__(self, other):
        return hex(int(self.el, 16) + int(other.el, 16)).replace('0x', '')

    def __mul__(self, other):
        return hex(int(self.el, 16) * int(other.el, 16)).replace('0x', '')


if __name__ == '__main__':
    hx_1 = HexNumber()
    hx_2 = HexNumber()
    print(hx_1 + hx_2)
    print(hx_1 * hx_2)