"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.
Сортировка должна быть реализована в виде функции.
Обязательно доработайте алгоритм (сделайте его умнее).
Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение. Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность
Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.
Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""
from random import randrange
from timeit import timeit


def bubble_sort_desc(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_desc_mod(lst_obj):
    n = 1
    while n < len(lst_obj):
        have_premutation = False
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                have_premutation = True
        if have_premutation == False:
            break
        n += 1
    return lst_obj


# Доработка связанна с тем, что если во внутреннем цикле не было ни одной перестановки, то список упорядочен,
# а значит делать иттерации больше нет необходимости

def bubble_sort_desc_mod2(lst_obj):
    n = 1
    while n < len(lst_obj):
        have_premutation = False
        max = lst_obj[0]
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                have_premutation = True
            if lst_obj[i] > max:
                lst_obj[i], lst_obj[0] = lst_obj[0], lst_obj[i]
        if have_premutation == False:
            break
        n += 1
    return lst_obj


# В этой функции, дополнительно, в ходе проверок во внутреннем цикле одновременно проверялось является ли текущий
# элемент больше максимального.
# На первом заходе за максимальный элемент принят первый элемент.
# Если является, то помещаем его в начало списка, т.к. возможно он самый максимальный.


def bubble_sort_desc_mod3(lst_obj):
    n = len(lst_obj)
    while True:
        have_premutation = False
        for i in range(0, n - 1, 2):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                have_premutation = True
        for i in range(1, n - 1, 2):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                have_premutation = True
        if have_premutation == False:
            break
    return lst_obj


# В этой функции, реализован механизм четно-нечетной сортировки - разновидности пузырьковой,
# когда выбираются элементы с нечетными/четными индексами и сравниваются с соседними элементами
# таким образом обеспечивается параллельное движение сразу нескольких "пузырьков"

seq = [randrange(-100, 100) for i in range(20)]
# print(seq)
# print(bubble_sort_desc(seq[:]))
# print(bubble_sort_desc_mod(seq[:]))
# print(bubble_sort_desc_mod2(seq[:]))
# print(bubble_sort_desc_mod3(seq[:]))

# print(timeit('bubble_sort_desc(seq[:])', globals=globals(), number=1000))
# print(timeit('bubble_sort_desc_mod(seq[:])', globals=globals(), number=1000))
# print(timeit('bubble_sort_desc_mod2(seq[:])', globals=globals(), number=1000))
# print(timeit('bubble_sort_desc_mod3(seq[:])', globals=globals(), number=1000))

'''
Результаты замеров:
Массив из 20 элементов
bubble_sort_desc() - 0.1593357
bubble_sort_desc2() - 0.16448820000000003
bubble_sort_desc3() - 0.22351760000000004
bubble_sort_desc4() - 0.15271069999999998

Самой быстрой здесь оказалась функция реализующая алгоритм четно-нечетной сортировки. 
Функция bubble_sort_desc3() показала наибольшее время работы, что связано с тем, что приходится делать дополнительные 
сравнения, которых нет в других функциях

Массив из 1000 элементов
bubble_sort_desc() - 69.4174993
bubble_sort_desc2() - 74.02326519999998
bubble_sort_desc3() - 95.46221560000001
bubble_sort_desc4() - 73.93341669999998

Самой быстрой оказалась функция классической пузырьковой сортировки bubble_sort_desc(). Жаль, не получилось ускорить.
'''
