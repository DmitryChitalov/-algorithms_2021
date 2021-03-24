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

from timeit import default_timer
import random


def my_decor(func):
    def check_time(*args):
        t1 = default_timer()
        result = func(*args)
        t2 = default_timer()
        time_res = t2 - t1
        print(f'Время: {time_res}\nРезультат: {result}')

    return check_time


@my_decor
def bubble_sort_slow(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj

@my_decor
def bubble_sort_fast(lst_obj):
    n = 1
    flag = True
    while n < len(lst_obj) and flag:
        flag = False
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
                flag = True
        n += 1
    return lst_obj


orig_list = [random.randint(-100, 100) for _ in range(100)]
print(orig_list)
bubble_sort_slow(orig_list)
bubble_sort_fast(orig_list)
'''
для простой сортировки пузырьком: Время: 0.008364300000000019
для модифицированной сортировки : Время: 6.719999999998949e-05
Результат улучшился на несколько порядков за счет того, что 
когда массив уже отсортировани, алгоритм перестает работать, а не проходит его до конца
'''