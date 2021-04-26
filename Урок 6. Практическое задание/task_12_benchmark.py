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
from memory_profiler import memory_usage
from numpy import arange


def benchmark(func):
    def wrapper(*args, **kwargs):
        n = 10
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
def sieve(n):
    m = n * 10
    a = [i for i in range(m + 1)]
    a[1] = 0
    i = 2

    while i <= m:
        if a[i] != 0:
            j = i + i
            while j <= m:
                a[j] = 0
                j = j + i
        i += 1

    a = [i for i in a if i != 0]
    return a[n - 1]


@benchmark
def sieve_numpy(n):
    m = n * 10
    np_a = arange(m + 1)
    np_a[1] = 0
    i = 2

    while i <= m:
        if np_a[i] != 0:
            j = i + i
            while j <= m:
                np_a[j] = 0
                j = j + i
        i += 1

    np_a = np_a[np_a != 0]
    return np_a[n - 1]


n_3000 = 3000

print('sieve(3000): ', sieve(n_3000))
print('sieve(3000): ', sieve_numpy(n_3000))

"""
Результаты.
 *** Среднее использование памяти <function sieve at 0x000002BA9D94E1F0> - 0.15234375 MiB.
 *** Общее время выполнения <function sieve at 0x000002BA9D94E1F0> (10 проходов) - 2.3614076999999996 сек.
sieve(3000):  27449
 *** Среднее использование памяти <function sieve_numpy at 0x000002BA9DA3F310> - 0.005859375 MiB.
 *** Общее время выполнения <function sieve_numpy at 0x000002BA9DA3F310> (10 проходов) - 2.373280100000001 сек.
sieve(3000):  27449

В данном варианте алгоритма решето Эратосфена, требуется создание большого массива. При использовании для этих целей
библиотеки NumPy, функцией с "решетом" было использовано 0,006 MiB против 0.152 MiB для функции 
со встроенным списком.
Результаты показывают, что библиотека NumPy хорошо оптимизирована и эффективно управяет ресурсами памяти.
"""
