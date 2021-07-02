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

import timeit
import random


def bubble_reverse_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


"""_________ с доработкой _______________"""


def bubble_reverse_sort2(lst_obj):
    n = 1
    while n < len(lst_obj):
        ind = 0
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                ind += 1
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        if ind == 0:
            break
        n += 1
    return lst_obj


orig_list = [random.randint(-100, 100) for _ in range(10)]
# print(orig_list)
# print(bubble_reverse_sort(orig_list.copy()))
# print(bubble_reverse_sort2(orig_list.copy()))


print(min(
    timeit.repeat(
        "bubble_reverse_sort(orig_list.copy())",
        repeat=5,
        globals=globals(),
        number=1000)))
print(min(
    timeit.repeat(
        "bubble_reverse_sort2(orig_list.copy())",
        repeat=5,
        globals=globals(),
        number=1000)))

orig_list = [random.randint(-100, 100) for _ in range(100)]

print(min(
    timeit.repeat(
        "bubble_reverse_sort(orig_list.copy())",
        repeat=5,
        globals=globals(),
        number=1000)))
print(min(
    timeit.repeat(
        "bubble_reverse_sort2(orig_list.copy())",
        repeat=5,
        globals=globals(),
        number=1000)))

orig_list = [random.randint(-100, 100) for _ in range(1000)]

print(min(
    timeit.repeat(
        "bubble_reverse_sort(orig_list.copy())",
        repeat=5,
        globals=globals(),
        number=1000)))
print(min(
    timeit.repeat(
        "bubble_reverse_sort2(orig_list.copy())",
        repeat=5,
        globals=globals(),
        number=1000)))

"""
доработка - добавить индекс, который проверяет, были ли замены в цикле
(если их нет, значит, все числа уже стоят правильно)

0.017561093001859263
0.00823926500743255
0.6523187590064481
0.692457204015227
78.85791727202013
85.45332641899586

Process finished with exit code 0


проблема в том, что на больших массивах эта дополнительная проверка добавляет время работы функции
плюс память на индекс и его обработку.
вероятность постороения рандомных чисел в нужном нам порядке убывания - ничтожно мала,
поэтому эта доработка в большенстве случаев не дает выигрыша в скорости, а, скорее, наоборот.
"""
