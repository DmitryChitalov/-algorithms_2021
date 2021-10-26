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
import timeit
import random


def merge_sort(lst_obj):
    if len(lst_obj) > 1:
        center = len(lst_obj) // 2
        left = lst_obj[:center]
        right = lst_obj[center:]

        merge_sort(left)
        merge_sort(right)

        # перестали делить
        # выполняем слияние
        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst_obj[k] = left[i]
                i += 1
            else:
                lst_obj[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lst_obj[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst_obj[k] = right[j]
            j += 1
            k += 1
        return lst_obj


if __name__ == "__main__":

    num_iter = int(input('Введите размер массива: '))
    a, b = 0, 50  # параметры массива
    orig_list = [random.uniform(a, b) for _ in range(num_iter)]
    print(f'Исходный список: \n{orig_list}')
    print(f'Отсортированный список: \n{merge_sort(orig_list[:])}')

    """Замеры времени выполнения на массивах разной длины"""

    for i in range(3):

        t = 10 ** (i + 1)  # Кол-во повторений замеров
        orig_list = [random.uniform(a, b) for _ in range(t)]
        # замеры выполняем на копии массива
        print(f'Результаты замеров на массиве: {t}: '
              f'{timeit.timeit("merge_sort(orig_list[:])", globals=globals(), number=1000)}, сек.')


