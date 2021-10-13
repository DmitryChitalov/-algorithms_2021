import operator
import timeit
from random import random


amount_of_el = input('Введите количество элементов: ')
my_list = [random() * 50 for _ in range(int(amount_of_el))]


def merge_sort(lst, compare=operator.lt):
    if len(lst) < 2:
        return lst[:]
    else:
        middle = int(len(lst) / 2)
        left = merge_sort(lst[:middle], compare)
        right = merge_sort(lst[middle:], compare)
        return merge(left, right, compare)


def merge(left, right, compare):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


if __name__ == '__main__':
    print('Исходный массив:', my_list)
    print(f"Отсортированный массив: {merge_sort(my_list[:])}")
    my_list_10 = [random() * 50 for _ in range(10)]
    print("Замер для 10 элементов:")
    print(timeit.timeit("merge_sort(my_list_10[:])", globals=globals(), number=1000))
    my_list_100 = [random() * 50 for _ in range(100)]
    print("Замер для 100 элементов:")
    print(timeit.timeit("merge_sort(my_list_100[:])", globals=globals(), number=1000))
    my_list_1000 = [random() * 50 for _ in range(1000)]
    print("Замер для 1000 элементов:")
    print(timeit.timeit("merge_sort(my_list_1000[:])", globals=globals(), number=1000))

    """
    Введите количество элементов: 5
    Исходный массив: 
    [45.09768452300635, 3.775246799587151, 42.73910460357915, 36.64009213352199, 7.3361544632147115]
    Отсортированный массив:
     [3.775246799587151, 7.3361544632147115, 36.64009213352199, 42.73910460357915, 45.09768452300635]
    Замер для 10 элементов:
    0.036698140000225976
    Замер для 100 элементов:
    0.5001583879993632
    Замер для 1000 элементов:
    6.8031157570003415
    """
