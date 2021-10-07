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
import random
from timeit import timeit

test_massive = [random.randint(-100, 100) for _ in range(100)]


def bubble_sort_old(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort(lst_obj: list):
    n = 1
    while n < len(lst_obj):
        sort = True
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                sort = False
        if sort is True:
            break
        n += 1

    return lst_obj


# Выводим список до и после сортировки
print(f'Список до сортировки {test_massive}')
print(f'Список после сортировки {bubble_sort(test_massive.copy())}')
# Делаем замеры
# 100 измерений
print(timeit('bubble_sort_old(test_massive.copy())', number=100, globals=globals()))  # 0.08
print(timeit('bubble_sort(test_massive.copy())', number=100, globals=globals()))  # 0.13
# 1000 измерений
print(timeit('bubble_sort_old(test_massive.copy())', number=1000, globals=globals()))  # 1.06
print(timeit('bubble_sort(test_massive.copy())', number=1000, globals=globals()))  # 1.05
# 10000 измерений
print(timeit('bubble_sort_old(test_massive.copy())', number=10000, globals=globals()))  # 10.06
print(timeit('bubble_sort(test_massive.copy())', number=10000, globals=globals()))  # 10.27

'''
Аналитика:
Если за весь цикл не выполняется ни одной сортировки, то цикл завершается
Особого смысла в этой доработке нет, т.к получить отсортированный массив практически невозможно
'''
