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

from collections import deque


def convert_hex_to_int(num_str):
    # Здесь функция преобразует введенное 16-ричное число к десятичному виду.
    num_deq = deque(num_str)
    rate = 0        # разряд числа
    ret_val = 0     # возвращаемое значение
    while len(num_deq):
        ret_val += int(num_deq.pop(), 16) * 16 ** rate
        rate += 1

    return ret_val


class HexNum:
    def __init__(self, num_str):
        self.num = convert_hex_to_int(num_str)

    def __add__(self, other):
        return hex(self.num + other.num)

    def __mul__(self, other):
        return hex(self.num * other.num)


n1_str, n2_str = input('Введите первое 16-ричное число: '), input('Введите второе 16-ричное число: ')

print('# Вариант с применением deque')
n1 = convert_hex_to_int(n1_str)
n2 = convert_hex_to_int(n2_str)
# print(f'{n1_str} преобразовано в десятичное {n1}')
# print(f'{n2_str} преобразовано в десятичное {n2}')
print(f'{n1_str} + {n2_str} = {hex(n1 + n2)}')
print(f'{n1_str} * {n2_str} = {hex(n1 * n2)}')

print('# Вариант с применением ООП (хотя он и ссылается на функцию, в которой используется deque)')
print(f'{n1_str} + {n2_str} = {HexNum(n1_str) + HexNum(n2_str)}')
print(f'{n1_str} * {n2_str} = {HexNum(n1_str) * HexNum(n2_str)}')

print('# Вариант без коллекций и ООП')
print(f'{n1_str} + {n2_str} = {hex(int(n1_str, 16) + int(n2_str, 16))}')
print(f'{n1_str} * {n2_str} = {hex(int(n1_str, 16) * int(n2_str, 16))}')
