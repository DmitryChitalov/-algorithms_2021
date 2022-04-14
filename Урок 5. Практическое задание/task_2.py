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
from functools import reduce


class HexNumber:
    def __init__(self, str_num):
        self.__num__ = list(str_num)

    def __iter__(self):
        self.__a__ = 0
        return self

    def __add__(self, y):
        result = int("".join(self.__num__), 16) + int("".join(y), 16)
        return list(f'{result:X}')

    def __mul__(self, y):
        result = int("".join(self.__num__), 16) * int("".join(y), 16)
        return list(f'{result:X}')

    def __str__(self):
        return str(self.__num__)

    # https://pythonru.com/uroki/iteratory-python-uroki-po-python-dlja-nachinajushhih // для себя
    def __iter__(self):
        self.a = 0
        return self

    def __next__(self):
        if self.a < len(self.__num__):
            x = self.a
            self.a += 1
            return self.__num__[x]
        else:
            raise StopIteration


# Решение 1
numbers = defaultdict(list)
# number_x = 'A2'
# number_y = 'C4F'
number_x = input("Введите 1 значение: ")
number_y = input("Введите 2 значение: ")

numbers['x'] = list(number_x)
numbers['y'] = list(number_y)

num_sum = reduce(lambda x, y: int("".join(x), 16) + int("".join(y), 16), numbers.values())
num_multiplication = reduce(lambda x, y: int("".join(x), 16) * int("".join(y), 16), numbers.values())

print(f'Сумма чисел из примера: {list(hex(num_sum)[2:])}')
print(f'Произведение - : {list(hex(num_multiplication)[2:])}')

# Решение 2
x_obj = HexNumber(number_x)
y_obj = HexNumber(number_y)
print(f'Сумма чисел из примера: {x_obj + y_obj}')
print(f'Произведение - {x_obj * y_obj}')
