"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в
виде функции.

Обязательно доработайте алгоритм (сделайте его умнее)!

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение.
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.

Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""
from random import randint
from timeit import timeit


def bubble_sort(sort_list):
    n = 1
    while n <= len(sort_list):
        for i in range(len(sort_list) - n):
            if sort_list[i] < sort_list[i + 1]:
                sort_list[i], sort_list[i + 1] = sort_list[i + 1], sort_list[i]
        n += 1
    return sort_list


def bubble_sort_updated(sort_list):
    n = 1
    while n <= len(sort_list):
        с = 0
        for i in range(len(sort_list) - n):
            if sort_list[i] < sort_list[i + 1]:
                sort_list[i], sort_list[i + 1] = sort_list[i + 1], sort_list[i]
                с += 1
        if с == 0:
            break
        n += 1
    return sort_list

data_list = [randint(-100, 100) for _ in range(10)]
ord_list = list(range(100, -10, -1))

print(f'Исходный: {data_list}\n'
      f'Отсортированный: {bubble_sort_updated(data_list[:])}')

'''
Дороботка заключается в том, что если за проходку не насчитается ни одной
замены, то цикл прекратится. 
'''
print('unsorted')

print('bubble_sort')

print(timeit('bubble_sort(data_list[:])', globals=globals(), number=10000))

print('bubble_sort_updated:')

print(timeit('bubble_sort_updated(data_list[:])', globals=globals(), number=1000))

print('-' * 10)


print('sorted')
print('bubble_sort')

print(timeit('bubble_sort(ord_list[:])', globals=globals(), number=10000))

print('bubble_sort_updated')

print(timeit('bubble_sort_updated(ord_list[:])', globals=globals(), number=10000))


#Модифицированая сортировка на уже отсортированых списках отрабатывает значительно быстрее. На практике уже отсортированные
#списки встречаются ну очень редко.

Исходный: [-26, -53, 79, -36, 73, 78, -99, -16, 96, 81]
Отсортированный: [96, 81, 79, 78, 73, -16, -26, -36, -53, -99]
unsorted
bubble_sort
0.10573649999999998
bubble_sort_updated:
0.011058600000000002
----------
sorted
bubble_sort
4.3953561
bubble_sort_updated
0.07868860000000044
