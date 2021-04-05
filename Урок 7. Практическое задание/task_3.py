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
from statistics import median


# Реализация гномьей сортировки:
def sort_gnome(list_arg, n=1):
    if n == len(list_arg):
        return list_arg
    else:
        if list_arg[n] < list_arg[n-1] and n > 0:
            list_arg[n], list_arg[n-1] = list_arg[n-1], list_arg[n]
            n -= 1
        else:
            n += 1
        return sort_gnome(list_arg, n)


m = 10
original_list = [random.randint(-50, 50) for i in range(2*m+1)]
median_calculated = sort_gnome(original_list)[m]
print(original_list)
print(median_calculated)
print(median(original_list))
'''
[-32, -24, -21, -12, -11, -11, -9, -6, -2, -1, 0, 3, 8, 10, 12, 19, 21, 22, 32, 42, 48]
0
0
'''