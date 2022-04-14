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

from timeit import timeit
import random


def bubble_sort_desc(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_desc_with_check(lst_obj):
    n = 1
    action = True
    while n < len(lst_obj) and action:
        action = False
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                action = True
        n += 1
    return lst_obj


print('Список 10 элементов: ')
orig_list = [random.randint(-100, 100) for _ in range(10)]
print(orig_list)
print(bubble_sort_desc_with_check(orig_list[:]))

# замеры 10
print(timeit("bubble_sort_desc(orig_list[:])", globals=globals(), number=1000))  # 0.025638505000000006
print(timeit("bubble_sort_desc_with_check(orig_list[:])", globals=globals(), number=1000))  # 0.020817500999999988

print('Список 100 элементов: ')
orig_list = [random.randint(-100, 100) for _ in range(100)]
print(orig_list)
print(bubble_sort_desc_with_check(orig_list[:]))

# замеры 100
print(timeit("bubble_sort_desc(orig_list[:])", globals=globals(), number=1000))  # 1.9446257
print(timeit("bubble_sort_desc_with_check(orig_list[:])", globals=globals(), number=1000))  # 1.9121082620000003

print('Список 1000 элементов: ')
orig_list = [random.randint(-100, 100) for _ in range(1000)]
print(orig_list)
print(bubble_sort_desc_with_check(orig_list[:]))

# замеры 1000
print(timeit("bubble_sort_desc(orig_list[:])", globals=globals(), number=1000))  # 185.032831291
print(timeit("bubble_sort_desc_with_check(orig_list[:])", globals=globals(), number=1000))  # 193.19256437599998

# Оптимизация- устанавливаю признак выполнения замены в проходе, если его не случилось - сокращаю кол-во проходов
# Эффективности оптимизация не дала.
