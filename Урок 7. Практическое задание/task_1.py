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
from random import randrange
from timeit import repeat


def bubble_sort(array, ascending=True):
    for i in range(len(array)):
        for j in range(1, len(array) - i):
            if (ascending and array[j - 1] > array[j]) or (not ascending and array[j - 1] < array[j]):
                array[j], array[j - 1] = array[j - 1], array[j]
    return array


def bubble_sort_v2(array, ascending=True):
    for i in range(len(array) - 1):
        stop = len(array) - i - 1
        for j in range(stop):
            if (ascending and array[j] > array[stop]) or (not ascending and array[j] < array[stop]):
                array[j], array[stop] = array[stop], array[j]
    return array


if __name__ == '__main__':
    SIZE = 100
    arr = [randrange(-100, 100) for _ in range(SIZE)]
    print(arr)
    print(bubble_sort(arr[:], False))
    print(bubble_sort_v2(arr[:], False))

    print(f"Execution time of bubble_sort is "
          f"{min(repeat('bubble_sort(arr[:], False)', repeat=3, number=1000, globals=globals()))}")

    print(f"Execution time of bubble_sort_v2 is "
          f"{min(repeat('bubble_sort_v2(arr[:], False)', repeat=3, number=1000, globals=globals()))}")

    # Execution time of bubble_sort is 0.486086
    # Execution time of bubble_sort_v2 is 0.32046129999999984
    # Отказавшись от проверки всего массива каждый раз, пробегая вместо этого только по не сортированной части массива,
    # мы уменьшили количество операций, что привело к заметному приросту скорости сортировки.
