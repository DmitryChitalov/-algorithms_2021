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
        count = 0
        for i in range(len(sort_list) - n):
            if sort_list[i] < sort_list[i + 1]:
                sort_list[i], sort_list[i + 1] = sort_list[i + 1], sort_list[i]
                count += 1
        if count == 0:
            break
        n += 1
    return sort_list


my_list = [randint(-100, 99) for i in range(20)]
ord_list = list(range(9, -10, -1))

print(f'Исходный: {my_list}\nОтсортированный: {bubble_sort_updated(my_list[:])}')

'''
Суть данной доработки заключается в том, что если за проходку не насчитается ни одной
замены, то цикл прекратится. Это касается как изначально отсортированных списков,
так и списков, которые отсортировались бы еще до окончания цикла.
'''

print('-' * 200)

print('До:')
print(timeit('bubble_sort(my_list[:])', globals=globals(), number=10))
print(timeit('bubble_sort(my_list[:])', globals=globals(), number=100))
print(timeit('bubble_sort(my_list[:])', globals=globals(), number=1000))

print('После:')
print(timeit('bubble_sort_updated(my_list[:])', globals=globals(), number=10))
print(timeit('bubble_sort_updated(my_list[:])', globals=globals(), number=100))
print(timeit('bubble_sort_updated(my_list[:])', globals=globals(), number=1000))

print('-' * 200)

print('До:')
print(timeit('bubble_sort(ord_list[:])', globals=globals(), number=10))
print(timeit('bubble_sort(ord_list[:])', globals=globals(), number=100))
print(timeit('bubble_sort(ord_list[:])', globals=globals(), number=1000))

print('После:')
print(timeit('bubble_sort_updated(ord_list[:])', globals=globals(), number=10))
print(timeit('bubble_sort_updated(ord_list[:])', globals=globals(), number=100))
print(timeit('bubble_sort_updated(ord_list[:])', globals=globals(), number=1000))

'''
Результат:

Исходный: [16, 69, -93, -99, 0, -85, 48, -38, 75, -99, -38, -79, -96, -32, 62, -6, 45, 26, -8, -30]
Отсортированный: [75, 69, 62, 48, 45, 26, 16, 0, -6, -8, -30, -32, -38, -38, -79, -85, -93, -96, -99, -99]

Неотсортированный список:
До:
0.0004503000000000007
0.0045398999999999995
0.04437279999999999
После:
0.0004904999999999909
0.004847500000000005
0.0474021

Отсортированный список:
До:
0.00022880000000000122
0.002248899999999998
0.02259929999999999
После:
2.36000000000125e-05
0.0002198999999999951
0.0022019000000000066

По итогу, можно сказать, что толком ничего не изменилось, скорость остается все 
такой же, пусть мы и сделали функцию "Умнее". А раз на практике уже отсортированные
списки встречаются ну очень редко, то смысла таком изменении кода нет.
'''