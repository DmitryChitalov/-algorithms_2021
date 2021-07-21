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
import random
from timeit import timeit


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_mod(lst_obj):
    n = 1
    while n < len(lst_obj):
        old_lst = set(lst_obj)
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        if old_lst == set(lst_obj):
            return lst_obj
        n += 1
    return lst_obj


orig_list = [random.randint(-100, 99) for n in range(50)]
print(orig_list)
print(bubble_sort(orig_list[:]))
print(bubble_sort_mod(orig_list[:]))

orig_list = [random.randint(-100, 99) for n in range(10)]
print(timeit("bubble_sort(orig_list[:])", globals=globals(), number=100))
orig_list = [random.randint(-100, 99) for n in range(100)]
print(timeit("bubble_sort(orig_list[:])", globals=globals(), number=100))
orig_list = [random.randint(-100, 99) for n in range(1000)]
print(timeit("bubble_sort(orig_list[:])", globals=globals(), number=100))

orig_list = [random.randint(-100, 99) for n in range(10)]
print(timeit("bubble_sort_mod(orig_list[:])", globals=globals(), number=100))
orig_list = [random.randint(-100, 99) for n in range(100)]
print(timeit("bubble_sort_mod(orig_list[:])", globals=globals(), number=100))
orig_list = [random.randint(-100, 99) for n in range(1000)]
print(timeit("bubble_sort_mod(orig_list[:])", globals=globals(), number=100))

'''
Проведена модификация - проверка изменился ли сортируемый массив после прохода цикла с заданным n.
Узкое место - правильно сравнить массивы, я применил перевод во множество и их сравнение. 
Если провести неверно, результаты будут даже несколько хуже

Результаты замеров:
немодифицированная сортировка:
0.0021225110000000005
0.175764837
19.663375577
модифицированная сортировка:
0.0005840130000009935
0.006014940000000024
0.0646748410000022

Модификация дает огромную экономию времени, главное правильно провести сравнение списков
'''