"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в виде функции.

Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение. Обязательно сделайте замеры времени обеих реализаций
и укажите дала ли оптимизация эффективность.

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.

Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""

import timeit
import random


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-1, n-1, -1):
            if lst_obj[i] < lst_obj[i-1]:
                lst_obj[i], lst_obj[i-1] = lst_obj[i-1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_optimized(lst_obj):
    n = 1
    while n < len(lst_obj):
        stop = True
        for i in range(len(lst_obj)-1, n-1, -1):
            if lst_obj[i] < lst_obj[i-1]:
                lst_obj[i], lst_obj[i-1] = lst_obj[i-1], lst_obj[i]
                stop = False
        n += 1
        if stop:
            break
    return lst_obj


orig_list = [random.randint(-100, 100) for _ in range(5)]


print(
    timeit.timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))                       # 0.0023228999999999993
print(
    timeit.timeit(
        "bubble_sort_optimized(orig_list[:])",
        globals=globals(),
        number=1000))                       # 0.0019711999999999993

orig_list = [random.randint(-100, 100) for _ in range(100)]

# замеры 100
print(
    timeit.timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))                       # 0.6197293
print(
    timeit.timeit(
        "bubble_sort_optimized(orig_list[:])",
        globals=globals(),
        number=1000))                       # 0.6030686000000001

orig_list = [random.randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(
    timeit.timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))                       # 61.7965873
print(
    timeit.timeit(
        "bubble_sort_optimized(orig_list[:])",
        globals=globals(),
        number=1000))                      # 64.95550169999999

'''
Взяты замеры времени после оптимизации, путём остановки цикла, в случае
если не было перестановок за проход по массиву.
из резултатов видно что на маленьких и средних массивах, есть положительная динамика,
но на большом массиве ухудшение. 
Считаю что данная оптимизация не уместна, так как
по времени одно и тоже, а код выглядит массивней, есть множественное лишнее присваивание True/False флагу остановки.
Время показывает лучше только в том случае если массив в конце будет отсортирован 
'''