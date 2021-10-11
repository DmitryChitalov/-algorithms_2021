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
    for _ in range(len(lst_obj) - 1):
        for i in range(len(lst_obj) - 1):
            if lst_obj[i] < lst_obj[i+1]:  # Поменяли знак и сортировка по убыванию
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
    return lst_obj


def bubble_sort_2(lst_obj):
    flag = True
    while flag:
        flag = False
        for i in range(len(lst_obj) - 1):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
                flag = True
    return lst_obj


def bubble_sort_3(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i+1]:  # Поменяли знак и сортировка по убыванию
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_4(lst_obj):
    n = 1
    flag = True
    while flag:
        flag = False
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i+1]:  # Поменяли знак и сортировка по убыванию
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
                flag = True
        n += 1
    return lst_obj


orig_list = [random.randint(-100, 100) for _ in range(10)]
print(orig_list)

print(bubble_sort(orig_list[:]))
print(timeit.timeit("bubble_sort(orig_list[:])", globals=globals(), number=10000))

print(bubble_sort_2(orig_list[:]))
print(timeit.timeit("bubble_sort_2(orig_list[:])", globals=globals(), number=10000))

print(bubble_sort_3(orig_list[:]))
print(timeit.timeit("bubble_sort_3(orig_list[:])", globals=globals(), number=10000))

print(bubble_sort_4(orig_list[:]))
print(timeit.timeit("bubble_sort_4(orig_list[:])", globals=globals(), number=10000))

print(orig_list)

'''
bubble_sort_2: добавлено переменная булевая flag, идея такая: если не происходит перемена (своп) элементов,
значит список отсортирован и можно раньше выходить из цикла. Поможет если только массив хотя бы частично отсортирован.

bubble_sort_2: после прохода каждого цикла, число элементов проверяемого на один элемент меньше, так, как самый
максимальный уже находится в конце списка и его нет смысла проверять.

bubble_sort_4: реализованы способы описанные в bubble_sort_2 и bubble_sort_2, соответственно и прирост по скорости
заметен
'''
