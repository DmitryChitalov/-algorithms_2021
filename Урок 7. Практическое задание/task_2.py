"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Хотя в примерах к уроку уже есть вариант реализации слияния,
попробуйте предложить другой (придумать или найти).

И попытаться сделать замеры на массивах разной длины: 10, 100, 1000, ...

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644,
12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644,
41.62921998361278, 46.11436617832828]
"""
from random import random
from timeit import timeit

n = int(input('Введите количество элементов: \n'))

lst = [random() * 50 for i in range(n)]
print(f'Исходный список: {lst}')


def merge_sort(lst, start, end):
    if end - start > 1:
        mid = (start + end) // 2
        merge_sort(lst, start, mid)
        merge_sort(lst, mid, end)
        merge(lst, start, mid, end)
    return lst


def merge(lst, start, mid, end):
    left = lst[start:mid]
    right = lst[mid:end]
    s = start
    i = j = 0
    while (start + i < mid) and (mid + j < end):
        if left[i] <= right[j]:
            lst[s] = left[i]
            i += 1
        else:
            lst[s] = right[j]
            j += 1
        s += 1
    if start + i < mid:
        while s < end:
            lst[s] = left[i]
            i += 1
            s += 1
    else:
        while s < end:
            lst[s] = right[j]
            j += 1
            s += 1


print(f'Отсортированный - {merge_sort(lst[:], 0, len(lst))}')
lst_10 = [random() * 50 for _ in range(10)]
print('Время сортировки для массива из 10 элементов = ', end=' ')
print(timeit('merge_sort(lst_10[:], 0, len(lst_10))', globals=globals(),
             number=10000), '\n')

lst_100 = [random() * 50 for _ in range(100)]
print('Время сортировки для массива из 100 элементов = ', end=' ')
print(timeit('merge_sort(lst_100[:], 0, len(lst_100))', globals=globals(),
             number=10000), '\n')

lst_1000 = [random() * 50 for _ in range(1000)]
print('Время сортировки для массива из 1000 элементов = ', end=' ')
print(timeit('merge_sort(lst_1000[:], 0, len(lst_1000))', globals=globals(),
             number=10000), '\n')
