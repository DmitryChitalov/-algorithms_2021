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
from statistics import median
from timeit import timeit


# Сортировкой
def shell(n):
    m = 2 * n + 1
    my_lst = [random.randint(0, 100) for _ in range(m)]
    inc = len(my_lst) // 2
    while inc:
        for i, el in enumerate(my_lst):
            while i >= inc and my_lst[i - inc] > el:
                my_lst[i] = my_lst[i - inc]
                i -= inc
            my_lst[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    return f'Медиана: {my_lst[n]}, с индексом: {n} '


# statistics
def static(n):
    m = 2 * n + 1
    my_lst = [random.randint(0, 100) for _ in range(m)]
    return f'Медиана: {median(my_lst)}, с индексом: {n} '


# Без сортировки
def not_sort(n):
    m = 2 * n + 1
    my_lst = [random.randint(0, 100) for _ in range(m)]
    while (len(my_lst)) != n+1:
        my_lst.remove(max(my_lst))
    return f'Медиана: {max(my_lst)}, с индексом: {n} '


print(f'Сортировка Шелла(7): {timeit("shell(3)", globals=globals(), number=30000)}')
print(f'Методом median(7): {timeit("static(3)", globals=globals(), number=30000)}')
print(f'Без сортировки(7): {timeit("not_sort(3)", globals=globals(), number=30000)}')
print(f'Сортировка Шелла(21): {timeit("shell(10)", globals=globals(), number=10000)}')
print(f'Методом median(21): {timeit("static(10)", globals=globals(), number=10000)}')
print(f'Без сортировки(21): {timeit("not_sort(10)", globals=globals(), number=10000)}')
print(f'Сортировка Шелла(31): {timeit("shell(15)", globals=globals(), number=10000)}')
print(f'Методом median(31): {timeit("static(15)", globals=globals(), number=10000)}')
print(f'Без сортировки(31): {timeit("not_sort(15)", globals=globals(), number=10000)}')

"""
На массиве с длиной в 7 значений, без сортировки и через медиан практически одинаковы.
При увеличении длины массива, самый быстрый способ через медиан. Далее без сортировки. 
Самый долгий способ через сортировку.
"""