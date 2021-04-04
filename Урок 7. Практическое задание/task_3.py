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

from statistics import median
from random import randint
from timeit import timeit


def gnome_sort(lst):
    i, size = 1, len(lst)
    m = size // 2

    while i < size:
        if lst[i - 1] <= lst[i]:
            i += 1
        else:
            lst[i - 1], lst[i] = lst[i], lst[i - 1]
            if i > 1:
                i -= 1
    return lst[m]


def my_sort(lst):
    left_part = sorted(lst[:int((len(lst) - 1) / 2)])[::-1]
    right_part = sorted(lst[int((len(lst) - 1) / 2):])[::-1]
    list_sort = []
    m = len(lst) // 2

    while len(right_part) > 0 or len(left_part) > 0:

        if len(right_part) > 0 and len(left_part) > 0:
            num_left = max(left_part)
            num_right = max(right_part)
        elif len(right_part) > 0 and len(left_part) == 0:
            list_sort.append(num_right)
            right_part.remove(num_right)
            break
        else:
            list_sort.append(num_left)
            left_part.remove(num_left)
            break
        if num_left > num_right:
            list_sort.append(num_left)
            left_part.remove(num_left)
        else:
            list_sort.append(num_right)
            right_part.remove(num_right)
    return list_sort[m]


list_pattern = [randint(-100, 100) for _ in range(11)]
print('Исходный список:', list_pattern)
print('Медиана гномья сортировка:', gnome_sort(list_pattern))
print('Медиана моей сортировкой:', my_sort(list_pattern))
print('Медиана функция median:', median(list_pattern))  # используем её для проверки алгоритма

'''
Пример выполнения на моём пк:
Исходный список: [53, -69, 95, 31, -95, 96, 89, 39, 73, 62, -51]
Медиана гномья сортировка: 53
Медиана моей сортировкой: 53
Медиана функция median: 53
'''

# замеры
print()

print('Замеры гномья сортировка медиана:')
print(timeit("gnome_sort(list_pattern[:])", globals=globals(), number=1000))
list_pattern = [randint(-100, 100) for _ in range(101)]
print(timeit("gnome_sort(list_pattern[:])", globals=globals(), number=1000))
list_pattern = [randint(-100, 100) for _ in range(1001)]
print(timeit("gnome_sort(list_pattern[:])", globals=globals(), number=1000))

print()

print('Замеры моя сортировка медиана')
list_pattern = [randint(-100, 100) for _ in range(11)]
print(timeit("my_sort(list_pattern[:])", globals=globals(), number=1000))
list_pattern = [randint(-100, 100) for _ in range(101)]
print(timeit("my_sort(list_pattern[:])", globals=globals(), number=1000))
list_pattern = [randint(-100, 100) for _ in range(1001)]
print(timeit("my_sort(list_pattern[:])", globals=globals(), number=1000))

print()

print('Замеры функция median:')
list_pattern = [randint(-100, 100) for _ in range(11)]
print(timeit("my_sort(list_pattern[:])", globals=globals(), number=1000))
list_pattern = [randint(-100, 100) for _ in range(101)]
print(timeit("my_sort(list_pattern[:])", globals=globals(), number=1000))
list_pattern = [randint(-100, 100) for _ in range(1001)]
print(timeit("my_sort(list_pattern[:])", globals=globals(), number=1000))


'''
Выводы самая быстрый способ найти медиану это функция median.
За ней идёт мой способ так как там много встроенных функций, которые оптимизированы
под скорость выполнения, но там также есть цикл while и условия if как и в гномей
сортировке. Я разделил список на две части и отсортировал их заранее это существенно
упростило задачу создания основного списка.
Гномья сортировка показала худший результат так как приходится долго ходить по списку
туда сюда для сортировки.

Замеры гномья сортировка медиана:
0.002637675999721978 - длина списка 11
0.7083280509978067 - длина списка 101
73.18516890700266 - длина списка 1001

Замеры моя сортировка медиана:
0.008998347002489027 - длина списка 11
0.11158112900011474 - длина списка 101
6.7622168229972885 - длина списка 1001

Замеры функция median:
0.008581285997934174
0.10721022600046126
6.356750579998334
'''
