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

list1 = [int(random() * 100 + 1) for _ in range(int(2 * m + 1))]

print(f'Медиана: {shell_median(list1[:])}')
print('Замер на массиве shell_median(list1[:]) ',
      timeit('shell_median(list1[:])', globals=globals(), number=1000))

list2 = [int(random() * 100 + 1) for _ in range(int(2 * m + 1))]
print(f'Медиана: {gnome_median(list2[:])}')
print('Замер на массиве gnome_median(list2[:]) ',
      timeit('gnome_median(list2[:])', globals=globals(), number=1000))

list3 = [int(random() * 100 + 1) for _ in range(int(2 * m + 1))]
print(f'Медиана: {sorted_median(list3[:])}')
print('Замер на массиве sorted_median(list3[:])',
      timeit('sorted_median(list3[:])', globals=globals(), number=1000))

# В массивах были найдены медианы, и получились следующие результаты в секундах:
#
# Введите натуральное число m: >? 100
# Медиана: 51
# Замер на массиве shell_median(list1[:])  0.24466927400000005
# Медиана: 50
# Замер на массиве gnome_median(list2[:])  3.5955689299999998
# Медиана: 53
# Замер на массиве sorted_median(list3[:]) 0.009550433999999441
#
# Как и ожидалось, лучший результат поиска медианы дала функция sorted_median(list3[:]). Совершенно ясно,
# что внутренняя функция работает быстрее (O(n log n)), чем внешняя. Две других функции (O(n^2)) оказались более
# медленными. Гномья сортировка выдает самые плохие результаты.
#
# В чем ошибка: timeit('sorted_median(list3) был неправильно определен, нужно
#               timeit('sorted_median(list3[:])
