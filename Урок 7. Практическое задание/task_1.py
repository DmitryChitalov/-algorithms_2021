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

numbers_10 = [randint(-100, 100) for _ in range(10)]
numbers_100 = [randint(-100, 100) for _ in range(100)]
numbers_1000 = [randint(-100, 100) for _ in range(1000)]


def bubble_sort_reverse(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


print(bubble_sort_reverse(numbers_10[:]))
print(bubble_sort_reverse(numbers_100[:]))
print(bubble_sort_reverse(numbers_1000[:]))

print(timeit('bubble_sort_reverse(numbers_10[:])',
             globals=globals(),
             number=1000))

print(timeit('bubble_sort_reverse(numbers_100[:])',
             globals=globals(),
             number=1000))

print(timeit('bubble_sort_reverse(numbers_1000[:])',
             globals=globals(),
             number=1000))


# улучшенный вариант
def bubble_sort_reverse_1(lst_obj):
    n = 1
    while n < len(lst_obj):
        is_moved = False
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                is_moved = True
        if not is_moved:
            break
        n += 1
    return lst_obj


print(bubble_sort_reverse_1(numbers_10[:]))
print(bubble_sort_reverse_1(numbers_100[:]))
print(bubble_sort_reverse_1(numbers_1000[:]))

print(timeit('bubble_sort_reverse_1(numbers_10[:])',
             globals=globals(),
             number=1000))

print(timeit('bubble_sort_reverse_1(numbers_100[:])',
             globals=globals(),
             number=1000))

print(timeit('bubble_sort_reverse_1(numbers_1000[:])',
             globals=globals(),
             number=1000))

"""
Такое улучшение, как завершение цикла, если при проходе не было совершено ни одной перестановки, смысла вообще не имеет,
если на малых объемах данных еще заметно какое-то улучшение, то на больших имеется замедление работы. Видимо это происходит
из-за увеличения количества операций в цикле. 
А смысла нет потому, что помимо увеличения времени работы функции вероятность завершения сортировки ранее, чем 
она бы завершилась без такого улучшения, очень мала.
"""
