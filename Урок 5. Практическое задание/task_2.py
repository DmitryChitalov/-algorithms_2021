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


first_number = input("Введите первое шестнадцатиричное число - ")
second_number = input("Введите второе шестнадцатиричное число - ")

my_tuple = namedtuple("Numbers", "first_number second_number")

numbers = my_tuple(first_number=list(first_number),
                   second_number=list(second_number))


def sum_numbers():
    return list(hex(int(first_number, 16) + int(second_number, 16))[2:].upper())


def multiply():
    return list(hex(int(first_number, 16) * int(second_number, 16))[2:].upper())


print(numbers)
print(sum_numbers())
print(multiply())
print("--------Вариант с классом---------")


class HexNumbers:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return list(hex(int(self.num, 16) + int(other.num, 16))[2:].upper())

    def __mul__(self, other):
        return list(hex(int(self.num, 16) * int(other.num, 16))[2:].upper())


hx1 = HexNumbers("A2")
hx2 = HexNumbers("C4F")
print(hx1 + hx2)
print(hx1 * hx2)
