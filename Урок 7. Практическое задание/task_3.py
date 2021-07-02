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
from timeit import timeit
from statistics import median
from random import randint


def sort_gnom(arr):             # метод сортировки Гномья
    n = 1
    k = 2
    while n < len(arr):
        if arr[n - 1] <= arr[n]:
            n = k
            k += 1
        else:
            arr[n - 1], arr[n] = arr[n], arr[n - 1]
            n -= 1
            if n == 0:
                n = k
                k += 1
    return arr


def median_left_right(arr):       # метод через построение левой и правой части
    for elem in arr:
        left = [elem2 for elem2 in arr if elem2 < elem]
        right = [elem2 for elem2 in arr if elem2 > elem]
        if len(left) == len(right) or abs(len(left) - len(right)) < arr.count(elem):
            return elem


def median_remove_max(arr):       # метод через удаление максимумов
    for _ in range(len(arr) // 2):
        arr.remove(max(arr))
    return max(arr)


if __name__ == '__main__':

    m = int(input('Введите целое число: '))
    test_arr = [randint(0, 100) for _ in range(2 * m + 1)]

    print('-' * 50)
    print('Медиана методом сортировки (Гномья):', sort_gnom(test_arr[:])[m])
    print('\tСкорость поиска:', timeit("sort_gnom(test_arr[:])[m]", globals=globals(), number=1000))
    print('-' * 50)
    print('Медиана методом построения левой и правой частей:', median_left_right(test_arr[:]))
    print('\tСкорость поиска:', timeit("median_left_right(test_arr[:])", globals=globals(), number=1000))
    print('-' * 50)
    print('Медиана методом удаления максимумов:', median_remove_max(test_arr[:]))
    print('\tСкорость поиска:', timeit("median_remove_max(test_arr[:])", globals=globals(), number=1000))
    print('-' * 50)
    print('Медиана встроенной функцией:', median_remove_max(test_arr[:]))
    print('\tСкорость поиска:', timeit("median(test_arr[:])", globals=globals(), number=1000))

"""
вывод
    Введите целое число: 100
    --------------------------------------------------
    Медиана методом сортировки (Гномья): 49
        Скорость поиска: 3.4506821999999997
    --------------------------------------------------
    Медиана методом построения левой и правой частей: 49
        Скорость поиска: 2.4412177
    --------------------------------------------------
    Медиана методом удаления максимумов: 49
        Скорость поиска: 0.28119020000000017
    --------------------------------------------------
    Медиана встроенной функцией: 49
        Скорость поиска: 0.008138800000001112
"""

# встроенная функция победила (кто бы сомневался)
# из НЕ встроенных методов самым быстрым оказался - метод удаления максимумов
# а самым медленным, ожидаемо, метод с сортировкой

