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
import random
from statistics import median

m = 3
orig_list = [random.randint(0, 50) for _ in range(2 * m + 1)]


# Решение без сортировки
def my_median(lst_obj):
    middle = len(lst_obj) // 2
    while True:
        maximum = lst_obj[0]
        for el in lst_obj:  # O(n)
            if el > maximum:  # O(1)
                maximum = el  # O(1)
        lst_obj.remove(maximum)  # O(1)
        if middle == 0:
            return maximum
        middle -= 1


# Сортировка Шелла

def shell(lst_obj):
    inc = len(lst_obj) // 2
    middle = len(lst_obj) // 2
    while inc:
        for i, el in enumerate(lst_obj):
            while i >= inc and lst_obj[i - inc] > el:
                lst_obj[i] = lst_obj[i - inc]
                i -= inc
            lst_obj[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    return lst_obj[middle]


# Гномья сортировка
def gnome(lst_obj):
    i, size = 1, len(lst_obj)
    middle = len(lst_obj) // 2
    while i < size:
        if lst_obj[i - 1] <= lst_obj[i]:
            i += 1
        else:
            lst_obj[i - 1], lst_obj[i] = lst_obj[i], lst_obj[i - 1]
            if i > 1:
                i -= 1
    return lst_obj[middle]


# Сортировка кучей
def heapsort(lst_obj):
    middle = len(lst_obj) // 2
    for start in range((len(lst_obj) - 2) // 2, -1, -1):
        siftdown(lst_obj, start, len(lst_obj) - 1)
    for end in range(len(lst_obj) - 1, 0, -1):
        lst_obj[end], lst_obj[0] = lst_obj[0], lst_obj[end]
        siftdown(lst_obj, 0, end - 1)
    return lst_obj[middle]


def siftdown(lst_obj, start, end):
    root = start
    while True:
        child = root * 2 + 1
        if child > end:
            break
        if child + 1 <= end and lst_obj[child] < lst_obj[child + 1]:
            child += 1
        if lst_obj[root] < lst_obj[child]:
            lst_obj[root], lst_obj[child] = lst_obj[child], lst_obj[root]
            root = child
        else:
            break


print(f'Сalibre {median(orig_list[:])}')
print(shell(orig_list[:]))
print(my_median(orig_list[:]))
print(gnome(orig_list[:]))
print(heapsort(orig_list[:]))
