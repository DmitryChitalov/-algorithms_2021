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


def bubble_sort_1(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in reversed(range(len(lst_obj) - n)):
            if lst_obj[i] > lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_2(lst_obj):
    n = 1
    end_cycle = False
    while n < len(lst_obj):
        for i in reversed(range(len(lst_obj) - n)):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                end_cycle = True
        n += 1
        if not end_cycle:
            return lst_obj
        end_cycle = False
    return lst_obj


orig_list = [random.randint(-100, 100) for _ in range(10)]

print(orig_list)
print(bubble_sort_2(orig_list[:]))

# замеры 10
print(
    timeit.timeit(
        "bubble_sort_1(orig_list[:])",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "bubble_sort_2(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.randint(-100, 100) for _ in range(100)]

# замеры 100
print(
    timeit.timeit(
        "bubble_sort_1(orig_list[:])",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "bubble_sort_2(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(
    timeit.timeit(
        "bubble_sort_1(orig_list[:])",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "bubble_sort_2(orig_list[:])",
        globals=globals(),
        number=1000))

"""
замеры 10
без выхода из цикла - 0.009643400000000003
с выхода из цикла - 0.005939800000000002

замеры 100
без выхода из цикла - 0.5724684
с выхода из цикла - 0.47207999999999994

замеры 1000
без выхода из цикла - 64.4959357
с выхода из цикла - 57.7190696

Доработка заключалась в том, что мы ставим флаг True если есть хоть одна сортировка, после обнуляем флаг.
Если в конце цикла for у нас флаг False(сортировок не было) возращаем массив
При добовлении дополнительной проверки время сортировки массива уменьшилось!

ДОработка ускорила время выполнения функции сортировки!
"""
