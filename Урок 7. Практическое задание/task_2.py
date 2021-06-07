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

import timeit
import random

def merge_two_list(a, b):
    lst = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            lst.append(a[i])
            i += 1
        else:
            lst.append(b[j])
            j += 1
    if i < len(a):
        lst += a[i:]
        if j < len(b):
            lst += b[j:]
    return lst


def merge_sort(lst_obj):
    if len(lst_obj) == 1:
        return lst_obj
    center = len(lst_obj) // 2
    left = merge_sort(lst_obj[:center])
    right = merge_sort(lst_obj[center:])
    return merge_two_list(left, right)


orig_list = [random.uniform(0, 50) for _ in range(10)]

print(f'Не отсортированный массив - {orig_list}')
print(f'Отсортированный массив - {merge_sort(orig_list)}')

# замеры 10
print(
    timeit.timeit(
        "merge_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.uniform(0, 50) for _ in range(100)]

# замеры 100
print(
    timeit.timeit(
        "merge_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.uniform(0, 50) for _ in range(1000)]

# замеры 1000
print(
    timeit.timeit(
        "merge_sort(orig_list[:])",
        globals=globals(),
        number=1000))
