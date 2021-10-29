#!/usr/bin/env python3

from array import array
from random import randint

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


def median(array: list):
    middle = len(array) // 2
    while True:
        maximum = array[0]
        for i in array:
            if i > maximum:
                maximum = i
        array.remove(maximum)
        if middle == 0:
            return maximum
        middle -= 1


def gnome_sort(array: list):
    i, size = 1, len(array)
    while i < size:
        if array[i - 1] <= array[i]:
            i += 1
        else:
            array[i - 1], array[i] = array[i], array[i - 1]
            if i > 1:
                i -= 1


def main():
    m = int(input("Введите m: "))

    array = [randint(0, 10) for i in range(2 * m + 1)]
    print(array)

    print(f'Медиана (без сортировки): {median(array[:])}')

    gnome_sort(array)
    print(array)
    print(f"Медиана (гномья сортировка): {array[m]}")


if __name__ == '__main__':
    main()
