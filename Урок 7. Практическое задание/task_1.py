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


def bubble_revers(lst):
    n = 1
    while n < len(lst):
        for i in range(len(lst) - n):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
        n += 1
    return lst


def bubble_revers_update_1(lst):
    n = 1
    while n < len(lst):
        trigger = 1
        for i in range(len(lst) - n):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                trigger = 0
            if trigger == 1:
                break
        n += 1
    return lst


def bubble_revers_update_2(lst):
    n = 1
    while n < len(lst):
        trigger = 1
        for i in range(len(lst) - n - 1):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                trigger = 0
            if trigger == 1:
                break
        n += 1
    return lst


num_list = [randint(-100, 100) for i in range(100)]
print(num_list, '- исходный массив\n')
print(bubble_revers(num_list), '- отсортированный массив')

print(timeit('bubble_revers(num_list[:])', globals=globals(), number=10000),
      'пузырьковый')
print(timeit('bubble_revers_update_1(num_list[:])', globals=globals(),
             number=10000), 'доработанный с тригером')
print(timeit('bubble_revers_update_2(num_list[:])', globals=globals(),
             number=10000), 'доработанный тригер и итерация')
"""
после доработки получилась прибавки в скорость порядка 41%
не совсем понял почему просто с тригером работает чуть быстрее чем тригер минус
итерация, например для списка из 200 элементов получил следующие результаты:
13.9202265 пузырьковый
0.8913884000000003 доработанный с тригером
0.9137287000000001 доработанный тригер и итерация
"""