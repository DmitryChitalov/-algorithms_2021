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
from random import randint
from statistics import median

m = int(input("Введите натуральное число m "))
random_list = [randint(0, 10) for _ in range(2 * m + 1)]
print(f"Исходный массив: {random_list}")
print(f"Отсортированный массив: {sorted(random_list[:])}")


def list_median(lst):
    while len(lst) > m + 1:
        lst.remove(max(lst))
    return max(lst)


def gnome_median(lst):
    i, j, size = 1, 2, len(lst)
    while i < size:
        if lst[i - 1] <= lst[i]:
            i, j = j, j + 1
        else:
            lst[i - 1], lst[i] = lst[i], lst[i - 1]
            i -= 1
            if i == 0:
                i, j = j, j + 1
    return lst[m]


print(f"Медиана без сортировки: {list_median(random_list[:])}")
print(f"Медиана встроенной функцией: {median(random_list[:])}")
print(f"Медиана с гномьей сортировкой {gnome_median(random_list[:])}")


"""
Введите натуральное число m 5
Исходный массив: [7, 0, 10, 5, 4, 7, 9, 3, 10, 4, 5]
Отсортированный массив: [0, 3, 4, 4, 5, 5, 7, 7, 9, 10, 10]
Медиана без сортировки: 5
Медиана встроенной функцией: 5
Медиана с гномьей сортировкой 5
"""
