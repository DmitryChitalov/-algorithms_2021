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
from timeit import timeit
from statistics import median


def select_med(lst, user_num):
    for i in range(user_num):
        lst.pop(lst.index(max(lst)))
    return max(lst)


def shell_sort(lst):
    inc = len(lst) // 2
    while inc:
        for i, el in enumerate(lst):
            while i >= inc and lst[i - inc] > el:
                lst[i] = lst[i - inc]
                i -= inc
            lst[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    return lst


user_number = int(input('Введите число: '))

some_lst = [random.randint(0, 100) for i in range(user_number * 2 + 1)]
print(some_lst)
print('-' * 50, 'Поиск встроенной функцией', '-' * 50)
print(f'Медиана - {median(some_lst)}')
print(timeit('median(some_lst)', globals=globals(), number=1000000))

print('-' * 50, 'Определение медианы без сортировки', '-' * 50)
print(f'Медиана - {select_med(some_lst[:], user_number)}')
print(timeit('select_med(some_lst[:], user_number)', globals=globals(), number=1000000))

print('-' * 50, 'Определение медианы с сортировкой Шелла', '-' * 50)
print(f'Медиана - {median(shell_sort(some_lst[:]))}')
print(timeit('median(shell_sort(some_lst[:]))', globals=globals(), number=1000000))

"""
Добавил сортировку Шелла. Сравнил 3 подхода - функция median(), написанная мной функция select_med() и median совместно 
с сортировкой Шелла. 
Шелл проигрывает во много раз, т.к. происходит фактически сортировка вставками. Напиманная функция работает достаточно
быстро, но самая быстрая встроенная функция - median(). 
"""
