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
from timeit import timeit
from statistics import median


def median_gnome(data, m):
    i, size = 1, len(data)
    while i < size:
        if data[i - 1] <= data[i]:
            i += 1
        else:
            data[i - 1], data[i] = data[i], data[i - 1]
            if i > 1:
                i -= 1
    return f'Медианой массива является число: {data[m]}'


def median_func(lst):
    return f'Медианой массива является число: {median(lst)}'


m = int(input('Введите m: '))
lst = [randint(1, 10) for i in range(2 * m + 1)]

print(median_gnome(lst, m))
print(median_func(lst))
print(f"Время выполнения с gnome: {timeit('median_gnome(lst[:], m)', globals=globals(), number=1000)}")
print(f"Время выполнения с median: {timeit('median_func(lst[:])', globals=globals(), number=1000)}")

# Вывод.
# Сортировка gnome оказалась медленнее встроенной функции median, что подтверждает гипотезу о том,
# что в работе при возможности следует пользоваться встроенными функциями.
# Время выполнения с gnome: 0.005399000000000154
# Время выполнения с median: 0.001725399999999766
