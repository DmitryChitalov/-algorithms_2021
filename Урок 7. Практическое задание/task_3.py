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
import timeit
import random

from statistics import median

m = int(input('Введите натуральное число m, с помощью которого будет построен массив с 2m + 1 элементами: '))
orig_list = [random.randint(-100, 100) for _ in range(2*m + 1)]

print(orig_list)


# Решение с помощью сортировки методом Шелла
def mediana_sort(a):
    def shellsort(a):
        def new_increment(a):
            i = int(len(a) / 2)
            yield i
            while i != 1:
                if i == 2:
                    i = 1
                else:
                    i = int(round(i/2.2))
                yield i
        for increment in new_increment(a):
            for i in range(increment, len(a)):
                for j in range(i, increment-1, -increment):
                    if a[j - increment] < a[j]:
                        break
                    a[j],a[j - increment] = a[j - increment],a[j]
        return a
    shellsort(a)
    return a[m]


print(mediana_sort(orig_list[:]))


# решение с помощью рекурсии без сортировки
def mediana_no_sort(myl):
    while len(myl) != 1:
        myl.remove(max(myl))
        myl.remove(min(myl))
    return myl[0]


print(mediana_no_sort(orig_list[:]))

# Решение с помощью модуля statistics
def func_mediana(myl):
    return median(myl)

print(func_mediana(orig_list[:]))

print(
    timeit.timeit(
        "mediana_sort(orig_list[:])",
        globals=globals(),
        number=1000))
# на m = 100 - 0.3424195
# на m = 500 - 3.1384524
# на m = 1000 - 8.3649093
print(
    timeit.timeit(
        "mediana_no_sort(orig_list[:])",
        globals=globals(),
        number=1000))
# на m = 100 - 0.3008193
# на m = 500 - 7.5413795
# на m = 1000 - 31.264921
print(
    timeit.timeit(
        "func_mediana(orig_list[:])",
        globals=globals(),
        number=1000))
# на m = 100 - 0.00499030
# на m = 500 - 0.0597656
# на m = 1000 - 0.1374816
'''''
Вывод: После замеров результаты моей функции оказались следующими: Медленне всего с задачей справляется 
функция, основанная на цикле, не сортирующая массив, а постепенно за каждый шаг удаляющая максимальный и минимальный
объекты. На втором месте по времени выполнения стоит функция, использующая сортировку Шелла для упорядочивания массива,
а после берущая медиану массива по заданному индексу.
На первом месте по скорости выполнения стоит функция median из библиотеки statistics, она наиболее быстро 
находит медиану. 
В очередной раз втроенные функции pythona справляются с задачей быстрее, чем самостоятельные решения. 
'''''
