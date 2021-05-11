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
from functools import reduce
from timeit import timeit


def check_user_numbers(hex_numbers):
    for num in hex_numbers:
        for digit in num:
            if digit in ('1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'):
                return True


while True:
    numbers = [input(f'Введите {i}-ое число в 16-ой системе счисления: ') for i in range(1, 3)]
    if check_user_numbers(numbers):
        break
    else:
        print('Что-то не так. Повторите ввод')


def add_hex(iterable: list):
    sum_hex = hex(reduce(lambda general, num: general + int(num, 16), iterable, 0))
    return list(str(sum_hex)[2:].upper())


def multiple_hex(iterable: list):
    mul_hex = hex(reduce(lambda general, num: general * int(num, 16), iterable, 1))
    return list(str(mul_hex)[2:].upper())


def get_result_from_dict():
    hex_dict = defaultdict(list)
    for i, number in enumerate(numbers):
        hex_dict[i+1] = [digit for digit in number]
    all_numbers = [f'{number}' for number in hex_dict.values()]
    print(f"Сумма чисел \n{' + '.join(all_numbers)} = {add_hex(numbers)}")
    print(f"Произведение чисел \n{' * '.join(all_numbers)} = {multiple_hex(numbers)}")


print('\nИспользуя словарь:', round(timeit('get_result_from_dict', globals=globals()), 3), 'sec')
get_result_from_dict()

# В данном случае словарь не нужен, можно и списками обойтись


def get_result_from_list():
    all_numbers = [f'{[el for el in num]}' for num in numbers]
    print(f"Сумма чисел \n{' + '.join(all_numbers)} = {add_hex(numbers)}")
    print(f"Произведение чисел \n{' * '.join(all_numbers)} = {multiple_hex(numbers)}")


print('\nИспользуя список:', round(timeit('get_result_from_dict', globals=globals()), 3), 'sec')
get_result_from_list()


class HexNumber:
    def __init__(self, hex_number):
        self.hex_number = hex_number

    def __add__(self, other):
        sum_hex = hex(reduce(lambda general, num: general + int(num, 16), (self.hex_number, other.hex_number), 0))
        return list(str(sum_hex)[2:].upper())

    def __mul__(self, other):
        mul_hex = hex(reduce(lambda general, num: general * int(num, 16), (self.hex_number, other.hex_number), 1))
        return list(str(mul_hex)[2:].upper())

    def __str__(self):
        return f'{[el for el in self.hex_number]}'


hx1 = HexNumber(str(numbers[0]))
hx2 = HexNumber(str(numbers[1]))


def get_result_from_oop():
    print(f'{hx1} + {hx2} =', hx1 + hx2)
    print(f'{hx1} * {hx2} =', hx1 * hx2)


print('\nИспользуя ООП:', round(timeit('get_result_from_oop', globals=globals()), 3), 'sec')
get_result_from_oop()

# Используя словарь: 0.055 sec
# Используя список: 0.042 sec
# Используя ООП: 0.041 sec

# Использование словаря здесь неуместно, занимает лишнюю память и не самое производительное по времени
# Примерно одинаковое время показали алгоритмы с использованием списков и с использованием ООП
# Наиболее гибкий и ясный на мой взгляд является алгоритм с ООП, так что последний вариант предпочтительнее
