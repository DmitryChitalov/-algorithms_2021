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
import numpy as np
from statistics import median
import timeit


def gnome(lst):
    i, size = 1, len(lst)
    while i < size:
        if lst[i - 1] <= lst[i]:
            i += 1
        else:
            lst[i - 1], lst[i] = lst[i], lst[i - 1]
            if i > 1:
                i -= 1
    return lst


def get_mediana(lst):
    [lst.remove(max(lst)) for _ in range(len(lst) // 2)]
    return max(lst)


m = int(input('Введите параметр m: '))
arr = np.random.randint(0, 100, 2 * m + 1)
print(arr)
print(f'Медиана from statistics = {median(arr)}')
arr2 = gnome(arr.tolist())
print(f'Медиана после гномьей сортировки = {arr2[m]}')
print(f'Медиана без сортировки = {get_mediana(arr.tolist())}')
print('Замеры:')
print(
    f'Медиана определенная при помощи гномьей сортировки: {timeit.timeit("gnome(arr[:])", globals=globals(), number=10000)}')
print(
    f'Медиана определенная без сортировки: {timeit.timeit("get_mediana(arr[:].tolist())", globals=globals(), number=10000)}')

# Результаты при m = 100:
# Медиана определенная при помощи гномьей сортировки: 0.7720960259999998
# Медиана определенная без сортировки: 5.4709724799999995
# Результаты при m = 10:
# Медиана определенная при помощи гномьей сортировки: 0.08645303000000037
# Медиана определенная без сортировки: 0.10227028799999971
# Определение медианы быстрее с помощью сортировки, при том, что гномья сортировка не самая быстрая,
# особенно на большом количестве элементов
