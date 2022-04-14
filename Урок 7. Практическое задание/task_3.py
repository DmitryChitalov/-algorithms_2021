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
from statistics import median
from timeit import timeit
from random import randint


def heap_sort(s_list):
    n = len(s_list)
    for i in range(n//2, -1, -1):
        heapify(s_list, n-1, i)

    for i in range(n-1, -1, -1):
        s_list[i], s_list[0] = s_list[0], s_list[i]
        heapify(s_list, i-1, 0)
    return s_list


def heapify(s_list, n, i):
    biggest, left, right = i, 2*i + 1, 2*i + 2
    if left <= n and s_list[left] > s_list[biggest]:
        biggest = left
    if right <= n and s_list[right] > s_list[biggest]:
        biggest = right
    if biggest != i:
        s_list[i], s_list[biggest] = s_list[biggest], s_list[i]
        heapify(s_list, n, biggest)


def list_median(s_list):
    for el in range(len(s_list)//2):
        s_list.pop(s_list.index(max(s_list)))
    return max(s_list)


# m = int(input("Enter the number of elements: "))
# Допустим, введенное число 20
m = 20
main_list = [randint(0, 100) for _ in range(2*m + 1)]
sorted_list = heap_sort(main_list[:])

print(f'Main array: {main_list[:]}\n'
      f'Sorted array: {sorted_list}\n'
      f'Median by sorted list: {sorted_list[m]}\n'
      f'Median without sorted: {list_median(main_list[:])}\n'
      f'Median by statistics library: {median(main_list[:])}\n'
      f'{"~"*30}Time for search median{"~"*30}\n'
      f'Time by sort: {timeit("heap_sort(main_list[:])", globals=globals(), number=1000)}\n'
      f'Time without sort: {timeit("list_median(main_list[:])", globals=globals(), number=1000)}\n'
      f'Time by statistics library: {timeit("median(main_list[:])", globals=globals(), number=1000)}')

"""
Поиск медианы сортировкой самый долгий. Хоть пирамидальная сортировка и является одним из быстрых методов сортировки. 
Медиана путем перебора элементов списка с удалением максимального при каждой итерации быстрее, чем работа с сортировкой,
но медленнее, чем встроенная бибилиотека statistics, которая оказалась наиболее быстрой. 


Main array: [9, 27, 17, 42, 57, 9, 1, 45, 34, 9, 7, 83, 23, 34, 73, 74, 39, 64, 47, 17, 77, 2, 48, 40, 56, 1, 20, 49, 
             6, 88, 96, 68, 58, 86, 37, 42, 63, 66, 77, 27, 73]
Sorted array: [1, 1, 2, 6, 7, 9, 9, 9, 17, 17, 20, 23, 27, 27, 34, 34, 37, 39, 40, 42, 42, 45, 47, 48, 49, 56, 57, 58, 
               63, 64, 66, 68, 73, 73, 74, 77, 77, 83, 86, 88, 96]
Median by sorted list: 42
Median without sorted: 42
Median by statistics library: 42
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Time for search median~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Time by sort: 0.07179885900040972
Time without sort: 0.012017754001135472
Time by statistics library: 0.0011412969979573973
"""
