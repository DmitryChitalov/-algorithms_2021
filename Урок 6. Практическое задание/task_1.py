"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
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
from memory_profiler import memory_usage, profile
from collections import namedtuple
from collections import deque
from timeit import default_timer


def decor(func):
    def wrapper(*args):
        start_time = default_timer()
        m1 = memory_usage()
        res = func(*args)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        end_time = default_timer()
        print(f'Затрачено {end_time - start_time} сек.')
        print(f"Объем памяти: {mem_diff} Mib")
        return res, mem_diff

    return wrapper


# Пример 1

@decor
def func_1(num):
    numbers_list = list(range(num))
    for i in numbers_list:
        return i


@decor
def func_2(num):
    numbers_list = list(range(num))
    for i in numbers_list:
        yield i


print('Пример 1')
result_1, mem_diff_1 = func_1(100000)
result_2, mem_diff_2 = func_2(100000)


# При использовании ленивых вычислений(генератора) память не тратится, поэтому если не нужно хранить массив
# то лучше использовать генератор.
# По времени они практически идентичны.

# Пример 2

@decor
def func_3(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


@decor
def func_4(nums):
    return (i for i in range(len(nums)) if nums[i] % 2 == 0)


print('Пример 2')
my_list = [el for el in range(10000000)]
result_3, mem_diff_3 = func_3(my_list)
result_4, mem_diff_4 = func_4(my_list)


# В первой функции новый массив с отобранными эдлементами сохраняется и занимает много памяти.
# Во второй используется генератор который возвращает элементы поочередно
# Память и время намного ниже во второй функции.

# Пример 3
@decor
def func_5(num):
    for i in range(len(num)):
        num[i] = str(num[i])
    return num


@decor
def func_6(num):
    return list(map(str, num))


print('Пример 3')
func_5(my_list)
func_6(my_list)

# Преобразование списка чисел в список строк через функцию map сокращает время и объем памяти в несколько раз.
