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
from random import uniform, randint


def merge_sort(lst_obj):
    len_lst = len(lst_obj)
    if len_lst < 2:
        return lst_obj
    left = merge_sort(lst_obj[:len_lst // 2])
    right = merge_sort(lst_obj[len_lst // 2:len_lst])

    i, j = 0, 0
    result = []

    while i < len(left) or j < len(right):
        if not i < len(left):
            result.append(right[j])
            j += 1
        elif not j < len(right):
            result.append(left[i])
            i += 1
        elif left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    return result


random_array_10 = [uniform(0, 50) for _ in range(10)]
random_array_100 = [uniform(0, 50) for _ in range(100)]
random_array_1000 = [uniform(0, 50) for _ in range(1000)]
random_array_10000 = [uniform(0, 50) for _ in range(1000)]

print(random_array_10)
print(merge_sort(random_array_10.copy()))

print(f'Merge sort: 10: {timeit("merge_sort(random_array_10.copy())", globals=globals(), number=1000)}')
print(f'Merge sort: 100: {timeit("merge_sort(random_array_100.copy())", globals=globals(), number=1000)}')
print(f'Merge sort: 1000: {timeit("merge_sort(random_array_1000.copy())", globals=globals(), number=1000)}')
print(f'Merge sort: 10000: {timeit("merge_sort(random_array_10000.copy())", globals=globals(), number=1000)}')

'''
[44.16933717349461, 29.34883145048645, 23.906922823979865, 4.722207468371287, 30.919086489025844, 2.9463867706769786, 6.791529312446659, 14.594206511052626, 7.232636464875042, 34.68259871786476]
[2.9463867706769786, 4.722207468371287, 6.791529312446659, 7.232636464875042, 14.594206511052626, 23.906922823979865, 29.34883145048645, 30.919086489025844, 34.68259871786476, 44.16933717349461]
Merge sort: 10: 0.0170262
Merge sort: 100: 0.2693126
Merge sort: 1000: 3.9904195000000002
Merge sort: 10000: 4.0012417000000005

Сортировка слиянием весьма эффективный способ сортировки. Его минусом и больным местом является 
повышенное использование памяти из-за рекурсии.
'''
