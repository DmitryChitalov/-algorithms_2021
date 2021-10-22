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


m = int(input('введите длину рандомного списка:'))
data = [random.randint(0, 50) for _ in range(2 * m + 1)]


def shell(li):
    inc = len(li) // 2
    while inc:
        for i, el in enumerate(li):
            while i >= inc and li[i - inc] > el:
                li[i] = li[i - inc]
                i -= inc
            li[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    return f'{li}\nмедианна: {li[m]}'


def not_sort(li):
    for i in range(m):
        li.remove(max(li))
    return f'{li}\nмедианна: {max(li)}'


print(timeit('shell(data[:])', globals=globals(), number=100))
print(shell(data[:]), end='\n\n')

print(timeit('median(data[:])', globals=globals(), number=100))
print(f'медиана: {median(data[:])}', end='\n\n')

print(timeit('not_sort(data[:])', globals=globals(), number=100))
print(not_sort(data[:]))


'''
сортировка shell
0.021966280000000005
[3, 13, 14, 20, 22, 23, 23, 23, 26, 31, 33, 34, 35, 36, 38, 39, 40, 40, 41, 42, 50]
медианна: 33

встроенная функция median
0.0006376860000001372
медиана: 33

функция без сортировки
0.01781536699999986
[23, 14, 3, 26, 23, 33, 22, 23, 20, 31, 13]
медиана: 33

Выыод: встроенная функция median оказалась быстрее, за ней следует функция без сортировки. 
       Ну а самой медленной оказалась функция shell.
'''