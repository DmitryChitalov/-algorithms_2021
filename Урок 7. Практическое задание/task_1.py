from timeit import timeit
import random
"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в
виде функции.

Обязательно доработайте алгоритм (сделайте его умнее)!

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.

Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""
'''Сортировка выбором'''
unsorted_list_1 = [random.randint(-100, 100) for _ in range(10)]
sort_st = input('Ввдите тип сортировки, который вам нужен: <(обратная) или >(обычная) ')


def bubble_sort_1_opt(lst_obj):  # Оптимизиированный вариант
    iter_num = 1
    changes = True
    length = len(lst_obj)
    while changes:
        changes = False
        for el_1 in range(length-1):
            if sort_st == '>':
                if lst_obj[el_1] > lst_obj[el_1+1]:
                    lst_obj[el_1], lst_obj[el_1+1] = lst_obj[el_1+1], lst_obj[el_1]
                    changes = True
            if sort_st == '<':
                if lst_obj[el_1] < lst_obj[el_1+1]:
                    lst_obj[el_1], lst_obj[el_1+1] = lst_obj[el_1+1], lst_obj[el_1]
                    changes = True
        iter_num += 1
        length -= 1
    return lst_obj, iter_num


def funct():
    return timeit('bubble_sort_1_opt(unsorted_list_1[:])', globals=globals(), number=10000)


def bubble_sort_2(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] > lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj, n


def funct_1():
    return timeit('bubble_sort_2(unsorted_list_1[:])', globals=globals(), number=10000)


print(funct())
print(funct_1())
print(bubble_sort_1_opt(unsorted_list_1[:]))
print(bubble_sort_2(unsorted_list_1[:]))
'''Оптимизация заключается в том, что при обычной сортировке пузырьком нет разницы, отсортирован ли список хоть как нибудь, 
цикл в любом случае будет проходить весь список и выполняться за время O(n^2), а оптимизированная сортировка работает 
быстрее, чем стандартный вариант т.к. цикл итерируется только тогда, когда в списке есть изменения,если их нет, 
то после крайней итерации переменная changes принимает значение false, это означает, что скрипт отсортирован. '''
