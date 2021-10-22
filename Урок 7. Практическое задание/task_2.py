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


def merge_sort(sim_arr, compare=operator.lt):
    if len(sim_arr) < 2:
        return sim_arr[:]
    else:
        middle = int(len(sim_arr) / 2)
        left = merge_sort(sim_arr[:middle], compare)
        right = merge_sort(sim_arr[middle:], compare)
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


origin_list_10 = [random.triangular(0, 50) for _ in range(10)]
sort_list_10 = merge_sort(origin_list_10[:])
print(f'Исходный - {origin_list_10}')
print(f'Отсортированный - {sort_list_10}')

print(
    timeit.timeit(
        "merge_sort(origin_list_10[:])",
        globals=globals(),
        number=1000))

origin_list_100 = [random.triangular(0, 50) for _ in range(100)]

print(
    timeit.timeit(
        "merge_sort(origin_list_100[:])",
        globals=globals(),
        number=1000))

origin_list_1000 = [random.triangular(0, 50) for _ in range(1000)]

print(
    timeit.timeit(
        "merge_sort(origin_list_1000[:])",
        globals=globals(),
        number=1000))

'''
Сортировка слиянием  10 элементов = 0.015228374999999999
Сортировка слиянием  100 элементов = 0.234481792
Сортировка слиянием  1 000 элементов = 3.046565042
'''
