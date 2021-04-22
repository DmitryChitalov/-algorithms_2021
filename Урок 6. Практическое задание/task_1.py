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
from memory_profiler import memory_usage


def memory_profile(func):
    def wrapper(*args):
        start_time = default_timer()
        start_memory = memory_usage()
        func(*args)
        end_time = default_timer()
        end_memory = memory_usage()
        print(f'Временные затраты: {end_time - start_time}\n Затраты памяти: {end_memory[0] - start_memory[0]}')

    return wrapper

# script 1

@memory_profile
def iter_used(lst):
    for i in range(len(lst)):
        lst[i] = str(lst[i])
    return lst


@memory_profile
def map_used(lst):
    return list(map(str, lst))


my_list = [x+10 for x in range(1000000)]
print('\n\nСкрипт 2 \nБез map():')
iter_used(my_list)
print('\nС map():')
map_used(my_list)

'''
Без использования функции map():
Временные затраты: 0.385755195
Затраты памяти: 36.07421875
С использованием функции map():
Временные затраты: 0.2230677710000002
Затраты памяти: 6.78515625
Функция map_used эффективнее

# script 2

@memory_profile
def get_list(n):
    return [i**2 for i in range(n)]


@memory_profile
def get_dict(n):
    return {i**2: i for i in range(n)}

k = 100000

print('\n\nСкрипт 3\nСоздание словаря:')
get_dict(k)
print('\nСоздание списка:')
get_list(k)

'''
Создание словаря:
Временные затраты: 0.15319952100000012
Затраты памяти: 10.96875
Создание списка:
Временные затраты: 0.14219764099999987
Затраты памяти: 5.98828125
Создание словаря занимает больше памяти, чем создание списка
