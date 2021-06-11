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
from random import randint
from timeit import timeit


def sort_bubble(lst):
    n = 1
    while n < len(lst):
        for el in range(len(lst) - n):
            if lst[el] < lst[el+1]:
                lst[el], lst[el+1] = lst[el+1], lst[el]
        n += 1
    return lst


def sort_bubble_opt(lst):
    n = 1
    flag = True
    while n < len(lst) or flag:
        for el in range(len(lst) - n):
            if lst[el] < lst[el+1]:
                lst[el], lst[el+1] = lst[el+1], lst[el]
                flag = False
        n += 1
    return lst


def random_list(n):
    lst = [randint(-100, 100) for el in range(n)]
    return lst


lst_10 = random_list(10)
lst_100 = random_list(100)
lst_1000 = random_list(1000)
print(f' Исходный массив: \n {lst_10}')
print(f' Отсортированый массив пузырьком: \n {sort_bubble(lst_10[:])}')
print(f' Отсортированый массив пузырьком с оптимизацией: \n {sort_bubble_opt(lst_10[:])}')
print(
    timeit(
        "sort_bubble(lst_10[:])",
        globals=globals(),
        number=100))
print(
    timeit(
        "sort_bubble_opt(lst_10[:])",
        globals=globals(),
        number=100))
print(
    timeit(
        "sort_bubble(lst_100[:])",
        globals=globals(),
        number=100))
print(
    timeit(
        "sort_bubble_opt(lst_100[:])",
        globals=globals(),
        number=100))
print(
    timeit(
        "sort_bubble(lst_1000[:])",
        globals=globals(),
        number=100))
print(
    timeit(
        "sort_bubble_opt(lst_1000[:])",
        globals=globals(),
        number=100))

'''
Результаты:
0.0018331690000000025
0.0020826440000000015
0.139584924
0.14025163799999998
13.867078669
13.988059533

Оптимизация ничего не дала, так как очень маленькая вероятность получить из рандомных значений 
сразу отсортированный массив, а так как появилась дополнительная проверка стало даже чутку хуже. 

'''