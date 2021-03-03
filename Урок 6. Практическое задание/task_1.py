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
from timeit import default_timer
from memory_profiler import memory_usage, profile
from math import log
from pympler.asizeof import asizeof


def memory_time_profiler(func):
    def inner(*args, **kwargs):
        start_time = default_timer()
        start_memory = memory_usage()
        result = func(*args, **kwargs)
        print(f'Затраты времени: {default_timer() - start_time}')
        print(f'Затраты памяти: {memory_usage()[0] - start_memory[0]}')
        return result

    return inner


#  Мой скрипт с CodeWars
#  TODO:
#  Write a program that will calculate the number of trailing zeros in a factorial of a given number.
#  N! = 1 * 2 * 3 * ... * N
#  Be careful 1000! has 2568 digits...
#  Hint: You're not meant to calculate the factorial. Find another way to find the number of zeros.


@memory_time_profiler
def zeros(n):
    if n == 0:
        return 0
    k = round(log(n, 5))
    z = [int(n / (5 ** i)) for i in range(1, k + 1)]
    return sum(z)


@memory_time_profiler
def zeros_opt(n):
    if n == 0:
        return 0
    k = round(log(n, 5))
    z = (int(n / (5 ** i)) for i in range(1, k + 1))
    return sum(z)


print(zeros(100000000000000000))
print(zeros_opt(100000000000000000))

"""Результаты:
Затраты времени: 0.1051365
Затраты памяти: 0.01953125
24999999999999995
Затраты времени: 0.10917200000000005
Затраты памяти: 0.0
24999999999999995

Несмотря на не самый лучший пример (список получается небольшой), можно пронаблюдать что использование итератора,
вместо создания списка, экономит память.
"""

# Пример 2 - задание 5 из 4 урока
from numpy import array, fromiter


def sieve(n):
    a = [i for i in range(n + 1)]
    a[1] = 0
    i = 2
    while i <= n:  # O(N)
        if a[i] != 0:
            j = i + i
            while j <= n:
                a[j] = 0
                j = j + i  # O(log N)
        i += 1

    a = set(a)

    a.remove(0)
    return sorted(list(a))


@memory_time_profiler
def find_num(n):
    a = sieve(n * 100)
    return a[n - 1]


def sieve_opt(n):
    a = fromiter((i for i in range(n + 1)), int)
    # a = [i for i in range(n + 1)]
    a[1] = 0
    i = 2
    while i <= n:  # O(N)
        if a[i] != 0:
            j = i + i
            while j <= n:
                a[j] = 0
                j = j + i  # O(log N)
        i += 1

    return tuple(x for x in a if x)


@memory_time_profiler
def find_num_opt(n):
    a = sieve_opt(n * 100)
    return a[n - 1]


print(find_num(10000))
print(find_num_opt(10000))

"""
Оригинал:
    Затраты времени: 0.4239111
    Затраты памяти: 0.6171875
С использованием кортежа вместо списка:
    Затраты времени: 0.4115835000000001
    Затраты памяти: 0.25
С использованием кортежа и np.array:
    Затраты времени: 0.7291887000000001
    Затраты памяти: 0.15234375

Вывод: использование кортежа уменьшает затраты памяти в ~2.5 раза почти не влияя на время.
Использование np.array уменьшает затраты памяти в ~4 раза, но вырастает время выполнения скрипта.
"""

# Пример 3
from hashlib import sha256


class Cache:
    def __init__(self):
        self.cache_hash = {}
        self.salt = 'some_salt'

    def add_to_cache(self, url):
        self.cache_hash[url] = sha256(f'{url}{self.salt}'.encode())

    @memory_time_profiler
    def check_url(self, url):
        if not self.cache_hash.get(url):
            self.add_to_cache(url)
        else:
            print('in cache')


cache = Cache()

cache.check_url('https://geekbrains.ru/')
print(f'Размер экземпляра класса: {asizeof(cache)}')


class CacheOpt:
    __slots__ = ('cache_hash', 'salt')

    def __init__(self):
        self.cache_hash = {}
        self.salt = 'some_salt'

    def add_to_cache(self, url):
        self.cache_hash[url] = sha256(f'{url}{self.salt}'.encode())

    @memory_time_profiler
    def check_url(self, url):
        if not self.cache_hash.get(url):
            self.add_to_cache(url)
        else:
            print('in cache')


cache_opt = CacheOpt()

cache_opt.check_url('https://geekbrains.ru/')
print(f'Размер экземпляра класса: {asizeof(cache_opt)}')

"""
Замеры обьекта cache:
    Затраты времени: 0.11075360000000001
    Затраты памяти: 0.0
    Размер экземпляра класса: 672

Замеры обьекта cache_opt:
    Затраты времени: 0.1108722000000002
    Затраты памяти: 0.0
    Размер экземпляра класса: 448
    
Вывод: несмотря на то, что декоратор не показывает изменение памяти, используя pympler.asizeof можно 
пронаблюдать что использование слотов в классах может сэкономить память.
"""

# Пример 4. Сериализация. Урок 1, задание 4
import json


@profile
def authentication1(login, password):
    with open('accounts.json', 'r') as f:
        data = json.load(f)
        if data[login][0] != password:
            print('Login or password is incorrect')
        elif not data[login][1]:
            print('Please activate your account')
        elif data[login][0] == password and data[login][1]:
            print('Success')


authentication1('ivan', 'password')


accounts = {'ivan': ['password', 1],  # login: [password, is_active]
            'fedor': ['qwerty123', 0],
            'vasiliy': ['vasiliy', 1]}


@profile
def authentication2(login, password, data=accounts):
    if data[login][0] != password:
        print('Login or password is incorrect')
    elif not data[login][1]:
        print('Please activate your account')
    elif data[login][0] == password and data[login][1]:
        print('Success')


authentication2('ivan', 'password')

print(f'size of json: {asizeof(json.dumps(accounts))}')
print(f'size of dict: {asizeof(accounts)}')

"""В данном примере memory profile показывает инкремент 0.0 MiB в обоих случаях, 
но если замерить размер словаря и json файла - второй будет меньше в ~5 раза:
size of json: 128
size of dict: 800"""