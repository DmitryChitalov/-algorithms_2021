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


from statistics import median
from random import randint
from timeit import timeit


m = 100 # int(input('Введите число: '))
my_list = [randint(1, 10000) for i in range(m*2+1)]


def median_1(some_list):
    while len(some_list) > m + 1:
        some_list.remove(max(some_list))
    return max(some_list)


def median_2(lst):
    i = 1
    while i < len(lst):
        if (lst[i - 1] <= lst[i]):
            i += 1
        else:
            lst[i], lst[i - 1] = lst[i - 1], lst[i]
            i -= 1
            if (i == 0):
                i = 1
    return lst[m]


print(median(my_list[:]))
print(median_1(my_list[:]))
print(median_2(my_list[:]))

print(timeit('median(my_list[:])', globals=globals(), number=100))      # 0.0032846509999999995
print(timeit('median_1(my_list[:])', globals=globals(), number=100))    # 0.091496676
print(timeit('median_2(my_list[:])', globals=globals(), number=100))    # 1.165463713

# Наиболее быстрая - встроеная функция. Функция median_1 имеет квадратичную сложность, поэтому работает значительно
# медленнее. Алгоритм на базе сортировки также имеет квадратичную сложность, но работает еще медленнее, поскольку
# производит дополнительную работу по перестановке значений во всем массиве.
