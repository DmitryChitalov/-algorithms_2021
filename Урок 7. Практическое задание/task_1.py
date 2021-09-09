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


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] > lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_adv1(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_adv2(lst_obj):
    '''

    доработка ИНОГДА немного уменьшает время за счет экономии в проходе по циклу.
    0.573208 сортировка по убыванию
    0.5401336000000001 сортировка по убыванию с доработкой
    доработка будет полезна на многократных запусках небольших массивов, так как вероятность
    "досрочной" сортировки там больше, чем на больших
    '''
    n = 1
    while n < len(lst_obj):
        is_sort = False
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1], is_sort = lst_obj[i + 1], lst_obj[i], True
        if not is_sort:
            break
        n += 1
    return lst_obj


orig_list = [random.randint(-100, 100) for _ in range(100)]

print(
    timeit.timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000), 'исходный скрипт')

print(
    timeit.timeit(
        "bubble_sort_adv1(orig_list[:])",
        globals=globals(),
        number=1000), 'сортировка по убыванию')

print(
    timeit.timeit(
        "bubble_sort_adv2(orig_list[:])",
        globals=globals(),
        number=1000), 'сортировка по убыванию с доработкой')

print(orig_list)
print(bubble_sort(orig_list[:]))
print(bubble_sort_adv1(orig_list[:]))
print(bubble_sort_adv2(orig_list[:]))
