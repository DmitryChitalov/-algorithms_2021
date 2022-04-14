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
from timeit import timeit
import random

def merge_sort_origin(lst_obj):
    if len(lst_obj) > 1:
        center = len(lst_obj) // 2
        left = lst_obj[:center]
        right = lst_obj[center:]

        merge_sort_origin(left)
        merge_sort_origin(right)

        # перестали делить
        # выполняем слияние
        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst_obj[k] = left[i]
                i += 1
            else:
                lst_obj[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lst_obj[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst_obj[k] = right[j]
            j += 1
            k += 1
        return lst_obj

import operator
def merge_sort_1(L, compare=operator.lt):
    if len(L) < 2:
        return L[:]
    else:
        middle = int(len(L) / 2)
        left = merge_sort_1(L[:middle], compare)
        right = merge_sort_1(L[middle:], compare)
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


list_origin = [random.uniform(0, 50) for _ in range(10)]

print("Исходный:", list_origin)
print("Отсортированный:", merge_sort_origin(list_origin[:]))

print("\nЗамеры сортировки отстортированного по возрастанию массива из 10 эллементов ")
print(
    timeit(
        "merge_sort_origin(list_origin[:])",
        globals=globals(),
        number=500))
print(
    timeit(
        "merge_sort_1(list_origin[:])",
        globals=globals(),
        number=500))

list_origin = [random.uniform(0, 50) for _ in range(100)]
print("\nЗамеры сортировки отстортированного по возрастанию массива из 100 эллементов ")
print(
    timeit(
        "merge_sort_origin(list_origin[:])",
        globals=globals(),
        number=500))
print(
    timeit(
        "merge_sort_1(list_origin[:])",
        globals=globals(),
        number=500))

list_origin = [random.uniform(0, 50) for _ in range(1000)]
print("\nЗамеры сортировки отстортированного по возрастанию массива из 1000 эллементов ")
print(
    timeit(
        "merge_sort_origin(list_origin[:])",
        globals=globals(),
        number=500))
print(
    timeit(
        "merge_sort_1(list_origin[:])",
        globals=globals(),
        number=500))
