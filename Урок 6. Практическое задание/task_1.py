"""
Задание 1.

Выполните профилирование памяти в скриптах.
Проанализируйте результат и определите программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять только домашние задания с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""

from memory_profiler import profile
from random import randint
import math

"""Первый пример - сортировка, использум список создаваемый итератором 'range'.
В этом случае список хранится в памяти и занимает 0.3 MiB

"""

@profile
def bubble_sort1():
    array = list(range(10000))
    n = len(array)  # O(1)
    for i in range(n):  # O(n)
        for j in range(n - i - 1):  # O(n)
            already_sorted = True  # O(1)
            if array[j] > array[j + 1]:  # O(1)
                array[j], array[j + 1] = array[j + 1], array[j]  # O(1)
                already_sorted = False  # O(1)
        if already_sorted:  # O(1)
            break  # O(1)

    return array[0]  # O(1)

"""
Для уменьшения использования памяти, лучше применить, например генератор.
Генераторы не сохраняют все результаты в памяти, а вычисляют их на лету, 
а память используется только в случае, если мы запрашиваем результат вычислений.
"""
@profile
def bubble_sort():
    array = [randint(-1000000, 1000000) for i in range(1000)]
    n = len(array)  # O(1)
    for i in range(n):  # O(n)
        for j in range(n - i - 1):  # O(n)
            already_sorted = True  # O(1)
            if array[j] > array[j + 1]:  # O(1)
                array[j], array[j + 1] = array[j + 1], array[j]  # O(1)
                already_sorted = False  # O(1)
        if already_sorted:  # O(1)
            break  # O(1)

    return array[0]  # O(1)

"""
Второй пример - нахождение минимального элемента 

"""
@profile
def my_min():
    lst = list(range(100000))
    minimum = lst[0]  # O(1)
    for i in range(1, len(lst)):  # O(n)
        if lst[i] < minimum:  # O(1)
            minimum = lst[i]  # O(1)

    return minimum  # O(1)

"""
Для освобождения памяти применяем инструкцию 'del'
-3.6 MiB           1       del lst
"""

@profile
def my_min1():

    lst = list(range(100000))
    minimum = lst[0]  # O(1)
    for i in range(1, len(lst)):  # O(n)
        if lst[i] < minimum:  # O(1)
            minimum = lst[i]  # O(1)

    del lst
    return minimum  # O(1)

"""
Третий пример - вычислить квадраты четных чисел и вывести их в списке
"""

@profile
def check_even(numbers):
    even = []
    cubes = range(numbers)
    for num in cubes:
        if num % 2 == 0:
            even.append(num*num)
    return even

"""
используя генератор, мы экономим память, в этом случае список 
создается в момент вычисления и не храниться в памяти
"""

@profile
def check_even1(numbers):

    return list(i*i for i in range(numbers) if i % 2 == 0)

if __name__ == "__main__":

    print('Минимальный элемент равен:', bubble_sort1())
    print('Минимальный элемент равен:', bubble_sort())
    print('Минимальный элемент равен:', my_min())
    print('Минимальный элемент равен:', my_min1()) 
    print(check_even1(10000))
