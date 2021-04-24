"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Хотя в примерах к уроку уже есть вариант реализации слияния,
попробуйте предложить другой (придумать или найти)

И попытаться сделать замеры на массивах разной длины: 10, 100, 1000, ...

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""

"""Нашёл похожий вариант"""

import operator
from random import randint
from timeit import timeit

def merge_sort(L, compare=operator.lt):
    if len(L) < 2:
        return L[:]
    else:
        middle = int(len(L) / 2)
        left = merge_sort(L[:middle], compare)
        right = merge_sort(L[middle:], compare)
        return merge(left, right, compare)

def merge(left, right, compare):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

n = int(input("Введите число элементов:"))
orig_list = [randint(0, 50) for _ in range(n)]
print(orig_list)

print(merge_sort(orig_list[:]))

# замеры 10
n = 10
orig_list = [randint(0, 50) for _ in range(n)]
print(timeit("merge_sort(orig_list[:])", globals=globals(), number=1000))

# замеры 100
n = 100
orig_list = [randint(0, 50) for _ in range(n)]
print(timeit("merge_sort(orig_list[:])", globals=globals(), number=1000))

# замеры 1000
n = 1000
orig_list = [randint(0, 50) for _ in range(n)]
print(timeit("merge_sort(orig_list[:])", globals=globals(), number=1000))

"""
Введите число элементов:5
[18, 30, 50, 35, 29]
[18, 29, 30, 35, 50]
0.018980201999999835
0.21166592500000014
2.6454337819999996
"""