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
from statistics import median
from random import randint


def gnome_sort(lst_obj):
    i = 1
    while i < len(lst_obj):
        if lst_obj[i - 1] <= lst_obj[i]:
            i += 1
        else:
            lst_obj[i - 1], lst_obj[i] = lst_obj[i], lst_obj[i - 1]
            if i > 1:
                i -= 1
    return lst_obj


m = randint(1, 10)
real_list = [randint(1, 20) for _ in range(2*m + 1)]

print(real_list)
print(gnome_sort(real_list))

print(f"Медиана массива - {gnome_sort(real_list)[m]}")
print(f"Проверка встроенной функцией: медиана - {median(real_list)}")

"""
[1, 11, 10, 17, 3]
[1, 3, 10, 11, 17]
Медиана массива - 10
Проверка встроенной функцией: медиана - 10
"""