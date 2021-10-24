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


def sorted_by_bubble(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


random_list = [2346, 3456, 253, 2344, 324, -1, 24]
# random_list = [random.randint(-100, 100) for i in range(20)]

# замеры 20
print(
    timeit.timeit(
        "sorted_by_bubble(random_list[:])",
        globals=globals(),
        number=1000),
    f'\nИсходный массив - {random_list};\nОтсортированный массив - {sorted_by_bubble(random_list[:])}.')


# updated

def sorted_by_bubble(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] >= lst_obj[i+1]:
                continue
            elif lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


random_list = [2346, 3456, 253, 2344, 324, -1, 24]
# random_list = [random.randint(-100, 100) for i in range(20)]

# замеры 20
print(
    timeit.timeit(
        "sorted_by_bubble(random_list[:])",
        globals=globals(),
        number=1000),
    f'\nИсходный массив - {random_list};\nОтсортированный массив - {sorted_by_bubble(random_list[:])}.')


# Используя рекурсию оптимизация не увенчается успехом. Даже если оптимизация со счетчиком, 
# то дальнейшая проверка на больших массивах будет давать дополнительное время. Так что тоже мимо.