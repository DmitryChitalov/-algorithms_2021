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

import collections

hx_dec = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
          'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

dec_hx = {'0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9',
          '10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F'}

# 1. вариант


def get_dec(hx_in):
    dec_out = 0
    for i in range(len(hx_in)):
        dec_out += hx_dec[hx_in.pop()] * pow(16, i)
    return dec_out


def get_hx(dec_in):
    hx_out = collections.deque()
    while dec_in != 0:
        hx_out.appendleft(dec_hx[str(dec_in % 16)])
        dec_in //= 16
    return hx_out


# 2. вариант


class HexNumber:

    def __init__(self, num: str):
        try:
            self.hex = int(num, 16)
        except ValueError as ex:
            self.hex = int('FF', 16)

    def __add__(self, other):
        if type(other) is HexNumber:
            return f"{(self.hex + other.hex):X}"
        else:
            return f"{(int(str(other), 16) + self.hex):X}"

    def __mul__(self, other):
        if type(other) is HexNumber:
            return f"{(self.hex * other.hex):X}"
        else:
            return f"{(int(str(other), 16) * self.hex):X}"


if __name__ == '__main__':
    s_in1 = list('A2')
    s_in2 = list('C4F')
    hx1 = collections.deque(s_in1)
    hx2 = collections.deque(s_in2)

    dec1 = get_dec(hx1)
    dec2 = get_dec(hx2)
    print(f"Got numbers {s_in1}, {s_in2}")

    summ_dec = dec1 + dec2
    summ_hx = get_hx(summ_dec)
    print(f"The sum of {s_in1} and {s_in2} is {str(summ_hx)}")

    mul_dec = dec1 * dec2
    mul_hx = get_hx(mul_dec)
    print(f"The product of {s_in1} and {s_in2} is {str(mul_hx)}")

    num1 = HexNumber('A2')
    num2 = HexNumber('C4F')

    print(num1 + num2)
    print(num1 * num2)
