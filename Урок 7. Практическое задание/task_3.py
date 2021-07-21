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
from random import randint
from statistics import median
from timeit import timeit

m = int(input('Введите натуральное число m '))
orig_list = [randint(-10, 10) for i in range(2 * m + 1)]
print(orig_list)


def get_median(lst):
    return median(lst[:])


def gnome_sort(lst):
    i, size = 1, len(lst)
    while i < size:
        if lst[i - 1] <= lst[i]:
            i += 1
        else:
            lst[i - 1], lst[i] = lst[i], lst[i - 1]
            if i > 1:
                i -= 1
    return lst[m]


print(get_median(orig_list))
print(f'Время работы через функцию median :'
      f' {timeit("get_median(orig_list[:])", globals=globals(), number=1000)}')


print(gnome_sort(orig_list))
print(f'Время работы через Гномью сортировку :'
      f' {timeit("gnome_sort(orig_list[:])", globals=globals(), number=1000)}')

'''
Время работы через функцию median : 0.0006550000000000722
Время работы через гномью сортировку : 0.0013469000000001508
Через встроенную функцию median нахождение медианы происходит намного быстрее, чем через Гномью сортировку.
'''