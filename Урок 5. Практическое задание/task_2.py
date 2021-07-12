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
from pympler import asizeof
from collections import defaultdict


def fill_list(value):
    numbers = defaultdict(list)
    numbers[value] = list(value)
    return numbers


def sum_values(number_1, number_2):
    return list(format(int("".join(number_1.keys()), 16) + int("".join(number_2.keys()), 16), 'X'))


def composition_numbers(number_1, number_2):
    return list(format(int("".join(number_1.keys()), 16) * int("".join(number_2.keys()), 16), 'X'))


val1 = fill_list("A2")
val2 = fill_list("C4F")

print(f"Сумма {list(val1.values())[0]} и {list(val2.values())[0]} равняется: {sum_values(val1, val2)}")
print(f"Произведение {list(val1.values())[0]} и {list(val2.values())[0]} равняется: {composition_numbers(val1, val2)}")
del val1, val2


print("Реализация на ООП")


class HexNumber:
    __slots__ = ["first", "second"]     # с их использованием занимаемая память стала 424 вместо 640

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def to_str1(self):
        return "".join(self.first)

    def to_str2(self):
        return "".join(self.second)

    def __add__(self, other):
        s = list(hex(int(self.to_str1(), 16) + int(other.to_str2(), 16)))[2:]
        return [f.upper() for f in s]

    def __mul__(self, other):
        s2 = list(hex(int(self.to_str1(), 16) * int(other.to_str2(), 16)))[2:]
        return [f.upper() for f in s2]


hex_1 = list(input('Введите первое шестнадцетиричное число : '))
hex_2 = list(input('Введите второе шестнадцетиричное число : '))

a = HexNumber(hex_1, hex_2)

print("Сумма двух чисел равна: ", a + a)
print("Произведение двух чисел равно: ", a * a)
print("Память : ", asizeof.asizeof(a))
del a



