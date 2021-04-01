"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).
Идея доработки: если за проход по списку не совершается ни одной сортировки, то завершение
Обязательно сделайте замеры времени обеих реализаций

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""

import random
import timeit

my_list = [random.randint(-100, 100) for i in range(1000)]


def sort_func_1(example_list):
    n = 1
    while n < len(example_list):
        for i in range(len(example_list)-n):
            if example_list[i] < example_list[i+1]:
                example_list[i], example_list[i+1] = example_list[i+1], example_list[i]
        n += 1
    return example_list


def sort_func_2(example_list):
    n = 1
    k = 0
    while n < len(example_list):
        for i in range(len(example_list)-n):
            if example_list[i] < example_list[i+1]:
                example_list[i], example_list[i+1] = example_list[i+1], example_list[i]
                k = 1
        if k == 0:
            break
        n += 1
    return example_list


print('Исходный массив: ', my_list)
print(timeit.timeit("sort_func_1(my_list[:])",
                    setup="from __main__ import sort_func_1, my_list",
                    number=100))
print(timeit.timeit("sort_func_2(my_list[:])",
                    setup="from __main__ import sort_func_2, my_list",
                    number=100))
print('Отсортированный массив: ', sort_func_1(my_list))
print('Отсортированный массив: ', sort_func_2(my_list))

# результат
# 15.181708225
# 15.467141186
# Вывод: доработка не является полезной :(
