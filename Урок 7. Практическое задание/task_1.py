"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в
виде функции.

Обязательно доработайте алгоритм (сделайте его умнее)!

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение.
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.

Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""

import timeit
import random

def bubble_revsort1(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:     #перевернул в сторону уменьшения
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj

def bubble_revsort2(lst_obj):   #оптимизированный - меняем while -> for + If is_sorted
    for n in range(1, len(lst_obj)):
        is_sorted = True
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i+1]:     #перевернул в сторону уменьшения
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
                is_sorted = False
        if is_sorted:
                break
    return lst_obj


orig_lst = [random.randint(-100, 100) for _ in range(10)]
print(f"Random array for func-s with range = 10 -> {orig_lst}")
print(timeit.timeit("bubble_revsort1(orig_lst[:])", globals=globals(), number=1000))
print(timeit.timeit("bubble_revsort2(orig_lst[:])", globals=globals(), number=1000))
print(f"Sorted with reverse - func 1: {bubble_revsort1(orig_lst)}\n func 2: {bubble_revsort2(orig_lst)}")

print(f"Random array for func-s with range = 100 -> {orig_lst}")
orig_lst = [random.randint(-100, 100) for _ in range(100)]
print(timeit.timeit("bubble_revsort1(orig_lst[:])", globals=globals(), number=1000))
print(timeit.timeit("bubble_revsort2(orig_lst[:])", globals=globals(), number=1000))
print(f"Sorted with reverse - func 1: {bubble_revsort1(orig_lst)}\n func 2: {bubble_revsort2(orig_lst)}")

print(f"Random array for func-s with range = 300 -> {orig_lst}")
orig_lst = [random.randint(-100, 100) for _ in range(300)]
print(timeit.timeit("bubble_revsort1(orig_lst[:])", globals=globals(), number=1000))
print(timeit.timeit("bubble_revsort2(orig_lst[:])", globals=globals(), number=1000))
print(f"Sorted with reverse - func 1: {bubble_revsort1(orig_lst)}\n func 2: {bubble_revsort2(orig_lst)}")

print(f"Random array for func-s with range = 500 -> {orig_lst}")
orig_lst = [random.randint(-100, 100) for _ in range(500)]
print(timeit.timeit("bubble_revsort1(orig_lst[:])", globals=globals(), number=1000))
print(timeit.timeit("bubble_revsort2(orig_lst[:])", globals=globals(), number=1000))
print(f"Sorted with reverse - func 1: {bubble_revsort1(orig_lst)}\n func 2: {bubble_revsort2(orig_lst)}")

"""
Оптимизацию проводил через замену while на for + доп. условие по досрочному выходу из цикла
Вывод: 
Исходя из полученных результатов оптимизация поспособствовала увеличению производительности, времени затратилось меньше.
Извиняюсь, но на с 1000 элементов ноут уже прост не тянет)))

Результаты ниже (первый результат - без оптимизации, второй - с оптимизацией):
    10 elems
    0.013217699999999999
    0.012487099999999973
    
    100 elems
    0.9141052999999999
    0.8870591000000001
    
    300 elems
    7.8539137
    7.836256399999998
    
    500 elems
    24.865369299999998
    24.2510932

"""