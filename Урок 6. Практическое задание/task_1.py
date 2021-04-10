"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять задачи с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""

import random
from timeit import default_timer, timeit
from memory_profiler import memory_usage, profile
from hashlib import sha256
from uuid import uuid4
from pympler.asizeof import asizeof
from collections import namedtuple
from recordclass import recordclass


def decor(func):
    def wrapper(*args, **kwargs):
        start_time = default_timer()
        start_memory = memory_usage()
        func(*args, **kwargs)
        end_memory = memory_usage()
        end_time = default_timer()
        return f'Функция {func.__name__}\n' \
               f'Замер времени: {end_time - start_time}\n' \
               f'Замер памяти: {end_memory[0] - start_memory[0]}'
    return wrapper


#######################################################################################
"""
Реализуйте скрипт "Кэширование веб-страниц"
Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш
Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
"""


class Caching:
    def __init__(self):
        self.__cache = {}
        self.__salt = uuid4().hex

    def get_page(self, url):
        if self.__cache.get(url):
            print(f'Данный адрес: {url} присутствует в кэше')
        else:
            res = sha256(self.__salt.encode() + url.encode()).hexdigest()
            self.__cache[url] = res
            print(self.__cache)


cache_url = Caching()
cache_url.get_page('https://geekbrains.ru/')
print(f'Размер экземпляра Caching: {asizeof(cache_url)}')
print(timeit("Caching()", number=1000000, globals=globals()))


class CachingOpt:
    __slots__ = ('__cache', '__salt')

    def __init__(self):
        self.__cache = {}
        self.__salt = uuid4().hex

    def get_page(self, url):
        if self.__cache.get(url):
            print(f'Данный адрес: {url} присутствует в кэше')
        else:
            res = sha256(self.__salt.encode() + url.encode()).hexdigest()
            self.__cache[url] = res
            print(self.__cache)


cache_url_opt = CachingOpt()
cache_url_opt.get_page('https://geekbrains.ru/')
print(f'Размер экземпляра CachingOpt: {asizeof(cache_url_opt)}')
print(timeit("CachingOpt()", number=1000000, globals=globals()))

# Размер экземпляра Caching: 792
# 3.015237
# Размер экземпляра CachingOpt: 560
# 2.7285852999999998
# Использования слотов для оптимизации по памяти
# класс с использованием __slots__ быстрее на операциях доступа к атрибутам.
#######################################################################################
"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""


@decor
def company(n):
    companies = namedtuple('company', 'name profit')
    companies_count = n
    companies_lst = []
    for i in range(companies_count):
        name = f'Firm_{i}'
        profit = '100000 200000 300000 400000'
        companies_lst.append(companies(name, sum(map(int, profit.split()))))
    return sum(el.profit for el in companies_lst) / companies_count


@decor
def company_opt(n):
    companies = recordclass('company', 'name profit')
    companies_count = n
    companies_lst = []
    for i in range(companies_count):
        name = f'Firm_{i}'
        profit = '100000 200000 300000 400000'
        companies_lst.append(companies(name, sum(map(int, profit.split()))))
    return sum(el.profit for el in companies_lst) / companies_count


print(company(10000))
print(company_opt(10000))

# Функция company
# Замер времени: 0.22512079999999998
# Замер памяти: 0.46484375
# Функция company_opt
# Замер времени: 0.2489824
# Замер памяти: 0.2734375
# Оптимизации по памяти с использованием recordclass.
# Разница по сравнению с применением namedtuple почти в 2 раза.
#######################################################################################


@decor
def func_2(lst_obj):
    """Функция должная вернуть True, если все элементы списка различаются.
    Алгоритм 1:
    Проходимся по списку и для каждого элемента проверяем,
    что такой элемент отстутствует
    в оставшихся справа элементах
    Сложность: O(N^2).
    """
    for j in range(len(lst_obj)):  # O(N)
        if lst_obj[j] in lst_obj[j + 1:]:  # O(N)
            return False  # O(1)
    return True  # O(1)


lst = random.sample(range(1, 100000), 40000)
print(func_2(lst))

"""""
Line #    Mem usage    Increment  Occurrences   Line Contents
============================================================
    74     22.3 MiB     22.3 MiB           1   @profile
    75                                         def func_2(lst_obj):
    76                                             '''Функция должная вернуть True, если все элементы списка 
                                                   различаются.
    77                                             Алгоритм 1:
    78                                             Проходимся по списку и для каждого элемента проверяем,
    79                                             что такой элемент отстутствует
    80                                             в оставшихся справа элементах
    81                                             Сложность: O(N^2).
    82                                             '''
    83     22.8 MiB      0.0 MiB       40001       for j in range(len(lst_obj)):  # O(N)
    84     22.8 MiB      0.4 MiB       40000           if lst_obj[j] in lst_obj[j + 1:]:  # O(N)
    85                                                     return False  # O(1)
    86     22.8 MiB      0.0 MiB           1       return True  # O(1)
"""


@decor
def func_3(lst_obj):
    """Функция должная вернуть True, если все элементы списка различаются.
    Алгоритм 2:
    Вначале выполним для списка сортировку, далее, сравниваем элементы попарно
    Если присутствуют дубли, они будут находиться рядом.
    Сложность: O(N log N)
    """
    lst_copy = list(lst_obj)  # O(N)
    lst_copy.sort()  # O(N log N)
    for i in range(len(lst_obj) - 1):  # O(N)
        if lst_copy[i] == lst_copy[i + 1]:  # O(1)
            return False  # O(1)
    return True  # O(1)


lst = random.sample(range(1, 100000), 50000)
print(func_3(lst))

"""
Line #    Mem usage    Increment  Occurrences   Line Contents
============================================================
   110     22.3 MiB     22.3 MiB           1   @profile
   111                                         def func_3(lst_obj):
   112                                             ''' Функция должная вернуть True, если все элементы списка 
                                                   различаются.
   113                                             Алгоритм 2:
   114                                             Вначале выполним для списка сортировку, далее, 
                                                   сравниваем элементы попарно
   115                                             Если присутствуют дубли, они будут находиться рядом.
   116                                             Сложность: O(N log N)
   117                                             '''
   118     22.7 MiB      0.4 MiB           1       lst_copy = list(lst_obj)  # O(N)
   119     22.9 MiB      0.2 MiB           1       lst_copy.sort()  # O(N log N)
   120     22.9 MiB      0.0 MiB       50000       for i in range(len(lst_obj) - 1):  # O(N)
   121     22.9 MiB      0.0 MiB       49999           if lst_copy[i] == lst_copy[i + 1]:  # O(1)
   122                                                     return False  # O(1)
   123     22.9 MiB      0.0 MiB           1       return True  # O(1)
"""
# Функция func_2
# Замер времени: 24.3662338
# Замер памяти: 0.2734375
# Функция func_3
# Замер времени: 0.22613390000000066
# Замер памяти: 0.0
