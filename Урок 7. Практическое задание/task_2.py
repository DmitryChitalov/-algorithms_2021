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
import operator


def merge_sort(lst_obj):
    if len(lst_obj) > 1:
        center = len(lst_obj) // 2
        left = lst_obj[:center]
        right = lst_obj[center:]

        merge_sort(left)
        merge_sort(right)

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

# merge_sort_2
def merge_sort_2(x):
    if len(x) < 2:
        return x
    result = []
    mid = int(len(x) / 2)
    y = merge_sort_2(x[:mid])
    z = merge_sort_2(x[mid:])
    i = 0
    j = 0
    while i < len(y) and j < len(z):
        if y[i] > z[j]:
            result.append(z[j])
            j += 1
        else:
            result.append(y[i])
            i += 1
    result += y[i:]
    result += z[j:]
    return result


orig_list = [random.uniform(0,50) for _ in range(10)]

# замеры 10_1
print(
    timeit.timeit(
        "merge_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.uniform(0,50) for _ in range(10)]

# замеры 10_2
print(
    timeit.timeit(
        "merge_sort_2(orig_list[:])",
        globals=globals(),
        number=1000))

print(f'{orig_list}')
print(f'{merge_sort_2(orig_list)}')

orig_list = [random.uniform(0,50) for _ in range(100)]

# замеры 100_1
print(
    timeit.timeit(
        "merge_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.uniform(0,50) for _ in range(100)]

# замеры 100_2
print(
    timeit.timeit(
        "merge_sort_2(orig_list[:])",
        globals=globals(),
        number=1000))

print(f'{orig_list}')
print(f'{merge_sort_2(orig_list)}')

orig_list = [random.uniform(0,50) for _ in range(1000)]

# замеры 1000_1
print(
    timeit.timeit(
        "merge_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.uniform(0,50) for _ in range(1000)]

# замеры 1000_2
print(
    timeit.timeit(
        "merge_sort_2(orig_list[:])",
        globals=globals(),
        number=1000))

print(f'{orig_list}')
print(f'{merge_sort_2(orig_list)}')

"""
Аналитика:
Ускорить не удалось . Веб Алгоритмы выдают либо практические идентичные, либо меньшие цифры.
10
0.013278399999999996
0.015296099999999993
100
0.23768809999999999
0.2344506
1000
3.2199934999999997
3.3893226
"""
