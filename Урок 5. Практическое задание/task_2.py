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

# 1 вариант
# Решение странное, но как по-другому применить коллекции не придумал

hex_table = defaultdict(int, {'1': 1,
                              '2': 2,
                              '3': 3,
                              '4': 4,
                              '5': 5,
                              '6': 6,
                              '7': 7,
                              '8': 8,
                              '9': 9,
                              'A': 10,
                              'B': 11,
                              'C': 12,
                              'D': 13,
                              'E': 14,
                              'F': 15,
                              })

hex_table_reverse = '0123456789ABCDEF'

first_hex, second_hex = map(list, (input('Введите два шестнадцатеричных числа через пробел: ').split()))


def sum_hex(first, second):
    first = defaultdict(int, {i: v for i, v in enumerate(first[::-1])})
    second = defaultdict(int, {i: v for i, v in enumerate(second[::-1])})
    result = [0]
    for i in range(max(len(first), len(second))):
        result[i] += hex_table[first[i]] + hex_table[second[i]]
        result.append(0)
        if result[i] > 15:
            result[i+1] += 1
            result[i] -= 16
        result[i] = hex_table_reverse[result[i]]
    if not result[-1]:
        result.pop(-1)
    return result[::-1]


def mul_hex(first, second):
    first = defaultdict(int, {i: v for i, v in enumerate(first[::-1])})
    second = defaultdict(int, {i: v for i, v in enumerate(second[::-1])})
    result = [0, 0]
    for i in range(len(second)):
        for k in range(len(first)):
            while len(result) <= k + i + 1:
                result.append(0)
            q, r = divmod((hex_table[first[k]] * hex_table[second[i]]), 16)
            result[k+i] += r
            result[k+i+1] += q
    for i in range(len(result)):
        if result[i] > 16:
            q, r = divmod(result[i], 16)
            result[i] = r
            if len(result) < i + 1:
                result.append(0)
            result[i+1] += q
        result[i] = hex_table_reverse[result[i]]
    return result[::-1]


print('Коллекции: ')
print(''.join(sum_hex(first_hex, second_hex)))
print(''.join(mul_hex(first_hex, second_hex)))


# 2 вариант


class HexNumber:
    def __init__(self, number):
        self.number = list(number)

    def __add__(self, other):
        result = self.convert_to_dec() + other.convert_to_dec()
        return HexNumber(self.convert_to_hex(result))

    def __str__(self):
        return ''.join(self.number)

    def __mul__(self, other):
        result = self.convert_to_dec() * other.convert_to_dec()
        return HexNumber(self.convert_to_hex(result))

    def convert_to_dec(self):
        multiplier = 0
        result = 0
        for elem in reversed(self.number):
            result += hex_table[elem] * (16**multiplier)
            multiplier += 1
        return result

    @staticmethod
    def convert_to_hex(num):
        res = []
        while num > 0:
            num, a = divmod(num, 16)
            res.append(hex_table_reverse[a])
        return res[::-1]


hex_one = HexNumber('A2')
hex_two = HexNumber('C4F')
print('ООП: ')
hex_three = hex_two + hex_one
print(hex_three)
hex_three = hex_two * hex_one
print(hex_three)
