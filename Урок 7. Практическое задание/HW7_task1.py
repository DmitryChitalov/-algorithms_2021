"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в виде функции.

Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение. Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.

Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""

import random
import timeit


def bubble_sort_unoptimized(some_lst):
    """Выполняет самую простую сортировку пузырьком"""
    for i in range(len(some_lst)):
        for j in range(len(some_lst) - 1):
            if some_lst[j] < some_lst[j + 1]:
                some_lst[j], some_lst[j + 1] = some_lst[j + 1], some_lst[j]
    return some_lst


def bubble_sort_optimized1(some_lst):
    """Сортировка пузырьком с использованием маркера"""
    flag = True
    while flag:
        flag = False
        for i in range(len(some_lst) - 1):
            if some_lst[i] < some_lst[i + 1]:
                some_lst[i], some_lst[i + 1] = some_lst[i + 1], some_lst[i]
                flag = True
    return some_lst


orig_list = [random.randint(-100, 100) for i in range(1000)]

print(
    timeit.timeit(
        "bubble_sort_unoptimized(orig_list)",
        globals=globals(),
        number=100))
print(
    timeit.timeit(
        "bubble_sort_optimized1(orig_list)",
        globals=globals(),
        number=100))


"""
если сортировать один и тот же список, то после оптимизации, он уже отсортирован за первое прохождение циклов, следующие 99 замеров не имеют смысла
Нужно поместить генерацию списка внутрь функции


"""
def bubble_sort_unoptimized_1():
    """Выполняет самую простую сортировку пузырьком"""
    some_lst = [random.randint(-100, 100) for i in range(1000)]
    #print(some_lst)
    for i in range(len(some_lst)):
        for j in range(len(some_lst) - 1):
            if some_lst[j] < some_lst[j + 1]:
                some_lst[j], some_lst[j + 1] = some_lst[j + 1], some_lst[j]
    #print(some_lst)
    return some_lst


def bubble_sort_optimized1_1():
    """Сортировка пузырьком с использованием маркера"""
    some_lst = [random.randint(-100, 100) for i in range(1000)]
    #print(some_lst)
    flag = True
    while flag:
        flag = False
        for i in range(len(some_lst) - 1):
            if some_lst[i] < some_lst[i + 1]:
                some_lst[i], some_lst[i + 1] = some_lst[i + 1], some_lst[i]
                flag = True
    #print(some_lst)
    return some_lst

print(
    timeit.timeit(
        "bubble_sort_unoptimized_1()",
        globals=globals(),
        number=100))
print(
    timeit.timeit(
        "bubble_sort_optimized1_1()",
        globals=globals(),
        number=100))
