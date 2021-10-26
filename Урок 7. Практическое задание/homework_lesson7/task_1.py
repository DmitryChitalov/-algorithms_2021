import timeit
import random


# 1 вариант
def bubble_sorting_1(lst):
    for i in range(len(lst)-1, -1, -1):
        for j in range(len(lst)-1, -1, -1):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst


# 2 вариант
def bubble_sorting_2(lst):
    attribute = False
    for i in range(len(lst)-1, -1, -1):
        for j in range(len(lst)-1, -1, -1):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
                attribute = True
        if attribute is False:
            return lst
    return lst


my_list = [random.randint(-100, 100) for _ in range(30)]


print('1 ВАРИАНТ')
print(f'Исходный массив: {my_list}')
print(f'Отсортированный массив: {bubble_sorting_1(my_list[:])}')
print(timeit.timeit("bubble_sorting_1(my_list[:])", globals=globals(), number=1000))
print()

print('2 ВАРИАНТ')
my_list = bubble_sorting_1(my_list[:])
print(f'Исходный массив: {my_list}')
print(f'Отсортированный массив: {bubble_sorting_2(my_list[:])}')
print(timeit.timeit("bubble_sorting_2(my_list[:])", globals=globals(), number=1000))
print()


'''
Вывод
Второй вариант выполняется быстрее. Моя доработка заключается в проверке ситуации 
когда один из элементов не выполнил ни одну перестановку с другими элементами массива. 
В такой ситуации attribute остается в значении False и сортировка прерывается.
'''
