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



def vector_gen(count):
    return [randint(-100, 100) for i in range(count)]


def bubble_sort(vector):
    count = 1
    while count < len(vector):
        for i in range(len(vector) - count):
            if vector[i] < vector[i + 1]:
                vector[i], vector[i + 1] = vector[i + 1], vector[i]
        count += 1
    return vector


def bubble_sort_mod(vector):
    count = 1
    complete = True
    while count < len(vector):
        for i in range(len(vector) - count):
            if vector[i] < vector[i + 1]:
                vector[i], vector[i + 1] = vector[i + 1], vector[i]
                complete = False
        count += 1
        if complete:
            break
    return vector


low_vector = bubble_sort(vector_gen(10))
mid_vector = bubble_sort(vector_gen(100))
top_vector = bubble_sort(vector_gen(1000))

print(
    timeit("bubble_sort(low_vector)",
           globals=globals(),
           number=1000))
print(
    timeit("bubble_sort(mid_vector)",
           globals=globals(),
           number=1000))
print(
    timeit("bubble_sort(top_vector)",
           globals=globals(),
           number=1000))


print(
    timeit("bubble_sort_mod(low_vector)",
           globals=globals(),
           number=1000))
print(
    timeit("bubble_sort_mod(mid_vector)",
           globals=globals(),
           number=1000))
print(
    timeit("bubble_sort_mod(top_vector)",
           globals=globals(),
           number=1000))


# print(bubble_sort(low_vector))
# print(bubble_sort(mid_vector))
# print(bubble_sort(top_vector))
# print(bubble_sort_mod(low_vector))
# print(bubble_sort_mod(mid_vector))
# print(bubble_sort_mod(top_vector))



"""
Замеры оригинальной функции:
10 элементов:   0.008328200000000008
100 элементов:  0.5882072
1000 элементов: 59.736061299999996
Замеры улучшенной функции:
10 элементов:   0.0014275999999995292
100 элементов:  0.011245999999999867
1000 элементов: 0.12454710000000091

Уменьшение времени работы получено за счет уменьшения количества 
итераций прохода по списку. Т.е. нет необходимости отрабатывать условия цикла,
когда элементы отсортированы. Достигается это проверкой на отсутствие замен
элементов в списке после каждой итерации.
"""

