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
import timeit
from functools import reduce

from memory_profiler import memory_usage


def benchmark(func):
    def wrapper(*args, **kwargs):
        n = 5
        mem_usage = []
        time = 0
        for _ in range(n):
            start_timer = timeit.default_timer()
            memory_1 = memory_usage()[0]
            result = func(*args, **kwargs)
            mem_usage.append(memory_usage()[0] - memory_1)
            time += timeit.default_timer() - start_timer
        print(f' *** Среднее использование памяти {func} - {sum(mem_usage) / n} MiB.')
        print(f' *** Общее время выполнения {func} ({n} проходов) - {time} сек.')
        return result
    return wrapper


@benchmark
def print_list_1():
    new_list = [el for el in range(100, 10001) if el % 2 == 0]
    result = reduce((lambda mul, cur: mul + cur), new_list)
    print(result)


@benchmark
def print_list_2():
    new_list = (el for el in range(100, 10001) if el % 2 == 0)
    result = reduce((lambda mul, cur: mul + cur), new_list)
    print(result)


print_list_1()
print_list_2()

"""
Результаты:
 *** Среднее использование памяти <function print_list_1 at 0x000001FAA49338B0> - 0.0375 MiB.
 *** Общее время выполнения <function print_list_1 at 0x000001FAA49338B0> (5 проходов) - 1.0067525000000002 сек.
 
 *** Среднее использование памяти <function print_list_2 at 0x000001FAA4933B80> - 0.00078125 MiB.
 *** Общее время выполнения <function print_list_2 at 0x000001FAA4933B80> (5 проходов) - 1.0184408 сек.
 
 Для оптимизации использования памяти в функции print_list_2 был использовано генератор, вместо list comprehension.
 Теперь нет необходимости хранить список в памяти.
"""
