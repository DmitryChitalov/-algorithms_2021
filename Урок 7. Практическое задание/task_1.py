"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в виде функции.

Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение. Обязательно сделайте замеры времени обеих реализаций
и укажите дала ли оптимизация эффективность.

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.

Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""
import timeit
import random


# def time(func):
#     def wrapped(*args, **kwargs):

def bubble_sort(l: list):
    for i in range(len(l)):
        for j in range(len(l) - 1):
            if l[j] < l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    return l


def bubble_sort_better(l: list):
    is_sorted = False
    for i in range(len(l)):
        if is_sorted is False and i > 0:
            return l
        for j in range(len(l) - 1):
            if l[j] < l[j + 1]:
                is_sorted = True
                l[j], l[j + 1] = l[j + 1], l[j]
    return l


def generate_list():
    return [random.randint(-100, 100) for _ in range(100)]


my_list_1 = generate_list()
b_1 = bubble_sort(my_list_1[:])
print(b_1)
b_2 = bubble_sort_better(my_list_1[:])
print(b_2)
print(
    f"Сортировка списка функцией bubble_sort составила {timeit.timeit('bubble_sort(my_list_1[:])', globals=globals(), number=1000)} секунд")
print(
    f"Сортировка списка функцией bubble_sort_better составила {timeit.timeit('bubble_sort_better(my_list_1[:])', globals=globals(), number=1000)} секунд")
# Сортировка списка функцией bubble_sort составила 2.1801306 секунд
# Сортировка списка функцией bubble_sort_better составила 1.9687242 секунд
#
# Сортировка списка функцией bubble_sort составила 1.9808310999999998 секунд
# Сортировка списка функцией bubble_sort_better составила 1.9300709 секунд
#
# Сортировка списка функцией bubble_sort составила 2.0358642999999996 секунд
# Сортировка списка функцией bubble_sort_better составила 1.8717679 секунд

"""В общем-то улучшение алгоритма привело к уменьшению затраченного на сортировку
времени. Однако на больших n сортировка  по прежнему остается малоэффективной"""
