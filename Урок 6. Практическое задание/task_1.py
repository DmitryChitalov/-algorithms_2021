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
from timeit import default_timer
from numpy import array

import memory_profiler


def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_profiler.memory_usage()
        start_time = default_timer()
        res = func(args[0])
        time_diff = default_timer() - start_time
        m2 = memory_profiler.memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff, time_diff

    return wrapper


"""
1 скрипт.
Создать список, состоящий из кубов нечётных чисел от 0 до 1000.
"""
# 1, изначальный вариант
cubes = []


@decor
def check_cubes(lst):
    for i in lst:
        if i % 2 != 0:
            cubes.append(i ** 3)
    return cubes


# 2 вариант
@decor
def cubes_gen(numbers):
    for num in numbers:
        if num % 2 != 0:
            yield num ** 3


# 3 вариант
@decor
def numpy_cubes(arr):
    lst_obj = array([i ** 3 for i in arr if i % 2 != 0])
    return lst_obj


if __name__ == '__main__':
    my_gen, m_diff, t_diff = check_cubes(list(range(10000)))

    print(f"Выполнение check_cubes заняло {m_diff} Mib")
    print(f'Время выполнения check_cubes: {t_diff}')

    my_generator, mem_diff, time_diff = cubes_gen(list(range(10000)))

    print(f"Выполнение cubes_gen заняло {mem_diff} Mib")
    print(f'Время выполнения cubes_gen: {time_diff}')

    m_g, m_d, t_d = numpy_cubes(list(range(10000)))

    print(f"Выполнение numpy_cubes заняло {m_d} Mib")
    print(f'Время выполнения numpy_cubes: {t_d}')

'''
Выполнение check_cubes заняло 0.18359375 Mib
Время выполнения check_cubes - 0.003954102999999987
Выполнение cubes_gen заняло 0.0 Mib
Время выполнения cubes_gen - 8.39500000004989e-06
Выполнение numpy_cubes заняло 0.15625 Mib
Время выполнения numpy_cubes - 0.004544611000000032
1) во втором варианте использовался генератор и выполнение функции заняло 0.0 Mib;
2) в третьем варианте использовались возможности библиотеки numpy, что позволило немного сэкономить ресурсы памяти;
Итог:
3) в данном примере наиболее эффективным оказалось использование генератора (2 вариант), с помощью него расход памяти 
можно минимизировать.
'''

from pympler import asizeof

'''
2 скрипт.
Реализовать класс Road (дорога).
'''


# изначальный вариант
class Road:
    _length: float
    _width: float
    _asphalt_mass: float

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width
        self._asphalt_mass = 25.0

    def weight(self, thickness: float = 1):
        return (self._length * self._width * self._asphalt_mass * thickness) / 1000


mass_1 = Road(20, 5000)
print(f'Общий размер объекта mass_1: {asizeof.asizeof(mass_1)}')


# оптимизированный вариант
class OptimizedRoad:
    _length: float
    _width: float
    _asphalt_mass: float

    __slots__ = ('_length', '_width', '_asphalt_mass')

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width
        self._asphalt_mass = 25.0

    def weight(self, thickness: float = 1):
        return (self._length * self._width * self._asphalt_mass * thickness) / 1000


mass_2 = OptimizedRoad(20, 5000)
print(mass_2.__slots__)
print(f'Общий размер объекта mass_2: {asizeof.asizeof(mass_2)}')

'''
Общий размер объекта mass_1: 416
Общий размер объекта mass_2: 144
Здесь использовались слоты вместо словаря для оптимизации памяти. Для хранения атрибутов и их значений используется
кортеж вместо динамического словаря.
Вывод: слоты удобны для более эффективного использования памяти.
'''

'''
3 скрипт.
Реализуйте скрипт "Кэширование веб-страниц"
Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносить ее в кэш
'''

# 1 вариант
import hashlib
from uuid import uuid4

cache = dict()
salt = uuid4().hex


def checker(url):
    if url in cache.keys():
        print(f'Адрес {url} уже есть в кэше')
    else:
        url_address = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
        cache[url] = url_address


checker('https://yandex.ru')
checker('https://www.google.com/')
checker('https://yandex.ru')
checker('https://gb.ru')
print(f'Общий размер объекта cache: {asizeof.asizeof(cache)}')

# 2 вариант
dumped_cache = json.dumps(cache)
print(f'Общий размер объекта cache после дампа: {asizeof.asizeof(dumped_cache)}')

'''
Общий размер объекта cache: 800
Общий размер объекта cache после дампа: 320
Вывод: после сериализации словаря в json-формат с целью хранения этот объект стал занимать меньше места в памяти.
'''
