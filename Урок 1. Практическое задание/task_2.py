"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.

Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.

Не забудьте указать где какая сложность.

Примечание:
Построить список можно через списковое включение.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.
"""
import random
""" Алгоритм первый O(N^2) """
def bubble_sort (lst_obj): # O(N+N*N+O(1)) = O(N^2)
    lst = list(lst_obj)# O(N)
    for index_one in range(len(lst)):# O(N)
        for index_next in range(index_one + 1, len(lst)): # O(N)
            if lst[index_next] < lst[index_one]: # O(1)
                lst[index_next], lst[index_one] = lst[index_one], lst[index_next] # O(1)
    return lst[0]
""" Алгоритм второй O(N) """
def min_func(lst_obj):# O(N)
    lst = lst_obj # O(N)
    min_val = lst[0] # O(1)
    for val in lst: # O(N)
        if val < min_val: # O(1)
            min_val = val # O(1)
    return min_val # O(1)

original_list = [(element + 1) for element in range(random.randint(5, 25)) if element > 5]
random.shuffle(original_list)
print(original_list)
print(bubble_sort(original_list))
print(min_func(original_list))



