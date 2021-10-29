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

import random
from timeit import timeit


def merge(left_list: list, right_list: list):
    sorted_list = []
    left_list_index = right_list_index = 0
    left_list_len, right_list_len = len(left_list), len(right_list)

    for _ in range(left_list_len + right_list_len):
        if left_list_index < left_list_len and right_list_index < right_list_len:
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1
        elif left_list_index == left_list_len:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        elif right_list_index == right_list_len:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list


def merge_sort(nums: list):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2

    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])
    return merge(left_list, right_list)


count = int(input('Введите число элементов: '))

test_massive = [random.randint(0, 50) for _ in range(count)]

print(f'Исходный - {test_massive}')
print(f'Отсортированный - {merge_sort(test_massive.copy())}')
print(timeit('merge_sort(test_massive.copy())', number=1000, globals=globals()))

# Замеры на 10 элементов - 0.028 сек
print(timeit('merge_sort(test_massive.copy())',
             number=1000,
             globals=globals(),
             setup='test_massive = [random.randint(0, 50) for _ in range(10)]'))

# Замеры на 100 элементов - 0.322 сек
print(timeit('merge_sort(test_massive.copy())',
             number=1000,
             globals=globals(),
             setup='test_massive = [random.randint(0, 50) for _ in range(100)]'))

# Замеры на 1000 элементов - 4.581 сек
print(timeit('merge_sort(test_massive.copy())',
             number=1000,
             globals=globals(),
             setup='test_massive = [random.randint(0, 50) for _ in range(1000)]'))
