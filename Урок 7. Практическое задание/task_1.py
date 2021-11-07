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


def bubble_sort(lst_obj):    # изначальная функция
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] > lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_opt(lst_obj):    # доработанная функция
    n = 1
    flag_stop = False
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] > lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
                flag_stop = True
        if flag_stop is False:    # сработает, если список 'отсортирован'
            return lst_obj
        n += 1
    return lst_obj


# замеры 10
orig_list = [random.randint(-100, 100) for _ in range(10)]
print(f'Исходный массив: {orig_list}')
print(f'{timeit.timeit("bubble_sort(orig_list[:])", globals=globals(), number=1000),} '
      f'Отсортированный массив: {bubble_sort(orig_list[:])}')
print(f'{timeit.timeit("bubble_sort_opt(orig_list[:])", globals=globals(), number=1000),} '
      f'Отсортированный массив: {bubble_sort(orig_list[:])}')


# # замеры 100
orig_list = [random.randint(-100, 100) for _ in range(100)]
print(f'Исходный массив: {orig_list}')
print(f'{timeit.timeit("bubble_sort(orig_list[:])", globals=globals(), number=1000),} '
      f'Отсортированный массив: {bubble_sort(orig_list[:])}')
print(f'{timeit.timeit("bubble_sort_opt(orig_list[:])", globals=globals(), number=1000),} '
      f'Отсортированный массив: {bubble_sort(orig_list[:])}')


# замеры 1000
orig_list = [random.randint(-100, 100) for _ in range(1000)]
print(f'Исходный массив: {orig_list}')
print(f'{timeit.timeit("bubble_sort(orig_list[:])", globals=globals(), number=1000),} '
      f'Отсортированный массив: {bubble_sort(orig_list[:])}')
print(f'{timeit.timeit("bubble_sort_opt(orig_list[:])", globals=globals(), number=1000),} '
      f'Отсортированный массив: {bubble_sort(orig_list[:])}')

# результаты (иногда разняться, но в целом примерно равны):

# замеры 10
# 0.017188600002555177
# 0.018408600008115172    # доработанная функция

# замеры 100
# 1.2412993000034476
# 1.2933679999987362    # доработанная функция

# замеры 1000
# 140.4500088999921
# 145.33028889998968    # доработанная функция

"""вероятность получить при генерации уже отсортированный массив крайне мала, 
но данный флаг (flag_stop) можно оставить как "предохранитель" от такой вероятности"""

