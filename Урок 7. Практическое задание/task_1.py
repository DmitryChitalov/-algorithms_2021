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

from random import randint
from timeit import timeit


def bubble_sort1(my_list):
    n = 1
    while n < len(my_list):
        for i in range(len(my_list) - n):
            if my_list[i] < my_list[i + 1]:
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
        n += 1
    return my_list


def bubble_sort2(my_list):
    n = 1
    while n < len(my_list):
        was_sorted = False
        for i in range(len(my_list) - n):
            if my_list[i] < my_list[i + 1]:
                was_sorted = True
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
        if was_sorted == False:
            break
        n += 1
    return my_list


rand_list = [randint(-100, 100) for _ in range(10)]

print(rand_list)
print(bubble_sort1(rand_list[:]))
print(bubble_sort2(rand_list[:]))

# замеряем на массиве из 10 элементов
print(timeit("bubble_sort1(rand_list[:])", globals=globals(), number=1000))
print(timeit("bubble_sort2(rand_list[:])", globals=globals(), number=1000))

# замеряем на массиве из 100 элементов
rand_list = [randint(-100, 100) for _ in range(100)]
print(timeit("bubble_sort1(rand_list[:])", globals=globals(), number=1000))
print(timeit("bubble_sort2(rand_list[:])", globals=globals(), number=1000))

# замеряем на массиве из 1000 элементов
rand_list = [randint(-100, 100) for _ in range(1000)]
print(timeit("bubble_sort1(rand_list[:])", globals=globals(), number=1000))
print(timeit("bubble_sort2(rand_list[:])", globals=globals(), number=1000))

"""
Алгоритм сортировки "пузырьком" был доработан - если во внутреннем цикле не выполняется ни одной перестановки, 
это означает, что список полностью отсортирован и проводить последующие итерации с n+1 до последнего элемента
не имеет смысла. Для проверки во внутреннем цикле используется флаг.
Результаты замеров ниже показывают, что чем больше диапазон массива, тем существеннее разница во времени выполнения
оптимизированного алгоритма.

Результаты замеров первоначальной функции и функции после оптимизации:

10 элементов:
0.017633813999999998
0.018519571999999998

100 элементов:
1.341438467
1.2773276610000002

1000 элементов:
153.247725018
152.23674889699998
"""