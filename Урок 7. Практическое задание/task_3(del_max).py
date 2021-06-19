from timeit import timeit
from random import randint


def median_el(lst):
    for _ in range(len(lst) // 2):
        lst.remove(max(lst))
    return max(lst)


m = int(input(f'Введите значение m: '))
unsort_lst = [randint(-100, 100) for _ in range(2 * m + 1)]
print(unsort_lst)
print(median_el(unsort_lst))
print(timeit("median_el(unsort_lst)", globals=globals(), number=1000))
