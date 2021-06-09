from timeit import timeit
from random import randint

def median_in_list(lst_obj):
    left_side = []
    right_side = []
    for i in range(len(lst_obj)):
        for j in range(len(lst_obj)):
            if lst_obj[i] > lst_obj[j]:
                left_side.append(lst_obj[j])
            if lst_obj[i] < lst_obj[j]:
                right_side.append(lst_obj[j])
            if lst_obj[i] == lst_obj[j] and i > j:
                left_side.append(lst_obj[j])
            if lst_obj[i] == lst_obj[j] and i < j:
                right_side.append(lst_obj[j])
        if len(left_side) == len(right_side):
            return lst_obj[i]
        left_side.clear()
        right_side.clear()


m = int(input("Введите натуральное число: "))
some_list = [randint(0, 100) for i in range(2 * m + 1)]
print(timeit('median_in_list(some_list)', globals=globals(), number=100))

"""Вот измерения на различных числах:
--------- 10 ---------
0.001005600000000051
--------- 100 ---------
0.19796440000000004
--------- 300 ---------
1.924983
"""