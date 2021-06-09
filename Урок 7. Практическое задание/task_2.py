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

# подсмотрено на https://habr.com/ru/post/510970/


def iter_merge(list1, list2):
    result, it1, it2 = [], iter(list1), iter(list2)
    el1 = next(it1, None)
    el2 = next(it2, None)
    while el1 is not None or el2 is not None:
        if el1 is None or (el2 is not None and el2 < el1):
            result.append(el2)
            el2 = next(it2, None)
        else:
            result.append(el1)
            el1 = next(it1, None)
    return result


# но на слияние не как на хабре, там с генераторами в основном, поэтому решил так
def merge_sort(arr):
    if len(arr) == 1:
        return arr
    middle = len(arr) // 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])
    return iter_merge(left, right)


def custom():
    n = int(input('Введите число элементов: '))
    orig_list = [random.randint(0, 50) + random.random() for _ in range(n)]
    return f'Исходный - {orig_list}\nОтсортированный - {merge_sort(orig_list)}'


print(custom())
orig_list = [random.randint(0, 50) + random.random() for _ in range(10)]

# замеры 10
print(
    timeit.timeit(
        "merge_sort(orig_list[:])",
        globals=globals(),
        number=1000))
print('# замеры 10\n')
orig_list2 = [random.randint(0, 50) + random.random() for _ in range(100)]

# замеры 100
print(
    timeit.timeit(
        "merge_sort(orig_list2[:])",
        globals=globals(),
        number=1000))
print('# замеры 100\n')
orig_list3 = [random.randint(0, 50) + random.random() for _ in range(1000)]

# замеры 1000
print(
    timeit.timeit(
        "merge_sort(orig_list3[:])",
        globals=globals(),
        number=1000))
print('# замеры 1000\n')