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
import random
from statistics import median
import timeit


def median_sort(lst_obj):
    return sorted(lst_obj)[(len(lst_obj) - 1) // 2]


def gnome_sort(lst_obj):
    i, size = 1, len(lst_obj)
    while i < size:
        if lst_obj[i - 1] <= lst_obj[i]:
            i += 1
        else:
            lst_obj[i - 1], lst_obj[i] = lst_obj[i], lst_obj[i - 1]
            if i > 1:
                i -= 1
    return lst_obj[(size - 1) // 2]


def median_max(lst_obj):
    for _ in range(len(lst_obj) // 2):
        lst_obj.remove(max(lst_obj))
    return max(lst_obj)


def median_left_right(lst_obj):
    left = []
    right = []
    for i in range(len(lst_obj)):
        for j in range(len(lst_obj)):
            if i == j:
                continue
            if lst_obj[j] < lst_obj[i]:
                left.append(lst_obj[j])
            elif lst_obj[j] > lst_obj[i]:
                right.append(lst_obj[j])
            else:
                if j < i:
                    left.append(lst_obj[j])
                else:
                    right.append(lst_obj[j])
        if len(left) == len(right):
            return lst_obj[i]
        else:
            left.clear()
            right.clear()


m = 10
orig_list = [random.randint(-100, 100) for _ in range(2 * m + 1)]
print(orig_list)
print(f'Медиана встроенная функция: {median(orig_list[:])}')
print(f'Медиана встроенная сортировка: {median_sort(orig_list[:])}')
print(f'Медиана гномья сортировка: {gnome_sort(orig_list[:])}')
print(f'Медиана удаление максимальных элементов: {median_max(orig_list[:])}')
print(f'Медиана два массива: {median_left_right(orig_list[:])}')

print('m = 10')
print(f'Медиана встроенная функция: {timeit.timeit("median(orig_list[:])", globals=globals(), number=1000)}')
print(f'Медиана встроенная сортировка: {timeit.timeit("median_sort(orig_list[:])", globals=globals(), number=1000)}')
print(f'Медиана гномья сортировка: {timeit.timeit("gnome_sort(orig_list[:])", globals=globals(), number=1000)}')
print(f'Медиана удаление максимальных элементов:'
      f' {timeit.timeit("median_max(orig_list[:])", globals=globals(), number=1000)}')
print(f'Медиана два массива: {timeit.timeit("median_left_right(orig_list[:])", globals=globals(), number=1000)}')

m = 100
orig_list = [random.randint(-100, 100) for _ in range(2 * m + 1)]
print('m = 100')
print(f'Медиана встроенная функция: {timeit.timeit("median(orig_list[:])", globals=globals(), number=1000)}')
print(f'Медиана встроенная сортировка: {timeit.timeit("median_sort(orig_list[:])", globals=globals(), number=1000)}')
print(f'Медиана гномья сортировка: {timeit.timeit("gnome_sort(orig_list[:])", globals=globals(), number=1000)}')
print(f'Медиана удаление максимальных элементов:'
      f' {timeit.timeit("median_max(orig_list[:])", globals=globals(), number=1000)}')
print(f'Медиана два массива: {timeit.timeit("median_left_right(orig_list[:])", globals=globals(), number=1000)}')

m = 500
orig_list = [random.randint(-100, 100) for _ in range(2 * m + 1)]
print('m = 500')
print(f'Медиана встроенная функция: {timeit.timeit("median(orig_list[:])", globals=globals(), number=1000)}')
print(f'Медиана встроенная сортировка: {timeit.timeit("median_sort(orig_list[:])", globals=globals(), number=1000)}')
print(f'Медиана гномья сортировка: {timeit.timeit("gnome_sort(orig_list[:])", globals=globals(), number=1000)}')
print(f'Медиана удаление максимальных элементов:'
      f' {timeit.timeit("median_max(orig_list[:])", globals=globals(), number=1000)}')
print(f'Медиана два массива: {timeit.timeit("median_left_right(orig_list[:])", globals=globals(), number=1000)}')

"""
m = 10
Медиана встроенная функция: 0.0015953999999999968
Медиана встроенная сортировка: 0.0015812000000000048
Медиана гномья сортировка: 0.08861199999999998
Медиана удаление максимальных элементов: 0.012586399999999998
Медиана два массива: 0.0669805
m = 100
Медиана встроенная функция: 0.0157515
Медиана встроенная сортировка: 0.015816400000000008
Медиана гномья сортировка: 10.055439199999999
Медиана удаление максимальных элементов: 0.7736961000000004
Медиана два массива: 15.453290999999998
m = 500
Медиана встроенная функция: 0.12870510000000124
Медиана встроенная сортировка: 0.12971849999999918
Медиана гномья сортировка: 260.3074643
Медиана удаление максимальных элементов: 15.706856200000004
Медиана два массива: 294.89806319999997

Функция median_sort() использует встроенный алгоритм сортировки и имеет сложность O(NlogN), выполняется очень
быстро, особенно это заметно при больших размерах входного массива
Функция gnome_sort() использует алгоритм гномьей сортировки и имеет сложность O(n^2), выполняется намного медленнее, 
особенно при больших входных данных
Функция  median_max() имеет сложность O(n^2), несмотря на это благодаря встроенным фунциям выполняется значительно
быстрее, чем гномья сортировка
Функция median_left_right() имеет сложность O(n^2), выполняется медленнее чем все остальные варианты.
"""
