"""
Задание 1.

Выполните профилирование памяти в скриптах.
Проанализируйте результат и определите программы с
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

from memory_profiler import memory_usage
from timeit import default_timer
from pympler import asizeof
from numpy import array


# Декоратор для измерения времени и памяти
def decor(func):
    def wrapper(*args):
        start_time = default_timer()
        m1 = memory_usage()
        res = func(*args)
        m2 = memory_usage()
        time_diff = default_timer() - start_time
        mem_diff = m2[0] - m1[0]
        print(f"m1 = {m1} Mib, m2 = {m2} Mib\nВыполнение заняло {mem_diff} Mib, {time_diff} sec")
        return res

    return wrapper


# Задача 1. Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего.
# [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# Вариант 1.
@decor
def smaller_big_1(lst):
    return [lst[i + 1] for i in range(len(lst) - 1) if lst[i] < lst[i + 1]]


# Вариант 2.
@decor
def smaller_big_2(lst):
    for i in range(len(lst) - 1):
        if lst[i] < lst[i + 1]:
            yield lst[i + 1]


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
v1 = smaller_big_1(src)
v2 = smaller_big_2(src)


# Выводы.
# m1 = [30.5390625] Mib, m2 = [30.54296875] Mib
# Выполнение заняло 0.00390625 Mib, 0.22180960000000005 sec

# m1 = [30.54296875] Mib, m2 = [30.54296875] Mib
# Выполнение заняло 0.0 Mib, 0.2183005 sec

# Генераторы возвращают элементы один за другим, а не как списки - любое количество элементов сразу.
# Текущие затраты памяти сведены практически к нулю.

# Задача 2. Генератор нечётных чисел от 1 до 10000 (включительно), квадрат которых меньше 10000000
# без использования ключевого слова yield. Полностью истощить генератор, сохранив результаты в список вида:
# ['next(gen1) 1', 'next(gen1) 3', 'next(gen1) 5', 'next(gen1) 7', 'next(gen1) 9', 'next(gen1) 11',
# 'next(gen1) 13',...]
# Вариант 1.
@decor
def gen1():
    n = 10000
    lst = []
    gen1 = (i for i in range(1, n + 1, 2) if i ** 2 < 10000000)
    for i in gen1:
        res = f"next(gen1) {i}"
        lst.append(res)
    return lst


# Вариант 2.
@decor
def gen2():
    n = 10000
    lst = []
    gen2 = (i for i in range(1, n + 1, 2) if i ** 2 < 10000000)
    for i in gen2:
        res = f"next(gen2) {i}"
        lst.append(res)
    return array(lst)


print(f"gen1() = lst: {asizeof.asizeof(gen1())} байт")
print(f"gen2() = array(lst): {asizeof.asizeof(gen2())} байт")


# Выводы.
# m1 = [30.66796875] Mib, m2 = [30.80078125] Mib
# Выполнение заняло 0.1328125 Mib, 0.2107055 sec
# gen1() = lst: 113912 байт

# m1 = [31.11328125] Mib, m2 = [31.11328125] Mib
# Выполнение заняло 0.0 Mib, 0.2336054999999999 sec
# gen2() = array(lst): 94984 байт

# Бибилиотека NumPy оптимизирует большой объем данных и эффективно управляет ресурсами памяти.
# Замеры декоратором с memory_profiler.memory_usage и замеры pympler.asizeof.asizeof() показывают
# снижение расхода ресурсов даже на небольшом списке при использовании numpy.array().

# Задача 3. Программа сложения и умножения двух шестнадцатиричных чисел (ООП).
# Вариант 1.
class HexNumber:
    def __init__(self, a):
        self.lst = list(a)

    def __str__(self):
        return f'{self.lst}'

    def int_lst(self):
        d1 = []
        n = 0
        for d in reversed(list(map(lambda x: int(x, 16), self.lst))):
            d1.insert(0, d * 16 ** n)
            n += 1
        return d1

    def __add__(self, other):
        d1 = sum(self.int_lst())
        d2 = sum(other.int_lst())
        res = (hex(d1 + d2).upper())[2:]
        return HexNumber(res)

    def __mul__(self, other):
        d1 = sum(self.int_lst())
        d2 = sum(other.int_lst())
        res = (hex(d1 * d2).upper())[2:]
        return HexNumber(res)


HN_OBJ = HexNumber('A2')
print(HN_OBJ.__dict__)
print(f'Объём занимаемой списком атрибутов HexNumber памяти: {asizeof.asizeof(HN_OBJ)} байт')


# Вариант 2.
class HexNumber2:
    __slots__ = ['lst']

    def __init__(self, a):
        self.lst = list(a)

    def __str__(self):
        return f'{self.lst}'

    def int_lst(self):
        d1 = []
        n = 0
        for d in reversed(list(map(lambda x: int(x, 16), self.lst))):
            d1.insert(0, d * 16 ** n)
            n += 1
        return d1

    def __add__(self, other):
        d1 = sum(self.int_lst())
        d2 = sum(other.int_lst())
        res = (hex(d1 + d2).upper())[2:]
        return HexNumber(res)

    def __mul__(self, other):
        d1 = sum(self.int_lst())
        d2 = sum(other.int_lst())
        res = (hex(d1 * d2).upper())[2:]
        return HexNumber(res)


HN_OBJ2 = HexNumber2('A2')
print(HN_OBJ2.__slots__)
print(f'Объём занимаемой списком атрибутов HexNumber2 памяти: {asizeof.asizeof(HN_OBJ2)} байт')

# Выводы.
# {'lst': ['A', '2']}
# Объём занимаемой списком атрибутов HexNumber памяти: 392 байт

# ['lst']
# Объём занимаемой списком атрибутов HexNumber2 памяти: 224 байт

# Использование слотов позволяет сохранить атрибуты в менее затратном по памяти контейнере,
# в данном случае - списке.
