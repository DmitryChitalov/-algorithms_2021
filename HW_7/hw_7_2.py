"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Хотя в примерах к уроку уже есть вариант реализации слияния, попробуйте предложить другой
(придумать или найти)

И попытаться сделать замеры на массивах разной длины: 10, 100, 1000, ...

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
import random
from timeit import timeit


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

    return merge(merge_sort(array[:midpoint]), merge_sort(array[midpoint:]))


t1 = [random.uniform(0, 50) for _ in range(10)]
t2 = [random.uniform(0, 50) for _ in range(100)]
t3 = [random.uniform(0, 50) for _ in range(1000)]
print(f'оригинальный массив: {t1}')
print(f'Отсортированны массив: {merge_sort(t1[:])}')
print('10 чисел', timeit('merge_sort(t1[:])', globals=globals(), number=1000))
print(f'оригинальный массив: {t2}')
print(f'Отсортированны массив: {merge_sort(t2[:])}')
print('100 чисел', timeit('merge_sort(t2[:])', globals=globals(), number=1000))
print(f'оригинальный массив: {t3}')
print(f'Отсортированны массив: {merge_sort(t3[:])}')
print('1000 чисел', timeit('merge_sort(t3[:])', globals=globals(), number=1000))
'''
10 чисел: 0.12600700000000004
100 чисел: 1.229647
1000 чисел: 16.0801639
'''
