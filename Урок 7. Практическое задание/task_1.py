from random import randint
from timeit import timeit

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


def bubble_sort(lst):
    n = 1
    while n < len(lst):
        for elements in range(len(lst) - n):
            if lst[elements] < lst[elements + 1]:
                lst[elements], lst[elements + 1] = lst[elements + 1], lst[elements]
        n += 1
    return lst


def new_bubble_sort(lst, flag=False):
    n = 1
    while n < len(lst):
        if flag:
            break
        flag = True
        for elements in range(len(lst) - n):
            if lst[elements] < lst[elements + 1]:
                lst[elements], lst[elements + 1] = lst[elements + 1], lst[elements]
                flag = False
        n += 1
    return lst


"""
Улучшение кода состоит в том, чтобы цикл не работал еще раз,если массив отсортирован.
Эффективности это не принесло, время уменьшилось совсем на немного. Доработка не помогла.

"""

if __name__ == "__main__":
    my_lst = [randint(-100, 100) for x in range(100)]
    print(my_lst)
    print(bubble_sort(my_lst[:]))
    print(
        timeit(
            "bubble_sort(my_lst[:])",
            globals=globals(),
            number=10000
        )
    )
    print(my_lst)
    print(new_bubble_sort(my_lst[:]))
    print(
        timeit(
            "new_bubble_sort(my_lst[:])",
            globals=globals(),
            number=10000
        )
    )
