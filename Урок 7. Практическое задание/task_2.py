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
import random
from timeit import timeit

numb = int(input('Введите число элементов: '))
some_list = [random.random() * 50 for _ in range(0, numb)]

print(some_list)


def merge(left, right):
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left
    result = []
    index_left = index_right = 0
    while len(result) < len(left) + len(right):
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1
        if index_right == len(right):
            result += left[index_left:]
            break
        if index_left == len(left):
            result += right[index_right:]
            break
    return result


def merge_sort(array):
    if len(array) < 2:
        return array
    midpoint = len(array) // 2
    return merge(
        left=merge_sort(array[:midpoint]),
        right=merge_sort(array[midpoint:]))


print(merge_sort(some_list[:]))

print(timeit('merge_sort(some_list)',
      setup='some_list = [random.random() * 50 for _ in range(0, 10)]', globals=globals(), number=1000))
# 0.024291398000000353
print(timeit('merge_sort(some_list)',
      setup='some_list = [random.random() * 50 for _ in range(0, 100)]', globals=globals(), number=1000))
# 0.4178041829999999
print(timeit('merge_sort(some_list)',
      setup='some_list = [random.random() * 50 for _ in range(0, 1000)]', globals=globals(), number=1000))
# 6.016083912999999


