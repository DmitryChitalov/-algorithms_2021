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


def gnome_sort(array):
    i, j, size = 1, 2, len(array)
    while i < size:
        if array[i - 1] <= array[i]:
            i, j = j, j + 1
        else:
            array[i - 1], array[i] = array[i], array[i - 1]
            i -= 1
            if i == 0:
                i, j = j, j + 1
    return f'Отсортированный массив - {array}\nМедианное значение с сортировкой массива: {array[m]}'


def find_median(array):
    n = len(array) // 2
    for i in range(n):
        array.remove(max(array[:]))
    return max(array)


m = int(input('Введите m для построения массива: '))
user_array = [random.randint(0, 100) for i in range((2 * m) + 1)]
print(f'Исходный массив - {user_array}')

print(gnome_sort(user_array[:]))
print(f'Медианное значение без сортировки: {find_median(user_array[:])}')
print(f'Медианное значение через функцию median: {median(user_array[:])}')

print('-' * 100)
print('Замер поиска сортировкой')
print(timeit('gnome_sort(user_array[:])', globals=globals(), number=1000))

print('-' * 100)
print('Замер поиска через ф-ию find_median')
print(timeit('find_median(user_array[:])', globals=globals(), number=1000))

print('-' * 100)
print('Замер поиска через ф-ию median')
print(timeit('median(user_array[:])', globals=globals(), number=1000))


"""
Замер поиска сортировкой
0.014257799999999987
----------------------------------------------------------------------------------------------------
Замер поиска через ф-ию find_median
0.003452099999999847
----------------------------------------------------------------------------------------------------
Замер поиска через ф-ию median
0.0006059000000000481

Исходя из полученных результатов видно, что 1-й результат с сортировкой самый медленный, т.к трятится время на
сортировку массива. Самый быстрый оказался с помощью ф-ии median
"""
