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
from math import sqrt


def get_median(lst):
    for i in range(n):
        lst.pop(lst.index(min(lst)))

    return min(lst)


def shell_sort(lst, d):
    for i in range(len(lst)):
        while True:
            is_move = False
            for j in range(i, len(lst), d):
                if j + d < len(lst) and lst[j] > lst[j + d]:
                    lst[j], lst[j + d] = lst[j + d], lst[j]
                    is_move = True

            if not is_move:
                break

    if d == 1:
        return lst
    else:
        d = int(sqrt(d))
        shell_sort(lst, d)


n = randint(10, 1000)
print(f'n = {n}')
lst = [randint(0, 1000) for _ in range(n * 2 + 1)]
print(lst)
median = get_median(lst[:])
print(f'Медиана по простому алгоритму = {median}')

# В качестве значения d для алгоритма Шелла взял квадратный корень от числа n
# Хотя, если задаться целью, можно поэкспериментировать над этим значением
shell_sort(lst, int(sqrt(n)))
median = lst[n]
print(f'Медиана при сортировке Шелла = {median}')

# Вчем подвох? Слишком просто
# n = 836
# [585, 498, 891, 640, 196, 211, 732, 632, 707, 251, 366, 862, 449, 32, 747, 439, 521, 462, 392,
# .......................
# 152, 705, 871, 283, 961, 772, 91, 803, 905, 785, 941, 471, 761, 36, 577, 177, 130, 36, 367, 439, 245]
# Медиана по простому алгоритму = 492
# Медиана при сортировке Шелла = 492


