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


def gnome_sort(lst_obj):
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


m = int(input('Enter "m" number in size of array 2m+1: '))
orig_list = [random.randint(-100, 100) for _ in range(2*m+1)]
gnome_sorted_list = gnome_sort(orig_list[:])
print(f'Original list: {orig_list}\n'
      f'Gnome sorted list: {gnome_sorted_list}\n'
      f'Median is: {gnome_sorted_list[m]}')

