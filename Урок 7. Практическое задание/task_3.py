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
# Прочитал про метод  с пивотами. Реализовал. Сортировка не используется. Очень был сложный момент в скатывание
# в бесконечную реккурсию, когда оставались одинаковые элементы с одной стороны от пивота, решил с разбрасыванием
# таких по очереди в разные стороны от пивота. На удивление сложность О(n) Учивая, что рекурсия вызывается от
# массива, который в среднем вдвое меньше предыдущего получаем последовательность n+ n/2 + n/4 + ... и т.д.
# матан 1 курс, сумма такого ряда стремится к 2n.

from statistics import median
from random import randint, choice
from timeit import timeit


def element_array_split(element, my_array):
    left = []
    right = []
    equal_left = True
    for el in my_array:
        if el < element:
            left.append(el)
        elif el > element:
            right.append(el)
        elif el == element and equal_left:
            left.append(el)
            equal_left = False
        else:
            right.append(el)
            equal_left = True
    return left, right


def find_median(my_array, median_index):
    if len(my_array) == 1:
        return my_array[0]
    else:
        left, right = element_array_split(choice(my_array), my_array)
        if len(left) > median_index:
            return find_median(left, median_index)
        else:
            return find_median(right, median_index-len(left))


my_array = [randint(1, 100) for el in range(21)]
median_index = len(my_array)//2
print(median(my_array))
print(find_median(my_array, median_index))


