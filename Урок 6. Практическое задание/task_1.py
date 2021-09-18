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

from memory_profiler import memory_usage
from timeit import default_timer
from pympler import asizeof
from numpy import array


def decor(func):
    def wrapper(*args):
        start_time = default_timer()
        m1 = memory_usage()
        res = func(*args)
        m2 = memory_usage()
        time_diff = default_timer() - start_time
        mem_diff = m2[0] - m1[0]
        print(f"m1 = {m1} Mib, m2 = {m2} Mib\ncompleted in {mem_diff} Mib, {time_diff} sec")
        return res

    return wrapper


# 1


def func1(number, even=0, odd=0):
    if number == 0:
        return even, odd
    else:
        if number % 10 % 2 == 0:
            even += 1
        else:
            odd += 1
        return func1(number // 10, even, odd)


@decor
def main_f(num):
    print(f'even and odd numbers: {func1(num)}')


@decor
def func2(number, even=0, odd=0):
    while number > 0:
        if number % 10 % 2 == 0:
            even += 1
        else:
            odd += 1
        number //= 10
    return even, odd


main_f(8734563)
print(f'even and odd numbers: {func2(6655523002)}')


# 2


@decor
def func3(num):
    return [i for i in range(0, len(num), 2)]


@decor
def func4(num):
    return array([i for i in range(0, len(num), 2)])


nums = [num ** 2 for num in range(1000000)]

func3(nums)
func4(nums)


# 3


@decor
def func5(lst):
    return [lst[i + 1] for i in range(len(lst) - 1) if lst[i] < lst[i + 1]]


@decor
def func6(lst):
    for i in range(len(lst) - 1):
        if lst[i] < lst[i + 1]:
            yield lst[i + 1]


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
v1 = func5(src)
v2 = func6(src)
