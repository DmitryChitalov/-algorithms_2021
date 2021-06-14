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


from random import randint
from statistics import median


def vector_gen(count):
    return [randint(-100, 100) for i in range(2 * count + 1)]


def median_from_sorted(sorted_array):
    return sorted_array[len(sorted_array) // 2]


def median_statistics(unsorted_array):
    return median(unsorted_array)


def median_by_del_max(unsorted_array):
    stop = (len(unsorted_array) // 2) + 1
    while len(unsorted_array) != stop:
        unsorted_array.pop(
            unsorted_array.index(
                max(unsorted_array)
            )
        )
    return max(unsorted_array)


def median_with_double_list(unsorted_array):
    left = []
    right = []
    while len(unsorted_array) != 1:
        left.append(
            unsorted_array.pop(
                unsorted_array.index(
                    min(unsorted_array)
                )
            )
        )
        right.append(
            unsorted_array.pop(
                unsorted_array.index(
                    max(unsorted_array)
                )
            )
        )
    return unsorted_array[0]


def shell_sort(data):
    length = len(data)
    center = length // 2
    while center > 0:
        for i in range(center, length):
            el = data[i]
            j = i
            while j >= center and data[j - center] > el:
                data[j] = data[j - center]
                j -= center
                data[j] = el
        center //= 2
    return data


try:
    num = int(input('Введите m для построения массива по выражению "2m+1": '))
except ValueError:
    print('Необходимо вводить число!')

vector = vector_gen(num)
sorted_vector = shell_sort(vector)
print(f'Несортированна последовательность:\n{vector}')
print(f'Массив сортированный Шеллом:\n{sorted_vector}')
print(f'Медиана из сортированного массива: {median_from_sorted(sorted_vector)}')
print(f'Нахождение медианы из несортированного массива (функция из модуля '
      f'statistics): {median_statistics(vector[:])}')
print(f'Нахождение медианы удалением максимальных значений из массива: '
      f'{median_by_del_max(vector[:])}')
print(f'Нахождение медианы разделением массива на 2 списка: '
      f'{median_with_double_list(vector[:])}')
