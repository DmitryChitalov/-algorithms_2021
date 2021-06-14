"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Хотя в примерах к уроку уже есть вариант реализации слияния,
попробуйте предложить другой (придумать или найти).

И попытаться сделать замеры на массивах разной длины: 10, 100, 1000, ...

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""

from random import random
from timeit import timeit

n = int(input("Введите число элементов: "))
random_list = [random() * 50 for _ in range(n)]


def merge_sort(lst, start, end):
    if end - start > 1:
        mid = (start + end) // 2
        merge_sort(lst, start, mid)
        merge_sort(lst, mid, end)
        merge_list(lst, start, mid, end)


def merge_list(lst, start, mid, end):
    left = lst[start:mid]
    right = lst[mid:end]
    k = start
    i = 0
    j = 0
    while start + i < mid and mid + j < end:
        if left[i] <= right[j]:
            lst[k] = left[i]
            i = i + 1
        else:
            lst[k] = right[j]
            j = j + 1
        k = k + 1
    if start + i < mid:
        while k < end:
            lst[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < end:
            lst[k] = right[j]
            j = j + 1
            k = k + 1


print(random_list)
merge_sort(random_list, 0, len(random_list))
print(random_list)

print(f"Время сортировки {n} элементов:")
print(timeit("merge_sort(random_list, 0, len(random_list))",
             globals=globals(), number=1000))

"""
Время сортировки 10 элементов:
0.021028531999999878

Время сортировки 100 элементов:
0.31392888200000013

Время сортировки 1000 элементов:
4.60448005

Время сортировки 10000 элементов:
59.270194003
"""

