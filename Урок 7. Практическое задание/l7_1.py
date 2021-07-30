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
from statistics import median


def create_list(m):
    return [randint(-100, 100) for i in range(m + m + 1)]


def median_no_sort(elem):
    while len(elem) > 1:
        elem.remove(min(elem))
        elem.remove(max(elem))
    return elem[0]


def median_no_sort_2(elem):
    j = (len(elem) - 1) / 2 + 1
    while len(elem) > j:
        elem.remove(max(elem))
    return max(elem)


def shell_sort(data):  # и для сравнения ещё взята сортировка Шелла.

    last_index = len(data) - 1
    step = len(data)//2
    while step > 0:
        for i in range(step, last_index + 1, 1):
            j = i
            delta = j - step
            while delta >= 0 and data[delta] > data[j]:
                data[delta], data[j] = data[j], data[delta]
                j = delta
                delta = j - step
        step //= 2
    return data[len(data)//2]


def bubble_sort_3(lst_obj):  # Использую для сравнения решение из первого задания для пузырьковой сортировки.
    n = 1
    j = 1

    while j:

        j = 0

        for i in range(len(lst_obj) - n):
            a = i + 1

            if lst_obj[i] < lst_obj[a]:
                lst_obj[i], lst_obj[a] = lst_obj[a], lst_obj[i]
                j = 1

        n += 1

    return lst_obj[len(lst_obj)//2]


print(median_no_sort((a := create_list(10))[:]))                          # time for 21 elems = 0.0013625939999999948
print(a)
print(
    timeit(
        "median_no_sort(a[:])",
        globals=globals(),
        number=100))
print(median_no_sort_2(a[:]), '\nСпособ два без сортировки: ')            # time for 21 elems = 0.0010110229999999998
list_of_ranges = [a_100 := create_list(50), a_1000 := create_list(500)]  # time for 101 elems = 0.014239995000000005
for i in [a[:], a_100[:], a_1000[:]]:                                   # time for 1001 elems = 1.135056896
    print(
        timeit(
            f"median_no_sort_2({i})",
            globals=globals(),
            number=100))
print(median(a), '\nПри помощи statistics.median: ')                      # time for 21 elems = 9.796199999989597e-05
for i in [a[:], a_100[:], a_1000[:]]:                                    # time for 101 elems = 0.0005389619999998096
    print(                                                              # time for 1001 elems = 0.012283825999999998
        timeit(
            f"median({i})",
            globals=globals(),
            number=100))
print(shell_sort(a[:]), '\nСортировка Шелла:')                            # time for 21 elems = 0.0024456379999999722
for i in [a[:], a_100[:], a_1000[:]]:                                    # time for 101 elems = 0.022106312999999878
    print(                                                              # time for 1001 elems = 0.348538386
        timeit(
            f"shell_sort({i})",
            globals=globals(),
            number=100))
print(bubble_sort_3(a[:]))                                                # time for 21 elems = 0.004357434000000104
print(
    timeit(
        "bubble_sort_3(a[:])",
        globals=globals(),
        number=100))

''' Среди всех способов для начала были сделаны замеры со списком из 21 элемента. Самым медленным, как и ожидалось,
оказалась сортировка пузырьковая, затем сортировка Шелла и чуть лучше оказался первый способ без сортировки. 
Самым быстрым — способ через медиану из модуля статистики. Затем для уточнения были произведены замеры с количеством 
элементов 101, 1001, где преимущества в работе медианы из внешнего модуля стали ещё более очевидными, а сортровка
Шелла показывается меньшую скорость роста затрачиваемого времени в зависимости от увеличения количества сортируемых 
элементов, чем второй способ без сортировки. Для 1000 элементов скорость сортировки Шеллом быстрее в 4 раза позволяет 
найти медиану, чем второй способ без сортировки, хотя и медленнее более чем в 20 раз в сравнении с statistics.median.'''