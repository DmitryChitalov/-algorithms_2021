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
from random import randint
from statistics import median
from timeit import timeit


def median_with_gnome_opt(data, n):
    i, j = 1, 2
    while i < len(data):
        if data[i-1] <= data[i]:
            i, j = j, j + 1
        else:
            data[i-1], data[i] = data[i], data[i-1]
            i -= 1
            if i == 0:
                i, j = j, j + 1
    return data[n], n


def median_without_sort(data):
    mid = len(data) // 2
    while True:
        max = data[0]
        for el in data:
            if el > max:
                max = el
        data.remove(max)
        if mid == 0:
            return max
        mid -= 1


m = int(input('Введите m: '))
ls = [randint(1, 10) for i in range(2 * m + 1)]

print('median_with_gnome_opt: ', timeit('median_with_gnome_opt(ls[:], m)', globals=globals(), number=1000))
print('median: ', timeit('median(ls[:])', globals=globals(), number=1000))
print('median_without_sort', timeit('median_without_sort(ls[:])', globals=globals(), number=1000))

"""
при m, равным 100:
median_with_gnome_opt:  1.7919282
median:  0.006295199999999834
median_without_sort 0.42165849999999994

На удивление вариант с использованием гномьей сортировки оказался самым медленным: если решение путем циклов,
проходит лишь половину списка, то алгоритм сортировки вынужден сначала отсортировать список целиком.
Конечно, скорость median_without_sort далека от встроенной функции median, однако этот алгоритм
куда более эффективен.
"""
