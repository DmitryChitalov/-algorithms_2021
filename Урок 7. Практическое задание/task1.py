from random import randint
from timeit import timeit

l = [randint(-100, 100) for _ in range(500)]
print(l)


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_modific(lst_obj):
    n = 1
    while n < len(lst_obj):
        flag = False
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                flag = True
        n += 1
        if flag == False:
            break
    return lst_obj


print(bubble_sort(l))
print(bubble_sort_modific(l))

print(timeit(f"bubble_sort({l})", globals=globals(), number=1000))
print(timeit(f"bubble_sort_modific({l})", globals=globals(), number=1000))

