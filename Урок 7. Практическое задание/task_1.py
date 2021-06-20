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

# Доработка выполнена, если оставшийся после предыдущего прохода массив случайным образом оказался отсортированным
# в нужном порядке, код апгрейд работает. Правда при значительной длине начального массива, вероятность срабатывания
# нашего флага на начальных шагах около 0. Есть шанс, что оставшийся мелкий кусочек после n-го прохода будет уже
# отсортирован, но это уже значительного по времени выигрыша уже не даст. С ростом n длина цикла for сокращается

from random import randint
from timeit import timeit

def buble(my_array):
    n = 1
    while n < len(my_array):
        for i in range(len(my_array) - n):
            if my_array[i] < my_array[i+1]:
                my_array[i], my_array[i+1] = my_array[i+1], my_array[i]
        n += 1
    return my_array


def buble_upgraded(my_array):
    n = 1
    is_modified = True
    while is_modified and n < len(my_array):
        is_modified = False
        for i in range(len(my_array) - n):
            if my_array[i] < my_array[i+1]:
                my_array[i], my_array[i+1] = my_array[i+1], my_array[i]
                is_modified = True
        n += 1
    return my_array


my_array = [randint(-100, 100) for _ in range(200)] # произвольный массив
# my_array = [i for i in range(200, 1, -1)]  # отсортированный по убыванию массив
# print(buble(my_array[:]))
# print(buble_upgraded(my_array[:]))
print(timeit("buble(my_array[:])", globals=globals(), number=10))
print(timeit("buble_upgraded(my_array[:])", globals=globals(), number=10))
print(timeit("buble(my_array[:])", globals=globals(), number=100))
print(timeit("buble_upgraded(my_array[:])", globals=globals(), number=100))
print(timeit("buble(my_array[:])", globals=globals(), number=1000))
print(timeit("buble_upgraded(my_array[:])", globals=globals(), number=1000))

