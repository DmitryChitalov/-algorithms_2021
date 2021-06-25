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


"""
вариант 1
"""


class HexNumber:
    def __init__(self, num):
        self.num = list(num)

    def __str__(self):
        return f'{self.num}'

    def hex_to_str(self):
        return ''.join(self.num)

    def __add__(self, other):
        result = format(int(self.hex_to_str(), 16) + int(other.hex_to_str(), 16), 'X')
        return HexNumber(result)

    def __mul__(self, other):
        result = list(format(int(self.hex_to_str(), 16) * int(other.hex_to_str(), 16), 'X'))
        return result


a = HexNumber('A2')
b = HexNumber('C4F')
print(a, b)
print(a * b)

"""
вариант 2
"""


def num_to_list(num):
    result = defaultdict(list)
    result[num] = list(num)
    return result


def sum_hex_nums(num1, num2):
    return list(format(int(''.join(num1.keys()), 16) + int(''.join(num2.keys()), 16), 'X'))


def multiplication_hex_nums(num1, num2):
    return list(format(int(''.join(num1.keys()), 16) * int(''.join(num2.keys()), 16), 'X'))


a = num_to_list('A2')
b = num_to_list('C4F')
print(sum_hex_nums(a, b))
print(multiplication_hex_nums(a, b))



