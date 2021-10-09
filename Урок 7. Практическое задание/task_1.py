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

import timeit
import random

orig_list_10 = [random.randint(-100, 100) for _ in range(10)]
orig_list_100 = [random.randint(-100, 100) for _ in range(100)]
orig_list_1000 = [random.randint(-100, 100) for _ in range(1000)]

orig_list_10000000_rev = [sorted(list(range(10000000)), reverse=True)]


def bubble_sort_v1(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - 1):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_v2(lst_obj):
    n = 1
    while n < len(lst_obj):
        check = 0
        for i in range(len(lst_obj) - 1):
            if lst_obj[i] < lst_obj[i + 1]:
                check += 1
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        if check == 0:
            break
        n += 1
    return lst_obj


def bubble_sort_v3(lst_obj):
    n = 1
    while n < len(lst_obj):
        check = 0
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                check += 1
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        if check == 0:
            break
        n += 1
    return lst_obj


print(
    timeit.timeit(
        "bubble_sort_v1(orig_list_10[:])",
        globals=globals(),
        number=1000))

# замеры 100
print(
    timeit.timeit(
        "bubble_sort_v1(orig_list_100[:])",
        globals=globals(),
        number=1000))

# замеры 1000
print(
    timeit.timeit(
        "bubble_sort_v1(orig_list_1000[:])",
        globals=globals(),
        number=1000))
'''''
0.00765110  на 10 элементов
0.60052849  на 100 элементов
72.7954015  на 1000 элементов
'''''

print(
    timeit.timeit(
        "bubble_sort_v2(orig_list_10[:])",
        globals=globals(),
        number=1000))


# замеры 100
print(
    timeit.timeit(
        "bubble_sort_v2(orig_list_100[:])",
        globals=globals(),
        number=1000))


# замеры 1000
print(
    timeit.timeit(
        "bubble_sort_v2(orig_list_1000[:])",
        globals=globals(),
        number=1000))
'''''
0.00522010  на 10 элементов
0.5844475  на 100 элементов
74.1844878  на 1000 элементов
'''''

print(
    timeit.timeit(
        "bubble_sort_v3(orig_list_10[:])",
        globals=globals(),
        number=1000))


# замеры 100
print(
    timeit.timeit(
        "bubble_sort_v3(orig_list_100[:])",
        globals=globals(),
        number=1000))


# замеры 1000
print(
    timeit.timeit(
        "bubble_sort_v3(orig_list_1000[:])",
        globals=globals(),
        number=1000))
'''''
0.0067294  на 10 элементов
0.45787560  на 100 элементов
48.2702016  на 1000 элементов
'''''

# замеры работы алгоритмов с уже отсортированным списком из 10 000 000 элементов.
print(
   timeit.timeit(
       "bubble_sort_v1(orig_list_10000000_rev[:])",
       globals=globals(),
       number=1000))

print(
   timeit.timeit(
       "bubble_sort_v2(orig_list_10000000_rev[:])",
       globals=globals(),
       number=1000))

print(
   timeit.timeit(
       "bubble_sort_v3(orig_list_10000000_rev[:])",
       globals=globals(),
       number=1000))
'''''
0.000145190  1 функ на отсортированный список 10 000 000 элементов
0.000144800  2 функ на отсортированный список 10 000 000 элементов
0.000147100  3 функ на отсортированный список 10 000 000 элементов
'''''


'''''
Вывод: 
В первой версии "сортировки пузырьком" (bubble_sort_v1)  по убыванию алгоритм работает по принципу:
берет элемент, и если следующий по индексу элемент больше его, то меняет элементы местами. Таким образом, 
рано или поздно, в прицел попадает самый минимальный элемент массива, и по ходу цикла for премещается в правый край.
Этот алгоритм довольно долгий,на сотрироку 1000 элементов уходит около 72 секунд. 
Во второй версии (bubble_sort_v2) добавлено одно улучшение: проверка на необходимость дальнейших итераций цикла
while. Если во время исполнения цикла for не было зафиксировано ни одного перемещения, это может означать одно -
список уже полностью отсортирован, дальнейшего смысла в работе алгоритма нет. Однако это совершенно не ускоряет работу
программы, чтобы убедиться в этом, я провел дополнительные замеры с уже отсортированным списком на 10 000 000 элементов.
Вручную установленный выход из цикла не играет существенной роли, так как проход цикла for 1го алгоритма по уже отсортированному 
списку занимает тысячные доли секунды.
В третей версии (bubble_sort_v3) изменен принцип работы цикла for. За первый цикл самое минимальное число всегда занимает
крайнюю правую позицию. Теперь нет смысла обходить весь массив целиком, поэтому можно ограничить предел на единицу. В 
следующую итерацию, второе минимально, либо раное первому число займет крайнюю правую позицию и тд. N-ое число будет 
занимать N позицию от правого края. Зная это, нет смысла заставлять цикл проходить в последующих итерациях по всему 
массиву. Скорость работы алгоритма с таким ограничением сильно отличается от (bubble_sort_v1) и (bubble_sort_v2):
74 секунды против 48 секунд.
'''''
