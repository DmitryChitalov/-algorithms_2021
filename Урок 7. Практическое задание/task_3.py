"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные по длине части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, Кучей...

Важно: стройте массив именно по формуле 2m+1
Потому что параметр m вам пригодится при поиске медианы, когда массив будет отсортирован.
Этот парамет m вам нужно запрашивать у пользователя.

"""

import random, timeit
import statistics

"""Вариант без сортировки"""
def median(l, pivot_fn=random.choice):
    if len(l) % 2 == 1:
        return quickselect(l, len(l) // 2, pivot_fn)
    else:
        return 0.5 * (quickselect(l, len(l) // 2 - 1, pivot_fn) +
                      quickselect(l, len(l) // 2, pivot_fn))


def quickselect(l, k, pivot_fn):
    """
    Выбираем k-тый элемент в списке l (с нулевой базой)
    :param l: список числовых данных
    :param k: индекс
    :param pivot_fn: функция выбора pivot, по умолчанию выбирает случайно
    :return: k-тый элемент l
    """
    if len(l) == 1:
        assert k == 0
        return l[0]

    pivot = pivot_fn(l)

    lows = [el for el in l if el < pivot]
    highs = [el for el in l if el > pivot]
    pivots = [el for el in l if el == pivot]

    if k < len(lows):
        return quickselect(lows, k, pivot_fn)
    elif k < len(lows) + len(pivots):
        # Нам повезло и мы угадали медиану
        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots), pivot_fn)

"""Вариант со встроеннной функцией"""
def median_2(items):
    return statistics.median(items)

"""Вариант с сортировкой"""
def median_3(l):
    l = sorted(l)
    if len(l) % 2 == 1:
        return l[len(l) // 2]
    else:
        return 0.5 * (l[len(l) // 2 - 1] + l[len(l) // 2])

if __name__ == "__main__":

    n = int(input('Введите 1/2 размера массива: '))
    array = [random.randint(-100, 100) for _ in range(2 * n + 1)]

    print(f'Исходный массив {array}')

    """__________________Замеры времени выполнения____________________________"""

    print(f'Медиана вариант без сортировки: {median(array[:])}')
    for i in range(3):
        t = 100 ** (i + 1)  # Кол-во повторений замеров
                       # замеры выполняем на копии массива
        print(f'Результаты замеров на {t} повторений: '
              f'{timeit.timeit("median(array[:])", globals=globals(), number=t)}, сек.')

    print(f'Медиана варианта со встроеннной функцией: {median_2(array[:])}')
    for i in range(3):
        t = 100 ** (i + 1)  # Кол-во повторений замеров
                        # замеры выполняем на копии массива
        print(f'Результаты замеров на {t} повторений: '
              f'{timeit.timeit("median_2(array[:])", globals=globals(), number=t)}, сек.')

    print(f'Медиана варианта с сортировкой: {median_3(array[:])}')
    for i in range(3):
        t = 100 ** (i + 1)  # Кол-во повторений замеров
               # замеры выполняем на копии массива
        print(f'Результаты замеров на {t} повторений: '
              f'{timeit.timeit("median_3(array[:])", globals=globals(), number=t)}, сек.')
    del array

""" 
Вариант со встроенной функцией и сортировкой самый быстрый:
    Введите 1/2 размера массива: 5
Исходный массив [-37, -4, 39, 58, 57, -6, -14, 45, 10, 77, -91]
Медиана вариант без сортировки: 10
Результаты замеров на 100 повторений: 0.0013312000000000879, сек.
Результаты замеров на 10000 повторений: 0.11187900000000006, сек.
Результаты замеров на 1000000 повторений: 11.508643099999999, сек.
Медиана варианта со встроеннной функцией: 10
Результаты замеров на 100 повторений: 8.920000000145478e-05, сек.
Результаты замеров на 10000 повторений: 0.008629899999998969, сек.
Результаты замеров на 1000000 повторений: 0.8754070999999968, сек.
Медиана варианта с сортировкой: 10
Результаты замеров на 100 повторений: 7.349999999917145e-05, сек.
Результаты замеров на 10000 повторений: 0.007096799999999348, сек.
Результаты замеров на 1000000 повторений: 0.7246062999999978, сек.
"""