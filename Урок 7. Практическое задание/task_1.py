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

not_sorted_list = [randint(-100, 100) for i in range(100)]

def bubble(lst: list):
    n = 1
    while n < len(lst):
        for i in range(len(lst) - n):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
        n += 1
    return lst


def bubble_mod(lst: list):
    n = 1
    while n < len(lst):
        count = False
        for i in range(len(lst) - n):
            if lst[i] < lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                count = True
        if count:
            break
        n += 1
    return lst

print(bubble(not_sorted_list))
print(bubble_mod(not_sorted_list))

print(
    timeit("bubble(not_sorted_list)", globals=globals(), number=1000),
    timeit("bubble_mod(not_sorted_list)", globals=globals(), number=1000), sep='\n'
)

"""
Не вижу особого смысла в доработке, т.к. скорость выполнение зависит от везения
"""