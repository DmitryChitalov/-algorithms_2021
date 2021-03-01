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


def hex_number():
    hex_1 = list(input("Введите шестнадцатеричное число: "))
    hex_dct = defaultdict(list)
    for el in range(len(hex_1) - 1, -1, -1):
        hex_dct[el].append(hex_1[len(hex_1) - el - 1])
    return hex_dct


def sum_hex_number(dst_1, dst_2):
    """Сложение столбиком"""
    num_str = '0123456789ABCDEF'
    summ = defaultdict(list)
    for i in range(max(len(dst_1), len(dst_2))):
        x = "".join(dst_1[i])
        y = "".join(dst_2[i])
        summ[i].append(num_str.index(x) + num_str.index(y))
    res = []
    i = 0
    for j in summ.values():
        z = i + j[0]
        if z < 16:
            res.append(num_str[z])
            i = 0
        else:
            res.append(num_str[z % 16])
            i = z // 16
    res.reverse()
    return res


def mul_hex_number(dst_1, dst_2):
    """Умножение столбиком"""
    num_str = '0123456789ABCDEF'
    mul = []
    for i in range(len(dst_1)):
        mul_1 = defaultdict(list)
        for j in range(len(dst_2)):
            x = "".join(dst_1[i])
            y = "".join(dst_2[j])
            mul_1[j].append(num_str.index(x) * num_str.index(y))
        res = []
        i = 0
        for j in mul_1.values():
            z = i + j[0]
            if z < 16:
                res.append(num_str[z])
                i = 0
            else:
                res.append(num_str[z % 16])
                i = z // 16
        res.append(str(i))
        mul.append(res)
    mul_2 = []
    for i in range(len(mul[0]) + 1):
        if i == 0:
            mul_2.append(num_str.index(mul[0][0]))
        elif i == len(mul[0]):
            mul_2.append(num_str.index(mul[1][-1]))
        else:
            mul_2.append(num_str.index(mul[0][i]) + num_str.index(mul[1][i - 1]))
    mul_2.reverse()
    res = []
    i = 0
    for j in mul_2:
        z = i + j
        if z < 16:
            res.append(num_str[z])
            i = 0
        else:
            res.append(num_str[z % 16])
            i = z // 16
    return res


num1 = hex_number()
num2 = hex_number()
print(f"Сумма шестнадцатеричных чисел: {sum_hex_number(num1, num2)}")
print(f"Произведение шестнадцатеричных чисел: {mul_hex_number(num1, num2)}")

"""
Через ООП
"""


class HexNumber:
    def __init__(self, hex_number):
        self.hex_number = list(str(hex_number))

    def __add__(self, other):
        el_1 = int("".join(self.hex_number), 16)
        el_2 = int("".join(other.hex_number), 16)
        return list(hex(el_1 + el_2))[2:]

    def __mul__(self, other):
        el_1 = int("".join(self.hex_number), 16)
        el_2 = int("".join(other.hex_number), 16)
        return list(hex(el_1 * el_2))[2:]


a = "A2"
b = "C4F"
num_1 = HexNumber(a)
num_2 = HexNumber(b)
print(f"Сумма шестнадцатеричных чисел: {num_1 + num_2}")
print(f"Произведение шестнадцатеричных чисел: {num_1 * num_2}")
