"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные по длине части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, Кучей...

[5, 3, 4, 3, 3, 3, 3]

[3, 3, 3, 3, 3, 4, 5]
"""
from statistics import median
from random import randint


def find_med(lst):
    mid = len(lst) // 2
    while mid:
        lst.remove(max(lst))
        mid -= 1
    return max(lst)


def gnom_sort(lst, m):
    base = 0
    memory = 1
    while base in range(len(lst) - 1):
        if lst[base] <= lst[base + 1]:
            base +=1
            memory +=1
        else:
            lst[base], lst[base + 1] = lst[base + 1], lst[base]
            base -= 1
            if base < 0:
                base += 1
                memory += 1
    return lst[m]


# lst = [5, 3, 4, 3, 3, 3, 3]
m = int(input('Введите число: '))
lst = [randint(-10, 10) for _ in range(2 * m + 1)]
# print(lst)
print(find_med(lst[:]))
print(median(lst))
print(gnom_sort(lst[:], m))