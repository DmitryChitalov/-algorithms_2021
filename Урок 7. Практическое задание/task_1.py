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


def bubble_sort(array):
    n = 1
    while n < len(array):
        for i in range(0, len(array) - 1):
            if array[i + 1] > array[i]:
                array[i + 1], array[i] = array[i], array[i + 1]
        n += 1
    return array


def my_bubble_sort(array):
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for j in range(0, len(array) - 1):
            if array[j + 1] > array[j]:
                array[j + 1], array[j] = array[j], array[j + 1]
                is_sorted = False
    return array


def another_bubble_sort(array):
    i = len(array) - 1
    while i > 1:
        for j in range(0, i):
            if array[j + 1] > array[j]:
                array[j + 1], array[j] = array[j], array[j + 1]
        i -= 1
    return array


my_list = [randint(-100, 100) for i in range(5000)]

assert (bubble_sort(my_list[:]) == my_bubble_sort(my_list[:]) == another_bubble_sort(my_list[:]))

print(f'bubble_sort: '
      f'{timeit("bubble_sort(my_list[:])", "from __main__ import bubble_sort, my_list", number=10)}')
print(f'my_bubble_sort: '
      f'{timeit("my_bubble_sort(my_list[:])", "from __main__ import my_bubble_sort, my_list", number=10)}')
print(f'another_bubble_sort: '
      f'{timeit("another_bubble_sort(my_list[:])", "from __main__ import another_bubble_sort, my_list", number=10)}')

""" Первая доработка (завершение сортировки, если при проходе не совершается ни одной перестановки)
практически не уменьшает затраты времени, по сравнению с оригинальной функцией.

Но вторая доработка (уменьшение массива на каждом проходе, т.е. минимальный элемент встает на последнее место и 
в следующем проходе он не берется в расчет) дает некоторое ускорение в ~1.6 раза

Результаты замеров для массива 1000 элементов:
bubble_sort: 0.7014956
my_bubble_sort: 0.6923876
another_bubble_sort: 0.43010250000000005

Результаты замеров для массива 5000 элементов:
bubble_sort: 17.870640799999997
my_bubble_sort: 17.8755284
another_bubble_sort: 11.330250900000003"""
