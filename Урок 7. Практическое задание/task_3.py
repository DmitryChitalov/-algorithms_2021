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

import random


m = int(input('Введите m: '))
my_list = [random.randint(0, 9) for i in range(2 * m + 1)]


def median(some_list):
    left = []
    right = []
    for i in range(len(some_list)):
        for j in range(len(some_list)):
            if some_list[i] < some_list[j]:
                left.append(some_list[j])
            if some_list[i] > some_list[j]:
                right.append(some_list[j])
            if some_list[i] == some_list[j] and i > j:
                left.append(some_list[j])
            if some_list[i] == some_list[j] and i < j:
                right.append(some_list[j])
        if len(left) == len(right):
            return some_list[i]
        left.clear()
        right.clear()


print(my_list)
print(median(my_list))
