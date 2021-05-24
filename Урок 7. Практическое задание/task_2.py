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
import timeit


def merge_sort_combine(left, right):
    result = []
    i = j = 0
    while i < (len(left)) and j < (len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if i < (len(left)):
        result += left[i:]
    if j < (len(right)):
        result += right[j:]
    return result


def merge_sort(input_list):
    if len(input_list) == 1:
        return input_list
    middle = len(input_list) // 2
    left_side = merge_sort(input_list[:middle])
    right_side = merge_sort(input_list[middle:])
    return merge_sort_combine(left_side, right_side)


n = int(input('Введите количество элементов в списке: '))
rand_list = [random.randint(0, 50) for _ in range(n)]

print(f'Исходный список: {rand_list}')
print(f'Отсортированный список: {merge_sort(rand_list[:])}')

rand_list_10 = [random.randint(0, 50) for _ in range(10)]
rand_list_100 = [random.randint(0, 50) for _ in range(100)]
rand_list_1000 = [random.randint(0, 50) for _ in range(1000)]

print(f'Замер времени при сортировке списка из 10 элементов:'
      f' {timeit.timeit("merge_sort(rand_list_10[:])", globals=globals(), number=1000)} сек.')
print(f'Замер времени при сортировке списка из 100 элементов:'
      f' {timeit.timeit("merge_sort(rand_list_100[:])", globals=globals(), number=1000)} сек.')
print(f'Замер времени при сортировке списка из 1000 элементов:'
      f' {timeit.timeit("merge_sort(rand_list_1000[:])", globals=globals(), number=1000)} сек.')

"""
Замер времени при сортировке списка из 10 элементов: 0.016387900000000233 сек.
Замер времени при сортировке списка из 100 элементов: 0.19501279999999976 сек.
Замер времени при сортировке списка из 1000 элементов: 2.6545567 сек.
"""
