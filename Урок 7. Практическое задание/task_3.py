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


import timeit
from random import randint, choice
from statistics import median


def quickselect_median(arr, pivot_fn=choice):
    if len(arr) % 2 == 1:
        return quickselect(arr, len(arr) / 2, pivot_fn)
    else:
        return 0.5 * (quickselect(arr, len(arr) / 2 - 1, pivot_fn) +
                      quickselect(arr, len(arr) / 2, pivot_fn))


def quickselect(arr, k, pivot_fn):
    """
    Выбираем k-тый элемент в списке l (с нулевой базой)
    arr: список числовых данных
    k: индекс
    pivot_fn: функция выбора pivot, по умолчанию выбирает случайно
    """
    if len(arr) == 1:
        assert k == 0
        return arr[0]
    pivot = pivot_fn(arr)
    lows = [el for el in arr if el < pivot]
    highs = [el for el in arr if el > pivot]
    pivots = [el for el in arr if el == pivot]
    if k < len(lows):
        return quickselect(lows, k, pivot_fn)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots), pivot_fn)


def gnome_sort(sort_list):
    """
    Сортировка списка методом gnome_sort
    Происходит просмотр массива слева-направо,
    при этом сравниваются (и меняются, если это неотсортированная пара) соседние элементы.
    Если происходит обмен элементов, то проиходит возвращение на один шаг назад.
    Если обменов не происходит, то алгоритм продолжает просмотр массива слева-направо
    в поиске неотсортированных пар.
    """
    i = 1
    while i < len(sort_list):
        if not i or sort_list[i - 1] <= sort_list[i]:
            i += 1
        else:
            sort_list[i], sort_list[i - 1] = sort_list[i - 1], sort_list[i]
            i -= 1
    return sort_list


def gnome_median(sort_list):
    return gnome_sort(sort_list)[len(sort_list) // 2]


m = int(input('Введите m: '))
orig_list = [randint(0, 100) for i in range(2 * m + 1)]
print(f'Исходный массив:\n{orig_list}\n')
print(f'Медиана (Функция quickselect_median)- {quickselect_median(orig_list)}')
print(f'Медиана (через встроенную функцию) - {median(orig_list)}')
print(f'Медиана (метод сортировки Гномья) - {gnome_sort(orig_list)[m]}')


print(
    timeit.timeit(
        "quickselect_median(orig_list[:])",
        globals=globals(),
        number=10000))
print(
    timeit.timeit(
        "median(orig_list[:])",
        globals=globals(),
        number=10000))

print(
    timeit.timeit(
        "gnome_sort(orig_list[:])",
        globals=globals(),
        number=10000))

"""
Введите m: 5
Исходный массив:
[48, 28, 88, 30, 71, 97, 52, 35, 74, 68, 68]

Медиана (Функция quickselect_median)- 68
Медиана (через встроенную функцию) - 68
Медиана (метод сортировки Гномья) - 68
0.10921669999999994
0.008400799999999986
0.044560399999999944

Введите m: 100
Исходный массив:
[61, 64, 19, 11, 85, 72, 31, 2, 25, 99, 24, 37, 23, 54, 18, 19, 65, 14, 7, 5, 6, 3, 47, 18, 42, 100, 75, 18, 97, ...]

Медиана (Функция quickselect_median)- 48
Медиана (через встроенную функцию) - 48
Медиана (метод сортировки Гномья) - 48
1.4353312000000003
0.05036549999999984
0.6424282000000003

Введите m: 1000
Исходный массив:
[59, 86, 3, 26, 34, 87, 25, 34, 77, 43, 88, 64, 88, 27, 33, 45, 17, 7, 20, 98, 15, 32, 37, 12, 50, 85, 48, ... ]

Медиана (Функция quickselect_median)- 50
Медиана (через встроенную функцию) - 50
Медиана (метод сортировки Гномья) - 50
12.0432396
0.3283333000000006
6.212762999999999

Лучший результат по замеру показал ествественно встроенная функция median
"""