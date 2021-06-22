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
from timeit import timeit
from statistics import median

m = int(input(f'Введите m: '))
user_list = [randint(0, 10000) for i in range(2 * m + 1)]


def median_delete(lst):
    for i in range(len(lst) // 2):
        lst.remove(max(lst))
    return max(lst)


def median_sort(lst):
    lst.sort()
    return lst[m]


def gnome_sort(arr):
    n = len(arr)
    index = 0
    while index < n:
        if index == 0:
            index += 1
        if arr[index] >= arr[index - 1]:
            index += 1
        else:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index -= 1

    return arr[m]


print(
    f'Функция удаления максимального элемента: {timeit("median_delete(user_list[:])", globals=globals(), number=1000)}')
print(f'Обычная сортировка: {timeit("median_sort(user_list[:])", globals=globals(), number=1000)}')
print(f'Функция median: {timeit("median(user_list[:])", globals=globals(), number=1000)}')
print(f'Сортировка gnome: {timeit("gnome_sort(user_list[:])", globals=globals(), number=1000)}')

'''
m = 100
Функция удаления максимального элемента: 0.26111289999999987
Обычная сортировка: 0.008954000000000129
Функция median: 0.009854099999999866
Сортировка gnome: 3.9031618

m = 300
Функция удаления максимального элемента: 2.179484199999999
Обычная сортировка: 0.04013850000000119
Функция median: 0.0404605999999994
Сортировка gnome: 36.39318

m = 1000
Функция удаления максимального элемента: 23.4133266
Обычная сортировка: 0.1750606000000019
Функция median: 0.1794165999999997
Сортировка gnome: 423.85444040000004

Самая эффективная как показывают замеры это штатная функция median(),
или обычная сортировка sort() и возврат эелемента с индексом m.

"Гномья сортировка" - крайне не эффективная при большом объеме входящих данных.
Вычисление медианы путём удаления максимального элемента - показывает не плохой результат, 
но все еще далеко от стандартного набора вычисление медианы.
'''
