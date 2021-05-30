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
import timeit
import random


def bubble_revers_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:  # сортируем по убыванию
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_revers_sort_optimized(lst_obj):
    gap = len(lst_obj)
    swaps = True
    while gap > 1 or swaps:
        gap = max(1, int(gap / 1.25))  # minimum gap is 1
        swaps = False
        for i in range(len(lst_obj) - gap):
            j = i + gap
            if lst_obj[i] > lst_obj[j]:
                lst_obj[i], lst_obj[j] = lst_obj[j], lst_obj[i]
                swaps = True
    return lst_obj


orig_list_10 = [random.randint(-100, 100) for _ in range(10)]

print("замеры 10")
print(
    timeit.timeit(
        "bubble_revers_sort(orig_list_10[:])",
        globals=globals(),
        number=1000))
print(
    timeit.timeit(
        "bubble_revers_sort_optimized(orig_list_10[:])",
        globals=globals(),
        number=1000))
print("---------------------------------------------------------------")
orig_list_100 = [random.randint(-100, 100) for _ in range(100)]

print("замеры 100")
print(
    timeit.timeit(
        "bubble_revers_sort(orig_list_100[:])",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "bubble_revers_sort_optimized(orig_list_100[:])",
        globals=globals(),
        number=1000))
print("---------------------------------------------------------------")
orig_list_1000 = [random.randint(-100, 100) for _ in range(1000)]

print("замеры 1000")
print(
    timeit.timeit(
        "bubble_revers_sort(orig_list_1000[:])",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "bubble_revers_sort_optimized(orig_list_1000[:])",
        globals=globals(),
        number=1000))

"""
замеры 10
0.012790099999999999
0.010164300000000001
---------------------------------------------------------------
замеры 100
0.8254282000000001
0.17965189999999998
---------------------------------------------------------------
замеры 1000
89.3048457
3.011578500000013

Сортировка расческой, основой для которой является пузырек, превосходит по скорости своего родителя.
Расческа начинает проверку элементов с обоих сторон, в отличие от пузырька, который сравнивает ближайшие 2 элемента. 
С каждым шагом как бы выравнивая список и сокращая шаг между проверяемыми элементами.
"""