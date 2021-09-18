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

lst = [randint(-100, 100) for _ in range(0, 100)]


def func1(obj):
    n = 1
    while n < len(obj):
        for i in range(len(obj) - n):
            if obj[i] < obj[i + 1]:
                obj[i], obj[i + 1] = obj[i + 1], obj[i]
        n += 1
    return obj


def func2(obj):
    n = 1
    while n < len(obj):
        check = obj.copy()
        for i in range(len(obj) - n):
            if obj[i] < obj[i + 1]:
                obj[i], obj[i + 1] = obj[i + 1], obj[i]
        if check == obj:
            break
        n += 1
    return obj


print(lst)
print(func2(lst[:]))

print(timeit('func1(lst[:])', globals=globals(), number=10000))
print(timeit('func2(lst[:])', globals=globals(), number=10000))
