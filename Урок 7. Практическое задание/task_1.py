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


# Сортировка по убыванию
def bubble_sort_rev1(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i + 1] > lst_obj[i]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


# Доработанная сортировка
def bubble_sort_rev2(lst_obj):
    n = 1
    lst_end = 0
    while n < len(lst_obj):
        break_counter = True
        for i in range(len(lst_obj) - 1, lst_end, -1):
            if lst_obj[i - 1] > lst_obj[i]:
                lst_obj[i], lst_obj[i - 1] = lst_obj[i - 1], lst_obj[i]
                break_counter = False
        if break_counter is True:
            return lst_obj
        lst_end += 1
        n += 1
    return lst_obj


# На каждом проходе цикла исключается отсортированная часть.
# Цикл прерывается если за проход по списку не совершилась не одна перестановка.

list_10 = [randint(-100, 100) for _ in range(10)]
list_100 = [randint(-100, 100) for _ in range(100)]
list_1000 = [randint(-100, 100) for _ in range(1000)]

print('Сравнение стандартной пузырьковой сортировки и доработанной:')
print(f'Стандартная сортировка список 10: {timeit("bubble_sort_rev1(list_10[:])", globals=globals(), number=1000)}')
print(f'Доработанная сортировка список 10: {timeit("bubble_sort_rev2(list_10[:])", globals=globals(), number=1000)}')
print('*' * 50)
print(f'Стандартная сортировка список 100: {timeit("bubble_sort_rev1(list_100[:])", globals=globals(), number=1000)}')
print(f'Доработанная сортировка список 100: {timeit("bubble_sort_rev2(list_100[:])", globals=globals(), number=1000)}')
print('*' * 50)
print(f'Стандартная сортировка список 1000: {timeit("bubble_sort_rev1(list_1000[:])", globals=globals(), number=1000)}')
print(
    f'Доработанная сортировка список 1000: {timeit("bubble_sort_rev2(list_1000[:])", globals=globals(), number=1000)}')

print(list_10)
print(bubble_sort_rev2(list_10))

# Прервывание списка даст прирост производительности только если список близок к отсортированному состоянию
# На это есть шанс только в маленьком списке
