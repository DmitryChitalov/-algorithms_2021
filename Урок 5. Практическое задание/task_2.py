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
from functools import reduce
from timeit import timeit


print('1 вариант')


def summa_composition16():
    try:
        dict_lst = defaultdict()
        number1 = input('Введите первое шестнадцатиричное число: ').upper()
        number2 = input('Введите второе шестнадцатиричное число: ').upper()
        dict_lst[1] = list(number1)
        dict_lst[2] = list(number2)
        summa = int(reduce(lambda a, b: a + b, dict_lst[1]), 16) + int(reduce(lambda a, b: a + b, dict_lst[2]), 16)
        composition = int(reduce(lambda a, b: a + b, dict_lst[1]), 16) * int(reduce(lambda a, b: a + b, dict_lst[2]), 16)
        summa = list(hex(summa)[2:].upper())
        composition = list(hex(composition)[2:].upper())
        dict_lst[3] = summa
        dict_lst[4] = composition
        return f'Сумма чисел: {dict_lst[3]}\nПроизведение чисел: {dict_lst[4]}'
    except ValueError:
        print('Неверный ввод')
        return summa_composition16()


print(summa_composition16())
print('_________________________')
print('2 Вариант')


class HexNumber:

    def __init__(self, string):
        self.string = string

    def __add__(self, other):
        # Можно конечно было без deque, но очень понравилось как он превращает строку (быстрее)
        final = deque(hex(int(self.string, 16) + int(other.string, 16)).upper()[2:])
        final = str(final)[6:][:-1]
        return f'Сумма чисел: {final}'

    def __mul__(self, other):
        final = deque(hex(int(self.string, 16) * int(other.string, 16)).upper()[2:])
        final = str(final)[6:][:-1]
        return f'Произведение чисел: {final}'


a = HexNumber('a2')
b = HexNumber('c4f')
print(a+b)
print(a*b)

print('_________________________')
# Замеры list и deque
print('Замеры list и deque')


def list_str(n):
    return list(n)


def deque_str(n):
    return deque(n)


n = '7c9fe'
print(list_str(n))
print(deque_str(n))

print(f'list: {timeit("list_str(n)", globals=globals())}')
print(f'deque: {timeit("deque_str(n)", globals=globals())}')
