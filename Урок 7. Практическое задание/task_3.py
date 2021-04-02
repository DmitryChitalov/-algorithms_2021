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
from random import randint
from timeit import timeit
from memory_profiler import profile
from statistics import median


def gnome_median(nums):
    def gnome(data):
        i, j, size = 1, 2, len(data)
        while i < size:
            if data[i - 1] <= data[i]:
                i, j = j, j + 1
            else:
                data[i - 1], data[i] = data[i], data[i - 1]
                i -= 1
                if i == 0:
                    i, j = j, j + 1
        return data

    n = len(nums)

    if n < 1:
        return None
    if n % 2 == 1:
        return gnome(nums)[n // 2]
    else:
        return sum(gnome(nums)[n // 2 - 1:n // 2 + 1]) / 2.0


# c использованием встроенной функции сортировки
def median_sort(lst):
    n = len(lst)
    if n < 1:
        return None
    if n % 2 == 1:
        return sorted(lst)[n // 2]
    else:
        return sum(sorted(lst)[n // 2 - 1:n // 2 + 1]) / 2.0


@profile
def test_gnome_median(data):
    return gnome_median(data)


@profile
def test_median_sort(data):
    return median_sort(data)


@profile
def test_statistics_median(data):
    return median(data)


lists = [randint(-100, 100) for _ in range(100)]
print(f'Метод сортировки "Гномья"\n'
      f'100 элементов, выполняем 1000 раз: {timeit("gnome_median(lists[:])", globals=globals(), number=1000)}\n'
      f'Элемент: {gnome_median(lists)}')
print('=' * 70)
print(f'Метод сортировки "C использованием встроенных функции сортировки"\n'
      f'100 элементов, выполняем 1000 раз: {timeit("median_sort(lists[:])", globals=globals(), number=1000)}\n'
      f'Элемент: {median_sort(lists)}')
print('=' * 70)
print(f'Метод сортировки "ПРОВЕРКА, функция из модуля"\n'
      f'100 элементов, выполняем 1000 раз: {timeit("median(lists[:])", globals=globals(), number=1000)}\n'
      f'Элемент: {median(lists)}')

print('=' * 70)
print('=' * 70)

lists_1000 = [randint(-100, 100) for _ in range(1000)]
print(f'Метод сортировки "Гномья"\n'
      f'1000 элементов, выполняем 1000 раз: {timeit("gnome_median(lists_1000[:])", globals=globals(), number=1000)}\n'
      f'Элемент: {gnome_median(lists_1000)}')
print('=' * 70)
print(f'Метод сортировки "C использованием встроенных функции сортировки"\n'
      f'1000 элементов, выполняем 1000 раз: {timeit("median_sort(lists_1000[:])", globals=globals(), number=1000)}\n'
      f'Элемент: {median_sort(lists_1000)}')
print('=' * 70)
print(f'Метод сортировки "ПРОВЕРКА, функция из модуля"\n'
      f'1000 элементов, выполняем 1000 раз: {timeit("median(lists_1000[:])", globals=globals(), number=1000)}\n'
      f'Элемент: {median(lists_1000)}')

test_gnome_median(lists)
test_median_sort(lists)
test_statistics_median(lists)
print('*' * 100)
test_gnome_median(lists_1000)
test_median_sort(lists_1000)
test_statistics_median(lists_1000)

"""
Метод сортировки "Гномья"
100 элементов, выполняем 1000 раз: 0.43196310000000004
Элемент: 8.5
======================================================================
Метод сортировки "C использованием встроенных функции сортировки"
100 элементов, выполняем 1000 раз: 0.0014913000000000842
Элемент: 8.5
======================================================================
Метод сортировки "ПРОВЕРКА, функция из модуля"
100 элементов, выполняем 1000 раз: 0.0012088000000000099
Элемент: 8.5
======================================================================
======================================================================
Метод сортировки "Гномья"
1000 элементов, выполняем 1000 раз: 52.007930699999996
Элемент: 2.0
======================================================================
Метод сортировки "C использованием встроенных функции сортировки"
1000 элементов, выполняем 1000 раз: 0.00799400000000361
Элемент: 2.0
======================================================================
Метод сортировки "ПРОВЕРКА, функция из модуля"
1000 элементов, выполняем 1000 раз: 0.0077920000000020195
Элемент: 2.0

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    88     20.0 MiB     20.0 MiB           1   @profile
    89                                         def test_gnome_median(data):
    90     20.0 MiB      0.0 MiB           1       return gnome_median(data)
    
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    93     20.0 MiB     20.0 MiB           1   @profile
    94                                         def test_median_sort(data):
    95     20.0 MiB      0.0 MiB           1       return median_sort(data)

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    98     20.0 MiB     20.0 MiB           1   @profile
    99                                         def test_statistics_median(data):
   100     20.0 MiB      0.0 MiB           1       return median(data)
 
****************************************************************************************************

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    88     20.0 MiB     20.0 MiB           1   @profile
    89                                         def test_gnome_median(data):
    90     20.0 MiB      0.0 MiB           1       return gnome_median(data)

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    93     20.0 MiB     20.0 MiB           1   @profile
    94                                         def test_median_sort(data):
    95     20.0 MiB      0.0 MiB           1       return median_sort(data)

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    98     20.0 MiB     20.0 MiB           1   @profile
    99                                         def test_statistics_median(data):
   100     20.0 MiB      0.0 MiB           1       return median(data)

Вывод:
Результаты проведенных измерений показали, что
из 3х предложенных способов поиска медианы ряда, самый быстрый - это использование функции median
из модуля statistics. Также использование "Гнемьей" сортировки проигрывает по времени выполнения
стандартной функции сортировки ряда.
Использование памяти во всех функциях примерно одинаковое, из чего можно смело выбрать
from statistics import median для задач такого рода.
"""
