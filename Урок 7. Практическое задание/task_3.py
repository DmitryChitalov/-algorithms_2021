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
import random
import timeit

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

def gnome_sort(data):
    i, j, size = 1, 2, len(data)
    while i < size:
        if data[i - 1] <= data[i]:
            i, j = j, j + 1
        else:
            data[i - 1], data[i] = data[i], data[i - 1]
            i -= 1
            if i == 0:
                i, j = j, j + 1
    return data

def median(lst):
    for i in range(len(lst)//2):
        lst.pop(lst.index(max(lst)))
    return max(lst)

m = int(input('Введите значение m для построения массива 2m+1:'))
lst = [random.randint(0, 100) for _ in range(2 * m + 1)]

print(lst)
print(f'Массив гномьей сортировкой: {gnome_sort(lst)}')
print(f'Массив сортировкой Шелла: {shell(lst)}')

print(f'Медиана массива: {median(lst)}')

print(f'Время на выполнение гномьей сортировкой: ',
    timeit.timeit(
        "gnome_sort(lst)",
        globals=globals(),
        number=1000))

print(f'Время на выполнение сортировки Шелла: ',
    timeit.timeit(
        "shell(lst)",
        globals=globals(),
        number=1000))