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

from timeit import timeit
from random import randint


def bubble_sort_not_good(lst_obj):
    for i in range(len(lst_obj)):
        for j in range(1, len(lst_obj)-1):
            if lst_obj[j] < lst_obj[j + 1]:
                lst_obj[j], lst_obj[j + 1] = lst_obj[j + 1], lst_obj[j]
    return lst_obj


def bubble_sort_good(lst_obj):
    n = 1
    while n < len(lst_obj):
        flag = False
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                flag = True
        if flag is False:
            break
        n += 1
    return lst_obj


orig_list = [randint(-100, 100) for _ in range(10)]
print(f'{orig_list}\n{bubble_sort_good(orig_list[:])}')
# замеры 10
print(
    f'неоптимизированная на 10\n{timeit("bubble_sort_not_good(orig_list[:])", globals=globals(), number=1000)}')

print(
   f'оптимизированная на 10\n{timeit("bubble_sort_good(orig_list[:])",globals = globals(),number = 1000)}')

orig_list = [randint(-100, 100) for _ in range(100)]
print(f'{orig_list}\n{bubble_sort_good(orig_list[:])}')

# замеры 100
print(
    f'неоптимизированная на 100\n{timeit("bubble_sort_not_good(orig_list[:])", globals=globals(), number=1000)}')

print(
   f'оптимизированная на 100\n{timeit("bubble_sort_good(orig_list[:])",globals = globals(),number = 1000)}')

orig_list = [randint(-100, 100) for _ in range(1000)]
print(f'{orig_list}\n{bubble_sort_good(orig_list[:])}')

# замеры 1000
print(
    f'неоптимизированная на 1000\n{timeit("bubble_sort_not_good(orig_list[:])", globals=globals(), number=1000)}')

print(
   f'оптимизированная на 1000\n{timeit("bubble_sort_good(orig_list[:])",globals = globals(),number = 1000)}')

'''
неоптимизированная на 10
0.018218899999999996
оптимизированная на 10
0.018161300000000005

неоптимизированная на 100
1.6296674
оптимизированная на 100
1.1446981999999999

неоптимизированная на 1000
187.6291994
оптимизированная на 1000
123.01626200000001

Для оптимизации был добавлен флаг, контролирубщий наличие перестановки. Он в данном случае бесполезен, т.к.
работает на малых массивах и в редких случаях, когда массив уже почти или полностью отсортирован.
Так же был добавлен счетчик, чтобы уменьшить кол-во итераций. Он сыграл более существенную роль в уменьшении 
времени работы.
'''