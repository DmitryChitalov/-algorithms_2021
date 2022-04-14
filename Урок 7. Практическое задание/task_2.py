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

from random import random
from timeit import timeit

n = int(input('Введите число элементов: '))

lst = [random() * 50 for i in range(n)]
print(f'Исходный - {lst}')


def merge_sort(lst_obj, start, end):
    if end - start > 1:
        mid = (start + end) // 2
        merge_sort(lst_obj, start, mid)
        merge_sort(lst_obj, mid, end)
        merge(lst_obj, start, mid, end)
    return lst_obj


def merge(lst_obj, start, mid, end):
    left = lst_obj[start:mid]
    right = lst_obj[mid:end]
    k = start
    i = 0
    j = 0
    while (start + i < mid and mid + j < end):
        if (left[i] <= right[j]):
            lst_obj[k] = left[i]
            i = i + 1
        else:
            lst_obj[k] = right[j]
            j = j + 1
        k = k + 1
    if start + i < mid:
        while k < end:
            lst_obj[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < end:
            lst_obj[k] = right[j]
            j = j + 1
            k = k + 1

print(f'Отсортированный - {merge_sort(lst.copy(), 0, len(lst))}')

lst = [random() * 50 for i in range(10)]
print("Время выполнения для массива из 10 элементов =", end=' ')
print(timeit('merge_sort(lst.copy(), 0, len(lst))', globals=globals(), number=10000))  # 0.1153606779999996

lst = [random() * 50 for i in range(100)]
print("Время выполнения для массива из 100 элементов =", end=' ')
print(timeit('merge_sort(lst.copy(), 0, len(lst))', globals=globals(), number=10000))  # 1.6383625559999997

lst = [random() * 50 for i in range(1000)]
print("Время выполнения для массива из 1000 элементов =", end=' ')
print(timeit('merge_sort(lst.copy(), 0, len(lst))', globals=globals(), number=10000))  # 25.263315836

