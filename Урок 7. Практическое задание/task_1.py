"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в виде функции.

Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение. Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.

Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""

from random import randint
from timeit import timeit

my_list10 = [randint(-100, 100) for num in range(10)]
my_list100 = [randint(-100, 100) for num1 in range(100)]
my_list1000 = [randint(-100, 100) for num2 in range(1000)]


def bubble_sort1(any_list):
    n = len(any_list)
    for num in range(n):
        for i in range(len(any_list) - 1):
            if any_list[i + 1] > any_list[i]:
                any_list[i + 1], any_list[i] = any_list[i], any_list[i + 1]
    return any_list


def bubble_sort2(any_list):
    n = len(any_list)
    for x in range(n):
        for y in range(len(any_list[x:]) - 1):
            if any_list[y + 1] > any_list[y]:
                any_list[y + 1], any_list[y] = any_list[y], any_list[y + 1]
    return any_list


print(f'Исходный массив:\n'
      f'{my_list100}')

print('bubble_sort1', timeit('bubble_sort1(my_list10[:])', globals=globals(), number=1000))
print('bubble_sort2', timeit('bubble_sort2(my_list10[:])', globals=globals(), number=1000))
print('bubble_sort1', timeit('bubble_sort1(my_list100[:])', globals=globals(), number=1000))
print('bubble_sort2', timeit('bubble_sort2(my_list100[:])', globals=globals(), number=1000))
print('bubble_sort1', timeit('bubble_sort1(my_list1000[:])', globals=globals(), number=100))
print('bubble_sort2', timeit('bubble_sort2(my_list1000[:])', globals=globals(), number=100))

print(f'Отсортированный массив:\n'
      f'{bubble_sort1(my_list100)}')

"""
bubble_sort1 0.007590600000000003
bubble_sort2 0.006747999999999997
bubble_sort1 0.6360339
bubble_sort2 0.4199822999999999
bubble_sort1 11.8984772
bubble_sort2 6.957711800000002

На небольших массивах разницы практически нет, однако на больших вариант со срезом гораздо эффективнее т.к. с каждым 
новым проходом кол-во необходимых итераций уменьшается.
"""