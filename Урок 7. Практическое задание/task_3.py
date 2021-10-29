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
import math
import random
import timeit


# 2. Убрать максимумы из массива в цикле - мой вариант.
def my_median(list_in):  # O(n)
    list_obj = list_in[:]  # исходный массив оставим без изменений
    l_list = len(list_obj)
    while len(list_obj) >= l_list // 2 + 1:
        cur_max = max(list_obj)
        list_obj.pop(list_obj.index(cur_max))
    return cur_max


# 3. Варианты с сортировкой


# 3.1 Сортировка Шелла
def shell_sort(array):  #  O(n (log n)2)
    n = len(array)
    k = int(math.log2(n))
    interval = 2**k - 1
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp
        k -= 1
        interval = 2**k - 1
    return array


# 3.2 Сортировка "Гномья"
def gnome_sort(data):  # О(n^2)
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


# 3.3 Сортировка "Кучей"


def heapify(array, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and array[i] < array[l]:
        largest = l
    if r < n and array[largest] < array[r]:
        largest = r

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)


def heapSort(array):  # O(n log(n))
    n = len(array)
    for i in range(n // 2, -1, -1):
        heapify(array, n, i)
    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)
    return array


# -------- Ввод данных пользователем и результаты -----------
# Запросим параметр m у пользователя
m = int(input('Введите параметр m для массива размеро 2m + 1: '))
my_list = [random.randint(-100, 100) for i in range(2*m + 1)]
print(my_list)


print('Итоговые медианные знаения разными вариантами получились следующие:')
print('Вариант statistics:', median(my_list))
print('Вариант с исключением максимумов:', my_median(my_list))
print('Вариант с сортировкой Шелла:', shell_sort(my_list[:])[m])
print('Вариант с сортировкой Гномья:', gnome_sort(my_list[:])[m])
print('Вариант с сортировкой Кучей:', heapSort(my_list[:])[m])

# ---- Параметры замеров:
len_arr = [10, 20, 50, 100, 200, 300]           # размер сортируемого массива
res_time = {'Len_arr': ('Sh  ', 'Gn', '  He')}    # словарь для результатов замеров

# --- Делаем замер и выводим результаты:
for len_i in len_arr:
    # в условии 50 не включается, поэтому сделаем верхнюю границу 49.99
    orig_list = [random.randint(-100, 100) for i in range(2*len_i + 1)]
    time_shell = timeit.timeit(
            "shell_sort(orig_list[:])",
            globals=globals(), number=1000)
    time_gnome = timeit.timeit(
            "gnome_sort(orig_list[:])",
            globals=globals(), number=1000)
    time_heap = timeit.timeit(
            "heapSort(orig_list[:])",
            globals=globals(), number=1000)
    res_time[len_i] = (round(time_shell, 4), round(time_gnome, 4), round(time_heap, 4))

# Выводим результаты
for pos, item in enumerate(res_time.items()):
    print(f'{pos}){item[0]}        {item[1][0]} {item[1][1]} {item[1][2]}')


"""
Результаты решений и замеры:
 Замеры времени для рассмотренных вариантов сортировок:
 
 Итоговые медианные знаения разными вариантами получились при m = 100:
Вариант statistics: 3
Вариант с исключением максимумов - мой вариант: 3
Вариант с сортировкой Шелла: 3
Вариант с сортировкой Гномья: 3
Вариант с сортировкой Кучей: 3

Резльтат замеров:
0)Len_arr     Sh     Gn     He
1)10        0.0258 0.0503  0.0591
2)20        0.0628 0.1903  0.1261
3)50        0.1937 1.083   0.392
4)100       0.4676 4.1766  0.9247
5)200       1.1827 15.8691 2.1752
6)300       1.9257 37.1501 3.3905
 
Из результатов взамеров видно, что время работы рассмотренных сортировок на маленьких массивах примерно одинаковое. 
На больших массивах Гномья проигрывает, учитывая квадратичную сложность данного алгоритма.  
 """
