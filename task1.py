from random import randint
from timeit import timeit

ls = [randint(-100, 100) for i in range(50)]


def bubble_sort_classic(l):
    for i in range(len(l)-1):
        for j in range(len(l)-1):
            if l[j+1] > l[j]:
                l[j+1], l[j] = l[j], l[j+1]
    return l


def bubble_sort_with_break(l):
    for i in range(len(l)-1):
        count = 0
        for j in range(len(l)-1):
            if l[j+1] > l[j]:
                l[j+1], l[j] = l[j], l[j+1]
                count += 1
        if count == 0:
            break
    return l


def bubble_sort_modify(l):
    for i in range(len(l)-1):
        for j in range(len(l[i:])-1):
            if l[j+1] > l[j]:
                l[j+1], l[j] = l[j], l[j+1]
    return l


print('bubble_sort_classic', timeit('bubble_sort_classic(ls[:])', globals=globals(), number=1000))
print('bubble_sort_with_break', timeit('bubble_sort_with_break(ls[:])', globals=globals(), number=1000))
print('bubble_sort_modify', timeit('bubble_sort_modify(ls[:])', globals=globals(), number=1000))

"""
bubble_sort_classic 0.2115412
bubble_sort_with_break 0.21075550000000005
bubble_sort_modify 0.14560219999999996
Обычная версия пузырьковой сортиоовки является самой медленной: добавление в цикл break  несущественно 
ускоряет сортировку (возможно, избавляет от 1-2 проходов по списку). Оптимальный подход - это
использовать срез от i элемента и до конца списка - так количество итераций вложенного цикла for значительно
уменьшается к концу, свою очередь это не мешает правильной работе алгоритма.
"""