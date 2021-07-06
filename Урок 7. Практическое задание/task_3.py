"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные по длине части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, Кучей...

[5, 3, 4, 3, 3, 3, 3]

[3, 3, 3, 3, 3, 4, 5]

my_lst
new_lts

arr[m]


from statistics import median

[3, 4, 3, 3, 5, 3, 3]

left = []
right = []

left == right and

for i in
    for
    left == right
    left.clear()
    right.clear()


"""

import random


def var_1(data, m):
    """
    Использование встроенного алгоритма
    """
    data.sort()
    return data[m]


def var_2(data):
    """
    Без сортировки (нашел с помощью Гугл) )
    """

    def quickselect_median(l, pivot_fn=random.choice):
        if len(l) % 2 == 1:
            return quickselect(l, len(l) / 2, pivot_fn)
        else:
            return 0.5 * (quickselect(l, len(l) / 2 - 1, pivot_fn) +
                          quickselect(l, len(l) / 2, pivot_fn))

    def quickselect(l, k, pivot_fn):
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
            return pivots[0]
        else:
            return quickselect(highs, k - len(lows) - len(pivots), pivot_fn)

    return quickselect_median(data)


def var_3(data, m):
    """
    С помощью сортировки кучей
    """

    def HeapSort(data):
        for start in range(int((len(data) - 2) / 2), -1, -1):
            HeapSift(data, start, len(data) - 1)

        for end in range(len(data) - 1, 0, -1):
            data[end], data[0] = data[0], data[end]
            HeapSift(data, 0, end - 1)
        return data

    def HeapSift(data, start, end):
        root = start

        while True:

            child = root * 2 + 1
            if child > end: break

            if child + 1 <= end and data[child] < data[child + 1]:
                child += 1

            if data[root] < data[child]:
                data[root], data[child] = data[child], data[root]
                root = child
            else:
                break

    return HeapSort(data)[m]


m = int(input('Введите число m: '))
nums = [random.randint(0, 100) for _ in range(2 * m + 1)]
print(f'Исходный массив: {nums}')
print()
print(f'Медиана - первый способ: {var_1(nums[:], m)}')
print(f'Медиана - второй способ: {var_2(nums[:])}')
print(f'Медиана - третий способ: {var_3(nums[:], m)}')
