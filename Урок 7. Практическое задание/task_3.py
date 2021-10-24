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
from statistics import median
from random import randint
from timeit import timeit


def my_median(my_lst):
    """Поиск медианы с помощью рекурсии. При каждом вызове удаляем самый максимальный и минимальный элемент. частное решение - остался один элемент в массиве, он и есть медиана"""
    if len(my_lst) == 1:
        return my_lst[0]
    else:
        my_lst.pop(my_lst.index(max(my_lst)))
        my_lst.pop(my_lst.index(min(my_lst)))
        return my_median(my_lst)


def shell_sort(my_lst):
    """Функция сортирует список методом Шелла"""
    gap = len(my_lst) // 2
    while gap > 0:
        for value in range(gap, len(my_lst)):
            current_value = my_lst[value]
            position = value
            while position >= gap and my_lst[position - gap] > current_value:
                my_lst[position] = my_lst[position - gap]
                position -= gap
                my_lst[position] = current_value

        gap //= 2
    return my_lst


m = 10
my_lst = [randint(-1000, 1000) for _ in range(2 * m + 1)]
print(f'1000 измерений при длинне списка {len(my_lst)}')
print(f'Моя функция {timeit("my_median(my_lst[:])", globals=globals(), number=1000)}')
print(f'Моя функция {timeit("median(my_lst[:])", globals=globals(), number=1000)}')
print(f'Моя функция {timeit("shell_sort(my_lst[:])", globals=globals(), number=1000)}')
m = 100
my_lst = [randint(-1000, 1000) for _ in range(2 * m + 1)]
print(f'1000 измерений при длинне списка {len(my_lst)}')
print(f'Моя функция {timeit("my_median(my_lst[:])", globals=globals(), number=1000)}')
print(f'Моя функция {timeit("median(my_lst[:])", globals=globals(), number=1000)}')
print(f'Моя функция {timeit("shell_sort(my_lst[:])", globals=globals(), number=1000)}')
m = 500
my_lst = [randint(-1000, 1000) for _ in range(2 * m + 1)]
print(f'1000 измерений при длинне списка {len(my_lst)}')
print(f'Моя функция {timeit("my_median(my_lst[:])", globals=globals(), number=1000)}')
print(f'Моя функция {timeit("median(my_lst[:])", globals=globals(), number=1000)}')
print(f'Моя функция {timeit("shell_sort(my_lst[:])", globals=globals(), number=1000)}')
"""
1000 измерений при длинне списка 21
Моя функция 0.0568206
Моя функция 0.0037152000000000296
Моя функция 0.0802446
1000 измерений при длинне списка 201
Моя функция 1.1212688
Моя функция 0.027434100000000017
Моя функция 0.7530474
1000 измерений при длинне списка 1001
Моя функция 26.1143498
Моя функция 0.1791310000000017
Моя функция 5.561405699999998
Из замеров видно что моя функция эффективнее только при небольшой длинне списка.
Самая эффективная median из библиотеки statistics
"""
