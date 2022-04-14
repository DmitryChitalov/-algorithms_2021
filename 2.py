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
from random import uniform
from timeit import timeit

my_l1 = [uniform(0, 50) for q in range(10)]
my_l2 = [uniform(0, 50) for t in range(100)]
my_l3 = [uniform(0, 50) for c in range(1000)]


def s_sort(lister):
    c_lister = lister.copy()
    if len(lister) > 1:
        mid = len(lister) // 2
        left = lister[:mid]
        right = lister[mid:]
        s_sort(left)
        s_sort(right)
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lister[k] = left[i]
                i += 1
            elif left[i] > right[j]:
                lister[k] = right[j]
                j += 1
            else:
                lister[k] = left[i]
                i += 1
            k += 1
        while j < len(right):
            lister[k] = right[j]
            j += 1
            k += 1
        while i < len(left):
            lister[k] = left[i]
            i += 1
            k += 1
        return f'Длина :{len(lister)} \nИсходный : {c_lister}\nОтсортированный : {lister}'


print(timeit('s_sort(my_l1)', number=1000, globals=globals()))
# 0.0465649
print(timeit('s_sort(my_l2)', number=1000, globals=globals()))
# 0.8524904
print(timeit('s_sort(my_l3)', number=1000, globals=globals()))
# 12.0570294
'''Я посмотрел некоторые способы реализации  данной сортировки , но заметил что все они основаны на одном и том же 
принципе.(Они идентичные). Я выбрал вариант с урока ,(мне понравилось , что здесь всё врамках одной функции и она 
более оптимальная(по пониманию кода)) поняв принцип работы , я сам сделал данную сортировку и полностью разобрался в 
ней. '''
