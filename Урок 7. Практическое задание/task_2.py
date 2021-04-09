"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Хотя в примерах к уроку уже есть вариант реализации слияния,
попробуйте предложить другой (придумать или найти)

И попытаться сделать замеры на массивах разной длины: 10, 100, 1000, ...

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
import random
from timeit import timeit


def merge(left, right):
    # Если первый массив пуст, то ничего не нужно
    # для объединения, и вы можете вернуть второй массив в качестве результата
    if len(left) == 0:
        return right

    # Если второй массив пуст, то ничего не нужно
    # для объединения, и вы можете вернуть первый массив как результат
    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    # Теперь перебираем оба массива, пока все элементы
    # превратить его в результирующий массив
    while len(result) < len(left) + len(right):
        # Элементы необходимо отсортировать, чтобы добавить их в
        # результирующий массив, поэтому вам нужно решить, получать ли
        # следующий элемент из первого или второго массива
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        # Если вы дойдете до конца любого массива, вы можете
        # добавляем оставшиеся элементы из другого массива в
        # результат и разорвать цикл
        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break

    return result


def merge_sort(array):
    # Если входной массив содержит менее двух элементов,
    # затем вернуть его как результат функции
    if len(array) < 2:
        return array

    midpoint = len(array) // 2

    # Сортировать массив, рекурсивно разделяя ввод
    # на две равные половины, каждую половину сортируя и объединяя
    # вместе в окончательный результат
    return merge(
        left=merge_sort(array[:midpoint]),
        right=merge_sort(array[midpoint:]))


numb = int(input('Введите число элементов: '))
test = [random.uniform(0, 50) for _ in range(numb)]
print(f'Исходный массив - {test}')
print(f'Отсортированный - {merge_sort(test)}')

a = [random.uniform(0, 50) for _ in range(10)]
b = [random.uniform(0, 50) for _ in range(100)]
c = [random.uniform(0, 50) for _ in range(1000)]
print('Выполнение на списке из 10 чисел', timeit('merge_sort(a)', globals=globals(), number=1000))
print('Выполнение на списке из 100 чисел', timeit('merge_sort(b)', globals=globals(), number=1000))
print('Выполнение на списке из 1000 чисел', timeit('merge_sort(c)', globals=globals(), number=1000))
