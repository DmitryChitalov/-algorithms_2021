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


# БЕЗ ДОРАБОТОК
def bubble_sort_1(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj

my_list = [random.randint(-100, 100) for _ in range(10)]
print(
    timeit.timeit('bubble_sort_1(my_list[:])',
                  globals=globals(),
                  number=1000))

my_list = [random.randint(-100, 100) for _ in range(100)]
print(
    timeit.timeit('bubble_sort_1(my_list[:])',
                  globals=globals(),
                  number=1000))

my_list = [random.randint(-100, 100) for _ in range(1000)]
print(
    timeit.timeit('bubble_sort_1(my_list[:])',
                  globals=globals(),
                  number=1000))

"""
Без доработок.
Длина массива - 10:   0.017356797 сек
Длина массива - 100:  0.769939032 сек
Длина массива - 1000: 96.54486108100001 сек
"""


# С ДОРАБОТКАМИ

def bubble_sort_2(lst_obj):
    n = 1
    a = True
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
                a = False
        if a == True:
            break
        n += 1
    return lst_obj

my_list = [random.randint(-100, 100) for _ in range(10)]
print(
    timeit.timeit('bubble_sort_2(my_list[:])',
                  globals=globals(),
                  number=1000))

my_list = [random.randint(-100, 100) for _ in range(100)]
print(
    timeit.timeit('bubble_sort_2(my_list[:])',
                  globals=globals(),
                  number=1000))

my_list = [random.randint(-100, 100) for _ in range(1000)]
print(
    timeit.timeit('bubble_sort_2(my_list[:])',
                  globals=globals(),
                  number=1000))

"""
С доработками.
Длина массива - 10:   0.018912832 сек
Длина массива - 100:  0.9981121049999999 сек
Длина массива - 1000: 88.340531284 сек
"""

"""
Вывод:
В данном случае оптимизация не помогает, она не нужна. Она может помочь только в частично отсортированных массивах.
"""