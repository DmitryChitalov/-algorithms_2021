"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Хотя в примерах к уроку уже есть вариант реализации слияния,
попробуйте предложить другой (придумать или найти).

И попытаться сделать замеры на массивах разной длины: 10, 100, 1000, ...

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
import random
import operator
import timeit


def merge_sort(lst):
    if len(lst) < 2:
        return lst[:]
    else:
        middle = len(lst) // 2
        left = merge_sort(lst[:middle])
        right = merge_sort(lst[middle:])
        return merge(left, right)


def merge(left, right, compare=operator.lt):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


if __name__ == '__main__':
    orig_list = [random.randint(0, 50) for _ in range(100)]
    print('original list', orig_list)
    print('list sorted', merge_sort(orig_list[:]))
    print('sorted time', timeit.repeat('merge_sort(orig_list[:])', globals=globals(), number=(10**3)))
    orig_list = [random.randint(0, 50) for _ in range(1000)]
    print('sorted time', timeit.repeat('merge_sort(orig_list[:])', globals=globals(), number=(10 ** 3)))

""" Вывод:
sorted time [0.91843727, 0.528493672, 0.6594666069999999, 0.6340946780000003, 0.6043876589999999]
sorted time [9.989367258000001, 7.471268562000001, 7.215951621999999, 7.155767270000002, 7.267884308000006]
Выполняется значительно быстрее чем методом пузырька
Я не понимаю, почему на списке больше 1000 данный метод работает, ведь у рекурсии максимум 1000 вызывов
"""