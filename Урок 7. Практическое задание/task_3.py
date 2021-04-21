"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные по длине части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, Кучей...

[5, 3, 4, 3, 3, 3, 3]

[3, 3, 3, 3, 3, 4, 5]

my_lst
new_lts

arr[m]


from statistics import median

[3, 4, 3, 3, 5, 3, 3]


left.clear()
right.clear()


m = 3
len = 7
i
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


def heapify(arr, n, i):
    largest = i
    k = 2 * i + 1
    r = 2 * i + 2
    if k < n and arr[largest] < arr[k]:
        largest = k
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr


m = 10
generated_list = [random.randint(0, 999) for _ in range(2 * m + 1)]
print("Generated list: ", generated_list)

sorted_list = heap_sort(generated_list[:])
print("Heap sorted list: ", sorted_list)
print("Median from sorted list: ", sorted_list[m])
print("Median from built-in function: ", median(generated_list))

"""
Generated list:  [376, 478, 745, 582, 885, 71, 165, 238, 621, 980, 10, 912, 280, 938, 216, 194, 577, 152, 516, 319, 131]
Heap sorted list:  [10, 71, 131, 152, 165, 194, 216, 238, 280, 319, 376, 478, 516, 577, 582, 621, 745, 885, 912, 938, 980]
Median from sorted list:  376
Median from built-in function:  376

Использовал сортировку кучей (не своя, нашел).
В отсортированном массиве медиана из условия генерации массива окажется на позиции m.
Для проверки использовал встроенную функцию median. Результаты получаются одинаковые, значит алгоритм работает верно.
"""