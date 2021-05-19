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
from math import sqrt
import time


def get_median(lst):
    for i in range(n):
        lst.pop(lst.index(min(lst)))

    return min(lst)


def shell_sort(lst, d):
    for i in range(len(lst)):
        while True:
            is_move = False
            for j in range(i, len(lst), d):
                if j + d < len(lst) and lst[j] > lst[j + d]:
                    lst[j], lst[j + d] = lst[j + d], lst[j]
                    is_move = True

            if not is_move:
                break

    if d == 1:
        return
    else:
        d = int(sqrt(d))
        shell_sort(lst, d)


n = randint(10, 1000)
print(f'n = {n}')
lst = [randint(0, 1000) for _ in range(n * 2 + 1)]
print('lst без сортировки', lst)
lst1 = lst[:]
lst2 = lst[:]
print('Отсортированный lst', sorted(lst))
median = get_median(lst[:])
print(f'Медиана без сортировки = {median}')

# В качестве значения d для алгоритма Шелла взял квадратный корень от числа n
# Для каждой следующей итерации использую квадратный корень от d
# Результаты замеров ниже
t1 = time.time()
shell_sort(lst1, int(sqrt(n)))
print(f'Время выполнения сортировки Шелла: {time.time() - t1}')
median = lst1[n]
print(f'Медиана при сортировке Шелла = {median}')

t1 = time.time()
shell_sort(lst2, 1)
print(f'Время выполнения сортировки перестановкой (d = 1): {time.time()- t1}')
median = lst2[n]
print(f'Медиана при сортировке перестановкой = {median}')


# Вчем подвох? Слишком просто
# n = 582
# lst без сортировки [57, 613, ..., 67, 873]
# Отсортированный lst [0, 0, ..., 997, 1000]
# Медиана без сортировки = 501
# Время выполнения сортировки Шелла: 0.4956948757171631
# Медиана при сортировке Шелла = 501
# Время выполнения сортировки перестановкой (d = 1): 2.402531623840332
# Медиана при сортировке перестановкой = 501



