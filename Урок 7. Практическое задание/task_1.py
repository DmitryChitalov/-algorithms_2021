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

not_sorted_2 = not_sorted_list.copy()
print(bubble(not_sorted_list))
print(bubble_mod(not_sorted_2))

print(
    timeit("bubble(not_sorted_list)", globals=globals(), number=1000),
    timeit("bubble_mod(not_sorted_list)", globals=globals(), number=1000), sep='\n'
)

"""
Получился небольшой прирост скорости
Несколько замеров 1 и 2 функции:
0.41970752298948355 - 1
0.39952557999640703 - 2
0.4184046699956525 - 1
0.4243793750065379 - 2
0.41019101500569377 - 1
0.4024849039997207 - 2
"""