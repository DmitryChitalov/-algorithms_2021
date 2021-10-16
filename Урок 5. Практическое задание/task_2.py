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

from collections import defaultdict, deque
from itertools import zip_longest


# Сложение чисел
def sum_hex(in_a, in_b):
    a = in_a.copy()
    a.reverse()
    b = in_b.copy()
    b.reverse()
    input_data = zip_longest(a, b, fillvalue='0')
    res_sum = deque([])
    transfer = 0
    for i in input_data:
        res_pos = d.get(i[0]) + d.get(i[1]) + transfer
        num_in_pos = res_pos % 16
        transfer = res_pos // 16
        res_sum.appendleft(d.get(num_in_pos))
    return res_sum  # ''.join(res_sum).upper()


# Умножение чисел
def mul_hex(in_a, in_b):
    a = in_a.copy()
    a.reverse()
    b = in_b.copy()
    b.reverse()
    sum_list = []
    for pos, i in enumerate(a, start=0):
        transfer = 0
        res_sum = deque([])
        for j in b:
            res_pos = d.get(i) * d.get(j) + transfer
            num_in_pos = res_pos % 16
            res_sum.appendleft(d.get(num_in_pos))
            transfer = res_pos // 16
        while True:
            res_pos = transfer
            num_in_pos = transfer % 16
            res_sum.appendleft(d.get(num_in_pos))
            transfer = res_pos // 16
            if transfer == 0:
                break
        for_extend = ['0' for _ in range(pos)]
        res_sum.extend(for_extend)
        sum_list.append(res_sum)
    res_mul = sum_list[0]
    # складываем результаты перемножения и получаем итог
    for i in sum_list[1:]:
        res_mul = sum_hex(res_mul, i)
    return res_mul


# ---- Ввод результатов

a_in = list(input('Введите первое число в шестнадцатеричной системе: ').lower())
b_in = list(input('Введите второе число в шестнадцатеричной системе: ').lower())
# a_in = ['a', '2']
# b_in = ['c', '4', 'f']
input_data = []
d = defaultdict(list)
res_sum = deque([])
for i in range(16):
    d[hex(i)[2:3:1]] = i
    d[i] = hex(i)[2:3:1]

# Выводим результат
print('Результат сложения - ', *list(sum_hex(a_in, b_in)), sep='')
print('Результат умножения - ', *list(mul_hex(a_in, b_in)), sep='')

# Проверка:
# print(int('a2', 16))
# print(int('c4f', 16))
# print(int('cf1', 16))
