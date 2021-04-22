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

import timeit
import random


def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    else:
        middle = int(len(arr) / 2)
        left = merge_sort(arr[:middle])
        right = merge_sort(arr[middle:])
        return merge(left, right)


def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
    if len(left) > 0:
        result += left
    if len(right) > 0:
        result += right
    return result


orig_list = [random.uniform(0, 50) for _ in range(10)]

# замеры 10
print("#" * 100)
print("Массив длинной 10")
print(orig_list)
print(merge_sort(orig_list[:]))
print("Время")
print(timeit.timeit("merge_sort(orig_list[:])", globals=globals(), number=1000))

orig_list = [random.uniform(0, 50) for _ in range(100)]

# замеры 100
print("#" * 100)
print("Массив длинной 100")
print(orig_list)
print(merge_sort(orig_list[:]))
print("Время")
print(timeit.timeit("merge_sort(orig_list[:])", globals=globals(), number=1000))

orig_list = [random.uniform(0, 50) for _ in range(1000)]

# замеры 1000
print("#" * 100)
print("Массив длинной 1000")
print(orig_list)
print(merge_sort(orig_list[:]))
print("Время")
print(timeit.timeit("merge_sort(orig_list[:])", globals=globals(), number=1000))


"""
Массив длинной 10 - 0.014564
Массив длинной 100 - 0.27962770000000003
Массив длинной 1000 - 6.1289985
"""
