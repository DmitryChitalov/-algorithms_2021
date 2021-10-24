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
from timeit import timeit
from statistics import median


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


m = int(input('Введите m: '))
len_lst = 2 * m + 1
lst = [random.randint(0, 100) for i in range(len_lst)]
print(f'Исходный массив: \n {lst}')
print(f'Отсортированный массив: \n {shell(lst)} ')
print(f'Медиана: \n {median(lst)}')

list_range = [random.randint(-100, 100) for _ in range(len_lst)]

print(f'Сортировка шелла {len_lst}: ', timeit('shell(list_range)', globals=globals(), number=1000))

"""
Результат по времени лучше чем у сортировки слиянием.
При 1001 элементов:  1.1414395000000002
"""