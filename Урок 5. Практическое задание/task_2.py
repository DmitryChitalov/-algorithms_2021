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


nums = defaultdict(list)
nums['первое'] = list(input('Введите первое число: '))
nums['второе'] = list(input('Введите второе число: '))
print(nums)
sum_num = sum([int(''.join(i), 16) for i in nums.values()])
print(sum_num, list('%X' % sum_num))
multip_num = int(''.join(nums['первое']), 16) * int(''.join(nums['второе']), 16)
print(multip_num, list('%X' % multip_num))


class HexOp:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return list(hex(int(''.join(self.num), 16) + int(''.join(other.num), 16)))[2:]

    def __mul__(self, other):
        return list(hex(int(''.join(self.num), 16) * int(''.join(other.num), 16)))[2:]


hex_sum = HexOp(nums['первое']) + HexOp(nums['второе'])
hex_mul = HexOp(nums['первое']) * HexOp(nums['второе'])
print(hex_mul, hex_sum)
