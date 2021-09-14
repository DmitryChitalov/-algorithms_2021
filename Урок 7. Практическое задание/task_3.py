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


def median_no_sorted(arr):
    """Поиск медианы без сортировки"""
    for _ in range(len(arr) // 2):
        arr.remove(max(arr))
    return max(arr)


def gnome_sort(arr):
    """Гномья сортировка"""
    i, size = 1, len(arr)
    while i < size:
        if arr[i - 1] <= arr[i]:
            i += 1
        else:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            if i > 1:
                i -= 1
    return arr


def gnome_median(arr):
    """Поиск медианы в отсортированом массиве"""
    return gnome_sort(arr)[len(arr) // 2]


m = int(input('Ввведите m: '))
array = [randint(0, 100) for n in range(2 * m + 1)]

print(array)
print(f'statistics.median() = {median(array[:])}')
print(f'median_no_sorted() = {median_no_sorted(array[:])}')
print(f'gnome_median() = {gnome_median(array[:])}')

# Ввведите m: 5
# [5, 15, 48, 28, 74, 87, 28, 16, 84, 63, 36]
# statistics.median() = 36
# median_no_sorted() = 36
# gnome_median() = 36

print('#' * 100)
print(
    f'statistics.median() = {timeit("median(array[:])", globals=globals(), number=10000)}')
print(
    f'median_no_sorted() = {timeit("median_no_sorted(array[:])", globals=globals(), number=10000)}')
print(
    f'gnome_median_sort() = {timeit("gnome_median(array[:])", globals=globals(), number=10000)}')

# m = 10
# statistics.median() = 0.010674514998754603
# median_no_sorted() = 0.06205638399842428
# gnome_median_sort() = 0.42656386100134114

# m = 100
# statistics.median() = 0.07472337000035623
# median_no_sorted() = 3.1434248460009258
# gnome_median_sort() = 33.82871456900102

# Поиск медианы через гномью сортировку в данном случае самый медленный,
# лучший результат у statistics.median()
