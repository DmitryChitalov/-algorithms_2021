"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""

import random
import timeit



def merge_sort(alist):

    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1


n = int(input("Введите число элементов: "))
alist = [random.random()*50 for i in range(n)]

print(f"Исходный - {alist}")
merge_sort(alist)
print(f"Отсортированный - {alist}")

#-----------------------------------------------------------------------------------------------------------------
def func_1(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0
    left_list_length, right_list_ = len(left_list), len(right_list)
    for i in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1
    return sorted_list

def func_sort(n):
    if len(n) <= 1:
        return n
    mid = len(n) // 2
    left_list = func_sort(n[:mid])
    right_list = func_sort(n[mid:])
    return func_1(left_list, right_list)


random_list_of_nums = func_sort(alist)
print(random_list_of_nums)

print('1---  проверка на 100 запусков --', timeit.timeit("merge_sort(alist)",
                    setup="from __main__ import merge_sort, alist", number=100))
print('1---  проверка на 1000 запусков --', timeit.timeit("merge_sort(alist)",
                    setup="from __main__ import merge_sort, alist", number=1000))



print('2---  проверка на 100 запусков --', timeit.timeit("func_sort(alist)",
                    setup="from __main__ import func_sort, alist", number=100))
print('2---  проверка на 1000 запусков --', timeit.timeit("func_sort(alist)",
                    setup="from __main__ import func_sort, alist", number=1000))



#1---  проверка на 100 запусков -- 0.00098459999999978
#1---  проверка на 1000 запусков -- 0.008360099999999981
#2---  проверка на 100 запусков -- 0.0007662999999999975
#2---  проверка на 1000 запусков -- 0.007166100000000064