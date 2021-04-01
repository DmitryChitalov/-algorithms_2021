"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""

import random

my_list = [random.random()*50 for i in range(int(input("Введите число элементов: ")))]


def merger_func(sort_list):

    if len(sort_list) > 1:
        mid = len(sort_list) // 2
        left_half = sort_list[:mid]
        right_half = sort_list[mid:]

        merger_func(left_half)
        merger_func(right_half)

        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                sort_list[k] = left_half[i]
                i = i + 1
            else:
                sort_list[k] = right_half[j]
                j = j + 1
            k = k + 1

        while i < len(left_half):
            sort_list[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half):
            sort_list[k] = right_half[j]
            j = j + 1
            k = k + 1


print('Исходный массив: ', my_list)
merger_func(my_list)
print('Отсортированный массив: ', my_list)
