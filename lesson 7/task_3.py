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
import timeit
import random

def import_median(lst_obj):
    return median(lst_obj)

m = (int(input('Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Введите m: ')))
orig_list = [random.randint(0, 100) for i in range(2 * m + 1)]
print(f'Новый массив: {orig_list}')
print(f'Медиана: {import_median(orig_list)}')
print('')


def shell(orig_list, median):
    inc = len(orig_list) // 2
    while inc:
        for i, el in enumerate(orig_list):
            while i >= inc and orig_list[i - inc] > el:
                orig_list[i] = orig_list[i - inc]
                i -= inc
            orig_list[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    return orig_list[median]

m = (int(input('Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Введите m: ')))
orig_list = [random.randint(0, 100) for i in range(2 * m + 1)]
print(f'Новый массив: {orig_list}')
print(shell(orig_list, m))
print('')

def my_median(lst_obj):
    cnt = 0
    while cnt < len(lst_obj)/2:
        max_lst = max(lst_obj)
        lst_obj.remove(max_lst)
        cnt += 1
    return max(lst_obj)

m = (int(input('Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Введите m: ')))
orig_list = [random.randint(0, 100) for i in range(2 * m + 1)]
print(f'Новый массив: {orig_list}')
print(f'Медиана: {my_median(orig_list)}')
print('')
print('Замеры m = 10')
m = 10
orig_list = [random.randint(0, 100) for i in range(2 * m + 1)]
print(
    timeit.timeit(
        "import_median(orig_list[:])",
        globals=globals(),
        number=100))
print(
    timeit.timeit(
        "shell(orig_list[:], m)",
        globals=globals(),
        number=100))
print(
    timeit.timeit(
        "my_median(orig_list[:])",
        globals=globals(),
        number=100))

# Замеры
"""
0.00016719999999992297
0.002429100000000073
0.0007282000000001787
"""
print('')
print('Замеры m = 1000')
m = 1000
orig_list = [random.randint(0, 100) for i in range(2 * m + 1)]
print(
    timeit.timeit(
        "import_median(orig_list[:])",
        globals=globals(),
        number=100))
print(
    timeit.timeit(
        "shell(orig_list[:], m)",
        globals=globals(),
        number=100))
print(
    timeit.timeit(
        "my_median(orig_list[:])",
        globals=globals(),
        number=100))
"""
Выводы:
Встреченная функция всегда лучше.
"""
