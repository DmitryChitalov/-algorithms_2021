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
import timeit
from random import randint
from statistics import median

m = int(input("Введите целое значение m: "))
some_lst = [randint(0, 100) for i in range(2*m+1)]


# Вариант решения с использование Шелл сортировки
def shl_sort(some_lst):
    step = int(len(some_lst)/2)
    while step:
        for i, el in enumerate(some_lst):
            while i >= step and some_lst[i - step] > el:
                some_lst[i] = some_lst[i - step]
                i -= step
            some_lst[i] = el
        step = 1 if step == 2 else int(step*5.0/11)
    return some_lst


# Вариант решения без сортировки с поиском максимального значения
# путём удаления максимальных значений до половины массива.
def rem_max_sort(some_lst):
    lst = some_lst
    for i in range(len(some_lst) // 2):
        lst.remove(max(lst))
    return max(lst)


# Выведем результаты работы функций - встроенной, Шелл и без сортировки
print(f"some_lst:\n {some_lst}")
print(f"some_lst с сортировкой Шелла:\n {shl_sort(some_lst[:])}")
'''
При m = 10:
some_lst:
 [71, 11, 83, 82, 39, 26, 77, 46, 52, 52, 70, 41, 28, 50, 47, 32, 66, 26, 55, 34, 53]
some_lst с сортировкой Шелла:
 [11, 26, 26, 28, 32, 34, 39, 41, 46, 47, 50, 52, 52, 53, 55, 66, 70, 71, 77, 82, 83]
'''
print(f'Медиана со встроенной функцией: {median(some_lst[:])}')
print(f"Медиана с Шелл сортировкой: {shl_sort(some_lst[:])[m]}")
print(f'Медиана без сортировки: {rem_max_sort(some_lst[:])}')
'''
Медиана со встроенной функцией: 50
Медиана с Шелл сортировкой: 50
Медиана без сортировки: 50
'''
# Проведём замеры скорости работы этих функций
print(f'Скорость встроенной функции:\n'
      f' {timeit.timeit("median(some_lst[:])", globals=globals(), number=1000)} сек.')
print(f'Скорость функции с Шелл сортировкой:\n'
      f' {timeit.timeit("shl_sort(some_lst[:])[m]", globals=globals(), number=1000)} сек.')
print(f'Скорость функции без сортировки:\n'
      f' {timeit.timeit("rem_max_sort(some_lst[:])", globals=globals(), number=1000)} сек.')
'''
Скорость встроенной функции:
 0.0008372000000000934 сек.
Скорость функции с Шелл сортировкой:
 0.01535069999999994 сек.
Скорость функции без сортировки:
 0.005530800000000058 сек.
Использование встроенных функций позволяет значительно выиграть в скорости.
'''
