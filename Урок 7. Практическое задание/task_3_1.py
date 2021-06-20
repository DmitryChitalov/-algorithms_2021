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

from random import random


def sort_shell(my_list):  # для сортировки используем алгоритм Шелла
    last_index = len(my_list) - 1
    step = len(my_list) // 2
    while step > 0:
        for i in range(step, last_index + 1, 1):
            j = i
            delta = j - step
            while delta >= 0 and my_list[delta] > my_list[j]:
                my_list[delta], my_list[j] = my_list[j], my_list[delta]
                j = delta
                delta = j - step
        step //= 2
    return my_list


m = 10  # длина массива - 2m + 1

my_list = [round(random() * 100, 2) for _ in range(2 * m + 1)]

print(my_list)  # первоначальный массив
print(sort_shell(my_list))  # отсортированный массив
print("Медиана: ", my_list[m])  # в отсортированном массиве медиана будет ровно посередине - с индексом m
