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


from pympler import asizeof
import numpy as np
import json
from timeit import default_timer
from memory_profiler import memory_usage
import re


def decor(func):
    def wrapper(*args):
        m1 = memory_usage()
        t1 = default_timer()
        res = func(*args)
        m2 = memory_usage()
        t2 = default_timer()
        print(f'Memory {m2[0] - m1[0]}\nTime {t2 - t1}')
        return res
    return wrapper


@decor
def func_1():                           # Memory 4.53125
    return [i for i in range(100000)]   # Time 0.10799049999999999


@decor
def func_2():                # Memory 0.00390625
    for i in range(100000):  # Time 0.10806309999999997
        yield i


@decor
def func_3():                                    # Memory 0.33984375
    return np.array([i for i in range(100000)])  # Time 0.1223398


# func_1()
# func_2()
# func_3()
"""
Один из самых простых способов оптимизации памяти это использовать функцию генератор,
как видно из замеров func_2() значительно превосходит func_1() в испорльзовании пвмяти
это достигается тем что генератор возвращаят результат вычисления не весь сразу как LC,
а один за другим. Так же использовал функцию array модуля numpy для оптимизации func_3
что позволило выиграть в исполизовании памяти существенную разницу, но он так же уступает 
генератору.
"""
#################################################################################################


@decor
def func_4():
    parse = re.compile(r'(^[\d.]+)[\D]+([0-9a-zA-Z/: +]+)\S \"(GET) ([/a-z_\d]+) \S+ (\d+) (\d)')
    with open('nginx_logs.txt') as f:
        dict_1 = []
        for line in f:
            for i in parse.findall(line):  # Memory 23.52734375
                dict_1.append(i)           # Time 0.24651939999999994
        return dict_1


@decor
def func_5():
    parse = re.compile(r'(^[\d.]+)[\D]+([0-9a-zA-Z/: +]+)\S \"(GET) ([/a-z_\d]+) \S+ (\d+) (\d)')
    with open('nginx_logs.txt') as f:
        with open('file.json', 'w', encoding='utf-8') as file:
            for line in f:
                for i in parse.findall(line):  # Memory 0.546875
                    json.dump(i, file)         # Time 0.7116757


@decor
def func_6():
    parse = re.compile(r'(^[\d.]+)[\D]+([0-9a-zA-Z/: +]+)\S \"(GET) ([/a-z_\d]+) \S+ (\d+) (\d)')
    with open('nginx_logs.txt') as f:                                      # Memory 28.17578125
        return np.array(list(map(lambda x: parse.findall(x), f)), object)  # Time 0.2771439


def func(line):
    parse = re.compile(r'(^[\d.]+)[\D]+([0-9a-zA-Z/: +]+)\S \"(GET) ([/a-z_\d]+) \S+ (\d+) (\d)')
    for i in parse.findall(line):
        return i


@decor
def func_7():
    with open('nginx_logs.txt') as f:                   # Memory 23.6171875
        return np.array(list(map(func, f)), object)     # Time 0.29386390000000007


# print(asizeof.asizeof(func_4()))  # 21797744
# print(asizeof.asizeof(func_6()))  # 411816
"""
Ещё один способ оптимизации памяти это сохранение результата вычисления в json формат, что позволяет
значительно уменьшить её потребление как видно из замеров func_4 (Memory 23.5) и func_5 (Memory 0.54)
Так же я попробовал оптимизировать скрипт через map и np.array в func_6 но на момент работы функции
использование памяти стало больше чем изначально, я думаю что это связано с тем что результат парсинга
иначально сохраняется в обычный массив и только потом в np.array, но конечный результат работы функции
func_6 (411816) конечно же превосходит функцию func_4 (21797744) в 52 раза по объёму памяти результата
вычисления. Так же получилось улудшить производительность func_6 по памяти func_7(): путём переноса вычисления 
парсинга в отдельную функцию func(line):
"""
######################################################################################################


class Cell:
    def __init__(self, nums):
        self.nums = nums

    def result(self, value):
        return '\n'.join(['x' * value for _ in range(self.nums // value)]) + '\n' + 'x' * (self.nums % value)

    def __str__(self):
        return str(self.nums)

    def __add__(self, other):
        return Cell(self.nums + other.nums)

    def __mul__(self, other):
        return Cell(self.nums * other.nums)

    def __truediv__(self, other):
        return Cell(round(self.nums / other.nums))

    def __sub__(self, other):
        return Cell(self.nums - other.nums if self.nums - other.nums > 0 else print('Incorrect value of first cell'))


class CellSlot:
    __slots__ = ['nums']

    def __init__(self, nums):
        self.nums = nums

    def result(self, value):
        return '\n'.join(['x' * value for _ in range(self.nums // value)]) + '\n' + 'x' * (self.nums % value)

    def __str__(self):
        return str(self.nums)

    def __add__(self, other):
        return Cell(self.nums + other.nums)

    def __mul__(self, other):
        return Cell(self.nums * other.nums)

    def __truediv__(self, other):
        return Cell(round(self.nums / other.nums))

    def __sub__(self, other):
        return Cell(self.nums - other.nums if self.nums - other.nums > 0 else print('Incorrect value of first cell'))


cell_1 = Cell(45)
cell_2 = Cell(17)
# print((cell_1 + cell_2).result(10))
cell_3 = CellSlot(45)
cell_4 = CellSlot(17)
print(asizeof.asizeof(cell_1.__dict__))   # 192
print(asizeof.asizeof(cell_3.__slots__))  # 120
"""
В этой задаче я использовал метод __slots__ для оптимизации и этот метод действительно 
уменьшил потребления памяти где то в 1.5 раза, это не очень большая разница для одного 
экземпляра, но масштаб может вырасти когда экземпляров будет много. Так же хотелось бы добавить
что, теперь мы можем создать только те атрибуты, которые были предусмотренны заранее. 
"""
