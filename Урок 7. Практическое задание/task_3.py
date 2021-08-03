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

from random import randint
from statistics import median


def max_value(lst_obj):
    max_val = lst_obj[0]
    for i in lst_obj:
        if max_val < i:
            max_val = i
    return max_val
# Я так поняла, функцию max не следовало использовать, иначе это было бы слишком просто,
# поэтому я создала собственную функцию для нахождения максимального значения.


def find_median(list_obj):
    for j in range(len(list_obj) // 2):
        list_obj.remove(max_value(list_obj))
    return max_value(list_obj)


my_list = [randint(1, 100) for _ in range(randint(1, 10) * 2 + 1)]

if find_median(my_list[:]) == median(my_list[:]):
    print(f"Массив: {my_list}\nЕго медиана: {find_median(my_list[:])}")
else:
    print("В коде допущена ошибка")
    