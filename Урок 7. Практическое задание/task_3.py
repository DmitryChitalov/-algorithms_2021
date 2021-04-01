"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные по длине части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, Кучей...

[5, 3, 4, 3, 3, 3, 3]

[3, 3, 3, 3, 3, 4, 5]

my_lst
new_lts

arr[m]


from statistics import median

[3, 4, 3, 3, 5, 3, 3]


left.clear()
right.clear()


m = 3
len = 7
i
left = []
right = []

left == right and

for i in
    for
    left == right
    left.clear()
    right.clear()


"""
import sys
import random
from statistics import median
import timeit
m = int(input('Введите размер массива'))
unsorted_list = [random.randint(-100, 100) for _ in range(2 * m + 1)]

sys.setrecursionlimit(1000000)


def quickselect_median(list_, pivot_fn=random.choice):
    if len(list_) % 2 == 1:
        return quickselect(list_, int(len(list_) / 2), pivot_fn)
    else:
        return 0.5 * (quickselect(list_, len(list_) / 2 - 1, pivot_fn) +
                      quickselect(list_, len(list_) / 2, pivot_fn))


def quickselect(list_1, k, pivot_fn):
    """
    Выбираем k-тый элемент в списке l (с нулевой базой)
    :param list_1: список числовых данных
    :param k: индекс
    :param pivot_fn: функция выбора pivot, по умолчанию выбирает случайно
    :return: k-тый элемент l
    """
    if len(list_1) == 1:
        assert k == 0
        return list_1[0]

    pivot = pivot_fn(list_1)

    lows = [el for el in list_1 if el < pivot]
    highs = [el for el in list_1 if el > pivot]
    pivots = [el for el in list_1 if el == pivot]

    if k < len(lows):
        return quickselect(lows, k, pivot_fn)
    elif k < len(lows) + len(pivots):
        # Нам повезло и мы угадали медиану
        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots), pivot_fn)


print(quickselect_median(unsorted_list[:]))
print(median(unsorted_list[:]))
print(timeit.timeit('quickselect_median(unsorted_list[:])', globals=globals(), number=100))
'''Сортировка кучей'''


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    for i in range(n-1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


heap_sort(unsorted_list)
print(unsorted_list)
print(f'median array is {unsorted_list[int(len(unsorted_list) / 2)]}')
print(timeit.timeit('heap_sort(unsorted_list[:])', globals=globals(), number=100))
# arr = [1, 2, 3, 4, 5, 6]
# for el in range(len(arr) - 1, 0, -1):
#     print(arr[el])
'''Скорость первого алгоритма поиска выше, чем во втором т.к. по сути в нём не происходит сортировки массива,
берётся основное рандомное число, и искомое. Элементы исходного списка раскидываются по спискам, исходя из условия :
в lows добавляются элементы меньше опорного элемента, в highs добавляются элементы больше опорного элемента. Далее мы
рекурсивно вызываем функцию, пока k не станет больше, чем длина lows но меньше, чем сумма длин меньшего списка и списка 
с числами, равными опорному или пока длина списка не будет равна единице.
Второй алгоритм похож на сортировку вставками, где мы ищем больший элемент и переносим его в конец. Он работает 
медленнее т.к. мы рекурсивно два раза прогоняем список, чтобы его отсортировать, и только потом ищем медиану.'''
