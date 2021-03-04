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
import time
import memory_profiler
from random import randint


def benchmark(func):
    def wrapper(*args, **kwargs):
        m1 = memory_profiler.memory_usage()
        start = time.time()
        res = func(args[0])
        end = time.time()
        m2 = memory_profiler.memory_usage()
        mem_diff = m2[0] - m1[0]
        time_diff = end - start
        return res, mem_diff, time_diff

    return wrapper


"""Создание списка и словаря. Тут на создание словаря расходуется больше памяти и времени т.к. рассчитываетя хеш и 
реализуется механизм предотвращения коллизий.
"""


@benchmark
def get_list(n):
    return [i for i in range(n)]


@benchmark
def get_dict(n):
    return {key: key for key in range(n)}


res_list, mem_diff, time_diff = get_list(1000000)
print(f'Выполнение заняло {mem_diff} Mib, {"%.4f" % time_diff} секунд.')

res_dict, mem_diff, time_diff = get_dict(1000000)
print(f'Выполнение заняло {mem_diff} Mib, {"%.4f" % time_diff} секунд.')

"""Операции со словарём и списком. Поиск и удаление значения по индексу в списке и по ключу в словаре.
В словаре всё быстрее и меньше памяти, т.к. словарь это хеш таблица
"""


@benchmark
def list_oper(a):
    for i in range(1, 100000, 1000):
        a.pop(i)


@benchmark
def dict_oper(a):
    for i in range(1, 1000000, 1000):
        a.pop(i)


res, mem_diff, time_diff = list_oper(res_list)
print(f'Выполнение заняло {mem_diff} Mib, {"%.4f" % time_diff} секунд.')

res, mem_diff, time_diff = dict_oper(res_dict)
print(f'Выполнение заняло {mem_diff} Mib, {"%.4f" % time_diff} секунд.')

"""При использовании функции map можно достаточно сильно снизить расход памяти"""


@benchmark
def get_new_list(my_list):
    new_list = [i ** 2 for i in my_list]
    return new_list


@benchmark
def get_new_list_opt(my_list):
    new_list = map(lambda i: i ** 2, my_list)
    return new_list


res, mem_diff, time_diff = get_new_list(list(range(10000)))
print(f'Выполнение заняло {mem_diff} Mib, {"%.4f" % time_diff} секунд.')

res, mem_diff, time_diff = get_new_list_opt(list(range(10000)))
print(f'Выполнение заняло {mem_diff} Mib, {"%.4f" % time_diff} секунд.')
