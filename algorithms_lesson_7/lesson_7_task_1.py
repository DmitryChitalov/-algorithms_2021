from random import randint
from timeit import timeit


orig_list = [randint(-100, 100) for _ in range(10)]
print(orig_list[:])


def bubble_sort_usual(lst):
    n = 1
    while n < len(lst):
        for i in range(len(lst)-n):
            if lst[i] < lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
        n += 1
    return lst


def break_bubble_sort(lst):
    n = 1
    while n < len(lst):
        k = 0
        for i in range(len(lst)-n):
            if lst[i] < lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                k += 1
        if k == 0: # если счетчик не переключится, значит условие if не выполнено
            break
        n += 1
    return lst


def slice_bubble_sort(lst):
    n = 1
    while n < len(lst):
        k = 0
        for i in range(len(lst[k:])-n):
            if lst[i] < lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                k += 1
        n += 1
    return lst


def bubble_sort_with_count(lst):
    n = 1
    counter = 0
    while n < len(lst):
        for i in range(len(lst) - counter - n):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
        n += 1
        counter += 1
    return lst


print('bubble_sort_usual', timeit('bubble_sort_usual(orig_list[:])', globals=globals(), number=1000))
print('break_bubble_sort', timeit('break_bubble_sort(orig_list[:])', globals=globals(), number=1000))
print('slice_bubble_sort', timeit('slice_bubble_sort(orig_list[:])', globals=globals(), number=1000))
print('bubble_sort_with_count', timeit('bubble_sort_with_count(orig_list[:])', globals=globals(), number=1000))

'''
bubble_sort_usual 0.016020600000000003
break_bubble_sort 0.0170009
slice_bubble_sort 0.018734100000000004
bubble_sort_with_count 0.012807799999999994

ВЫВОД: радикальной разницы в скорости между этими вариантами нет. Решение с разрывом цикла
может дать эффект, если randint сгенерирует отсортированный массив, но вероятность такого 
события очень невелика. Решение со срезом тоже не дало эффекта даже при больших массивах. 
Заметное ускорение дает только вариант со счетчиком итераций.  
'''
