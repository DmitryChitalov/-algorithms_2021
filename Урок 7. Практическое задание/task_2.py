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


def merge_sort(lst_obj):
    n = len(lst_obj)
    if n < 2:
        return lst_obj

    left = merge_sort(lst_obj[:n // 2])
    right = merge_sort(lst_obj[n // 2:n])

    i = j = 0
    result = []
    while i < len(left) or j < len(right):
        if not i < len(left):
            result.append(right[j])
            j += 1
        elif not j < len(right):
            result.append(left[i])
            i += 1
        elif left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    return result


list_10 = [random() * 50 for _ in range(10)]
list_100 = [random() * 50 for _ in range(100)]
list_1000 = [random() * 50 for _ in range(1000)]

print(f'Исходный массив: {list_10}\n'
      f'Отсортированный массив: {merge_sort(list_10[:])}\n'
      f'Время затраченное на сортировку: {timeit("merge_sort(list_10[:])", globals=globals(), number=1000)}')
print('*' * 1000)
print(f'Исходный массив: {list_100}\n'
      f'Отсортированный массив: {merge_sort(list_100[:])}\n'
      f'Время затраченное на сортировку: {timeit("merge_sort(list_100[:])", globals=globals(), number=1000)}')
print('*' * 1000)
print(f'Исходный массив: {list_1000}\n'
      f'Отсортированный массив: {merge_sort(list_1000[:])}\n'
      f'Время затраченное на сортировку: {timeit("merge_sort(list_1000[:])", globals=globals(), number=1000)}')
print('*' * 1000)
