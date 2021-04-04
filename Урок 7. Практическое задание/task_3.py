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

my_lst
new_lts

arr[m]


from statistics import median

[3, 4, 3, 3, 5, 3, 3]


left.clear()
right.clear()


m = 3
len = 7
i
left = []
right = []

left == right and

for i in
    for
    left == right
    left.clear()
    right.clear()


"""

import random
import statistics


def my_median(lst, n):
    lst = lst.copy()
    max_val = False
    while len(lst) > 1:
        i = 0
        if max_val:
            i = min(lst)
            max_val = False
        else:
            i = max(lst)
            max_val = True
        lst.remove(i)
    return lst[0]


m = 3
my_lst = [random.randint(0, 50) for _ in range(2 * m + 1)]
print(my_lst)

print(statistics.median(my_lst))
print(my_median(my_lst, m))
