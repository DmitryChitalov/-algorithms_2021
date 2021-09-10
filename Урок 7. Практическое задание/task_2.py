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
from random import uniform


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

# Вывод.
# Сортировка слиянием является эффективным способом сортировки.
# Минусом является повышенное использование памяти из-за рекурсии.

# [24.182076681066082, 33.32813795695211, 20.26849910282292, 44.91151443372275, 16.504840025719535, 34.25894490739566, 1.0877946058703236, 35.40070309973549, 28.698904664157087, 10.694005703310976]
# [1.0877946058703236, 10.694005703310976, 16.504840025719535, 20.26849910282292, 24.182076681066082, 28.698904664157087, 33.32813795695211, 34.25894490739566, 35.40070309973549, 44.91151443372275]
# Merge sort: 10: 0.0436454
# Merge sort: 100: 0.5256658999999999
# Merge sort: 1000: 7.2867692
# Merge sort: 10000: 7.314221799999999
