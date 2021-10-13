from random import randint
from statistics import median
from timeit import timeit


def gnome_sort(data, med):
    i, size = 1, len(data)
    while i < size:
        if data[i - 1] <= data[i]:
            i += 1
        else:
            data[i - 1], data[i] = data[i], data[i - 1]
            if i > 1:
                i -= 1
    return f'Отсортированный массив: {data}\n' \
           f'Гномья сортировка: {data[med]}'


def opt_gnome_sort(data, med):
    i, j, size = 1, 2, len(data)
    while i < size:
        if data[i - 1] <= data[i]:
            i, j = j, j + 1
        else:
            data[i - 1], data[i] = data[i], data[i - 1]
            i -= 1
            if i == 0:
                i, j = j, j + 1
    return f'Оптимизированная гномья сортировка : {data[med]}'


def cycle(lst, med):
    for _ in range(med):
        lst.remove(max(lst))
    return f'Цикл без сортировки: {max(lst)}'


def median_sort(lst):
    return f'Встроенная median: {median(lst)}'


if __name__ == '__main__':
    m = int(input('Введите m: '))
    array = [randint(1, 10) for i in range(2 * m + 1)]
    print(f'Исходный массив: {array}')
    print(gnome_sort(array[:], m))
    print(opt_gnome_sort(array[:], m))
    print(cycle(array[:], m))
    print(median_sort(array[:]))
    print(f"Гномья сортировка: {timeit('gnome_sort(array[:], m)', globals=globals(), number=1000)}")
    print(f"Опт. гномья сортировка : {timeit('opt_gnome_sort(array[:], m)', globals=globals(), number=1000)}")
    print(f"Цикл: {timeit('cycle(array[:], m)', globals=globals(), number=1000)}")
    print(f"Встроенная median: {timeit('median_sort(array[:])', globals=globals(), number=1000)}")

    """
    Введите m: 6
    Исходный массив: [8, 2, 6, 10, 5, 10, 2, 6, 5, 2, 3, 8, 4]
    Отсортированный массив: [2, 2, 2, 3, 4, 5, 5, 6, 6, 8, 8, 10, 10]
    Гномья сортировка: 5
    Оптимизированная гномья сортировка : 5
    Цикл без сортировки: 5
    Встроенная median: 5
    Гномья сортировка: 0.072...
    Опт. гномья сортировка : 0.028...
    Цикл: 0.005...
    Встроенная median: 0.001..
    
    Введите m: 60
    
    Гномья сортировка: 2.852
    Опт. гномья сортировка : 1.863
    Цикл: 0.180
    Встроенная median: 0.005
    
    При определении медианы встроенная функция самая быстрая. Увеличив кол-во элементов мы видим значительную разницу.
    """
