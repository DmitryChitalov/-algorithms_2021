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

orig_list = [random.randint(-100, 100) for _ in range(100)]
count = 100
ordered_array = [random.randint(-100, 100) for _ in range(count)]


def bubble_sort(my_list):
    n = 1
    while n < len(my_list):
        for i in range(len(my_list) - n):
            if my_list[i] > my_list[i + 1]:
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
        n += 1
    return my_list


print('Не отсортированный список, превым способом')
print(timeit.timeit("bubble_sort(orig_list[:])", globals=globals(), number=1000))
print('Отсортированный список, превым способом')
print(timeit.timeit("bubble_sort(ordered_array[:])", globals=globals(), number=1000))


def buble_sort_2(my_list):
    exchange = True
    ln = len(my_list) - 1
    for i in range(ln):
        if not exchange:
            break
        exchange = False
        for j in range(ln, 0, -1):
            if my_list[j] < my_list[j - 1]:
                my_list[j - 1], my_list[j] = my_list[j], my_list[j - 1]
                exchange = True
        ln -= 1
    return my_list


print('Не отсортированный список, после доработки')
print(timeit.timeit("buble_sort_2(orig_list[:])", globals=globals(), number=1000))
print('Отсортированный список, после доработки')
print(timeit.timeit("buble_sort_2(ordered_array[:])", globals=globals(), number=1000))

'''Доработка ускорила работу функции в случае отсортированного и не осортированного списка.
Доработка состоит в том, цикл может завершится без лишних проходов по уже отсортированному.
Вероятность того что список будет уже отсортирован очень мала'''
