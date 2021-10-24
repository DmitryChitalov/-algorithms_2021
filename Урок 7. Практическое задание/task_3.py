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
import random
from statistics import median
from timeit import timeit


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


def find_med(arr):
    arr = shell(arr)
    return arr[m]


m = int(input('Введите число m: '))
ln_arr = 2 * m + 1
print(ln_arr)
lst = [random.randint(0, 100) for i in range(ln_arr)]
print(lst)
print(find_med(lst))
print(median(lst))
lst_10 = [random.randint(-100, 100) for _ in range(10)]
lst_100 = [random.randint(-100, 100) for _ in range(100)]
lst_1000 = [random.randint(-100, 100) for _ in range(1000)]
print('Сортировка 10 шелла - ', timeit('shell(lst_10)', globals=globals(), number=1000))
print('Сортировка 100 шелла - ', timeit('shell(lst_100)', globals=globals(), number=1000))
print('Сортировка 1000 шелла - ', timeit('shell(lst_1000)', globals=globals(), number=1000))

# Сортировка 10 шелла -  0.004217399999999927
# Сортировка 100 шелла -  0.07732800000000006
# Сортировка 1000 шелла -  1.2836762000000004
# Сортировка Шелла показывает результат лучше сортировки слияния
