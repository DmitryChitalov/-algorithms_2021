"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в виде функции.

Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение. Обязательно сделайте замеры времени обеих реализаций
и укажите дала ли оптимизация эффективность.

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.

Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""

from random import randint
import timeit


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_1(lst_obj):
    n = 1
    flag = True
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
                flag = False
        if flag:
            break
        n += 1
        flag = True
    return lst_obj


num = 1000
orig_list_10 = [randint(-100, 100) for _ in range(10)]
# print(f'Исходный массив : {orig_list_10}\nОтсортированный массив: {bubble_sort(orig_list_10[:])}')
# замеры 10
print(f'Звмер сортировки массива из 10 элементов без флага: '
      f'{timeit.timeit("bubble_sort(orig_list_10[:])", globals=globals(), number=num)}\n')
print(f'Звмер сортировки массива из 10 элементов с флагом: '
      f'{timeit.timeit("bubble_sort_1(orig_list_10[:])", globals=globals(), number=num)}\n')


orig_list_100 = [randint(-100, 100) for _ in range(100)]
# print(f'Исходный массив : {orig_list_100}\nОтсортированный массив: {bubble_sort(orig_list_100[:])}')
# замеры 100
print(f'Звмер сортировки массива из 100 элементов без флага: '
      f'{timeit.timeit("bubble_sort(orig_list_100[:])", globals=globals(), number=num)}\n')
print(f'Звмер сортировки массива из 100 элементов с флагом: '
      f'{timeit.timeit("bubble_sort_1(orig_list_100[:])", globals=globals(), number=num)}\n')

orig_list_1000 = [randint(-100, 100) for _ in range(1000)]
# print(f'Исходный массив : {orig_list_1000}\nОтсортированный массив: {bubble_sort(orig_list_1000[:])}')
# замеры 1000
print(f'Звмер сортировки массива из 1000 элементов без флага: '
      f'{timeit.timeit("bubble_sort(orig_list_1000[:])", globals=globals(), number=num)}')
print(f'Звмер сортировки массива из 1000 элементов с флагом: '
      f'{timeit.timeit("bubble_sort_1(orig_list_1000[:])", globals=globals(), number=num)}\n')

'''
За основу был взять пример с урока. Для того чтоб сделать сортировку по убыванию изменил знак ">" на "<" в конструкции:
if lst_obj[i] < lst_obj[i+1]:. Для прерывания цикла, при отсортированном массиве добавил переменную flag.
Добавление переменной имеет смысл только в если есть шанс того что массив будет отсортированный, но у нас массивы 
рандомные, поэтому смысла в этом нет.
'''
