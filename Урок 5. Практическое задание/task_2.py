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

# Решение 1
from collections import defaultdict
from functools import reduce

numbers = defaultdict(list)
numbers[1] = list(input("Введите 1 значение: "))
numbers[2] = list(input("Введите 2 значение: "))

sum_nums = reduce(lambda x, y: int("".join(x), 16) + int("".join(y), 16), numbers.values())
multiplication_nums = reduce(lambda x, y: int("".join(x), 16) * int("".join(y), 16), numbers.values())

print(f'Сумма чисел из примера: {list(hex(sum_nums)[2:].upper())}')
print(f'Сумма чисел из примера: {list(hex(multiplication_nums)[2:].upper())}')

""" не понимаю чем здесь defaultdict хоть как то полезен
    как и другие коллекции...
"""

# Решение 2

class HexNumber:
    def __init__(self, str_num):
        self.num = list(str_num)

    def __iter__(self):
        self.a = 0
        return self

    def __next__(self):
        if self.a < len(self.num):
            x = self.a
            self.a += 1
            return self.num[x]
        else:
            raise StopIteration

    def __add__(self, other):
        sum_nums = int("".join(self.num), 16) + int("".join(other), 16)
        return list(f"{sum_nums:X}")

    def __mul__(self, other):
        multi_nums = int("".join(self.num), 16) * int("".join(other), 16)
        return list(f"{multi_nums:X}")

    def __str__(self):
        return f"{self.num}"


a = HexNumber("A2")
b = HexNumber("C4F")
print(a + b)
print(a * b)

""" а вот ООП идеально подходит"""
