"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Хотя в примерах к уроку уже есть вариант реализации слияния,
попробуйте предложить другой (придумать или найти).

И попытаться сделать замеры на массивах разной длины: 10, 100, 1000, ...

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
from timeit import timeit
from random import uniform


# Вариант 1: методом слияния
def merge_sort(my_list):
    if len(my_list) > 1:
        mid = len(my_list) // 2
        left_half = my_list[:mid]
        right_half = my_list[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                my_list[k] = left_half[i]
                i = i + 1
            else:
                my_list[k] = right_half[j]
                j = j + 1
            k = k + 1

        while i < len(left_half):
            my_list[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half):
            my_list[k] = right_half[j]
            j = j + 1
            k = k + 1
        return my_list


# Вариант 2: методом слияния
def merge(left, right):
    if len(left) == 0:
        return right

    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    while len(result) < len(left) + len(right):
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break

    return result


def merge_sort2(my_list):
    if len(my_list) < 2:
        return my_list
    midpoint = len(my_list) // 2
    return merge(left=merge_sort(my_list[:midpoint]), right=merge_sort(my_list[midpoint:]))


list0 = [uniform(0, 50) for _ in range(int(input('Введите число элементов: ')))]
list1 = [uniform(0, 50) for _ in range(10)]
list2 = [uniform(0, 50) for _ in range(100)]
list3 = [uniform(0, 50) for _ in range(1000)]
print('Исходный        ', list0)
print('Отсортированный ', merge_sort(list0))
print('\nВариант 1')
print('Замер на массиве 10 элементов:  ', timeit('merge_sort(list1[:])', globals=globals(), number=1000))
print('Замер на массиве 100 элементов: ', timeit('merge_sort(list2[:])', globals=globals(), number=1000))
print('Замер на массиве 1000 элементов:', timeit('merge_sort(list3[:])', globals=globals(), number=1000))
del list1, list2, list3
list1 = [uniform(0, 50) for _ in range(10)]
list2 = [uniform(0, 50) for _ in range(100)]
list3 = [uniform(0, 50) for _ in range(1000)]
print('\nВариант 2')
print('Замер на массиве 10 элементов:  ', timeit('merge_sort2(list1[:])', globals=globals(), number=1000))
print('Замер на массиве 100 элементов: ', timeit('merge_sort2(list2[:])', globals=globals(), number=1000))
print('Замер на массиве 1000 элементов:', timeit('merge_sort2(list3[:])', globals=globals(), number=1000))

# Два немного разных варианта алгоритма методом слияния. Выполняю замеры: merge_sort работает
# немного быстрее, чем merge_sort2.
#
# Введите число элементов: >? 5
# Исходный         [9.757043880625943, 42.212402535574164, 43.107392836666016, 24.337279063942702, 5.131617628204715]
# Отсортированный  [5.131617628204715, 9.757043880625943, 24.337279063942702, 42.212402535574164, 43.107392836666016]
# Вариант 1
# Замер на массиве 10 элементов:   0.014870442999999511
# Замер на массиве 100 элементов:  0.22887798600000053
# Замер на массиве 1000 элементов: 3.184217909
# Вариант 2
# Замер на массиве 10 элементов:   0.016041464000000616
# Замер на массиве 100 элементов:  0.24808746200000087
# Замер на массиве 1000 элементов: 3.361935117
#
# Думаю, что второй вариант merge_sort2 уже хуже, потому что использует 2 функции: merge(left, right) и
# merge_sort2(my_list), вместо первого варианта merge_sort(my_list). Накладные расходы во втором случае больше, и они
# не нужны в качестве выбора.
