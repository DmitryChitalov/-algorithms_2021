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
import random
import timeit


def sort_gnome(our_list):
    k = 1
    while k < len(our_list):
        if not k or our_list[k] >= our_list[k - 1]:
            k += 1
        else:
            our_list[k], our_list[k - 1] = our_list[k - 1], our_list[k]
            k -= 1
    return our_list


def median_gnome(our_list):
    return sort_gnome(our_list)[len(our_list) // 2]


m = int(input('Введите m: '))
list_sort = [random.randint(0, 100) for _ in range(2 * m + 1)]
print(f'Исходный массив: {list_sort}')

print(f'Встроенная сортировка - {median(list_sort)}')
print(f'Гномья сортировка - {median_gnome(list_sort)}')

print(timeit.timeit('median(list_sort[:])',
                    setup='from __main__ import list_sort, median',
                    number=1000))

print(timeit.timeit('median_gnome(list_sort[:])',
                    setup='from __main__ import list_sort, median_gnome',
                    number=1000))

"""
Введите m: 3
Исходный массив: [76, 32, 31, 82, 3, 16, 29]
Встроенная сортировка - 31
Гномья сортировка - 31
0.0005841000000001983
0.0011999999999998678

Встроенная сортировка работает быстрее.
"""