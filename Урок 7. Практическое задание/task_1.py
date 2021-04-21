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


def bubble_sort_rework(lst_obj):
    n = 1
    flag = True
    while n < len(lst_obj) and flag:
        flag = False
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                flag = True
        n += 1
    return lst_obj


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


orig_list = [random.randint(-100, 100) for _ in range(10)]
print(f'Исходный массив {orig_list}')
print(f'Отсортированный по убыванию {bubble_sort_rework(orig_list[:])}')

# замеры 10
print('10')
print(
    timeit.timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "bubble_sort_rework(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.randint(-100, 100) for _ in range(100)]

# замеры 100 bubble_sort
print('100')
print(
    timeit.timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "bubble_sort_rework(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.randint(-100, 100) for _ in range(1000)]

# замеры 1000 bubble_sort
print('1000')
print(
    timeit.timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "bubble_sort_rework(orig_list[:])",
        globals=globals(),
        number=1000))
"""
10
0.0371166 - bubble_sort
0.03600299999999999 - bubble_sort_rework
100
1.8266663 - bubble_sort
1.7164565 - bubble_sort_rework
1000
190.3076528 - bubble_sort
187.019931 - bubble_sort_rework

В bubble_sort_rework если массив уже отсортирован и за проход по нему не призошло ни одной 
сортировки, то функция завершает работу
Значительной экономии времени данная оптимизация не дает так как при массиве случайных чисел
шанс получить упорядоченный массив крайне мал.
Поскольку сложность данных алгоритмов О(n^2) то при увеличении исходного массива скорость 
выполения растет очень быстро, алгоритм неэффективен.

"""