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
from random import random
from statistics import median
from timeit import timeit


m = int(input('Введите натуральное число m: '))
num_list = [int(random() * 1000 + 1) for _ in range(int(2 * m + 1))]
print(f'Полученный список: {num_list}')
print()

# Не испульзую сортировку списка:
def get_array_med_1(m, num_list):
    for i in range(len(num_list)):
        count_left = 0
        count_equal = 0
        for j in range(len(num_list)):
            if num_list[i] > num_list[j] and i != j:
                count_left += 1
            elif num_list[i] == num_list[j] and i != j:
                count_equal += 1
        if count_left <= m and (count_left + count_equal) >= m:
            med = num_list[i]
            return med


print('Вариант без сортировки списка')

med_1 = get_array_med_1(m, num_list)

print(f'Медиана списка:  {med_1}')
print(f'Проверка: медиана списка  {median(num_list)}')
print()

# с использованием метода Гномья сортировка:

def get_array_med_2(m, num_list):
    list_copy = num_list[:]
    i, j, size = 1, 2, len(list_copy)
    while i < size:
        if list_copy[i - 1] <= list_copy[i]:
            i, j = j, j + 1
        else:
            list_copy[i - 1], list_copy[i] = list_copy[i], list_copy[i - 1]
            i -= 1
            if i == 0:
                i, j = j, j + 1
    med = list_copy[m]
    return list_copy, med

print('Вариант с использованием метода Гномья сортировка')

sorted_list, med_2 = get_array_med_2(m, num_list)

print(f'Медиана списка:  {med_2}')
print(f'Отсортированный список: {sorted_list}')
print(f'Проверка: медиана списка {median(num_list)}')

print()
print(timeit('get_array_med_1', 'from __main__ import get_array_med_1, m, num_list', number=100000))
print(timeit('get_array_med_2', 'from __main__ import get_array_med_2, m, num_list', number=100000))

# Результат при m=10:

# Введите натуральное число m: 10
# Полученный список: [72, 469, 50, 735, 999, 913, 304, 955, 398, 88, 204, 381, 814, 851, 470, 748, 518, 412, 553, 623, 852]
#
# Вариант без сортировки списка
# Медиана списка:  518
# Проверка: медиана списка  518
#
# Вариант с использованием метода Гномья сортировка
# Медиана списка:  518
# Отсортированный список: [50, 72, 88, 204, 304, 381, 398, 412, 469, 470, 518, 553, 623, 735, 748, 814, 851, 852, 913, 955, 999]
# Проверка: медиана списка 518
#
# 0.0059651000000000565
# 0.006567599999999896

# Результаты быстродействия двух вариантов получения медианы массива (без сортировки и с применением метода Гномья сортировка)
# могут при прочих равных условиях показывать то явное преимущество на стороне второго, то первого варианта, то практически
# равные результаты. Очевидно, что в первом варианте, чем ближе медиана массива к началу списка, то есть чем ближе
# индекс искомого элемента медианы к нуль (в идеале равен 0), тем быстрее отрабатывает функция, и, соответственно, чем дальше
# искомый элемент от начала списка, тем больше времени требуется на выполнение функции.
