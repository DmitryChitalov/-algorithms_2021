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
from random import randint
from memory_profiler import memory_usage
from timeit import default_timer


def dec_time_mem_usage(func):
    """
    Декоратор замера времени и памяти
    """

    def wrapper(*args, **kwargs):
        memory = memory_usage()
        time = default_timer()
        n = func(*args, **kwargs)
        print(f'Время выполнения {default_timer() - time} выделено памяти {memory_usage()[0] - memory[0]} MiB')
        return n

    return wrapper


"""
Пример 1
"""


@dec_time_mem_usage
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


@dec_time_mem_usage
def func_2(nums):
    return (i for i in range(len(nums)) if nums[i] % 2 == 0)


print('Первый пример')

test1 = func_1([randint(0, 1000) for _ in range(50000)])
test2 = func_2([randint(0, 1000) for _ in range(50000)])

"""
Время выполнения 0.004479399999999967 ; выделено памяти 1.1328125 MiB
Время выполнения 1.1500000000053134e-05 ; выделено памяти 0.0 MiB

LC позволяет сократить объем памяти при большом массиве данных
"""

"""
Пример 2
Сравнение LC и Генератора
"""


@dec_time_mem_usage
def func3():
    my_list = [i for i in range(9999999)]
    return my_list


@dec_time_mem_usage
def func4():
    my_list = (i for i in range(9999999))
    yield my_list


print('Второй пример')

test3 = func3()

test4 = func4()

"""
Время выполнения 0.46675349999999993 выделено памяти 386.390625 MiB
Время выполнения 5.000000000032756e-06 выделено памяти 0.0 MiB

Генератор использует меньше памяти , т.к. не хранит целый список, а выдает элемент
при необходимости
"""

"""
Пример 3, Решето Эратосфена
"""

my_list = [randint(1, 100) for i in range(100000)]


@dec_time_mem_usage
def eratosthenes_sieve():
    number = my_list[:]
    number[1] = 0
    i = 2
    while i < len(number):
        if number[i] != 0:
            j = i + i
            while j < len(number):
                number[j] = 0
                j = j + i
        i += 1

    return number


@dec_time_mem_usage
def eratosthenes_sieve_del():
    clear_arr = []
    number2 = my_list[:]
    number2[1] = 0
    i = 2
    while i < len(number2):
        if number2[i] != 0:
            j = i + i
            while j < len(number2):
                number2[j] = 0

                j = j + i
        i += 1
    for x in number2:
        if x != 0:
            clear_arr.append(i)
    del number2
    return clear_arr


print('Третий пример')

test5 = eratosthenes_sieve()

test6 = eratosthenes_sieve_del()

'''
Время выполнения 0.04158190000000017 выделено памяти 0.765625 MiB
Время выполнения 0.049283399999999755 выделено памяти 0.0546875 MiB

В первой функциии удаляем нулевые элименты и выводим список этих элементов. Затрачиваем память на этот список.

Во второй функции проходим по уже готовому списку и от обратного, не нулевые элементы дабавляем в новый список, потом
удаляем не нужный список.

Затраты по времени примерно равны, память выигрываем во второй функции.

'''
