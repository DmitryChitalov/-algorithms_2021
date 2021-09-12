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
from random import randint
from statistics import median
from timeit import timeit


def gnome(data, m):
    i, size = 1, len(data)
    while i < size:
        if data[i - 1] <= data[i]:
            i += 1
        else:
            data[i - 1], data[i] = data[i], data[i - 1]
            if i > 1:
                i -= 1
    return f'Отсортированный: {data}\n' \
           f'Гномья сортировка: {data[m]}'


def gnome_opt(data, m):
    i, j, size = 1, 2, len(data)
    while i < size:
        if data[i - 1] <= data[i]:
            i, j = j, j + 1
        else:
            data[i - 1], data[i] = data[i], data[i - 1]
            i -= 1
            if i == 0:
                i, j = j, j + 1
    return f'Гномья сортировка оптимизированная: {data[m]}'


def cycle(lst, m):
    for _ in range(m):
        lst.remove(max(lst))
    return f'Цикл без сортировки: {max(lst)}'


def median_sort(lst):
    return f'Встроенная функция: {median(lst)}'


m = int(input('Введите m: '))
lst = [randint(1, 10) for i in range(2 * m + 1)]
print(f'Исходный массив: {lst}')
print(gnome(lst[:], m))
print(gnome_opt(lst[:], m))
print(cycle(lst[:], m))
print(median_sort(lst[:]))
print(f"Гномья:       {timeit('gnome(lst[:], m)', globals=globals(), number=1000)}")
print(f"Гномья (опт): {timeit('gnome_opt(lst[:], m)', globals=globals(), number=1000)}")
print(f"Цикл:         {timeit('cycle(lst[:], m)', globals=globals(), number=1000)}")
print(f"median:       {timeit('median_sort(lst[:])', globals=globals(), number=1000)}")

"""
Введите m: 4
Исходный массив: [5, 6, 9, 10, 1, 3, 1, 3, 8]
Отсортированный: [1, 1, 3, 3, 5, 6, 8, 9, 10]
Гномья сортировка: 5
Гномья сортировка оптимизированная: 5
Цикл без сортировки: 5
Встроенная функция: 5
Гномья:       0.0070653999999998884
Гномья (опт): 0.004582599999999992
Цикл:         0.001601899999999823
median:       0.0006470000000000642

Введите m: 100
Гномья:       2.9419400999999996
Гномья (опт): 2.1084819999999995
Цикл:         0.2713437999999986
median:       0.006293900000001074

При определении медианы встроенная функция работает быстрее всех. Особенно заметно это становится при увеличении кол-ва 
элементов.
"""
