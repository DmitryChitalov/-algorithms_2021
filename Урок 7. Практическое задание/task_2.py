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


def merge_sort(lst):
    if len(lst) > 1:
        center = len(lst) // 2
        left = lst[:center]
        right = lst[center:]

        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1
        return lst


try:
    array_len = int(input('Введите длину массива: '))
    need_list = [random.uniform(0, 50) for _ in range(array_len)]
    print(f'Исходный массив: {need_list}')
    print(f'Отсортированный методом слияния массив: {merge_sort(need_list[:])}')
    print(timeit.timeit('merge_sort(need_list[:])',
                        setup='from __main__ import merge_sort, need_list', number=1000))
except ValueError:
    print('Неккоректный ввод длины')

"""
Время для длины 10:
0.007698400000000216
Время для длины 100:
0.12373579999999995
Время для длины 1000:
1.8136354
"""