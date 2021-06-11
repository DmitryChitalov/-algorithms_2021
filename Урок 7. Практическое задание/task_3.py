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
from random import randint
from timeit import timeit
from statistics import median


def random_list(m):
    lst = [randint(0, 100) for el in range(2 * m + 1)]
    return lst


''' Самый простой вариант со встроеной сортировкой'''


def median_1(lst):
    return sorted(lst)[len(lst) // 2]


''' Вариант без сортировки'''


def median_2(lst):
    middle = len(lst) // 2
    for el in range(0, middle + 1):
        index_maximum = lst.index(max(lst))
        maximum = lst.pop(index_maximum)
    return maximum


''' Вариант сортировки пузырьком'''


def median_3(lst):
    n = 1
    middle = len(lst) // 2
    while n <= middle:
        for el in range(len(lst) - n):
            if lst[el] < lst[el+1]:
                lst[el], lst[el+1] = lst[el+1], lst[el]
        n += 1
    return lst[middle]


lst_11 = random_list(5)
lst_101 = random_list(10)
lst_1001 = random_list(100)
print(
    timeit(
        "median_1(lst_11[:])",
        globals=globals(),
        number=100))
print(
    timeit(
        "median_2(lst_11[:])",
        globals=globals(),
        number=100))
print(
    timeit(
        "median_3(lst_11[:])",
        globals=globals(),
        number=100))
print(
    timeit(
        "median_1(lst_101[:])",
        globals=globals(),
        number=100))
print(
    timeit(
        "median_2(lst_101[:])",
        globals=globals(),
        number=100))
print(
    timeit(
        "median_3(lst_101[:])",
        globals=globals(),
        number=100))
print(
    timeit(
        "median_1(lst_1001[:])",
        globals=globals(),
        number=100))
print(
    timeit(
        "median_2(lst_1001[:])",
        globals=globals(),
        number=100))
print(
    timeit(
        "median_3(lst_1001[:])",
        globals=globals(),
        number=100))
'''
Замеры трех функций нахождения медианы на массивах длинной:
11 элементов
8.368500000000001e-05
0.00047645000000000326
0.0014680349999999995
101 элемент
0.0001310539999999985
0.001000268999999998
0.004398183999999999
1001 элемент
0.0011956649999999985
0.039680766
0.415170539

Вывод можно сделать такой, что встроенные функции сортировки быстрые за счет использования алгоритма
слияния и нахождение медианы в них самое простое.
'''