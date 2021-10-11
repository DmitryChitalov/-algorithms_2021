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
from random import randint
from timeit import timeit

m = int(input('Введите медиану m: '))
my_list = [randint(0, 100) for i in range(2 * m + 1)]

# нахождение медианы без сортировки
def find_median(lst: list):
    for i in range(m):
        lst.pop(lst.index(max(lst)))
    return max(lst)

# находим медиану через сортировку Шелла
def shell(data):
    inc = len(data) // 2
    while inc:
        for i, el in enumerate(data):
            while i >= inc and data[i - inc] > el:
                data[i] = data[i - inc]
                i -= inc
            data[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    return max(data)

print(my_list)
print(median(my_list))
print(find_median(my_list))
print(shell(my_list))

print(
    timeit("median(my_list)", globals=globals(), number=1),
    timeit("find_median(my_list)", globals=globals(), number=1),
    timeit("shell(my_list)", globals=globals(), number=1), sep='\n'
)

"""
Самая быстрая оказалась функция median() что ожидаемо,
немного медленнее решение через сортировку Шелла,
решение без сортировки оказалось самым медленным.
5.918998795095831e-06 - median
9.155999578069896e-06 - без сортировки
3.2999960239976645e-06 - Шелла
В коде сортировке Шелла выбрал медиану максимальным элементом, так как этот алгоритм как раз сортирует до медианы,
а она как раз максимально значение в отсортированном массиве.
"""