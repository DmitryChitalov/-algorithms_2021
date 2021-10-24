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
import timeit


def sort_merge(list_obj):
    if len(list_obj) <= 1:
        return list_obj
    mid = len(list_obj) // 2
    left, right = sort_merge(list_obj[:mid]), sort_merge(list_obj[mid:])
    return merge(left, right, list_obj[:])


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


def func_timeit(list_obj):
    return f'Длина списка: {len(list_obj)}\n' \
           f'Список до сортировки: {list_obj}\n' \
           f'Список после сортировки: {sort_merge(list_obj[:])}\n' \
           f'Замеры времени сортировки: ' \
           f'{timeit.timeit(f"sort_merge({list_obj[:]})", globals=globals(), number=1000)}\n'


result_1 = [random.random() * 50 for _ in range(10)]
result_2 = [random.random() * 50 for _ in range(100)]
result_3 = [random.random() * 50 for _ in range(1000)]

# Результат:
print(func_timeit(result_1))  # 0.01714923800318502
print(func_timeit(result_2))  # 0.24511786899529397
print(func_timeit(result_3))  # 2.6684227130026557
