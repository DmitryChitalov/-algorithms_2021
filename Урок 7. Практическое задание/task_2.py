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

from timeit import timeit
from random import random


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])

    return merge(left, right, arr.copy())


def merge(left, right, merged):
    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):

        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1

    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]

    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return merged


list_10 = [random() * 50 for _ in range(10)]
list_100 = [random() * 50 for _ in range(100)]
list_1000 = [random() * 50 for _ in range(1000)]

print(
    timeit(
        "merge_sort(list_10[:])",
        globals=globals(),
        number=1000))
print(list_10)
print(merge_sort(list_10))
print("===============================================")
print(
    timeit(
        "merge_sort(list_100[:])",
        globals=globals(),
        number=1000))
print(list_100)
print(merge_sort(list_100))
print("===============================================")
print(
    timeit(
        "merge_sort(list_1000[:])",
        globals=globals(),
        number=1000))
print(list_1000)
print(merge_sort(list_1000))
print("===============================================")
"""
Реализовал метод сортировки слиянием через функцию merge_sort, которая рекурсивно делит массив и при объединении
вызывает функцию сортировки merge. Такой метод сортировки при замерах показал отличные результаты. Время работы
на больших массивах меньше чем пузырьком в 2-3 раза. 
"""
