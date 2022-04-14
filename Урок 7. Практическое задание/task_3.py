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



from statistics import median
import timeit
import random


def shell(data):
    inc = len(data) // 2
    while inc:
        for i, el in enumerate(data):
            while i >= inc and data[i - inc] > el:
                data[i] = data[i - inc]
                i -= inc
            data[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    return data


def gnome(data):
    i, size = 1, len(data)
    while i < size:
        if data[i - 1] <= data[i]:
            i += 1
        else:
            data[i - 1], data[i] = data[i], data[i - 1]
            if i > 1:
                i -= 1
    return data


def heapify(nums, heap_size, root_index):
    # Индекс наибольшего элемента считается корневым индексом
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    # Если левый потомок корня — это допустимый индекс, а элемент больше,
    # чем текущий наибольший, то мы обновляем наибольший элемент
    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    # То же самое и для правого потомка корня
    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    # Если наибольший элемент уже не корневой, они меняются местами
    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        heapify(nums, heap_size, largest)

def heap_sort(nums):
    n = len(nums)

    # Создаём Max Heap из списка
    # 2-й аргумент означает остановку алгоритма перед элементом -1, то есть
    # перед первым элементом списка
    # 3-й аргумент означает повторный проход по списку в обратном направлении,
    # уменьшая счётчик i на 1
    for i in range(n, -1, -1):
        heapify(nums, n, i)

    # Перемещаем корень Max Heap в самый конец списка
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)

"""
Тут пока что для меня мощное колдунство 
"""
def quickselect_median(l, pivot_fn=random.choice):
    if len(l) % 2 == 1:
        return quickselect(l, len(l) / 2, pivot_fn)
    else:
        return 0.5 * (quickselect(l, len(l) / 2 - 1, pivot_fn) +
                      quickselect(l, len(l) / 2, pivot_fn))


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


m = int(input('Число элементов массива 2m+1, введите m: '))
orig_list = [random.randint(1, 1000) for _ in range(2*m+1)]

print(f'Через statistics.median: '
      f'{timeit.timeit("median(orig_list[:])", globals=globals(), number=1000)}\n'
      f'Медиана {median(orig_list)}\n')

print(f'Через сортировку Шелла: '
      f'{timeit.timeit("shell(orig_list[:])", globals=globals(), number=1000)}\n'
      f'Медиана {shell(orig_list[:])[m]}\n')

print(f'Через сортировку Гномью: '
      f'{timeit.timeit("gnome(orig_list[:])", globals=globals(), number=1000)}\n'
      f'Медиана {gnome(orig_list[:])[m]}\n')

print(f'Через сортировку Кучей: '
      f'{timeit.timeit("heap_sort(orig_list[:])", globals=globals(), number=1000)}\n')
new_list = orig_list.copy()
heap_sort(new_list)
print(f'Медиана {new_list[m]}\n')

print(f'Через алгоритм деления списка: '
      f'{timeit.timeit("quickselect_median(orig_list[:])", globals=globals(), number=1000)}\n'
      f'Медиана {quickselect_median(orig_list[:])}\n')

"""
Аналитика:
Число элементов массива 2m+1, введите m: 999
Через statistics.median: 0.21788469999999993
Медиана 518
Через сортировку Шелла: 4.6542225
Медиана 518
Через сортировку Гномью: 385.97015369999997
Медиана 499
Через сортировку Кучей: 8.2476057
Медиана 518
Через алгоритм деления списка: 0.9118621000000005
Медиана 518
Поиск с помощью рекурисвных методов гораздо эффективнее. Отдельно "удивила" Гномья сортировка.
"""