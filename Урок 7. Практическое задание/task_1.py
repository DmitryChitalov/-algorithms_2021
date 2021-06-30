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


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] > lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj

def bubble_sort_updated(sort_list):
    n = 1
    while n <= len(sort_list):
        count = 0
        for i in range(len(sort_list) - n):
            if sort_list[i] < sort_list[i + 1]:
                sort_list[i], sort_list[i + 1] = sort_list[i + 1], sort_list[i]
                count += 1
        if count == 0:
            break
        n += 1
    return sort_list

orig_list = [randint(-100, 100) for _ in range(100)]

# замеры original
print(timeit("bubble_sort(orig_list[:])", globals=globals(), number=100))

# замеры updated
print(timeit("bubble_sort_updated(orig_list[:])", globals=globals(), number=100))

"""
Добавил флаг и прерывание цикла на случай подачи уже отсортированого списка на входе, 
в противном случае в оптимизации нет смысла
"""
