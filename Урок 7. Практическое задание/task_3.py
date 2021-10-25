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

import random


def select(a, left, right, n):
    while True:
        if left == right:
            return left

        pivotIndex = pivot(a, left, right)
        pivotIndex = partition(a, left, right, pivotIndex, n)
        if n == pivotIndex:
            return n
        elif n < pivotIndex:
            right = pivotIndex - 1
        else:
            left = pivotIndex + 1


def partition(a, left, right, pivot_index, n):
    pivot_value = a[pivot_index]
    # a[pivot_index], a[right] == a[right], a[pivot_index]
    store_index = left

    for i in range(left, right - 1):
        if a[i] < pivot_value:
            a[store_index], a[i] = a[i], a[store_index]
            store_index += 1
    store_index_eq = store_index
    for i in range(store_index, right - 1):
        if a[i] == pivot_value:
            a[store_index_eq], a[i] = a[i], a[store_index]
            store_index_eq += 1
    a[right], a[store_index_eq] = a[store_index_eq], a[right]

    if n < store_index:
        return store_index
    if n <= store_index_eq:
        return n
    return store_index_eq


def partition_5(a, left, right):
    i = left + 1
    while i <= right:
        j = i
        while j > left and a[j - 1] > a[j]:
            a[j - 1], a[j] = a[j], a[j - 1]
            j -= 1
        i += 1
    return (left + right) // 2


def pivot(a, left, right):
    if right - left < 5:
        return partition_5(a, left, right)

    for i in range(left, right, 5):
        sub_right = i + 4
        if sub_right > right:
            sub_right = right
        median_5 = partition_5(a, i, sub_right)
        a[median_5], a[left + (i - left) // 5] = a[left + (i - left) // 5], a[median_5]

    mid = (right - left) / 10 + left + 1
    return select(a, left, left + (right - left) // 5, mid)


if __name__ == '__main__':
    m = int(input("Введите длину половины массива: "))
    a = [random.randint(-100, 100) for _ in range(2 * m + 1)]
    print(a)

    left = 0
    right = len(a) - 1
    med_ind = pivot(a, left, right)

    print(f'медиана массива: {a[med_ind]}')
    print(sorted(a))
