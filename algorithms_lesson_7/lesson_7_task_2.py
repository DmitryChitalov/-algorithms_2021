from random import uniform
from timeit import timeit

rand_list = [uniform(0, 50) for i in range(100)]


def merge_lists(left, right):
    i, j = 0, 0
    res_list = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res_list.append(left[i])
            i += 1
        else:
            res_list.append(right[j])
            j += 1
    res_list += left[i:] + right[j:]
    return res_list


def merge_sort(lst):
    left = lst[:len(lst) // 2]
    right = lst[len(lst) // 2:]
    if len(lst) > 1:
        return merge_lists(merge_sort(left), merge_sort(right))
    else:
        return lst


print(f'Исходный массив - {rand_list}, \n'
      f'Отсортированный массив - {merge_sort(rand_list)}')


rand_list1 = [uniform(0, 50) for i in range(100)]
print('Время при длине массива 100: ', timeit('merge_sort(rand_list1[:])', globals=globals(), number=100))
print('###########################################################')
rand_list2 = [uniform(0, 50) for i in range(1000)]
print('Время при длине массива 1000: ', timeit('merge_sort(rand_list2[:])', globals=globals(), number=100))
print('###########################################################')
rand_list3 = [uniform(0, 50) for i in range(10000)]
print('Время при длине массива 10000: ', timeit('merge_sort(rand_list3[:])', globals=globals(), number=100))


'''
Время при длине массива 100:  0.04923609999999999
###########################################################
Время при длине массива 1000:  0.5879314999999999
###########################################################
Время при длине массива 10000:  7.568125300000001

ВЫВОД: Сортировка слиянием работает быстрее чем сортировка выбором или вставкой.
Однако по мере увеличения длины массива время работы функции существенно растет. Это во многом связано
с использованием рекурсии. 
'''
