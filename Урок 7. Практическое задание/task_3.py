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


def shell_sort(lst):
    """
    Функция сортировки методом Шелла
    """
    gap = len(lst) // 2
    while gap > 0:
        for value in range(gap, len(lst)):
            current_value = lst[value]
            position = value
            while position >= gap and lst[position - gap] > current_value:
                lst[position] = lst[position - gap]
                position -= gap
                lst[position] = current_value

        gap //= 2
    return lst


def gnome_sort(lst):
    """
    Функция Гномьей сортировки
    """
    index = 1
    i = 0
    while i < len(lst) - 1:
        if lst[i] <= lst[i + 1]:
            i, index = index, index + 1
        else:
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
            i -= 1
            if i < 0:
                i = index
                index += 1
    return lst


m = 100
orig_list = [random.randint(0, 10000) for _ in range(2 * m + 1)]

print(f'Медиана в списке, отсортированном методом Шелла: {shell_sort(orig_list[:])[m]}')
print(f'Медиана в списке, отсортированном Гномьей сортировкой: {gnome_sort(orig_list[:])[m]}')
print(f'Медиана, найденная встроенной функцией: {median(orig_list[:])}\n')

print(f'Замер времени поиска медианы при сортировке методом Шелла:'
      f' {timeit.timeit("shell_sort(orig_list[:])[m]", globals=globals(), number=1000)} сек.')
print(f'Замер времени поиска медианы при сортировке Гномьей сортировкой:'
      f' {timeit.timeit("gnome_sort(orig_list[:])[m]", globals=globals(), number=1000)} сек.')
print(f'Замер времени поиска медианы встроенной функцией:'
      f' {timeit.timeit("median(orig_list[:])", globals=globals(), number=1000)} сек.')

"""
Результаты при m = 100:
Медиана в списке, отсортированном методом Шелла: 5238
Медиана в списке, отсортированном Гномьей сортировкой: 5238
Медиана, найденная встроенной функцией: 5238

Замер времени поиска медианы при сортировке методом Шелла: 0.3673369 сек.
Замер времени поиска медианы при сортировке Гномьей сортировкой: 2.8845364 сек.
Замер времени поиска медианы встроенной функцией: 0.007851300000000005 сек.

Вывод: встроенная функция поиска медианы наиболее оптимальна для использования, так как затрачивает наименьшее
количество времени на выполнение. На втором месте - сортировка методом Шелла. По сравнению с ними Гномья сортировка к
использованию категорически не рекомендуется, так как занимает на порядки больше времени.
"""
