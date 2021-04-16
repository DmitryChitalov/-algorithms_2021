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
from numpy import array
from pympler import asizeof
from math import factorial
from uuid import uuid4
import hashlib
import json


def my_profile(function):
    def wrapper(*args, **kwargs):
        start_time = default_timer()
        start_memory = memory_usage()
        res = function(*args, **kwargs)
        end_time = default_timer()
        end_memory = memory_usage()
        return end_time - start_time, end_memory[0] - start_memory[0], res

    return wrapper


@my_profile
def eratosthenes_sieve(num):
    n = num * 100
    a = [el for el in range(n + 1)]
    a[1] = 0
    i = 2
    while i <= n:
        if a[i] != 0:
            j = i + i
            while j <= n:
                a[j] = 0
                j = j + i
        i += 1
    a = list(filter(lambda x: x != 0, a))
    return a[num - 1]


@my_profile
def eratosthenes_sieve_numpy(num):
    n = num * 100
    a = array([el for el in range(n + 1)])
    a[1] = 0
    i = 2
    while i <= n:
        if a[i] != 0:
            j = i + i
            while j <= n:
                a[j] = 0
                j = j + i
        i += 1
    a = array(list(filter(lambda x: x != 0, a)))
    return a[num - 1]


class Worker:
    def __init__(self, name, surname, position, wage):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage


class Worker_slots:
    __slots__ = ('name', 'surname', 'position', 'wage')

    def __init__(self, name, surname, position, wage):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage


@my_profile
def fact(n):
    list_fact = []
    for el in range(1, n + 1):
        list_fact.append(factorial(el))
    return list_fact


@my_profile
def fact_gen(n):
    for el in range(1, n + 1):
        yield factorial(el)


@my_profile
def list_pow_2(start_list):
    return [el * el for el in start_list]


@my_profile
def list_pow_2_map(start_list):
    return map(lambda x: x * x, start_list)


def create_url_dict():
    SALT = uuid4().hex
    url_dict = {}

    def url_dict_add(url):
        hash_url = hashlib.sha256(SALT.encode() + url.encode()).hexdigest()
        if not url_dict.get(hash_url):
            url_dict[hash_url] = url

    url_dict_add('https://gb.ru/')
    url_dict_add('https://gb.ru/')
    url_dict_add('https://github.com/')
    url_dict_add('https://mail.google.com/')
    dumped_dict = json.dumps(url_dict)
    return asizeof.asizeof(url_dict), asizeof.asizeof(dumped_dict)


print(f'time = {eratosthenes_sieve(1000)[0]}\nmemory = {eratosthenes_sieve(1000)[1]}')
print(f'time_numpy = {eratosthenes_sieve_numpy(1000)[0]}\nmemory_numpy = {eratosthenes_sieve_numpy(1000)[1]}')

worker_1 = Worker('Kate', 'Smith', 'teacher', 10000)
worker_slots = Worker_slots('Kate', 'Smith', 'teacher', 10000)
print(f'Obj_dict {asizeof.asizeof(worker_1)}')
print(f'Obj_slots_tuple {asizeof.asizeof(worker_slots)}')

print(f'time_factorial = {fact(1000)[0]}\nmemory = {fact(1000)[1]}')
print(f'time_fact_yield = {fact_gen(1000)[0]}\nmemory = {fact_gen(1000)[1]}')

print(f'time_list_pow_2 = {list_pow_2(list(range(10000)))[0]}\nmemory = {list_pow_2(list(range(10000)))[1]}')
print(
    f'time_list_pow_2_map = {list_pow_2_map(list(range(10000)))[0]}\nmemory = {list_pow_2_map(list(range(10000)))[1]}')

print(f'Obj_dict {create_url_dict()[0]}')
print(f'Obj_dumped_dict {create_url_dict()[1]}')

"""
1. Решето Эратосфена(numpy) 
time = 0.23342639999999998
memory = 0.24609375
time_numpy = 0.3444429
memory_numpy = 0.0
При использовании numpy памяти затрачивается меньше, однако время выполнения растет

2. ООП слоты
Obj_dict 336
Obj_slots_tuple 144
При использовании вместо словаря кортежа для хранения атрибутов класса память значительно экономится,
однако необходимо учитывать, что при таком варианте невозможно будет динамически добавить атрибут объекту

3. Списки(yield)
time_factorial = 0.20111820000000002
memory = 0.296875
time_fact_yield = 0.10884779999999994
memory = 0.0
При искользовании ленивых вычислений нет необходимости хранить хранить все разультаты вычислений, а производить их 
только по необходимости. За счет этого экономится время и большое количество памяти.

4. Списки(map)
time_list_pow_2 = 0.11073369999999993
memory = 0.16796875
time_list_pow_2_map = 0.10782299999999978
memory = 0.0
Использование map позволило сэкономить память так как встроенная функция map() возвращает объект map(итератор)

5. Сериализация
Obj_dict 560
Obj_dumped_dict 304
Хранение словаря в виде json объекта значительно экономит память.
"""
