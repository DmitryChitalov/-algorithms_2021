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

from timeit import timeit
from memory_profiler import memory_usage


def time_memory(func):
    def wrap(*args, **kwargs):
        start_time = timeit()
        start_mem = memory_usage()
        result = func(*args, **kwargs)
        print(f'Time: {start_time - timeit()}\nMemory: {memory_usage()[0] - start_mem[0]}')
        return result
    return wrap


"""
Составление списка четных значений
"""


@time_memory
def list_num_1(number):
    return [el for el in range(number+1) if el % 2 == 0]


@time_memory
def list_num_2(number):
    res_list = []
    for el in range(number):
        if el % 2 == 0:
            res_list.append(el)
    return res_list


list_num_1(100000)
list_num_2(100000)

"""
Генератор быстро, но забивает пямять. Итератор - медленно, но память экономит. 
Time: 0.0005797930002700014
Memory: 1.9375
Time: 0.008691018000263284
Memory: 1.54296875
"""
