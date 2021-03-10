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
import random
from timeit import timeit


def bubble_reverse(nums):
    for j in range(len(nums) - 1):
        for i in range(len(nums) - 1 - j):
            if nums[i] < nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
    return nums


def bubble_reverse_mod(lst_obj):
    n = 1
    while n < len(lst_obj):
        sort = True
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                sort = False
        n += 1
        if sort:
            break
    return lst_obj


m = [random.randint(-100, 100) for _ in range(100)]


print('100 измерений')
print('Выполнение без оптимизации', timeit('bubble_reverse(m[:])', globals=globals(), number=100))
print('Выполнение c оптимизацией', timeit('bubble_reverse_mod(m[:])', globals=globals(), number=100))

print('1000 измерений')
print('Выполнение без оптимизации', timeit('bubble_reverse(m[:])', globals=globals(), number=1000))
print('Выполнение c оптимизацией', timeit('bubble_reverse_mod(m[:])', globals=globals(), number=1000))

print('10000 измерений')
print('Выполнение без оптимизации', timeit('bubble_reverse(m[:])', globals=globals(), number=10000))
print('Выполнение c оптимизацией', timeit('bubble_reverse_mod(m[:])', globals=globals(), number=10000))

'''Модификация: если за проход по списку не совершается ни одной сортировки, то завершение..
Модификация ухудшила время сортировки, на выполнение проверки условий.
Получить сразу отсортированный массив практически не реально, поэтому смысла в доработке таким способом нет'''
