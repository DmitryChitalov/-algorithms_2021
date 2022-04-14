from random import random
from timeit import timeit

def create(n):
    l = [random()*50 for _ in range(n)]
    return l

def merge_two_lists(a, b):
    c = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    if i < len(a):
        c += a[i:]
    if j < len(b):
        c += b[j:]
    return c


def merge_sort(s):
    if len(s) == 1:
        return s
    middle = len(s) // 2
    left = merge_sort(s[:middle])
    right = merge_sort(s[middle:])
    return merge_two_lists(left, right)

l = create(10)
l1 = create(100)
l2 = create(1000)
print(l)
print(merge_sort(l))
print(timeit(f'merge_sort({l})', globals = globals(), number = 1000))
print(timeit(f'merge_sort({l1})', globals = globals(), number = 1000))
print(timeit(f'merge_sort({l2})', globals = globals(), number = 1000))
