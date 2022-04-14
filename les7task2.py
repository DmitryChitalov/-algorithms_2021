from random import randint
from timeit import timeit
from operator import lt


def merge_method(list_obj, compare=lt):
    if len(list_obj) < 2:
        return list_obj[:]
    else:
        middle = int(len(list_obj) / 2)
        left = merge_method(list_obj[:middle], compare)
        right = merge_method(list_obj[middle:], compare)
        return merge(left, right, compare)


def merge(left, right, compare):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

new_list1 = [randint(0, 50) for i in range(10)]
new_list2 = [randint(0, 50) for i in range(100)]
new_list3 = [randint(0, 50) for i in range(1000)]
new_list4 = [randint(0, 50) for i in range(10000)]

print(f"Исходный список номер 1: {new_list1}")
print(f"тсортированный список 1: {merge_method(new_list1)}")
print(f"Время выполнения: {timeit('merge_method(new_list1)', globals=globals(), number=1000)}")
print("-------------------------------------------------------------------")
print(f"Исходный список номер 2: {new_list2}")
print(f"тсортированный список 2: {merge_method(new_list2)}")
print(f"Время выполнения: {timeit('merge_method(new_list2)', globals=globals(), number=1000)}")
print("-------------------------------------------------------------------")
print(f"Исходный список номер 3: {new_list3}")
print(f"тсортированный список 3: {merge_method(new_list3)}")
print(f"Время выполнения: {timeit('merge_method(new_list3)', globals=globals(), number=1000)}")
print("-------------------------------------------------------------------")
print(f"Исходный список номер 4: {new_list4}")
print(f"тсортированный список 4: {merge_method(new_list4)}")
print(f"Время выполнения: {timeit('merge_method(new_list4)', globals=globals(), number=1000)}")



""" Вот результаты измерений:
---------------------------- 10 ------------------------------------
 0.011230199999999996
---------------------------- 100 -----------------------------------
0.1675897
---------------------------- 1000 ----------------------------------
2.3810086
---------------------------- 10000 --------------------------------------
33.1182412
"""

