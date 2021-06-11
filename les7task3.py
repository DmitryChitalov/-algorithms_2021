from timeit import timeit
from statistics import median
import random


def median_1(lst):
    lst = lst[:]
    for _ in range(len(lst) // 2):
        lst.remove(max(lst))
    return max(lst)



def median_2(lst, m):
    i = 1
    lst = lst[:]
    while i < len(lst):
        if lst[i - 1] <= lst[i]:
            i+=1
        else:
            tmp = lst[i]
            lst[i] = lst[i-1]
            lst[i-1] = tmp
            i-=1
            if i == 0:
                i = 1
    return lst[m]



m = int(input("Введите m: "))
new_list = [random.randint(1, 100) for _ in range(2 * m + 1)]
print(f"Созданный список: {new_list}")
print(f"Первая реализация: {median_1(new_list)}")
print(f"Вторая реализация(медиана находится по индексу m): {median_2(new_list, m)}")
print(f"Проверка через функцию median: {median(new_list)}")

new_list_10 = [random.randint(1, 100) for _ in range(2 * 10 + 1)]
new_list_100 = [random.randint(1, 100) for _ in range(2 * 100 + 1)]

print(timeit("median_1(new_list_10)", globals=globals(), number=1000))
print(timeit("median_2(new_list_10[:], 10)", globals=globals(), number=1000))
print(timeit("median(new_list_10)", globals=globals(), number=1000))
print(timeit("median_1(new_list_100)", globals=globals(), number=1000))
print(timeit("median_2(new_list_100[:], 10)", globals=globals(), number=1000))
print(timeit("median(new_list_100)", globals=globals(), number=1000))

"""Результаты измерений:
-------- 10 -------
0.005201000000000011
0.02507980000000032
0.0004820000000003155
-------- 100 -------
0.21238350000000006
2.4429996999999997
0.00552819999999965

Можно заметить, что встроенная функция median выполняется бустрее всех
На втором месте по скорости выполнения будет функция median_1 которая работает без сортировки
И на третьем месте функция median_2, она с сортировкой. То есть каждый раз требуется сортировать список, поэтому и
требуется больше времени.
"""
