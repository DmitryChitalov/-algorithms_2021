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


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_v2(lst_obj):
    count = 0
    for el in range(len(lst_obj)-1):
        for i in range(len(lst_obj)-1-el):
            if lst_obj[i] < lst_obj[i+1]:
                count += 1
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        if count == 0:
            break
    return lst_obj


orig_list = [random.randint(-100, 100) for _ in range(100)]
orig_list1 = [_ for _ in reversed(range(-100, 100))]

print(
    timeit.timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))
print('_______Обычная функция c не отсортированным массивом____')
print(
    timeit.timeit(
        "bubble_sort(orig_list1[:])",
        globals=globals(),
        number=1000))
print('_______Обычная функция с отсортированным массивом____')
print(
    timeit.timeit(
        "bubble_sort_v2(orig_list[:])",
        globals=globals(),
        number=1000))
print('_______Улучшенная функция с не отсортированным массивом____')
print(
    timeit.timeit(
        "bubble_sort_v2(orig_list1[:])",
        globals=globals(),
        number=1000))
print('_______Улучшенная функция с отсортированным массивом____')

print(orig_list)
print('_______Не отсортированный____')
print(orig_list1)
print('_______Отсортированный изначально____')
print(bubble_sort(orig_list))
print('_______Обычная функция с не отсортированным массивом____')
print(bubble_sort_v2(orig_list1))
print('_______Улучшенная функция с отсортированным массивом____')
print(bubble_sort_v2(orig_list))
print('_______Улучшенная функция не отсортированным массивом____')
# Обычный метод более медленный, так как он не прерывается если массив уже отсортированный изначально.
# C for код отрабатывает чуть медленней, применил чтобы сравнить с while
