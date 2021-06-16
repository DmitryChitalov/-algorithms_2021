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

from statistics import median
import random
from timeit import timeit


def gnome(lst_obj):
    i, size = 1, len(lst_obj)
    index = (len(lst_obj) - 1) // 2
    while i < size:
        if lst_obj[i - 1] <= lst_obj[i]:
            i += 1
        else:
            lst_obj[i - 1], lst_obj[i] = lst_obj[i], lst_obj[i - 1]
            if i > 1:
                i -= 1
    return lst_obj[index]


def sorted_median(lst_obj):
    quotient, remainder = divmod(len(lst_obj), 2)
    if remainder:
        return sorted(lst_obj)[quotient]
    return sum(sorted(lst_obj)[quotient - 1:quotient + 1]) / 2


def not_sort(lst_obj):
    left_side = []
    right_side = []
    for i in range(len(lst_obj)):
        for j in range(len(lst_obj)):
            if lst_obj[i] > lst_obj[j]:
                left_side.append(lst_obj[j])
            if lst_obj[i] < lst_obj[j]:
                right_side.append(lst_obj[j])
            if lst_obj[i] == lst_obj[j] and i > j:
                left_side.append(lst_obj[j])
            if lst_obj[i] == lst_obj[j] and i < j:
                right_side.append(lst_obj[j])
        if len(left_side) == len(right_side):
            return lst_obj[i]
        left_side.clear()
        right_side.clear()


m = int(input("Введите натуральное число: "))
orig_list = [random.randint(0, 1000) for _ in range(2 * m + 1)]

print(f'Исходный список: {orig_list}')
# print(median(orig_list[:])) # Проверка правильно ли мы нашли медиану
print(f'Поиск медианы Гномьей сортировкой: {gnome(orig_list[:])}\n'
      f'Затраченное время: {timeit("median(orig_list[:])", globals=globals(), number=1000)}')
print(f'Поиск медианы с помощью "divmod": {sorted_median(orig_list[:])}\n'
      f'Затраченное время: {timeit("sorted_median(orig_list[:])", globals=globals(), number=1000)}')
print(f'Поиск медианы без сортировки списка: {not_sort(orig_list[:])}\n'
      f'Затраченное время: {timeit("not_sort(orig_list[:])", globals=globals(), number=1000)}')

# С помощью сортировки поиск медианы происходит очень быстро.
# Без сортировки возрастает в десятки раз.

# P.S. c методом без сортировки очень помог интернет, но я постарался разобрать его.
