"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные по длине части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.
Задачу можно решить без сортировки исходного массива.
Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, Кучей...
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

import random


# алгоритм загуглен
# Сложность O(n)
import timeit


def quickselect_median(lst_obj, pv):
    if len(lst_obj) % 2 == 1:
        return quickselect(lst_obj, len(lst_obj) / 2, pv)
    else:
        return 0.5 * (quickselect(lst_obj, len(lst_obj) / 2 - 1, pv) +
                      quickselect(lst_obj, len(lst_obj) / 2, pv))


def quickselect(l, k, pivot_fn):
    if len(l) == 1:
        assert k == 0
        return l[0]

    pivot = pivot_fn(l)

    lows = [el for el in l if el < pivot]
    highs = [el for el in l if el > pivot]
    pivots = [el for el in l if el == pivot]

    if k < len(lows):
        return quickselect(lows, k, pivot_fn)
    elif k < len(lows) + len(pivots):

        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots), pivot_fn)


# гномья сортировка
# Сложность O(n^2)
def gnome_opt(lst_obj):
    i, j, size = 1, 2, len(lst_obj)
    while i < size:
        if lst_obj[i - 1] <= lst_obj[i]:
            i, j = j, j + 1
        else:
            lst_obj[i - 1], lst_obj[i] = lst_obj[i], lst_obj[i - 1]
            i -= 1
            if i == 0:
                i, j = j, j + 1
    return lst_obj


elem = int(input("Введите число: "))
orig_list = [random.randint(0, 10) for _ in range(2 * elem + 1)]
print(orig_list)
pivot_fn = random.choice
print(f'Медиана без сортировки: {quickselect_median(orig_list[:], pivot_fn)}')
print('-' * 50)
print(f'Медиана с Гномьей сортировкой: {gnome_opt(orig_list[:])[elem]}')

'''
Введите число: 5
[3, 3, 8, 7, 2, 4, 8, 10, 9, 6, 0]
Медиана без сортировки: 6
--------------------------------------------------
Медиана с Гномьей сортировкой: 6
'''