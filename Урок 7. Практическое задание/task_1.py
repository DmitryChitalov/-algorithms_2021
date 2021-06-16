"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в виде функции.

Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение. Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.

Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""
"""
Вывод: Обычный пузырьковый метод показал себя хуже всего, особенно при возрастание длины массива. Метод рассмотренный 
на уроке дал такие же результаты как и метод со срезом и они оказались самыми лучшими, так как в обои случаях количество
итераций с каждым проходом уменьшается. Функция bubble_sort_true_false будет выполнена быстро только в одном случае - 
если все элементы массива уже будут отсортированы, но с увеличением длины массива вероятность такого исхода стремится к 
нуля, поэтому такой метод можно считать не оптимизированным.
"""
from timeit import timeit
import random


def bubble_sort(lst_obj):
    n = len(lst_obj)
    for num in range(n):
        for i in range(len(lst_obj) - 1):
            if lst_obj[i + 1] < lst_obj[i]:
                lst_obj[i + 1], lst_obj[i] = lst_obj[i], lst_obj[i + 1]
    return lst_obj


def bubble_sort_lesson(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_true_false(lst_obj):
    n = 1
    swapped = True
    while swapped and n < len(lst_obj):
        swapped = False
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                swapped = True
        n += 1
    return lst_obj


def optimized_bubble_sort(lst_obj):
    n = len(lst_obj)
    for j in range(n):
        for i in range(len(lst_obj[j:]) - 1):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
    return lst_obj


orig_list_10 = [random.randint(-100, 100) for num in range(10)]
orig_list_100 = [random.randint(-100, 100) for num1 in range(100)]
orig_list_1000 = [random.randint(-100, 100) for num2 in range(1000)]
print('bubble_sort 10', timeit('bubble_sort(orig_list_10[:])', globals=globals(), number=1000))
print('bubble_sort_lesson 10', timeit('bubble_sort_lesson(orig_list_10[:])', globals=globals(), number=1000))
print('bubble_sort_true_false 10', timeit('bubble_sort_true_false(orig_list_10[:])', globals=globals(), number=1000))
print('optimized_bubble_sort 10', timeit('optimized_bubble_sort(orig_list_10[:])', globals=globals(), number=1000))
print('bubble_sort 100', timeit('bubble_sort(orig_list_100[:])', globals=globals(), number=1000))
print('bubble_sort_lesson 100', timeit('bubble_sort_lesson(orig_list_100[:])', globals=globals(), number=1000))
print('bubble_sort_true_false 100', timeit('bubble_sort_true_false(orig_list_100[:])', globals=globals(), number=1000))
print('optimized_bubble_sort 100', timeit('optimized_bubble_sort(orig_list_100[:])', globals=globals(), number=1000))
print('bubble_sort 1000', timeit('bubble_sort(orig_list_1000[:])', globals=globals(), number=1000))
print('bubble_sort_lesson 1000', timeit('bubble_sort_lesson(orig_list_1000[:])', globals=globals(), number=1000))
print('bubble_sort_true_false1000', timeit('bubble_sort_true_false(orig_list_1000[:])', globals=globals(), number=1000))
print('optimized_bubble_sort 1000', timeit('optimized_bubble_sort(orig_list_1000[:])', globals=globals(), number=1000))

"""
bubble_sort 10 0.0120409
bubble_sort_lesson 10 0.010873500000000001
bubble_sort_true_false 10 0.010849099999999993
optimized_bubble_sort 10 0.0105605
bubble_sort 100 1.0754035
bubble_sort_lesson 100 0.7069619999999999
bubble_sort_true_false 100 0.7244129000000001
optimized_bubble_sort 100 0.7457208
bubble_sort 1000 118.0728094
bubble_sort_lesson 1000 76.4505662
bubble_sort_true_false 1000 83.97445300000001
optimized_bubble_sort 1000 78.0812206
"""
