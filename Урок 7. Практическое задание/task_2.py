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


def merge_sort(lst_obj:list):
    def merging(left, right):
        i, k, result = 0, 0, []
        while i < len(left) and k < len(right):
            if left[i] <= right[k]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[k])
                k += 1
        result.extend(left[i:] if i < len(left) else right[k:])
        return result

    def merge(lst:list):
        if len(lst) <= 1:
            return lst
        else:
            return merging(merge(lst[:len(lst) // 2]), merge(lst[len(lst) // 2:]))
    return merge(lst_obj)

orig_list = [random.randint(-100, 100) for i in range(10)]
print(
    timeit.timeit(
        "merge_sort(orig_list[:])",
        globals=globals(),
        number=1000), f'\nИсходный: {orig_list},\nОтсортированный: {merge_sort(orig_list)}')

orig_list = [random.randint(-100, 100) for i in range(100)]


print(
    timeit.timeit(
        "merge_sort(orig_list[:])",
        globals=globals(),
        number=1000), f'\nИсходный: {orig_list},\nОтсортированный: {merge_sort(orig_list)}')

orig_list = [random.randint(-100, 100) for i in range(1000)]


print(
    timeit.timeit(
        "merge_sort(orig_list[:])",
        globals=globals(),
        number=1000), f'\nИсходный: {orig_list},\nОтсортированный: {merge_sort(orig_list)}')


# Быстрее алгоритм работать не стал, на уроке был показан самый оптимальный и понятный вариант,
# который приводится абсолютно на каждом сайте, уроке. Очень сложно заново изобрести велосипед, да и незачем
