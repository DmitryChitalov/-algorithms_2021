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
from random import randint


def bubble_sort(lst):
    for j in range(len(lst)):
        for i in range(len(lst)-1):
            if lst[i] < lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
    return lst


def bubble_sort_advance(lst):
    for j in range(len(lst)):
        lst_c = lst.copy()
        for i in range(len(lst)-1):
            if lst[i] < lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
        if lst_c == lst:
            return lst
    return lst


need_list = [randint(-100, 100) for el in range(-100, 100)]
print(f"Несортированный: {need_list}\nСортированный: {bubble_sort_advance(need_list[:])}\n")

print("Время обычной " + str(timeit("bubble_sort(need_list[:])", "from __main__ import bubble_sort, need_list",
                                    number=1000)))
print("Время доработанной " + str(timeit("bubble_sort_advance(need_list[:])",
                                         "from __main__ import bubble_sort_advance, need_list", number=1000)))

"""
Сделал вариант с завершением сортировки при уже сортированном массиве.
Время обычной 2.2190600000000003
Время доработанной 2.2268739
Замерял несколько раз, в целом +- одинаково, так что смысла нет.
"""