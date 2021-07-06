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


import timeit
import random


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - 1):
            if lst_obj[i] > lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


def reverse_bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        is_sort = True
        for i in range(1, len(lst_obj)):
            if lst_obj[-i] < lst_obj[-i - 1]:
                lst_obj[-i], lst_obj[-i - 1] = lst_obj[-i - 1], lst_obj[-i]
                is_sort = False
        if is_sort:
            break
        n += 1
    return lst_obj


def reverse_bubble_sort_update(lst_obj):
    n = 1
    while n < len(lst_obj):
        is_sort = True
        for i in range(1, len(lst_obj) + 1 - n):
            if lst_obj[-i] < lst_obj[-i - 1]:
                lst_obj[-i], lst_obj[-i - 1] = lst_obj[-i - 1], lst_obj[-i]
                is_sort = False
        if is_sort:
            break
        n += 1
    return lst_obj


num = 15
a = [random.randint(-100, 100) for _ in range(num)]
b = [1, 2, 3, 4, 5, 6]
print(bubble_sort(a[:]))
print(reverse_bubble_sort(a[:]))
print(reverse_bubble_sort_update(a[:]))
print(reverse_bubble_sort(b[:]))

stmt = [
    'reverse_bubble_sort(a[:])',
    'reverse_bubble_sort_update(a[:])'
]

for st in stmt:
    print(f'на выполение функции {st} затрачено времени: '
          f'{timeit.timeit(st, setup="a =[random.randint(-100, 100) for _ in range(10)]", number=1000, globals=globals())}')

for st in stmt:
    print(f'на выполение функции {st} затрачено времени: '
          f'{timeit.timeit(st, setup="a =[random.randint(-100, 100) for _ in range(100)]", number=1000, globals=globals())}')

for st in stmt:
    print(f'на выполение функции {st} затрачено времени: '
          f'{timeit.timeit(st, setup="a =[random.randint(-100, 100) for _ in range(1000)]", number=1000, globals=globals())}')
"""
Для улучшения алгоритма была создана переменная-флаг is_sort, которая в случае хотя бы одной перестановки принимала 
значение False. В том случае, если перестановки не было, то она оставалсь со значение True, что приводит 
к остановке внешнего цикла while и завершению функции

В функции reverse_bubble_sort_update для оптимизации изменен порядок определения значения 
крайней границы range len(lst_obj) + 1 - n), что позволяет не проверять уже отсортированные элементы.
В результате мы получаем сущесвенный прирост скорости:

на выполение функции reverse_bubble_sort(a[:]) затрачено времени: 0.0109859 (10 элементов)
на выполение функции reverse_bubble_sort_update(a[:]) затрачено времени: 0.011357600000000002 (10 элементов)
на выполение функции reverse_bubble_sort(a[:]) затрачено времени: 1.2977106999999999 (100 элементов)
на выполение функции reverse_bubble_sort_update(a[:]) затрачено времени: 0.9809941999999998 (100 элементов)
на выполение функции reverse_bubble_sort(a[:]) затрачено времени: 152.62518350000002 (1000 элементов)
на выполение функции reverse_bubble_sort_update(a[:]) затрачено времени: 106.3371616 (1000 элементов)
"""