from random import randint
from timeit import timeit
from statistics import median


def median_gnome(data, m):
    i, size = 1, len(data)
    while i < size:
        if data[i - 1] <= data[i]:
            i += 1
        else:
            data[i - 1], data[i] = data[i], data[i - 1]
            if i > 1:
                i -= 1
    return f'Медианой данного массива является число {data[m]}'


def median_func(lst):
    return f'Медианой данного массива является число {median(lst)}'


m = int(input('Введите m: '))
lst = [randint(1, 10) for i in range(2 * m + 1)]


print(median_gnome(lst, m))
print(median_func(lst))


print(
    f"время выполнения с gnome составило {timeit('median_gnome(lst[:], m)', globals=globals(), number=1000)}")
print(
    f"время выполнения с median составило {timeit('median_func(lst[:])', globals=globals(), number=1000)}")


'''
время выполнения с gnome составило 0.003144000000000702
время выполнения с median составило 0.0013648000000001659
Вывод: сортировка gnome оказалась медленнее встроенной функции median.
Это подтверждает гипотезу о том, что в реальной работе при возможности надо пользоваться 
встроенными функциями.  
'''
