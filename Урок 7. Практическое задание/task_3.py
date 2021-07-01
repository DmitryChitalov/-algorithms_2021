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

"""Создадим массив по формуле 2m+1 и проверим медиану через статистику"""

from timeit import timeit
from statistics import median
from random import randint
m = 6
arr1 = [randint(0, 10) for _ in range(2 * m + 1)]
print(arr1)

arr = arr1.copy()
print(median(arr))

"""
[4, 7, 0, 7, 0, 0, 10, 5, 3, 0, 1, 2, 5]
3

Получили ответ 3, это правильно. К этому будем стремиться.
И сделаем эталонный замер для сравнения.

"""
print('Медиана через сортировку statistics.median: ', end='')
print(median(arr))
print(timeit('median(arr)', globals=globals(), number=1000))

"""

Теперь найдем медиану через механизм сортировки.
В условии сказано что можно использовать Шелла, Гномья, Кучей...
Для меня они все одинаковые, поэтому берем первый из списка - Шелла
"""


def shell(data):
    data_copy = data.copy()
    inc = len(data_copy) // 2
    while inc:
        for i, el in enumerate(data_copy):
            while i >= inc and data_copy[i - inc] > el:
                data_copy[i] = data_copy[i - inc]
                i -= inc
            data_copy[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    return data_copy[int((len(data_copy)-1)/2)]


print('Медиана через сортировку Шелла: ', end='')
print(shell(arr))
print(timeit('shell(arr)', globals=globals(), number=1000))

"""Можно через гнома попробовать"""


def gnome(data):
    data_copy = data.copy()
    i, size = 1, len(data_copy)
    while i < size:
        if data_copy[i - 1] <= data_copy[i]:
            i += 1
        else:
            data_copy[i - 1], data_copy[i] = data_copy[i], data_copy[i - 1]
            if i > 1:
                i -= 1
    return data_copy[int((len(data_copy)-1)/2)]


print('Медиана через сортировку Гнома: ', end='')
print(gnome(arr))
print(timeit('gnome(arr)', globals=globals(), number=1000))

"""Решаем задачу через удаление максимальных значений"""


def max_el_delete(arr):
    arr_copy = arr.copy()
    for i in range(int((len(arr_copy)-1)/2)):
        arr_copy.pop(arr_copy.index(max(arr_copy)))
    return max(arr_copy)


print('Медиана через удаление максимальных значений: ', end='')
print(max_el_delete(arr))
print(timeit('max_el_delete(arr)', globals=globals(), number=1000))

"""
Реализуем последний механизм сравнением лева с правом
"""


# def left_right_compare(arr):
#     arr_copy = arr.copy()
#     left = []
#     right = []
#     for i in range(int((len(arr_copy)-1)/2)):
#         left.append(min(arr_copy))
#         right.append(max(arr_copy))
#         arr_copy.pop(arr_copy.index(left[-1]))
#         arr_copy.pop(arr_copy.index(right[-1]))

"""Здесь у меня не получилось придумать, я не понял как наполнять
элементами, их количество всегда равно"""

"""
ИТОГ:

[4, 1, 3, 2, 7, 0, 0, 4, 5, 4, 5, 1, 0]
3
Медиана через сортировку statistics.median: 3
0.0006458999999999979
Медиана через сортировку Шелла: 3
0.011745000000000005
Медиана через сортировку Гнома: 3
0.020375199999999996
Медиана через удаление максимальных значений: 3
0.003926100000000002

Все механизмы рабочие. Естественно самый быстрый - встроенный. Ему я отдам предпочтение,
с остальными - было интересно поизучать.
"""