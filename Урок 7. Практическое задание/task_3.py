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
import random
import time


def for_time(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            print('%r  %2.2f ms' % \
                  (method.__name__, (te - ts) * 1000))
        return result

    return timed


# сортировка Шелла:
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


# Со исползованием фннкции midian from statistics:
@for_time
def median_1(my_list):
    return median(my_list)


# C сортировкой исходного массива:
@for_time
def median_2(my_list):
    sorted_list = shell(my_list[:])
    return sorted_list[((len(sorted_list) - 1) // 2)]


#  без сортировки исходного массива:
@for_time
def median_3(my_list_1):
    my_list = my_list_1[:]
    for i in range((len(my_list) - 1) // 2):
        max_number = max(my_list)
        index_number = my_list.index(max_number)
        my_list.pop(index_number)
    return max(my_list)


m = int(input("Please enter the number 'm' :"))
x = 2 * m + 1
my_list = [random.randint(-10, 10) for i in range(x)]
# print("The list: ", my_list)

print(median_1(my_list))
print(median_2(my_list))
print(median_3(my_list))
"""
'median_1'  0.00 ms
0
'median_2'  46.86 ms
0
'median_3'  2357.15 ms
0
Как видим самые быстро - функция которая уже есть в питоне, для данного примена сильно отличается и отлично работает"""