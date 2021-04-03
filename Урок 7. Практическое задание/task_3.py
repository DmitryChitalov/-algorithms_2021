"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные по длине части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, Кучей...
"""

import statistics
import random


def shell_sort(lst):
    """Функция сортирует список методом Шелла"""
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
    """Функция гномьей сортировки списка"""
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


def media_out_sort_1(lst):
    """
    Функция нахождения медианы в неотсортированном списке
    выравниванием списков
    """
    left = []
    right = []
    for i in lst:
        for j in lst:
            if j <= i:
                left.append(j)
            if j >= i:
                right.append(j)
        if len(left) == len(right) \
                or len(left) + 1 == len(right) \
                or len(left) == len(right) + 1:
            return i

        left.clear()
        right.clear()


def media_out_sort_2(lst):
    """
    Функция нахождения медианы в неотсортированном списке
    удалением половины мах-значений
    """
    for i in range(len(lst) // 2):
        lst.remove(max(lst))
    return max(lst)


if __name__ == '__main__':
    m = 4

    orig_list = [random.randint(-10, 10) for _ in range(2 * m + 1)]

    print(f'Сгенерированный список          : {orig_list}')
    print(f'Сортировка методом Шелла        : {shell_sort(orig_list[:])}')
    print(f'Гномья сортировка               : {gnome_sort(orig_list[:])}')
    print(f'Медиана в отсортированном списке: {shell_sort(orig_list[:])[m]}')
    print(f'Медиана без сортировки\n'
          f'statistics.median               : {statistics.median(orig_list)}\n'
          f'выравниванием списков           : {media_out_sort_1(orig_list)}\n'
          f'удалением половины мах-значений : {media_out_sort_2(orig_list)}')


"""
При поиске медианы выравниванием списков при увеличении 
длинны списка % возвращения None увеличивается.
"""
