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


def bubble_sort1(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-1, 0, -1):
            if lst_obj[i] > lst_obj[i-1]:
                lst_obj[i], lst_obj[i-1] = lst_obj[i-1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort2(lst_obj):
    n = 1
    while n < len(lst_obj):
        change = False
        for i in range(len(lst_obj)-1, 0, -1):
            if lst_obj[i] > lst_obj[i-1]:
                lst_obj[i], lst_obj[i-1] = lst_obj[i-1], lst_obj[i]
                change = True
        n += 1
        if change is False:
            return lst_obj


def bubble_sort3(lst_obj):
    n = 1
    while n < len(lst_obj):
        change = False
        for i in range(len(lst_obj)-1, -1+n, -1):
            if lst_obj[i] > lst_obj[i-1]:
                lst_obj[i], lst_obj[i-1] = lst_obj[i-1], lst_obj[i]
                change = True
        n += 1
        if change is False:
            return lst_obj



orig_list = [random.randint(-100, 100) for _ in range(100)]

print(orig_list[:], '\n', bubble_sort3(orig_list[:]))

# замеры функции без доработок
print(
    timeit.timeit(
        "bubble_sort1(orig_list[:])",
        globals=globals(),
        number=1000))

# замеры функции с доработкой: если за проход по списку не совершается ни одной сортировки, то завершение
# (установлен флаг False/True на изменения в списке).
print(
    timeit.timeit(
        "bubble_sort2(orig_list[:])",
        globals=globals(),
        number=1000))

# замеры функции с доработкой: если за проход по списку не совершается ни одной сортировки, то завершение,
# а также отсечены лишние итерации: for i in range(len(lst_obj)-1, -1+n, -1):...
print(
    timeit.timeit(
        "bubble_sort3(orig_list[:])",
        globals=globals(),
        number=1000))

# 3.503420347
# 2.751149559
# 2.019774172
# !!! Каждая доработка дала прирост в скорости выполнения сортировки на 20-30%. Весьма существенно.
