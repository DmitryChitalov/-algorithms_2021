#!/usr/bin/env python3

import random
import timeit

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

array = [random.randint(-100, 100) for _ in range(200)]


def bubble_sort_1(data: list) -> list:
    for i in range(len(data)):
        for j in range(len(data)):
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]
    return data


def bubble_sort_2(data: list) -> list:
    is_sorted = True
    for i in range(len(data)):
        for j in range(len(data)):
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]
                is_sorted = False
        if is_sorted:
            return data
    return data


def main():
    print(f'#{"-" * 30} Unsorted array {"-" * 30}#\n{array}')
    data_v1 = bubble_sort_1(array[:])
    print(f'#{"-" * 30} Sorted array 1 {"-" * 30}#\n{data_v1}')
    data_v2 = bubble_sort_2(array[:])
    print(f'#{"-" * 30} Sorted array 2 {"-" * 30}#\n{data_v2}')


    print(timeit.timeit('bubble_sort_1(array.copy())', globals=globals(), number=1000))
    print(timeit.timeit('bubble_sort_2(array.copy())', globals=globals(), number=1000))


if __name__ == '__main__':
    main()


'''
3.613566249001451
3.41703729999972
Данная оптимизация больших рандомных масcивах бессмысленна, поможет только
если состояние массива будет близко к отсортированному
'''
