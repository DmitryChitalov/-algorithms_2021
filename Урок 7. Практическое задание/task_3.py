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

'''
Первый вариант поиска медианы. Ищем максимальный элемент m раз и удаляем его из списка. 
m+1-ый максимальный элемент - искомая медиана.

Этот вариант имеет сложность 3n*(n/2) = 1,5n^2 = O(n^2)
'''


def get_median_1(lst):
    new_list = lst[:]
    for _ in range(m):
        max_ind = new_list.index(max(new_list))
        del new_list[max_ind]
    return max(new_list)


'''
Второй вариант поиска медианы - взять средний элемент в отсортированном массива.
Я выбрала сортировку кучей HeapSort, которая имеет сложность n*log(n).
'''

def heapify(lst, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and lst[largest] < lst[l]:
        largest = l

    if r < n and lst[largest] < lst[r]:
        largest = r

    if not (largest == i):
        lst[largest], lst[i] = lst[i], lst[largest]
        heapify(lst, n, largest)


def heap_sort(list_to_sort):
    lst = list_to_sort[:]
    for i in range(round(len(lst) / 2 - 1), -1, -1):
        heapify(lst, len(lst), i)

    for i in range(len(lst) - 1, 0, -1):
        lst[0], lst[i] = lst[i], lst[0]
        heapify(lst, i,  0)
    return lst


m = int(input("Введите m (m - половина длины списка): "))
source_list = [randint(0, 10) for _ in range(2*m + 1)]
print(source_list)
print("Медиана 1: ", get_median_1(source_list))
print("Медиана 2: ", heap_sort(source_list)[m])

'''
Введите m (m - половина длины списка): 5
[7, 9, 9, 1, 7, 0, 5, 1, 5, 7, 1]
Медиана 1:  5
Медиана 2:  5
'''

