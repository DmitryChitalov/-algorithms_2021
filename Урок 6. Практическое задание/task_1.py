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
from timeit import default_timer
from memory_profiler import memory_usage
from pympler import asizeof
from collections import namedtuple
from recordclass import recordclass
from sys import getsizeof


# __slot__
class HexClass:

    def __init__(self, number):
        self.number = number


name_2 = HexClass(54558)
print(asizeof.asizeof(name_2))  # asizeof.asizeof = 240


class HexClassSlot:
    __slots__ = 'number'

    def __init__(self, number):
        self.number = number


name_1 = HexClassSlot(54558)
print(asizeof.asizeof(name_1))  # asizeof.asizeof = 40

# Уходим от хеша словаря и  получаем уменьшение занимаемой памяти.
# -----------------------------------------------------------------------
# namedtuple Vs recordclass


company = namedtuple('Company', 'one two tree four')
firms = {'Фирма1': company(one=235, two=345634, tree=55, four=235)}
print(f'namedtuple : {getsizeof(firms)}')  # 72
print(f'namedtuple : {asizeof.asizeof(firms)}')  # 168
# recordclass
company_1 = recordclass('Company', 'one two tree four')
firms_1 = company_1(one=235, two=345634, tree=55, four=235)
print(f'recordclass : {getsizeof(firms_1)}')  # 56
print(f'recordclass : {asizeof.asizeof(firms_1)}')  # 864

# Сильной разницы в памяти нет. А если мерить asasizeof наоборот recordclass больше памяти требует.
#  к примеру добавим объекты в словарь firms = {'Фирма1': company(one=235, two=345634, tree=55, four=235)}
# и показатели сравняются  232 б.

# -----------------------------------------------------
# Цикл vs Генератор vs list comprehension
numb = [i for i in range(100000)]


def decor(func):
    def wrapper(*args):
        m1 = memory_usage()
        s1 = default_timer()
        res = func(args[0])
        m2 = memory_usage()
        s2 = default_timer()
        mem = m2[0] - m1[0]
        sec = s2 - s1
        return mem, sec

    return wrapper


@decor
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


mem, sec = func_1(numb)
print(f'Память {mem}, Время {sec} : Цикл')


@decor
def func_2(nums):
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            yield i


mem, sec = func_2(numb)
print(f'Память {mem}, Время {sec} : Генератор')


@decor
def func_3(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


mem, sec = func_3(numb)
print(f'Память {mem}, Время {sec} : list comprehension')

# Память 1.94921875, Время 0.14106090000000004 : Цикл
# Память 0.0, Время 0.10869960000000001 : Генератор
# Память 1.6328125, Время 0.12466069999999996 : list comprehension

# И победитель генератор поскольку он не вычисляет значение всех элементов  а работает только по запросу.
