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
from functools import reduce
from collections import defaultdict


def sum_hex(first, second):
    """
    Сумма 2-х hex чисел. Возвращаем без 0x.
    :param first: Первое число.
    :param second: Второе число.
    :return: string
    """
    return f"{int(first, 16) + int(second, 16):02X}"


def mul_hex(first, second):
    """
    Произведение 2-х hex чисел. Возвращаем без 0x.
    :param first: Первое число.
    :param second: Второе число.
    :return: string
    """
    return f"{int(first, 16) * int(second, 16):02X}"


def assembly_hex(first, second):
    """
    Сборка строки.
    :param first: Первое число.
    :param second: Второе число.
    :return: string
    """
    return first + second


d = defaultdict(list)

a = input("Введите первое шестнадцатиричное число: ").upper()
# Значение по умолчанию, если пользователь ничего не ввёл. Для демонстрации работы.
a = 'A2' if a == str() else a
d[a] = list(a)
print(d[a])

b = input("Введите второе шестнадцатиричное число: ").upper()
# Значение по умолчанию, если пользователь ничего не ввёл. Для демонстрации работы.
b = 'C4F' if b == str() else b
d[b] = list(b)
print(d[b])

s = sum_hex(reduce(assembly_hex, d[a]), reduce(assembly_hex, d[b]))
d[s] = list(s)
print(f"Сумма чисел: {d[s]}")

m = mul_hex(reduce(assembly_hex, d[a]), reduce(assembly_hex, d[b]))
d[m] = list(m)
print(f"Произведение: {d[m]}")

# print(d)
print("\nВариант 2:")


# Вариант 2.
class HexNumber:
    def __init__(self, my_hex):
        self.hex = my_hex

    def __str__(self):
        return str(list(f"{int(self.hex, 16):02X}"))

    def __add__(self, other):
        return list(f"{int(self.hex, 16) + int(other.hex, 16):02X}")

    def __mul__(self, other):
        return list(f"{int(self.hex, 16) * int(other.hex, 16):02X}")


hx1 = HexNumber(a)
print("Первое шестнадцатиричное число: ", hx1)
hx2 = HexNumber(b)
print("Второе шестнадцатиричное число: ", hx2)
print("Сумма: ", hx1 + hx2)
print("Произведение: ", hx1 * hx2)

