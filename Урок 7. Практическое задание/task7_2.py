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

import operator
import timeit
import random


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


def merge_sort(some_list, compare=operator.lt):
    if len(some_list) < 2:
        return some_list[:]
    else:
        middle = len(some_list) // 2
        left = merge_sort(some_list[:middle], compare)
        right = merge_sort(some_list[middle:], compare)
        return merge(left, right, compare)


num = int(input('Введите число элементов: '))
my_list = [random.uniform(0, 50) for _ in range(num)]

print('Исходный массив:', my_list)
print('Отсортированный массив:', merge_sort(my_list))
print()

print('Результаты замеров:')

# замеры 10
orig_list = [random.uniform(0, 50) for _ in range(10)]
print('10 измерений:')
print(
    timeit.timeit(
        "merge_sort(orig_list[:])",
        globals=globals(),
        number=1000))
print()

# замеры 100
orig_list = [random.uniform(0, 50) for _ in range(100)]
print('100 измерений:')
print(
    timeit.timeit(
        "merge_sort(orig_list[:])",
        globals=globals(),
        number=1000))
print()

# замеры 1000
orig_list = [random.uniform(0, 50) for _ in range(1000)]
print('1000 измерений:')
print(
    timeit.timeit(
        "merge_sort(orig_list[:])",
        globals=globals(),
        number=1000))

# Слияние работает быстрее пузырька.