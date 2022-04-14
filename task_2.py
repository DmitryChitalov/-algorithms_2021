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


# вариант2
class HexNumber:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        num = str(hex(int(self.num, 16) + int(other.num, 16)).upper())[2:]
        return num

    def __mul__(self, other):
        num = str(hex(int(self.num, 16) * int(other.num, 16)).upper())[2:]
        return num


# вариант1
hex_nums = defaultdict(list)

num_1 = input("Введите первое шестнадцатиричное число: ").upper()
num_2 = input("Введите второе шестнадцатиричное число: ").upper()

first = HexNumber(num_1)
second = HexNumber(num_2)

print(first + second)
print(first * second)

hex_nums[num_1] = list(num_1)
hex_nums[num_2] = list(num_2)

int_num_1 = int(''.join(hex_nums[num_1]), 16)
int_num_2 = int(''.join(hex_nums[num_2]), 16)

sum_nums = int_num_1 + int_num_2
mult_nums = int_num_1 * int_num_2

sum_hex = list(hex(sum_nums).upper())[2:]
mult_sum = list(hex(mult_nums).upper())[2:]

print(sum_hex)
print(mult_sum)
