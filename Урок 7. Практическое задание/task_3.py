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
m = int(input())
orig_list = [random.randint(-100, 100) for _ in range(2 * m + 1)]


def without_sorting(lst):
    for _ in range(len(lst) // 2):
        lst.remove(max(lst))
    return max(lst)


def heap(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heap(arr, n, largest)


def heap_sort(arr):
    n = len(arr)
    for i in range(n, -1, -1):
        heap(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heap(arr, i, 0)
    return arr[m]


print(without_sorting(orig_list[:]))
print(heap_sort(orig_list[:]))
print(median(orig_list[:]))
print(
    timeit.timeit(
        "without_sorting(orig_list[:])",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "heap_sort(orig_list[:])",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "median(orig_list[:])",
        globals=globals(),
        number=1000))

"""
Work time of the functions:
                 | m = 5                 | m = 50                | m = 500
without_sorting  | 0.002399700000001559  | 0.08377720000000011   | 7.881510299999999
heap_sort        | 0.015935400000000044  | 0.25404410000000066   | 4.6418623
median           | 0.0005316000000004095 | 0.0034479000000002813 | 0.08312399999999798
"""
"""
Поиск медианы без сортировки более эффективен при малых входных данных,
тогда как поиск через сортировку кучей будет быстрее при большом колличестве
элементов в массиве. В данном примере при len(orig_list) > 800. 
"""
