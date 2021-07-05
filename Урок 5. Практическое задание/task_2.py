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
# 1. вариант
from collections import defaultdict
from functools import reduce

nums = defaultdict(list)
nums[1] = "A2"
nums[2] = "C4F"

sum_nums = reduce(lambda x, y: int("".join(x), 16) + int("".join(y), 16), nums.values())
mul_nums = reduce(lambda x, y: int("".join(x), 16) * int("".join(y), 16), nums.values())

print("Сумма чисел - ", list('%X' % sum_nums))
print("Произведение - ", list('%X' % mul_nums))

# 2. вариант
class HexNumber:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return HexNumber(format((self.num + other.num), 'X'))

    def __mul__(self, other):
        return HexNumber(format((self.num * other.num), 'X'))

    def __str__(self):
        return f'{list(self.num)}'


print(f'Сумма чисел - {HexNumber(int("A2", 16))+HexNumber(int("C4F", 16))}')
print(f'Произведение - {HexNumber(int("A2", 16))*HexNumber(int("C4F", 16))}')