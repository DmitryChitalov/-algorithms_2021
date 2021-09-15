from random import randint
from statistics import median
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


def sort_shell(arr):
    tmp = len(arr) // 2
    while tmp:
        for i, el in enumerate(arr):
            while i >= tmp and arr[i - tmp] > el:
                arr[i] = arr[i - tmp]
                i -= tmp
            arr[i] = el
        tmp = 1 if tmp == 2 else int(tmp * 5.0/11)
    return arr


def med(arr, num):
    while num > 0:
        arr.remove(min(arr))
        num -= 1
    return min(arr)


try:
    """
    Понял ошибку, переделал
    """
    m = int(input('Введите число: '))
    orig_array = [randint(0, 1000) for _ in range(2*m+1)]

    print(median(orig_array[:]))  # при помощи statistics.median

    print(med(orig_array[:], m))  # при помощи функции min

    print(sort_shell(orig_array[:])[m])  # при помощи сортировки Шелла
except ValueError:
    print('Необходимо ввести число')
