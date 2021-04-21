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
from statistics import median
from random import uniform, randint
from memory_profiler import profile, memory_usage
from timeit import default_timer


def decor(func):
    """Функция декортатор для замеров времени и памяти"""

    def wrapper(*args, **kwargs):
        t1 = default_timer()
        m1 = memory_usage()
        res = func(args[0])
        m2 = memory_usage()
        t2 = default_timer()
        mem_diff = m2[0] - m1[0]
        time_dif = t2 - t1
        print(f'Функция - {func.__name__}\n Время заняло: {time_dif}\n Памяти заняло:{mem_diff}\n')
        return res

    return wrapper


def own_median(rand_list):
    """собственное решение через рекурсию,
    при каждом вызове из списка убираются максимальное и минимальное значение
    частное решение - остался один элемент в массиве, он и есть медиана"""
    if len(rand_list) == 1:
        return rand_list[0]
    else:
        rand_list.pop(rand_list.index(max(rand_list)))
        rand_list.pop(rand_list.index(min(rand_list)))
        return own_median(rand_list)

@decor
def call_median(rand_list):
    median(rand_list)

@decor
def call_own_median(rand_list):
    own_median(rand_list)

m = 10
rand_list = [randint(-50, 50) for i in range(2 * m + 1)]
print(f'Исходный лист - {rand_list}')
print(f'Результат функции median: {median(rand_list)}')
print(f'Результат функции own_median: {own_median(rand_list)}')

print('/*'*30+'\n')
print('Замеры 10:\n')
m = 10
rand_list = [randint(-50, 50) for i in range(2 * m + 1)]
call_median(rand_list)
call_own_median(rand_list)

print('/*'*30+'\n')
print('Замеры 100:\n')
m = 100
rand_list = [randint(-50, 50) for i in range(2 * m + 1)]
call_median(rand_list)
call_own_median(rand_list)

print('/*'*30+'\n')
print('Замеры 1000:\n')
sys.setrecursionlimit(1500)
m = 1000
rand_list = [randint(-50, 50) for i in range(2 * m + 1)]
call_median(rand_list)
call_own_median(rand_list)



"""
Исходный лист - [12, -35, -21, -50, 44, 16, -44, 29, 49, 50, 14, 28, 0, 47, -38, 26, 3, 27, -47, -10, 38]
Результат функции median: 14
Результат функции own_median: 14
/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*

Замеры 10:

Функция - call_median
 Время заняло: 0.2008077
 Памяти заняло:0.0078125

Функция - call_own_median
 Время заняло: 0.20146710000000007
 Памяти заняло:0.0

/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*

Замеры 100:

Функция - call_median
 Время заняло: 0.20080260000000005
 Памяти заняло:0.0

Функция - call_own_median
 Время заняло: 0.20110519999999998
 Памяти заняло:0.02734375

/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*

Замеры 1000:

Функция - call_median
 Время заняло: 0.20145639999999987
 Памяти заняло:0.015625

Функция - call_own_median
 Время заняло: 0.2821773999999999
 Памяти заняло:1.08984375

Замеры показывают что собственная функция через рекурсию начинает проигрывать во времени и памяти при
увеличении элементов массива
"""
