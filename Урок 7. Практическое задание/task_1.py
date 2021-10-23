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

def bubble_sort_desc(lst_obj):
    for j in range(len(lst_obj)):
        for i in range(len(lst_obj)-1):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
    return lst_obj


def bubble_sort_desc_opt(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_desc_opt_flag(lst_obj):
    n = 1
    flag = True
    while n < len(lst_obj) and flag:
        flag = False
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
                flag = True
        n += 1
    return lst_obj

orig_list_10 = [random.randint(-100, 100) for _ in range(10)]
orig_list_100 = [random.randint(-100, 100) for _ in range(100)]

print('Без оптимизации')
print(
    timeit.timeit(
        "bubble_sort_desc(orig_list_10[:])",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "bubble_sort_desc(orig_list_100[:])",
        globals=globals(),
        number=1000))

print('С оптимизацией на колличество операций в каждом проходе')
print(
    timeit.timeit(
        "bubble_sort_desc_opt(orig_list_10[:])",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "bubble_sort_desc_opt(orig_list_100[:])",
        globals=globals(),
        number=1000))

print('С оптимизацией "выход, если не было изменений"')
print(
    timeit.timeit(
        "bubble_sort_desc_opt_flag(orig_list_10[:])",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "bubble_sort_desc_opt_flag(orig_list_100[:])",
        globals=globals(),
        number=1000))


print(orig_list_10)
print(bubble_sort_desc_opt_flag(orig_list_10))

'''Оптимизация с сокращением проходов после каждой итерации наружнего цикла, существенно влияет
на время выполнения функции, т.к. количество проходов сокращается очень значительно. В последней операции с начального n до 1.
Оптимизация с флагом помогает, но очень не сильно и при не большом колличестве данных, потому что при
большом колличестве данных количество исключенных интераций очень не значительное'''
