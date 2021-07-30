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


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_2(lst_obj):  # Добавляю условие выхода из цикла, чтобы не было лишних перепроходов.
    n = 1
    while n < len(lst_obj):
        j = 0
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                j = 1
        if j == 0:
            return lst_obj
        n += 1

    return lst_obj


def bubble_sort_3(lst_obj):  # Меняю условие цикла while, внтури for in убираю обращение к идентичным расчётам через a.
    n = 1
    j = 1

    while j:

        j = 0

        for i in range(len(lst_obj) - n):
            a = i + 1

            if lst_obj[i] < lst_obj[a]:
                lst_obj[i], lst_obj[a] = lst_obj[a], lst_obj[i]
                j = 1

        n += 1

    return lst_obj


orig_list = [randint(-100, 100) for i in range(100)]
print(orig_list)
print()
print(bubble_sort(orig_list[:]))
print()
print(bubble_sort_2(orig_list[:]))
print()
print(bubble_sort_3(orig_list[:]))

print(
    timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=100))

# time = 0.101981495 sec

print(
    timeit(
        "bubble_sort_2(orig_list[:])",
        globals=globals(),
        number=100))
# time = 0.10236242000000001 sec

print(
    timeit(
        "bubble_sort_3(orig_list[:])",
        globals=globals(),
        number=100))
# time = 0.08966013 sec

'''Не смотря на оптимизацию особых успехов в сокращении затрачиваемого времени добиться не удалось,а первая оптимизация
и вовсе не приносит результов, либо делает только хуже.'''