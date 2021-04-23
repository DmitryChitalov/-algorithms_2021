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

import timeit
import random


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_optimized(lst_obj):
    n = 1
    while n < len(lst_obj):
        revert_flag = False  # признак наличия перестановки в текущей итерации
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                revert_flag = True  # есть хотя бы одна перестановка
        if not revert_flag:
            return lst_obj  # если на конкретной итерации мы не совершили перестановок, значит массив уже отсортирован
        n += 1
    return lst_obj


orig_list = [random.randint(-100, 99) for _ in range(10)]
# замеры 10
print("bubble_sort",
      timeit.timeit(
          "bubble_sort(orig_list[:])",
          globals=globals(),
          number=1000))
print("bubble_sort_optimized",
      timeit.timeit(
          "bubble_sort_optimized(orig_list[:])",
          globals=globals(),
          number=1000))

orig_list = [random.randint(-100, 99) for _ in range(100)]
# замеры 100
print("bubble_sort",
      timeit.timeit(
          "bubble_sort(orig_list[:])",
          globals=globals(),
          number=1000))
print("bubble_sort_optimized",
      timeit.timeit(
          "bubble_sort_optimized(orig_list[:])",
          globals=globals(),
          number=1000))

orig_list = [random.randint(-100, 99) for _ in range(1000)]

# замеры 1000
print("bubble_sort",
      timeit.timeit(
          "bubble_sort(orig_list[:])",
          globals=globals(),
          number=1000))
print("bubble_sort_optimized",
      timeit.timeit(
          "bubble_sort_optimized(orig_list[:])",
          globals=globals(),
          number=1000))

"""
bubble_sort 0.0126975
bubble_sort_optimized 0.011104700000000002
bubble_sort 0.8095542
bubble_sort_optimized 0.7241498999999999
bubble_sort 78.07904620000001
bubble_sort_optimized 81.8162763
ВЫВОД:
Оптимизация сортировки может помочь в случаях небольших количеств элементов массива, т.к. для них есть ненулевая
вероятность наличия уже отсортированного набора данных на одной из итераций прохождения массива. 
На больших кол-вах элементов мы также можем попасть на уже отсортированный набор, но он будет уже в конце обработки 
массива и относительная экономия будет незаметна. 
Если набор данных имеет неслучайную природу и есть большая веротяность наличия уже отсортирвоанных подмножеств, то
сортировка пузырьком с оптмизацией покажет свою эффективность.
"""
