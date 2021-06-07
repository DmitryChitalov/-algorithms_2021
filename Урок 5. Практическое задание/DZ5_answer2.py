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
from functools import reduce

d = defaultdict(list)
number_1 = input('Введите шестнадцатиричное число: ').upper()
number_2 = input('Введите шестнадцатиричное число: ').upper()
oper = input('Введите операцию (+/*): ')

d[number_1] = list(number_1)
d[number_2] = list(number_2)

number_1 = int(f'0x{"".join(d[number_1])}', 16)
number_2 = int(f'0x{"".join(d[number_2])}', 16)
if oper == '+':
    result = reduce(lambda x, y: x + y, [number_1, number_2])
elif oper == '*':
    result = reduce(lambda x, y: x * y, [number_1, number_2])
result = hex(result)[2:].upper()
d[result] = list(result)

print(f'Результат операции: {d[result]}')