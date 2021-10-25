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


def merge_sort(lst_obj):
    if len(lst_obj) < 2:
        return lst_obj
    else:
        center = len(lst_obj) // 2
        left = merge_sort(lst_obj[:center])
        right = merge_sort(lst_obj[center:])

        return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
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


orig_list = [random.random() * 50 for _ in range(int(input('Введите число элементов: ')))]

print(f'Исходный -        {orig_list}\nОтсортированный - {merge_sort(orig_list[:])}'
      f'\n{timeit.timeit("merge_sort(orig_list[:])", globals=globals(), number=1000)}\n'
      )

"""
Введите число элементов: 10
Исходный -        [9.180434862973897, 42.3230477616931, 22.33963201379352, 18.112146087551835, 46.77777255201349, ...]
Отсортированный - [9.180434862973897, 9.503681433037581, 18.112146087551835, 20.24936048147043, 22.33963201379352, ...]
0.018002845999999906

Введите число элементов: 100
Исходный -        [29.387678968787533, 21.437614754121803, 28.671632253887196, 4.132429121041886, 13.076738352235, ...]
Отсортированный - [0.5169607436670332, 1.4290673072146487, 2.4105938841275765, 2.5796136689314575, 2.8973388146180 ...]
0.3460833700000001

Введите число элементов: 1000
Исходный -        [24.11039981705716, 26.26271113009468, 8.74365419432852, 0.3123607368850534, 15.9921943598504, ...]
Отсортированный - [0.06347620318121194, 0.17789706736391353, 0.2808080113641698, 0.30875457711489473, 0.312360736, ...]
4.7689019130000005

"""
