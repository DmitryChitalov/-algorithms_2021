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
from random import randint
from timeit import timeit


ARR = [randint(-100, 99) for _ in range(10)]
ARR1 = [randint(-100, 99) for _ in range(10)]

def bubble_sort_reverse(arr):
    for i in range(1, len(arr) - 1):
        already_sorted = True
        for j in range(len(arr) - 1, -1 + i, -1):
            if arr[j] > arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                already_sorted = False
        if already_sorted:
            return arr
    return arr


def bubble_non_flagged(arr):
    for i in range(1, len(arr) - 1):
        for j in range(len(arr) - 1, -1 + i, -1):
            if arr[j] > arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
    return arr


print(ARR)
print(bubble_sort_reverse(ARR))

print(timeit("bubble_sort_reverse(ARR)", globals=globals()))    # 0.7598002
print(timeit("bubble_non_flagged(ARR1)", globals=globals()))     # 3.5343288000000004
"""
Даже на таком небольшом массиве мы видим, что установка флага позволяет ускорить сортировку в 5 раз.
Если увеличить количество элементов массива до 100 и не изменять параметр 'number' функции timeit, 
то можно будет смело отойти от компьюетра, так как функция без флага 'не видит', 
что массив уже был ею отсортирован и продолжает совершать обходы.
"""
