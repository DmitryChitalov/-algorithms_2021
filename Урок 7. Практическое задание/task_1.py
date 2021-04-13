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


from random import randint
from timeit import timeit


def bubble_sort(arr):
    n = 1
    while n < len(arr):
        for i in range(len(arr) - n):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        n += 1
    return arr


def bubble_sort_upd(arr):
    n = 1
    while n < len(arr):
        swap = False
        for i in range(len(arr) - n):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swap = True
        if not swap:
            return arr
        n += 1
    return arr


list_rnd = [randint(-100, 100) for _ in range(200)]
list_opt = [el for el in range(200, 0, -1)]
list_neg = [el for el in range(200)]

print('Замеры на рандомном массиве')
print(timeit('bubble_sort(list_rnd[:])',
             number=1000,
             globals=globals()))
print(timeit('bubble_sort_upd(list_rnd[:])',
             number=1000,
             globals=globals()))
print('\nЗамеры на оптимальном массиве')
print(timeit('bubble_sort(list_opt[:])',
             number=1000,
             globals=globals()))
print(timeit('bubble_sort_upd(list_opt[:])',
             number=1000,
             globals=globals()))
print('\nЗамеры на худшем варианте массива')
print(timeit('bubble_sort(list_neg[:])',
             number=1000,
             globals=globals()))
print(timeit('bubble_sort_upd(list_neg[:])',
             number=1000,
             globals=globals()))

"""
Замеры на рандомном массиве
4.6160997
4.4848432

Замеры на оптимальном массиве
2.2553229000000012
0.04780640000000069

Замеры на худшем варианте массива
6.6131954
6.879781899999998

Исходя из полученых результатов видно, что при рандомных входящих данных и самом негативном варинте результаты схожи.
При оптимальном варианте массива доработаная сортировка пузырьком ожидаемо работает гараздо быстрее.
Поскольку оптимизированая функция не имеет проигрыша во времени на случайных данных, но может быть гараздо быстрее
при позитивных варинтах массива доработка оправдана.
"""
