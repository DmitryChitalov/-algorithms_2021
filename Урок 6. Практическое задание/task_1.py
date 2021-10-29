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
import json
from sys import getsizeof
from memory_profiler import memory_usage, profile
from numpy import array
from timeit import default_timer
from collections import namedtuple


def pinpoint(func):
    def wrapper(*args):
        m1 = memory_usage()
        start = default_timer()
        func(*args)
        finish = default_timer()
        m2 = memory_usage()
        print(f'time - {finish - start} memory - {m2[0] - m1[0]}', sep='\n')
    return wrapper

# из урока 4 задание 1
arr = [i for i in range(100000)]

@pinpoint
def func_2(nums):
    new_arr = [i for i in range(100000) if nums[i] % 2 == 0]
    return new_arr

@pinpoint
def add_array(nums):
    new_arr = array([i for i in range(100000) if nums[i] % 2 == 0])
    return new_arr

@pinpoint
def add_gen(nums):
    new_arr = (i for i in range(100000) if nums[i] % 2 == 0)
    return new_arr

@pinpoint
def add_map(nums):
    new_arr = map(str, [i for i in range(100000) if nums[i] % 2 == 0])
    return new_arr

"""
использование array доёт выигрыш по памяти в 2 раза, 
использование map даёт выигрыш примерно 30%,
самый большой выигрыш даёт генератор, что логично)
"""

# из основ урока 3 задание 1

def num_translate():
    numbers = {
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять',
    }
    print(getsizeof(numbers))
    return numbers.get('ten')

def num_translate_tuple():
    dict_ = namedtuple('dict_', ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten'))
    d = dict_(one='один',
              two='два',
              three='три',
              four='четыре',
              five='пять',
              six='шесть',
              seven='семь',
              eight='восемь',
              nine='девять',
              ten='десять'
    )
    print(getsizeof(d))
    return d.ten

class NumTranslate:
    __slots__ = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    def __init__(self, one, two, three, four, five, six, seven, eight, nine, ten):
        self.one = one
        self.two = two
        self.three = three
        self.four = four
        self.five = five
        self.six = six
        self.seven = seven
        self.eight = eight
        self.nine = nine
        self.ten = ten

num_class = NumTranslate('один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять')

"""
с namedtuple мы выигрываем память в 3 раза,
а с использованием слотов чуть больше, чем в 3 раза.
словарь - 360
namedtuple - 120
слоты - 112
"""

# из соснов урока 7 задание 4

import os

def stat():
    for root, dirs, files in os.walk('some_data'):
        size_100000 = [file for file in files if os.stat(os.path.join(root, file)).st_size > 10000]
        size_10000 = [file for file in files if 1000 < os.stat(os.path.join(root, file)).st_size < 10000]
        size_1000 = [file for file in files if 100 < os.stat(os.path.join(root, file)).st_size < 1000]
        size_100 = [file for file in files if os.stat(os.path.join(root, file)).st_size < 100]

    d = {100000: len(size_100000), 10000: len(size_10000), 1000: len(size_1000), 100: len(size_100)}
    print(getsizeof(d))
    return d

def json_stat():
    for root, dirs, files in os.walk('some_data'):
        size_100000 = [file for file in files if os.stat(os.path.join(root, file)).st_size > 10000]
        size_10000 = [file for file in files if 1000 < os.stat(os.path.join(root, file)).st_size < 10000]
        size_1000 = [file for file in files if 100 < os.stat(os.path.join(root, file)).st_size < 1000]
        size_100 = [file for file in files if os.stat(os.path.join(root, file)).st_size < 100]

    d = {100000: len(size_100000), 10000: len(size_10000), 1000: len(size_1000), 100: len(size_100)}
    dumped = json.dumps(d)
    print(getsizeof(dumped))
    return json.loads(dumped)

def tuple_stat():
    for root, dirs, files in os.walk('some_data'):
        size_100000 = [file for file in files if os.stat(os.path.join(root, file)).st_size > 10000]
        size_10000 = [file for file in files if 1000 < os.stat(os.path.join(root, file)).st_size < 10000]
        size_1000 = [file for file in files if 100 < os.stat(os.path.join(root, file)).st_size < 1000]
        size_100 = [file for file in files if os.stat(os.path.join(root, file)).st_size < 100]

    dict_ = namedtuple('dict_', ('k100', 'k10', 'k1', 'k01'))
    d = dict_(k100=len(size_100000), k10=len(size_10000), k1=len(size_1000), k01=len(size_100))
    print(getsizeof(d))
    return d

"""
с использованием json выигрыш почти 2.5 раза по памяти,
а с namedtuple больше, чем в 3 раза
словарь - 235
json - 96
namedtuple - 72
"""

if __name__ == '__main__':
    func_2(arr)
    add_array(arr)
    add_gen(arr)
    add_map(arr)
    num_translate()
    num_translate_tuple()
    print(getsizeof(num_class))
    stat()
    json_stat()
    tuple_stat()