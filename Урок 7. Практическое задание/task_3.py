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
from timeit import timeit
from random import randint
from statistics import median


def median_gnome(lst, m):
    i, size = 1, len(lst)
    while i < size:
        if lst[i - 1] <= lst[i]:
            i += 1
        else:
            lst[i - 1], lst[i] = lst[i], lst[i - 1]
            if i > 1:
                i -= 1
    return f'Медиана данного массива - {lst[m]}'


def get_median(lst):
    return f'Медиана данного массива - {median(lst)}'


m = int(input('Введите натуральное число: '))
test_lst = [randint(1, 10) for i in range(2 * m + 1)]

print(median_gnome(test_lst[:], m))
print(get_median(test_lst[:]))

print(f'Время работы median_gnome : {timeit("median_gnome(test_lst[:], m)", globals=globals(), number=1000)}')
print(f'Время работы get_median : {timeit("get_median(test_lst[:])", globals=globals(), number=1000)}')

"""
Время работы median_gnome : 0.03290850000000001
Время работы get_median : 0.0009292999999996887

Вывод: оказалось, что встроенная в библиотеку statistics функция median выполняется в сотни раз быстрее, 
чем фукция основанная по методу сортировки Гномья.
"""
