from collections import defaultdict
from random import randint


# гномья сортировка
def gnome_sort(array):
    i = 0
    while i < len(array):
        # если текущий элемент - нулевой, или больше предыдущего
        # сдвигаемся на следующий элемент
        if i == 0 or array[i] >= array[i - 1]:
            i += 1
        else:
            # иначе, меняем местами текущий элемент и предыдущий
            # сдвигаемся на предыдущий элемент
            array[i], array[i - 1] = array[i - 1], array[i]
            i -= 1

    return array


# сортировка Шелла
def shell_sort(array):
    # берём в качестве первоначального промежутка
    # сравнения элементов длину половины массива
    delta = len(array) // 2
    while delta > 0:
        # пока дельта больше нуля,
        # сравниваем элементы на текущем расстоянии
        for i in range(len(array) - delta):
            j = i
            while j >= 0 and array[j] > array[j + delta]:
                array[j], array[j + delta] = array[j + delta], array[j]
                j -= 1
        # уменьшаем расстояние между сравниваемыми элементами в 2 раза
        delta //= 2

    return array


# сортировка кучей
def heap_sort(array):

    # преобразуем подмассив в двоичную кучу
    # с текушей вершиной с индексом vertex
    # n - текущий размер массива
    def max_heap(arr, n, vertex):
        largest = vertex             # индекс текущей вершины
        left = 2 * vertex + 1        # индекс левого элемента
        right = 2 * vertex + 2       # индекс правого элемента

        # если у вершины есть потомок, больший, чем она
        # меняем их местами
        if left < n and arr[largest] < array[left]:
            largest = left
        if right < n and arr[largest] < array[right]:
            largest = right
        if largest != vertex:
            arr[vertex], arr[largest] = arr[largest], arr[vertex]
            # если порядок элементов изменился, перестраиваем кучу
            # для вершины с новым значением
            max_heap(arr, n, largest)

    # начиная с конца массива, преобразовываем его в кучу
    for i in range(len(array), -1, -1):
        max_heap(array, len(array), i)

    # вытаскиваем верхний (наибольший) элемент из кучи
    # и ставим его на последнее место в массиве.
    # Перестраиваем кучу для нового верхнего элемента,
    # уменьшив её длину на 1
    for i in range(len(array) - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        max_heap(array, i, 0)

    return array


# Сортировка подсчётом
def count_sort(array):
    # подсчитываем количесиво вхождений
    # каждого значения в массив
    el_count = defaultdict(int)
    for i in array:
        el_count[i] += 1
    array = []

    # достаём минимальное значение и
    # добавляем его в массив столько раз, сколько оно встретилось
    while el_count:
        val = min(el_count)
        for _ in range(el_count[val]):
            array.append(val)
        el_count.pop(min(el_count))

    return array


if __name__ == '__main__':

    test_lst = [randint(0, 10) for _ in range(25)]
    print(f'ORIGIN:\n{test_lst}')
    print()
    print(f'gnome_sort:\n{gnome_sort(test_lst[:])}')
    print(f'shell_sort:\n{shell_sort(test_lst[:])}')
    print(f'heap_sort:\n{heap_sort(test_lst[:])}')
    print(f'count_sort:\n{count_sort(test_lst[:])}')
