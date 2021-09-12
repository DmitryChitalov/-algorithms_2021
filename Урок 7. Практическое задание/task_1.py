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

import random
import timeit


def bubble_sort(some_list):
    n = 1
    while n < (len(some_list)):
        for i in range(len(some_list) - n):
            if some_list[i] < some_list[i + 1]:
                some_list[i], some_list[i + 1] = some_list[i + 1], some_list[i]
        n += 1
    return some_list


def new_bubble_sort(some_list):
    flag = True
    while flag:
        flag = False
        for i in range(len(some_list) - 1):
            if some_list[i] < some_list[i + 1]:
                some_list[i], some_list[i + 1] = some_list[i + 1], some_list[i]
                flag = True
    return some_list


my_list = [random.randint(-100, 100) for i in range(10)]


print(my_list)
print(timeit.timeit('bubble_sort(my_list[:])', globals=globals(), number=1000))
print(timeit.timeit('new_bubble_sort(my_list[:])', globals=globals(), number=1000))

"""
Выводы: Для завершения алгоритма в момент, в котором массив окажется полностью отсортированным создаем переменную flag.
По результатам замеров оптимизация ощутимого выиграша во времени не дает.
"""
