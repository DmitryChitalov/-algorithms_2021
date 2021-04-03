"""
2.*	Написать программу сложения и умножения двух шестнадцатеричных чисел.
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
from functools import reduce

class HexNumber:
    def __init__(self, num_hex):
        if num_hex == '':
            self.num_hex = ['0']
        else:
            self.num_hex = list(num_hex)

    def __str__(self):                          # to work as 'str' or 'print'
        return ''.join(self.num_hex)

    def __add__(self, other):                                   # it can add both with the HexNumber class
        return self.__sum_mul(other, True)

    def __mul__(self, other):                                   # it can add both with the HexNumber class
        return self.__sum_mul(other, False)

    def __sum_mul(self, other, is_sum=True):
        # other = (str(other)[2:] if str(other).startswith('0x') else str(other))
        l_1 = self.__hex_to_int(reversed(self.num_hex))         # перевернем список и приведем к десятичному виду
        l_2 = self.__hex_to_int(reversed(list(str(other))))     # перевернем список и приведем к десятичному виду
        if is_sum:
            l_3 = self.__sum_2_list(l_1, l_2)                   # сложим списки
        else:
            l_3 = self.__mul_2_list(l_1, l_2)                   # перемножим списки
        l_3 = self.__int_to_hex_one_sign_per_cell(l_3)          # Переведем список к 16-ричному виду
        return ''.join(reversed(l_3))

    def __int_to_hex(self, l_int):    # Перевод списка из int в hex
        return [hex(int(el))[2:] for el in l_int]

    def __int_to_hex_one_sign_per_cell(self, l_int):    # Перевод списка из int в hex (с поддержкой 1 цифры в ячейке)
        k = 0           # для учета переноса ("хвостика")
        l_hex = []
        for i in range(len(l_int)):
            k, num = divmod((l_int[i] + k), 16)
            l_hex.append(hex(int(num))[2:])
        if k > 0:       # учтем "хвостик"
            l_hex.extend(reversed(list(hex(int(k))[2:])))
        return l_hex

    def __hex_to_int(self, l_hex):    # Перевод списка из hex в int
        # return [str(int(el,16)) for el in l_hex]
        return [int(el,16) for el in l_hex]

    def __sum_2_list(self, l_1=[], l_2=[]):    # Сумма двух списков int произвольной длины
        return list(map(lambda x, y: x + y, l_1, l_2)) + (l_1 if len(l_1) >= len(l_2) else l_2)[min(len(l_1), len(l_2)):]

    def __mul_2_list(self, l_1, l_2):    # Перемножим два списка int
        l_3 = []
        for i in range(len(l_1)):
            l_3 = self.__sum_2_list(l_3, [0 for el in range(i)] + [l_1[i] * el for el in l_2])
        return l_3


def sum_16(*args):
    res_str = ''
    list_16 = list('0123456789ABCDEF')  # Список соответствия десятичной и шестнадцатеричной систем
                                # ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    work_dd = defaultdict(list)  # словарь для обработки
    for el in args:
        for i, x in enumerate(reversed(list(el))):  # занесем в словарь в обратном порядке
            work_dd[i].append(x)                    # с обычным dict выдавало-бы ошибку!!!
    i = 0
    k = '0'         # для учета переноса ("хвостика")
    while i < len(work_dd) or k != '0':
        # просуммируем в десятичной
        work_dd[i].extend(k)  # добавим "хвостик"
        res = sum([list_16.index(el) for el in work_dd[i]])
        k = '0'
        res_str = list_16[(res % 16)] + res_str
        if res > 16:                    # имеется "хвостик"
            k = list_16[(res // 16)]    # перенесем в следующий разряд (храним в 16-ричной)
        i += 1
    return res_str

def mult_16(a, b):
    list_16 = list('0123456789ABCDEF')  # Список соответствия десятичной и шестнадцатеричной систем
                                # ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    a_list = list(a)
    b_list = list(b)
    a_dd = defaultdict(str)     # словарь для 1-го аргумента
    b_dd = defaultdict(str)     # словарь для 2-го аргумента
    c_dd = {}                   # словарь для промежуточного результата
    for i, x in enumerate(reversed(a_list)):    # занесем в словарь в обратном порядке
        a_dd[i] = x
    for i, x in enumerate(reversed(b_list)):    # занесем в словарь в обратном порядке
        b_dd[i] = x
    # Блок расчета
    res_16 = ''
    for i in range(len(a_dd)):
        k = '0'
        for j in range(len(b_dd)):
            # в десятичной умножим и добавим "хвостик"
            res = list_16.index(a_dd[i]) * list_16.index(b_dd[j]) + list_16.index(k)
            k = '0'
            c_dd[j] = list_16[(res % 16)]  # Переведем из десятичной в 16-ричную
            if res > 16:  # имеется "хвостик"
                k = list_16[(res // 16)]  # перенесем в следующий разряд (храним в 16-ричной)
        res_16 = sum_16(res_16, k+''.join(list(reversed(c_dd.values())))+'0'*i)
    return res_16


a = 'A2'
b = 'C4F'
# a, b = input('Введите два шестнадцатиричных числа (через пробел): ').split()

print(f'Сумма ({a} и {b}): {sum_16(a,b)}')
print('Произведение:', mult_16(a,b))

print("Сумма ('A2'): ", sum_16('A2'))                 # Функция суммирования поддерживает произвольное количество аргументов
print("Сумма ('A2', 'C4F'): ", sum_16('A2', 'C4F'))
print("Сумма ('FFF', 'FFF', 'FFF'): ", sum_16('FFF', 'FFF', 'FFF'))
print()


cls_hex_1 = HexNumber(a)
cls_hex_2 = HexNumber(b)
print(f'Через ООП, cls_hex_1 = {cls_hex_1}, cls_hex_2 = {cls_hex_2}')
print('Сумма двух классов "перегрузкой": ', cls_hex_1 + cls_hex_2)
print('Произведение: ', cls_hex_1 * cls_hex_2)

'''
Вывод:
    Времени потратил массу.
    Из положительного - "вспомнил" перегрузку и потренировался ... наконец, разобрался в конвертации 10-и и 16-ричных 
    Честно говоря, решение притянуто за уши к весьма неудобному алгоритму расчета (сложение списков, их умножение)
'''