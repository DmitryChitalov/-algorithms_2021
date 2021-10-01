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
# Решение вариантом 1
from collections import defaultdict

first_num = list(input('Введите 1-е слогаемое: '))  # Сохраняем введеные значения как массив
second_num = list(input('Введите 2-е слогаемое: '))  # Сохраняем введеные значения как массив


# Функция для перевода числа в 16 систему исчисления
def convert_to_10(num_lst: list):
    alphabet = "0123456789ABCDEF"
    dict_num = defaultdict(int)
    for val, key in enumerate(alphabet):
        dict_num[key] = val
    # Формула для перевода числа из 16 в 10 систему
    numbers = sum([dict_num[el] * (16 ** (len(num_lst) - (num_lst.index(el) + 1))) for el in num_lst])
    return numbers


# Использование функции hex() через f-строку (сохранение результата в виде массива)
lst_sum = list(f"{convert_to_10(first_num) + convert_to_10(second_num) :X}")
lst_mul = list(f"{convert_to_10(first_num) * convert_to_10(second_num) :X}")
# Вывод результатов
print(f'Сумма чисел из примера: {lst_sum}')
print(f'Произведение - {lst_mul}')


# Решение вариантом 2, через ООП (Используя функцию, написанную выше)

class Conv():
    def __init__(self, num_lst: list):
        alphabet = "0123456789ABCDEF"
        dict_num = defaultdict(int)
        for val, key in enumerate(alphabet):
            dict_num[key] = val
        # Формула для перевода числа из 16 в 10 систему
        self.number = sum([dict_num[el] * (16 ** (len(num_lst) - (num_lst.index(el) + 1))) for el in num_lst])

    def __add__(self, other):
        return f'{list(f"{self.number + other.number:X}")}'

    def __mul__(self, other):
        return f'{list(f"{self.number + other.number:X}")}'


first_cls = Conv(first_num)
sec_cls = Conv(second_num)
print('---------------------Решение через ООП---------------------')
print(f'Сумма чисел из примера: {first_cls + sec_cls}')
print(f'Произведение - {first_cls * sec_cls}')
