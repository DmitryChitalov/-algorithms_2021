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
from random import uniform
from timeit import timeit

import operator


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


def merge_sort(L, compare=operator.lt):
    if len(L) < 2:
        return L[:]
    else:
        middle = int(len(L) / 2)
        left = merge_sort(L[:middle], compare)
        right = merge_sort(L[middle:], compare)
        return merge(left, right, compare)


lst_1, lst_2, lst_3 = [uniform(0, 49.9) for _ in range(10)], [uniform(0, 49.9) for _ in range(100)], \
                      [uniform(0, 49.9) for _ in range(1000)]
print("Old:",lst_1,lst_2,lst_3,sep="\n")
print("New:",merge_sort(lst_1),merge_sort(lst_2),merge_sort(lst_3),sep="\n")

print("time_10:",timeit('merge_sort(lst_1)',globals=globals(),number=1000))
print("time_100:",timeit('merge_sort(lst_2)',globals=globals(),number=1000))
print("time_1000:",timeit('merge_sort(lst_3)',globals=globals(),number=1000))

"Вывод: он сортирует, вывод вообще нужен?"
