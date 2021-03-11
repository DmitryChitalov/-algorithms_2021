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

from timeit import timeit
from random import randint


def bubble_sort(arr):
    n = 1
    while n < len(arr):
        for i in range(len(arr) - n):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        n += 1
    return arr


def bubble_sort_point(arr):
    n = 1
    while n < len(arr):
        c = True
        for i in range(len(arr) - n):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                c = False
        if c:
            break
        n += 1
    return arr


list_10 = [randint(-100, 100) for _ in range(10)]

print(
    timeit(
        "bubble_sort(list_10[:])",
        globals=globals(),
        number=1000))

print(
    timeit(
        "bubble_sort_point(list_10[:])",
        globals=globals(),
        number=1000))

print(list_10)
print(bubble_sort(list_10))
print("===============================================")
list_100 = [randint(-100, 100) for _ in range(100)]

print(
    timeit(
        "bubble_sort(list_100[:])",
        globals=globals(),
        number=1000))

print(
    timeit(
        "bubble_sort_point(list_100[:])",
        globals=globals(),
        number=1000))

print(list_100)
print(bubble_sort(list_100))
print("===============================================")
list_1000 = [randint(-100, 100) for _ in range(1000)]

print(
    timeit(
        "bubble_sort(list_1000[:])",
        globals=globals(),
        number=100))

print(
    timeit(
        "bubble_sort_point(list_1000[:])",
        globals=globals(),
        number=100))

print(list_1000)
print(bubble_sort(list_1000))
"""
Доработка алгоритма сортировки "пузырьком" заключалась в следующем: завершение работы алгоритма в случае,
если за проход по списку не совершается ни одной сортировки. Такое могло произойти только в случае, если
исходный массив уже был отсортирован, что маловероятно. Соответственно при замерах времени работы, доработка
положительного результата не дала. На больших массивах, алгоритм с доработкой работает даже дольше.
При массиве в 1000 элементов на 100 запусках: без доработки - 15,3 сек, с доработкой - 15,8 сек.
В доработке следовательно нет необходимости.
"""
