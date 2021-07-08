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

#  сортировка по убыванию:

def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj

my_list = [random.randint(-100, 100) for _ in range(10)]
print('bubble_sort:')
print(my_list)
print(bubble_sort(my_list))


# улучшенная сортировка по убыванию, подазумевающая ранний выход из икла при отсутствии замен:

def better_bubble_sort(lst_obj):
    n = 1
    finished = True
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
                finished = False
        if finished:
            break
        n += 1

    return lst_obj

my_list = [random.randint(-100, 100) for _ in range(10)]

print('better_bubble_sort:')
print(my_list)
print(better_bubble_sort(my_list))

# Замеры показали при малой длине списке (пять элементов):
# 2.0380067
# 1.8778858999999999
# Однако эти результаты нестабильные, а при увеличении числа элементов в списке, эффект отсутствует,
# так как очень низка вероятность, что список сгенерируется с числами по порядку.


my_list = [random.randint(-100, 100) for _ in range(5)]
print(
    timeit.timeit(
        "bubble_sort(my_list[:])",
        globals=globals(),
        number=1000_000))


my_list = [random.randint(-100, 100) for _ in range(5)]
print(
    timeit.timeit(
        "better_bubble_sort(my_list[:])",
        globals=globals(),
        number=1000_000))