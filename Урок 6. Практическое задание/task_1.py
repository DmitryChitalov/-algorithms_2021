"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять только домашние задания с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""
from pympler import asizeof
from numpy import array
from memory_profiler import memory_usage
from timeit import timeit

def memory_time_profiler(func):
    def inner(*args, **kwargs):
        start_time = timeit()
        start_memory = memory_usage()
        result = func(*args, **kwargs)
        print(f'Количество занимаемого времени: {timeit() - start_time}')
        print(f'Количество занимаемой памяти: {memory_usage()[0] - start_memory[0]}')
        return result
    return inner

# Вариант 1
@memory_time_profiler
def get_nums_1(end_num):
    res_list = [i for i in range(end_num + 1) if i % 10 == 0 or i % 10 == 0]
    return res_list

@memory_time_profiler
def get_nums_2(end_num):
    num_list = list(range(end_num + 1))
    for i in num_list:
        if i % 10 == 0 or i % 10 == 0:
            yield i

get_nums_1(1000)
get_nums_2(1000)

"""В отличии от списка генератор занимает очнеь малый объем памяти"""

# Вариант 2

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

class HexNumber_variant:
    __slots__ = ["hex_number"]

    def __init__(self, hex_number):
        self.hex_number = list(str(hex_number))

    def __add__(self, other):
        el_1 = int("".join(self.hex_number), 16)
        el_2 = int("".join(other.hex_number), 16)
        return list(hex(el_1 + el_2))[2:]

    def __mul__(self, other):
        el_1 = int("".join(self.hex_number), 16)
        el_2 = int("".join(other.hex_number), 16)
        return list(hex(el_1 * el_2))[2:]

a = "A2"
b = "C4F"
num_1 = HexNumber(a)
num_2 = HexNumber(b)
num_slot_1 = HexNumber_variant(a)
num_slot_2 = HexNumber_variant(b)
print(asizeof.asizeof(num_1.__dict__))
print(asizeof.asizeof(num_slot_1.__slots__))

"""При использовании slots существенно экономится память"""

# Вариант 3

def memory_time_profiler(func):
    def inner(*args, **kwargs):
        start_time = timeit()
        start_memory = memory_usage()
        result = func(*args, **kwargs)
        print(f'Количество занимаемого времени: {timeit() - start_time}')
        print(f'Количество занимаемой памяти: {memory_usage()[0] - start_memory[0]}')
        return result
    return inner

@memory_time_profiler
def numpy_array():
    elem = array([el for el in range(1000000)])
    return elem

@memory_time_profiler
def list_array():
    elem = list(el for el in range(1000000))
    return elem

numpy_array()
list_array()

"""Библиотека NumPy значительно экономит объем занимаемой памяти"""