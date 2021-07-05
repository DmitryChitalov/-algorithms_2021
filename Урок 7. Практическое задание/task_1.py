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


my_list = [randint(-100, 100) for i in range(1000)]


def bubble_sort_1(some_list):
    result_list = some_list[:]
    n = 1
    while n < len(result_list):
        for i in range(len(result_list) - n):
            if result_list[i] < result_list[i + 1]:
                result_list[i], result_list[i + 1] = result_list[i + 1], result_list[i]
        n += 1
    return result_list


def bubble_sort_2(some_list):
    result_list = some_list[:]
    n = 1
    m = True
    while m == True:
        m = False
        for i in range(len(result_list) - n):
            if result_list[i] < result_list[i + 1]:
                m = True
                result_list[i], result_list[i + 1] = result_list[i + 1], result_list[i]
        n += 1
    return result_list

my_list_1 = bubble_sort_1(my_list)

print(timeit('bubble_sort_1(my_list)', globals=globals(), number=1))      # 0.22295078000000002
print(timeit('bubble_sort_2(my_list)', globals=globals(), number=1))      # 0.25174984499999997
print(timeit('bubble_sort_1(my_list_1)', globals=globals(), number=1))    # 0.11300570700000001
print(timeit('bubble_sort_2(my_list_1)', globals=globals(), number=1))    # 0.00024055900000008457

print(my_list)
print(bubble_sort_1(my_list))
print(bubble_sort_2(my_list))

# Доработка не помогла, сортировка стала медленнее, но если массив уже отсортирован, то доработанная программа
# выполняется значительно быстрее, то есть чем более упорядочен массив тем эффективнее будет выполнятся
# доработанная программа