"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные по длине части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, Кучей...

[5, 3, 4, 3, 3, 3, 3]

[3, 3, 3, 3, 3, 4, 5]
"""
from statistics import median
from random import randint
from timeit import timeit


def find_med(lst):
    mid = len(lst) // 2
    while mid:
        lst.remove(max(lst))
        mid -= 1
    return max(lst)


def gnom_sort(lst, m):
    base = 0
    memory = 1
    while base in range(len(lst) - 1):
        if lst[base] <= lst[base + 1]:
            base +=1
            memory +=1
        else:
            lst[base], lst[base + 1] = lst[base + 1], lst[base]
            base -= 1
            if base < 0:
                base += 1
                memory += 1
    return lst[m]


# lst = [5, 3, 4, 3, 3, 3, 3]
m = int(input('Введите число: '))
lst = [randint(-100, 100) for _ in range(2 * m + 1)]
print(find_med(lst[:]))
print(median(lst))
print(gnom_sort(lst[:], m))

print('median():\n', timeit(
        "median(lst)",
        setup='from __main__ import median, lst',
        number=10000))
print('find_med():\n', timeit(
        "find_med(lst[:])",
        setup='from __main__ import find_med, lst',
        number=10000))
print('gnom_sort():\n', timeit(
        "gnom_sort(lst[:], m)",
        setup='from __main__ import gnom_sort, lst, m',
        number=10000))


"""
Введите число: 50
-5
-5
-5
median():
 0.033038900000000204
find_med():
 0.7090583000000001
gnom_sort():
 22.1635574
 
 Гномья сортировка имеет сложность О(n**2). Это видно и по результатам времени работы кода.
 Намного быстрее работат функция без сортировки, цикл делает ограниченное количество итераций 
 с использованием встроенной функции max. 
 Естественно самой быстрой оказалась встроенная функция, так как она уже является специально оптимизировнной под данную
 задачу.
"""