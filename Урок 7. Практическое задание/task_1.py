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


def bsort_reverse(my_lst):
    for i in range(len(my_lst) - 1):
        for j in range(len(my_lst) - 1 - i):
            if my_lst[j] < my_lst[j + 1]:
                my_lst[j], my_lst[j + 1] = my_lst[j + 1], my_lst[j]
    return my_lst


def my_bsort_reverse(my_lst):
    num = 1
    while num < len(my_lst):
        sort = True
        for i in range(len(my_lst) - num):
            if my_lst[i] < my_lst[i + 1]:
                my_lst[i], my_lst[i + 1] = my_lst[i + 1], my_lst[i]
                sort = False
        num += 1
        if sort:
            break
    return my_lst


my_lst = [randint(-100, 100) for _ in range(100)]

print('100 измерений')
print('без оптимизации', timeit('bsort_reverse(my_lst[:])', globals=globals(), number=100))
print('c оптимизацией', timeit('my_bsort_reverse(my_lst[:])', globals=globals(), number=100))

print('1000 измерений')
print('без оптимизации', timeit('bsort_reverse(my_lst[:])', globals=globals(), number=1000))
print('c оптимизацией', timeit('my_bsort_reverse(my_lst[:])', globals=globals(), number=1000))

print('10000 измерений')
print('без оптимизации', timeit('bsort_reverse(my_lst[:])', globals=globals(), number=10000))
print('c оптимизацией', timeit('my_bsort_reverse(my_lst[:])', globals=globals(), number=10000))

'''
100 измерений
без оптимизации 0.20755869999999998
c оптимизацией 0.26841170000000003
1000 измерений
без оптимизации 1.7884725
c оптимизацией 1.7293550999999998
10000 измерений
без оптимизации 19.3663943
c оптимизацией 20.364841700000003
Модификация: если за проход по списку не совершается ни одной сортировки, то завершение.
Такая модификация не целесообразна. Получитьб отсортированный массив практически невозможно.
'''
