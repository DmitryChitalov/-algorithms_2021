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

import random
from timeit import timeit


def sort_reversed(list_arg):
    n = 0
    while n < len(list_arg):
        for i in range(len(list_arg)-1-n):
            if list_arg[i] < list_arg[i+1]:
                list_arg[i], list_arg[i+1] = list_arg[i+1], list_arg[i]
        n += 1
    return list_arg


def sort_reversed_smart(list_arg):
    n = 0
    while n < len(list_arg):
        sorted_status = True
        for i in range(len(list_arg)-1-n):
            if list_arg[i] < list_arg[i+1]:
                list_arg[i], list_arg[i+1] = list_arg[i+1], list_arg[i]
                sorted_status = False
        if sorted_status:
            break
        n += 1
    return list_arg


'''
Доработка алгоритма заключается в том что на каждом этапе осуществляется проверка является ли списко уже отсортированным
или нет. В случае если список уже отсортирован, то остальные прогоны не делаются, что существенно экономит время.
'''


original_list = [random.randint(-100, 100) for i in range(100)]

print(timeit('sort_reversed(original_list[:])', globals=globals(), number=10000))
print(timeit('sort_reversed_smart(original_list[:])', globals=globals(), number=10000))
'''
Пока передаем неотсортированный список то особой разницы между двумя реализациями не видноЖ
7.234363200000001
7.2103318000000005
'''

sorted_original_list = sorted(original_list, reverse=True)

print(timeit('sort_reversed(sorted_original_list[:])', globals=globals(), number=10000))
print(timeit('sort_reversed_smart(sorted_original_list[:])', globals=globals(), number=10000))
'''
Как только передаем изначально отсортированный список, то smart реализация дает явную экономию времени:
3.7748766000000007
0.08054230000000118
'''
