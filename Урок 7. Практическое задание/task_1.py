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


"""Сортировка пузырьком"""

import timeit
import random


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj

def bubble_sort_ver2(lst_obj):
    n = 1
    count = 1
    for i in range(len(lst_obj)-n):
        if lst_obj[i] >= lst_obj[i+1]:
            count += 1
    if count != len(lst_obj):
        while n < len(lst_obj):
            for i in range(len(lst_obj)-n):
                if lst_obj[i] < lst_obj[i+1]:
                    lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
            n += 1
    return lst_obj

orig_list = [random.randint(-100, 100) for _ in range(10)]

print(f'Исходный массив            : {orig_list}')
sort_list = orig_list[:]
#sort_list = sorted(sort_list,reverse=True)
print(f'sort_list                  : {sort_list}')
print(f'Отсортированный массив     : {bubble_sort(orig_list[:])}')
print(f'Отсортированный массив ver2: {bubble_sort_ver2(sort_list[:])}')

# замеры 10
print(
    timeit.timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))
print(
    timeit.timeit(
        "bubble_sort_ver2(sort_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.randint(-100, 100) for _ in range(100)]
print(f'Исходный массив            : {orig_list}')
sort_list = orig_list[:]
#sort_list = sorted(sort_list,reverse=True)
print(f'sort_list                  : {sort_list}')

print(f'Отсортированный массив     : {bubble_sort(orig_list[:])}')
print(f'Отсортированный массив ver2: {bubble_sort_ver2(sort_list[:])}')

# замеры 100
print(
    timeit.timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))
print(
    timeit.timeit(
        "bubble_sort_ver2(sort_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.randint(-100, 100) for _ in range(1000)]
print(f'Исходный массив: {orig_list}')
sort_list = orig_list[:]
#sort_list = sorted(sort_list,reverse=True)
print(f'sort_list                  : {sort_list}')

print(f'Отсортированный массив     : {bubble_sort(orig_list[:])}')
print(f'Отсортированный массив ver2: {bubble_sort_ver2(sort_list[:])}')

# замеры 1000
print(
    timeit.timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))
print(
    timeit.timeit(
        "bubble_sort_ver2(sort_list[:])",
        globals=globals(),
        number=1000))
"""
В качестве идеи доработки использовал предложенную в задании идею - если за проход не выполнено ни одной сортировки,
то сортировка завершается. 

Замеры показали, что такая доработка эффективна, только если на вход в функцию подается уже отсортированный массив.
В данном случае показатели следующие: 
Замеры 10:
0.05573609999999998
0.006833300000000014 (доработанная версия)

Замеры 100:
2.5546225
0.033497499999999736 (доработанная версия)

Замеры 1000:
343.296175
0.38614839999996775 (доработанная версия)

Если же массив не отсортирован, то доработка только увеличивает время выполнения кода.
Замеры 10:
0.03699139999999998
0.03504990000000002 (доработанная версия)

Замеры 100:
2.5698001
3.0997470000000003 (доработанная версия)

Замеры 1000:
287.76469430000003
441.1675088 (доработанная версия)

"""
