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

from random import randint
from timeit import timeit


def create_random_list(num):
    unsorted_list = [randint(-100, 99) for _ in range(num)]
    print('Неотсортированный список:', unsorted_list)
    return unsorted_list


def bubble_sort(unsorted_list):
    for i in range(len(unsorted_list) - 1):
        for j in range(len(unsorted_list) - i - 1):
            if unsorted_list[j] < unsorted_list[j + 1]:
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]
    print('Отсортированный список:', unsorted_list)
    return unsorted_list


def bubble_sort_upgrade(unsorted_list):
    changed = True
    for i in range(len(unsorted_list) - 1):
        if not changed:
            break
        changed = False
        for j in range(len(unsorted_list) - 1):
            if unsorted_list[j] < unsorted_list[j + 1]:
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]
                changed = True
    print('Отсортированный список:', unsorted_list)
    return unsorted_list


def time_test():
    print(
        '\n10 обычная:', timeit('bubble_sort(create_random_list(10))', globals=globals(), number=1000),
        '\n10 улучшенная:', timeit('bubble_sort_upgrade(create_random_list(10))', globals=globals(), number=1000), '\n',
        '\n100 обычная:', timeit('bubble_sort(create_random_list(100))', globals=globals(), number=1000),
        '\n100 улучшенная:', timeit('bubble_sort_upgrade(create_random_list(100))', globals=globals(), number=1000), '\n',
        '\n1000 обычная:', timeit('bubble_sort(create_random_list(1000))', globals=globals(), number=1000),
        '\n1000 улучшенная:', timeit('bubble_sort_upgrade(create_random_list(1000))', globals=globals(), number=1000), '\n',
        '\n10000 обычная:', timeit('bubble_sort(create_random_list(10000))', globals=globals(), number=10),
        '\n10000 улучшенная:', timeit('bubble_sort_upgrade(create_random_list(10000))', globals=globals(), number=10))


# Улучшил алгортим выходом из цикла, в случае, если не происходят изменения.
# Это улучшение только ухудшает работу программы, по крайней мере, в моем случае.


if __name__ == '__main__':
    time_test()