"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные по длине части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, Кучей...

Важно: стройте массив именно по формуле 2m+1
Потому что параметр m вам пригодится при поиске медианы, когда массив будет отсортирован.
Этот парамет m вам нужно запрашивать у пользователя.

[5, 3, 4, 3, 3, 3, 3]
[3, 3, 3, 3, 3, 4, 5]

my_lst
new_lts

arr[m]

from statistics import median

[3, 4, 3, 3, 5, 3, 3]

left = []
right = []

left == right and

for i in
    for
    left == right
    left.clear()
    right.clear()
"""

import timeit
import random
from statistics import median


def shell_sort_med(lst_obj):
    last_index = len(lst_obj) - 1
    step = len(lst_obj)//2
    while step > 0:
        for i in range(step, last_index + 1):
            j = i
            delta = j - step
            while delta >= 0 and lst_obj[delta] > lst_obj[j]:
                lst_obj[delta], lst_obj[j] = lst_obj[j], lst_obj[delta]
                j = delta
                delta = j - step
        step //= 2
    return lst_obj, lst_obj[len(lst_obj)//2]


def median_del(lst):
    l = len(lst)
    while len(lst) > l//2 + 1:
        lst.remove(max(lst))
    return max(lst)


m = int(input("Введите m для построения массива размером 2m + 1: "))
orig_list = [random.randint(-100, 100) for _ in range(2 * m + 1)]

shell_lst, med = shell_sort_med(orig_list[:])

print(f'{orig_list[:]}\nСортировка Шелла: {shell_lst}; медиана: массив[m] = {med}'
      f'\nФункция поиска медианы без сортировки исходного массива: {median_del(orig_list[:])}'
      f'\nВстроенная функция поиска медианы: {median(orig_list[:])}')

# Введите m для построения массива размером 2m + 1: 3
# [-31, 93, -10, -13, -3, -56, 64]
# Сортировка Шелла: [-56, -31, -13, -10, -3, 64, 93]; медиана: массив[m] = -10
# Функция поиска медианы без сортировки исходного массива: -10
# Встроенная функция поиска медианы: -10


orig_list = [random.randint(-100, 100) for _ in range(100)]
# замеры функции поиска медианы c сортировкой Шелла
print(
    timeit.timeit(
        "shell_sort_med(orig_list[:])",
        globals=globals(),
        number=1000))

# замеры функции поиска медианы без сортировки исходного массива
print(
    timeit.timeit(
        "median_del(orig_list[:])",
        globals=globals(),
        number=1000))

# замеры встроенной функции поиска медианы (из модуля statistics)
print(
    timeit.timeit(
        "median(orig_list[:])",
        globals=globals(),
        number=1000))

# 0.261014195
# 0.149013579
# 0.006870629000000239

# !!!Как и ожидалось, встроенная функция statistics.median во много раз быстрее иных способов нахождения медианы.
# А поиск медианы без сортировки исходного массива почти вдвое быстрее, чем определение медианы после сортировки Шелла,
# т.к. лишние циклы сортировки отсутствуют в принципе!
# При этом, если сравнивать сортировку Шелла с сортировкой вставками, аналогом которой она является, то результат
# (0.264934221 против 0.7102375240000001) - более чем двукратное преимущество Шелла.

# def insertion_sort(lst_obj):
#     for i in range(len(lst_obj)):
#         v = lst_obj[i]
#         j = i
#         while (lst_obj[j-1] > v) and (j > 0):
#             lst_obj[j] = lst_obj[j-1]
#             j = j - 1
#         lst_obj[j] = v
#     return lst_obj
#
# print(
#     timeit.timeit(
#         "insertion_sort(orig_list[:])",
#         globals=globals(),
#         number=1000))
#
# 0.7102375240000001
