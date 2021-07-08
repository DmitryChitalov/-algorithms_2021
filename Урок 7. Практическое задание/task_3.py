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
from random import random
from timeit import timeit


def shell_median(my_list):  # O(n^2)
    inc = len(my_list) // 2
    while inc:
        for i, el in enumerate(my_list):
            while i >= inc and my_list[i - inc] > el:
                my_list[i] = my_list[i - inc]
                i -= inc
            my_list[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    return my_list[m]


def gnome_median(my_list):  # O(n^2)
    i, size = 1, len(my_list)
    while i < size:
        if my_list[i - 1] <= my_list[i]:
            i += 1
        else:
            my_list[i - 1], my_list[i] = my_list[i], my_list[i - 1]
            if i > 1:
                i -= 1
    return my_list[m]


def sorted_median(my_list):  # O(n log n)
    quotient, remainder = divmod(len(my_list), 2)
    if remainder:
        return sorted(my_list)[quotient]
    return sum(sorted(my_list)[quotient - 1:quotient + 1]) / 2.


m = int(input('Введите натуральное число m: '))
my_list1 = [int(random() * 100 + 1) for _ in range(int(2 * m + 1))]
my_list2 = my_list1.copy()
my_list3 = my_list1.copy()
print('Медиана:', my_list1[m])
print('Замер на массиве shell_median(my_list) ', timeit('shell_median(my_list1)', globals=globals(), number=100000))
print('Медиана:', my_list2[m])
print('Замер на массиве gnome_median(my_list) ', timeit('gnome_median(my_list2)', globals=globals(), number=100000))
print('Медиана:', my_list3[m])
print('Замер на массиве sorted_median(my_list)', timeit('sorted_median(my_list3)', globals=globals(), number=100000))

# В массивах были найдены медианы, и получились следующие результаты в секундах:
#
# Введите натуральное число m: >? 100
# Медиана: 66
# Замер на массиве shell_median(my_list)  12.315112509
# Медиана: 66
# Замер на массиве gnome_median(my_list)  2.139394009
# Медиана: 66
# Замер на массиве sorted_median(my_list) 0.8699387429999987
#
# Как и ожидалось, лучший результат поиска медианы дала функция sorted_median(my_list). Совершенно ясно,
# что внутренняя функция работает быстрее (O(n log n)), чем внешняя. Две других функции (O(n^2)) оказались более
# медленными. Правда Гномья сортировка тоже выдает неплохие результаты.
