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
import random
from timeit import timeit


def bubble_sort_1(array):
    n = 1
    change = 0
    while n < len(array):
        for i in range(len(array) - n):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                change += 1
        n += 1
    return array


def bubble_sort_2(array):
    change = 0
    n = 1
    while n < len(array):
        for i in range(len(array) - n):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                change += 1
        n += 1
        if change == 0:
            break
    return array


def bubble_sort_3(array):
    change = 0
    n = 1
    while n < len(array):
        for i in range(len(array) - n - change):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                change += 1
        n += 1
        if change == 0:
            break
    return array


user_array = [random.randint(-100, 100) for num in range(100)]

print(bubble_sort_1(user_array[:]))
print(bubble_sort_1(user_array[:]))
print(bubble_sort_1(user_array[:]))

print(timeit('bubble_sort_1(user_array[:])', globals=globals(), number=1000))
print('-' * 100)
print(timeit('bubble_sort_2(user_array[:])', globals=globals(), number=1000))
print('-' * 100)
print(timeit('bubble_sort_3(user_array[:])', globals=globals(), number=1000))

"""
1-я Доработка заключалась в том что, если генерируется рандомный массив, он может сгенироваться не требуя сортировки
и тогда не проиходит перемещений элементо и цикл завершается. Разницы с исходным нет, кроме вышеупомянутого случая.
2-я доработка оказаласть самой быстрой, за счет снижения кол-ва итерация в цикле

Исходная сортировка:  
0.8950947
----------------------------------------------------------------------------------------------------
1-я доработка сортировка: 
0.8128563999999999
----------------------------------------------------------------------------------------------------
2-я доработка сортировка: 
0.04944609999999994

"""