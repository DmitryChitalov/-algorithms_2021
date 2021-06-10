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

"""
[15, 10, 4, 5, 11, 18, 6, 5, 16]
[4, 5, 5, 6, 10, 11, 15, 16, 18]
Медиана массива - 10
Проверка встроенной функцией - 10
"""
from statistics import median
from random import randint


def sort(list_object):
    i = 1
    while i < len(list_object):
        if list_object[i - 1] <= list_object[i]:
            i += 1
        else:
            list_object[i - 1], list_object[i] = list_object[i], list_object[i - 1]
            if i > 1:
                i -= 1
    return list_object


m = randint(1, 10)
list = [randint(1, 20) for _ in range(2 * m + 1)]

print(list)
print(sort(list))

print(f"Медиана массива - {sort(list)[m]}")
print(f"Проверка встроенной функцией - {median(list)}")
