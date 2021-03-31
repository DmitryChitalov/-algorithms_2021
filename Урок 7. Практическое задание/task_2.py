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

from random import random
from timeit import timeit

MAX_NUMBER = 50

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])
    return merge(left, right, arr.copy())


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

def rand_list_generator(list_lenght):
    lst = []
    for _ in range(list_lenght):
        lst.append(random() * MAX_NUMBER)
    return lst

user_list_lenght = int(input('Введите число элементов: '))
user_list = rand_list_generator(user_list_lenght)

print(f'Исходный - {user_list[:]}')
print(f'Отсортированный - {merge_sort(user_list[:])}')

list_10 = rand_list_generator(10)
list_100 = rand_list_generator(100)
list_1000 = rand_list_generator(1000)
list_10000 = rand_list_generator(10000)

print(f'Массив из 10 элементов: {timeit("merge_sort(list_10[:])", globals=globals(), number=1000)}')
print(f'Массив из 100 элементов: {timeit("merge_sort(list_100[:])", globals=globals(), number=1000)}')
print(f'Массив из 1000 элементов: {timeit("merge_sort(list_1000[:])", globals=globals(), number=1000)}')
print(f'Массив из 10000 элементов: {timeit("merge_sort(list_10000[:])", globals=globals(), number=1000)}')
print(f'Массив из 10000 элементов отсортированный методом sorted: {timeit("sorted(list_10000[:])", globals=globals(), number=1000)}')

"""
Массив из 10 элементов: 0.036093485000000314
Массив из 100 элементов: 0.2341322589999999
Массив из 1000 элементов: 3.0760044210000004
Массив из 10000 элементов: 40.613186163
Массив из 10000 элементов отсортированный методом sorted: 1.272181433

замеры показывают, что сортировка слиянием вполне соответствует сложности O(N log N)
"""
