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
from statistics import StatisticsError

from memory_profiler import memory_usage
from timeit import default_timer

def heapify(nums, heap_size, root_index):

    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]

        heapify(nums, heap_size, largest)
def heap_sort(nums):
    n = len(nums)

    for i in range(n, -1, -1):
        heapify(nums, n, i)

    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)


def my_decor(func):
    def check_optimize(*args):
        t1 = default_timer()
        m1 = memory_usage()
        result = func(*args)
        m2 = memory_usage()
        t2 = default_timer()
        mem_res = m2[0] - m1[0]
        time_res = t2 - t1
        return f'Память: {mem_res},\nВремя: {time_res},\nРезультат: {result}'
    return check_optimize

@my_decor
def my_median(list):

    heap_sort(list)
    l = len(list)

    mid = (l - 1) // 2

    if (l % 2 == 0):
        return (list[mid] + list[mid + 1]) / 2
    else:
        return list[mid]
@my_decor
def median(data):

    data = sorted(data)
    n = len(data)
    if n == 0:
        raise StatisticsError("no median for empty data")
    if n%2 == 1:
        return data[n//2]
    else:
        i = n//2
        return (data[i - 1] + data[i])/2

data_list = [randint(-100, 100) for i in range(10000 * 2 + 1)]


print(my_median(data_list[:]))
print(median(data_list[:]))

#При использовании сортировки функция получаеться дастаточно отимизированой
Память: 0.00390625,
Время: 0.3525551,
Результат: 0

Память: 0.1484375,
Время: 0.21860960000000007,
Результат: 0