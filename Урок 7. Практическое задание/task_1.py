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

import random, timeit

count = 1000

num_array = [random.randint(-100, 99) for i in range(count)]
ordered_num_array = [count - i for i in range(count)]
print('ordered_array', ordered_num_array)
print(num_array)


def bubble_sort(arr):
    arr_count = len(arr)
    i = 0
    while i < arr_count:
        j = i
        while j < arr_count:
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
            j += 1
        i += 1
    return arr


def optimized_bubble_sort(arr):
    arr_count = len(arr)
    i = 0
    is_ordered = True
    while i < arr_count:
        j = i
        while j < arr_count:
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                is_ordered = False
            j += 1
        if is_ordered:
            break
        i += 1
    return arr


print(
    timeit.timeit(
        "bubble_sort(num_array[:])",
        globals=globals(),
        number=1000))


print(
    timeit.timeit(
        "bubble_sort(ordered_num_array[:])",
        globals=globals(),
        number=1000))


print(
    timeit.timeit(
        "optimized_bubble_sort(num_array[:])",
        globals=globals(),
        number=1000))


print(
    timeit.timeit(
        "optimized_bubble_sort(ordered_num_array[:])",
        globals=globals(),
        number=1000))


"""
44.10900157900005 неотсортированный неоптимизированный массив
37.7617872360006 отсортированный неоптимизированный массив
44.542092404999494 неотсортированный оптимизированный массив
0.07441270199979044 отсортированный оптимизированный массив

Оптимизированный алгоритм на упорядоченном массиве показал очень хороший прирост скорости, однако если 
передать ему неотсортированный массив, то мы ничего не выиграемю

Доработка помогла, но шанс на то, что мы попадем на такой массив крайне мал 
"""