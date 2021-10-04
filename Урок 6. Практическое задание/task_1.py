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

from pympler.asizeof import asizeof
from memory_profiler import profile, memory_usage
from timeit import default_timer


# Создаем декоратор для замеров памяти и времени исполнения
def time_profiler(func):
    def wrapper(*args):
        t1 = default_timer()
        m1 = memory_usage()
        res = func(*args)
        mem_diff = memory_usage()[0] - m1[0]
        time_diff = default_timer() - t1
        return res, mem_diff, time_diff

    return wrapper


#######################################################################################################################

# Скрипт №1 (Задача: Написать регулярное выражение для парсинга файла логов web-сервера)

import requests
import re


# Замеряем время выполнения  и использованную память
@time_profiler
def parcing():
    URL = 'https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
    r = requests.get(URL)
    re_find = re.compile(r'(\d*[.]\d*[.]\d*[.]\d*).*\[(.*?)] .(\S*).(\S*).*(\d{3}).(\d+)')
    parsed_raw = re_find.findall(r.text)
    return parsed_raw


# Выводим результаты
# Использованная память - 28.25
# Время выполнения скрипта - 0.876896
mem_use, time_run = parcing()[1:]
print(f'Использованная память - {mem_use} \nВремя выполнения скрипта - {time_run}')


# Замер той же функции с помощью profile
@profile
def parcing():
    URL = 'https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
    r = requests.get(URL)
    re_find = re.compile(r'(\d*[.]\d*[.]\d*[.]\d*).*\[(.*?)] .(\S*).(\S*).*(\d{3}).(\d+)')
    parsed_raw = re_find.findall(r.text)
    return parsed_raw


# Результаты замеров parcing():
'''
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    64     26.9 MiB     26.9 MiB           1   @profile
    65                                         def parcing():
    66     26.9 MiB      0.0 MiB           1       URL = 'https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
    67     36.7 MiB      9.8 MiB           1       r = requests.get(URL)
    68     36.7 MiB      0.0 MiB           1       re_find = re.compile(r'(\d*[.]\d*[.]\d*[.]\d*).*\[(.*?)] .(\S*).(\S*).*(\d{3}).(\d+)')
    69     61.8 MiB     25.1 MiB           1       parsed_raw = re_find.findall(r.text)
    70     61.8 MiB      0.0 MiB           1       return parsed_raw
'''


# Оптимизируем функцию и делаем замеры

@time_profiler
def parcing_opt():
    URL = 'https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
    r = requests.get(URL)
    re_find = re.compile(r'(\d*[.]\d*[.]\d*[.]\d*).*\[(.*?)] .(\S*).(\S*).*(\d{3}).(\d+)')
    # Сохраняем логи не в оперативной памяти, а на жестком диске
    print(re_find.findall(r.text), file=open('log.txt', 'w'))
    return 'Done'


# Использованная память - 4.37109375
# Время выполнения скрипта - 1.4851861999999998
mem_use, time_run = parcing_opt()[1:]
print(f'Использованная память - {mem_use} \nВремя выполнения скрипта - {time_run}')

# Сравнение:

# Изначальная функция parcing()
# Использованная память - 28.25
# Время выполнения скрипта - 0.876896

# Оптимизированная функция parcing_opt()
# Использованная память - 4.37109375
# Время выполнения скрипта - 1.4851861999999998

'''
Аналитика скрипта 1:
Оптимизируя скрипт парсинга, вместо получения и сохранения данных в переменной я сохранил их на жестком диске,
тем самым слегка увеличил время выполнения скрипта, но и сократил объем используемой памяти в 7 раз
'''


#######################################################################################################################

# Скрипт №2 (Задача: Создать список, состоящий из кубов нечётных чисел от 1 до 1000000)

@time_profiler
def cub_num():
    numbers = [i ** 3 for i in range(1, 1000000, 2)]
    return numbers


# Использованная память - 26.734375
# Время выполнения скрипта - 0.4754028000000001
# mem_use, time_run = cub_num()[1:]
# print(f'Использованная память - {mem_use} \nВремя выполнения скрипта - {time_run}')

# Оптимизируем функцию, используя модуль NumPy
import numpy as np


@time_profiler
def cub_num_opt():
    numb = np.arange(1, 1000000, 2)  # Создаем массив c нечетными цифрами от 1 до 1000000 используя NumPy
    numb = np.power(numb, 3)  # Возводим весь массив в куб
    return numb


# Использованная память - 1.92578125
# Время выполнения скрипта - 0.21873620
# mem_use, time_run = cub_num_opt()[1:]
# print(f'Использованная память - {mem_use} \nВремя выполнения скрипта - {time_run}')

# Сравнение:

# Изначальная функция cub_num()
# Использованная память - 26.734375
# Время выполнения скрипта - 0.4754028000000001

# Оптимизированная функция cub_num_opt()
# Использованная память - 1.92578125
# Время выполнения скрипта - 0.21873620

'''
Аналитика скрипта 2:
Используя полученные данные, можно сделать вывод, что для создания и использования массивов и работой с числами 
лучше использовать библиотеку NumPy, которая ускоряет время выполнения скрипта и существенно уменьшает объем
используемой памяти. В моем случае объем потребляемой памяти сокращается в 13 раз
'''


#######################################################################################################################

# Скрипт №3
# Задача: Реализовать класс «Дата», функция-конструктор которого должна принимать дату.
class Date:
    """Дата"""

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"{self.day:02}.{self.month:02}.{self.year:04}"


dt = Date(1, 1, 2020)
print(f'Разамер класса без слотов = {asizeof(dt)}')  # 384


# Оптимизируем класс коллекцией slots

class DateOpt:
    """Дата"""
    __slots__ = ('day', 'month', 'year')

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"{self.day:02}.{self.month:02}.{self.year:04}"


dt_opt = DateOpt(1, 1, 2020)
print(f'Разамер класса с использованием слотов = {asizeof(dt_opt)}')  # 120

'''
Аналитика скрипта №3:
Благодаря коллекции __slots__ можно сократить размер потребляемой памяти в 3 раза
Что видно, исходя из замеров 2х идентичных классов, где в последнем используется __slots__ для минимизации
затрат оперативной памяти
'''
