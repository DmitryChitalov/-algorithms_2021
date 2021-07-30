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

from timeit import timeit
import random


def bubble_sort1(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort2(lst_obj):
    n = 1
    chk = True
    while n < len(lst_obj) and chk:
        chk = False
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
                chk = True
        n += 1
    return lst_obj


print('Список 10 элементов: ')
orig_list = [random.randint(-100, 100) for _ in range(10)]
print(orig_list)
print(bubble_sort2(orig_list[:]))
# замеры 10
print(
    timeit(
        "bubble_sort1(orig_list[:])",
        globals=globals(),
        number=1000))                   # 0.006827300000000001
# замеры 10
print(
    timeit(
        "bubble_sort2(orig_list[:])",
        globals=globals(),
        number=1000))                   # 0.007032300000000002

print('Список 100 элементов: ')
orig_list = [random.randint(-100, 100) for _ in range(100)]
print(orig_list)
print(bubble_sort2(orig_list[:]))
# замеры 100
print(
    timeit(
        "bubble_sort1(orig_list[:])",
        globals=globals(),
        number=1000))                   # 0.4919928
# замеры 100
print(
    timeit(
        "bubble_sort2(orig_list[:])",
        globals=globals(),
        number=1000))                   # 0.49634580000000006

print('Список 1000 элементов: ')
orig_list = [random.randint(-100, 100) for _ in range(1000)]
print(orig_list)
print(bubble_sort2(orig_list[:]))
# замеры 1000
print(
    timeit(
        "bubble_sort1(orig_list[:])",
        globals=globals(),
        number=1000))                   # 59.757040599999996
# замеры 1000
print(
    timeit(
        "bubble_sort2(orig_list[:])",
        globals=globals(),
        number=1000))                   # 60.308510899999995

# Оптимизация- устанавливаю признак выполнения замены в проходе, если его не случилось - сокращаю кол-во проходов
# Эффективности оптимизация не дала.

