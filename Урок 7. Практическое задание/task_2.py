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
import numpy as np
import operator

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


orig_list = [random.uniform(0,50) for _ in range(10)]
print(f'Исходный массив            : {orig_list}')
print(f'Отсортированный массив     : {merge_sort(orig_list[:])}')

# замеры 10
print(
    timeit.timeit(
        "merge_sort(orig_list[:])",
        globals=globals(),
        number=1000))


orig_list = [random.uniform(0,50) for _ in range(100)]
print(f'Исходный массив            : {orig_list}')
print(f'Отсортированный массив     : {merge_sort(orig_list[:])}')

# замеры 100
print(
    timeit.timeit(
        "merge_sort(orig_list[:])",
        globals=globals(),
        number=1000))


orig_list = [random.uniform(0,50) for _ in range(1000)]
print(f'Исходный массив            : {orig_list}')
print(f'Отсортированный массив     : {merge_sort(orig_list[:])}')

# замеры 1000
print(
    timeit.timeit(
        "merge_sort(orig_list[:])",
        globals=globals(),
        number=1000))
"""
Попытка 1

замер 10
0.08398820000000007
замер 100
0.9893521999999999
замер 1000
15.9870899

Попытка 2

замер 10
0.0753995999999999
замер 100
0.9053216000000002
замер 1000
16.176525100000003

Попытка 3

замер 10
0.08484009999999986
замер 100
1.3644018999999998
замер 1000
12.3606444

Попытка 4

замер 10
замер 100
замер 1000

Попытка 5

замер 10
замер 100
замер 1000

"""