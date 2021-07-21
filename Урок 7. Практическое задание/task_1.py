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
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


# Идея доработки: ставим флаг 1(True) на операцию перестановки элементов swapped, цикл while работает пока swapped = 1.
# По замерам видно, что данная доработка намного ускоряет выполнение кода.
def bubble_sort2(lst_obj):
    swapped = 1
    while swapped:
        swapped = 0
        for i in range(len(lst_obj) - 1):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                swapped = 1
    return lst_obj


orig_list = [random.randint(-100, 100) for _ in range(10)]
print(orig_list)
print(bubble_sort(orig_list))
# замеры 10
print(
    timeit.timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.randint(-100, 100) for _ in range(10)]
print(orig_list)
print(bubble_sort2(orig_list))
# замеры 10
print(
    timeit.timeit(
        "bubble_sort2(orig_list[:])",
        globals=globals(),
        number=1000))

'''
0.008718799999999999
0.0007810999999999998
'''

orig_list = [random.randint(-100, 100) for _ in range(100)]
print(orig_list)
print(bubble_sort(orig_list))
# замеры 100
print(
    timeit.timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.randint(-100, 100) for _ in range(100)]
print(orig_list)
print(bubble_sort2(orig_list))
# замеры 100
print(
    timeit.timeit(
        "bubble_sort2(orig_list[:])",
        globals=globals(),
        number=1000))

'''
0.2759998
0.005573300000000003
'''

orig_list = [random.randint(-100, 100) for _ in range(1000)]
print(orig_list)
print(bubble_sort(orig_list))
# замеры 1000
print(
    timeit.timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.randint(-100, 100) for _ in range(1000)]
print(orig_list)
print(bubble_sort2(orig_list))
# замеры 1000
print(
    timeit.timeit(
        "bubble_sort2(orig_list[:])",
        globals=globals(),
        number=1000))

'''
29.8596316
0.06326230000000166
'''
