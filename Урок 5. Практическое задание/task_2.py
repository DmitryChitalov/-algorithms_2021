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


def function_1(num_1, num_2):
    def_dict = defaultdict(list)
    def_dict[num_1] = list(num_1)
    def_dict[num_2] = list(num_2)
    def_dict['sum'] = list(hex(int(num_1, 16) + int(num_2, 16))[2:])
    def_dict['multiplication'] = list(hex(int(num_1, 16) * int(num_2, 16))[2:])
    return f'{num_1} + {num_2} = {"".join(def_dict["sum"])}\n' \
           f'{num_1} * {num_2} = {"".join(def_dict["multiplication"])}\n' \
           f'{def_dict[num_1]} + {def_dict[num_2]} = {def_dict["sum"]}\n' \
           f'{def_dict[num_1]} * {def_dict[num_2]} = {def_dict["multiplication"]}'


print(f'{function_1.__name__}\n{function_1("A2", "C4F")}')
print('=' * 60)


class HexNumber:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return list(hex(int(self.num, 16) + int(other.num, 16))[2:])

    def __mul__(self, other):
        return list(hex(int(self.num, 16) * int(other.num, 16))[2:])


number_1 = HexNumber('A2')
number_2 = HexNumber('C4F')
print(f'Сложение: {number_1 + number_2}')
print(f'Умножение: {number_1 * number_2}')
