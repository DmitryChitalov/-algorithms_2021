"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках
"""
from random import randint
from statistics import median
import timeit

my_list = [randint(0, 100) for i in range(2 * int(input('Введите m: ')) + 1)]


def without_sort_1(ex_list):
    res_list = ex_list
    left_list = []
    right_list = []
    for i in range(len(res_list)):
        for j in range(len(res_list)):
            if res_list[i] > res_list[j]:
                left_list.append(res_list[j])
            if res_list[i] < res_list[j]:
                right_list.append(res_list[j])
            if res_list[i] == res_list[j] and i > j:
                left_list.append(res_list[j])
            if res_list[i] == res_list[j] and i < j:
                right_list.append(res_list[j])
        if len(left_list) == len(right_list):
            return res_list[i]
        left_list.clear()
        right_list.clear()


def without_sort_2(ex_list):
    res_list = ex_list
    for i in range(len(ex_list) // 2):
        res_list.remove(max(res_list))
    return max(res_list)


print('Исходный массив: ', my_list)
print('Медиана со встроенной функцией: ', median(my_list))
print('Медиана без сортировки вариант № 1: ', without_sort_1(my_list))
print('Медиана без сортировки вариант № 2: ', without_sort_2(my_list))
print('--------------------')
print(timeit.timeit("median(my_list[:])",
                    setup="from __main__ import median, my_list",
                    number=1000))
print(timeit.timeit("without_sort_1(my_list[:])",
                    setup="from __main__ import without_sort_1, my_list",
                    number=1000))
print(timeit.timeit("without_sort_2(my_list[:])",
                    setup="from __main__ import without_sort_2, my_list",
                    number=1000))

# Встроенная функция - самый быстрый вариант (что и ожидалось изначально)
