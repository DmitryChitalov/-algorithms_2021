from timeit import timeit
from random import randint


def median_shell(lst, m):
    step = len(lst) // 2
    while step:
        for i in range(len(lst)):
            while i >= step and lst[i] < lst[i - step]:
                lst[i], lst[i - step] = lst[i - step], lst[i]
                i -= step
        step = 1 if step == 2 else step // 2
    return lst[m]


m = int(input(f'Введите значение m: '))
unsort_lst = [randint(-100, 100) for _ in range(2 * m + 1)]
print(unsort_lst)
print(median_shell(unsort_lst[:], m))
print(timeit("median_shell(unsort_lst[:], m)", globals=globals(), number=1000))
