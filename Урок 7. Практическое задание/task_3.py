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

import numpy as np
from statistics import median
import timeit


def func1(lst):
    i, size = 1, len(lst)
    while i < size:
        if lst[i - 1] <= lst[i]:
            i += 1
        else:
            lst[i - 1], lst[i] = lst[i], lst[i - 1]
            if i > 1:
                i -= 1
    return lst


def func2(lst):
    [lst.remove(max(lst)) for _ in range(len(lst) // 2)]
    return max(lst)


m = int(input('Enter m: '))
arr = np.random.randint(0, 100, 2 * m + 1)
print(arr)
print(f'Median: = {median(arr)}')
arr2 = func1(arr.tolist())
print(f'Median after sorting = {arr2[m]}')
print(f'Median without sorting  = {func2(arr.tolist())}')
print(f'Median after sorting: {timeit.timeit("func1(arr[:])", globals=globals(), number=10000)}')
print(f'Median without sorting: {timeit.timeit("func2(arr[:].tolist())", globals=globals(), number=10000)}')
