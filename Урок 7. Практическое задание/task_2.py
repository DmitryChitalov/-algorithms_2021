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

from random import uniform
from timeit import timeit

my_list10 = [uniform(0.0, 50.0) for num0 in range(10)]
my_list100 = [uniform(0.0, 50.0) for num1 in range(100)]
my_list1000 = [uniform(0.0, 50.0) for num2 in range(1000)]
print(f'Несортированный массив: \n {my_list10}')


def merge_lists(lst1, lst2):
    i = j = 0
    merged_lst = []
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            merged_lst.append(lst1[i])
            i += 1
        else:
            merged_lst.append(lst2[j])
            j += 1
    merged_lst += lst1[i:] + lst2[j:]
    return merged_lst


def input_data(any_list):
    if len(any_list) == 1:
        return any_list
    else:
        lst1 = input_data(any_list[:len(any_list)//2])
        lst2 = input_data(any_list[len(any_list)//2:])
        return merge_lists(lst1, lst2)


def bubble_sort(any_list):
    n = len(any_list)
    for x in range(n):
        for y in range(len(any_list[x:]) - 1):
            if any_list[y + 1] > any_list[y]:
                any_list[y + 1], any_list[y] = any_list[y], any_list[y + 1]
    return any_list


print(f'Проверка сортировки: \n {input_data(my_list10)}')

print('Merge 10 элементов в списке', timeit('input_data(my_list10[:])', globals=globals(),
                                                           number=10000))
print('Merge 100 элементов в списке', timeit('input_data(my_list100[:])', globals=globals(),
                                                            number=10000))
print('Bubble 100 элементов в списке', timeit('bubble_sort(my_list100[:])', globals=globals(),
                                                             number=10000))
print('Merge 1000 элементов в списке', timeit('input_data(my_list1000[:])', globals=globals(),
                                                             number=10000))


"""
Merge 10 элементов в списке 0.10386949999999999
Merge 100 элементов в списке 2.0953494
Bubble 100 элементов в списке 5.454131
Merge 1000 элементов в списке 27.315076100000002

Пузырьковая сортировка со срезом, которая показала себя лучшей в предыдущем задании, в данном задании проиграла с 
огромным отрывом методу слияния.
"""