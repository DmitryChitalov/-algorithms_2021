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


#  Функция декоратор для замера времени и памяти
import random
from timeit import default_timer

import memory_profiler


def decorator(func):
    def wrapper(*args, **kwargs):
        start_time = default_timer()
        m1 = memory_profiler.memory_usage()
        res = f'{func(*args, **kwargs)}'
        m2 = memory_profiler.memory_usage()
        mem_result = m2[0] - m1[0]
        time_result = default_timer() - start_time
        # Устанавливаем на тестовом режиме 30 цифр для вывода результатов.
        # После увеличения массива до 1000 - ставим ограничитель на вывод рузельтатов
        return res, mem_result, time_result
    return wrapper


# Создаем массивы случафных цифр
num_lst_10 = list(random.randrange(0, 50) + random.random() for el in range(10))
num_lst_100 = list(random.randrange(0, 50) + random.random() for i in range(100))
num_lst_1000 = list(random.randrange(0, 50) + random.random() for num in range(1000))


"""
В задании предложено придумать или найти алгоритмы, отличные от того, что был на уроке. 
Нашел гибридный рабочий вариант. 
источник: https://gist.github.com/nandajavarma/a3a6b62f34e74ec4c31674934327bbd3
Немного переделал его.
В комментариях обнаружил, что алгоритм не совсем timsort
"""


def binary_search(the_array, item, start, end):
    if start == end:
        if the_array[start] > item:
            return start
        else:
            return start + 1
    if start > end:
        return start

    mid = (start + end) // 2
    if the_array[mid] < item:
        return binary_search(the_array, item, mid + 1, end)
    elif the_array[mid] > item:
        return binary_search(the_array, item, start, mid - 1)
    else:
        return mid


"""
Insertion sort that the heap sort uses if the array size is small or if
the size of the "run" is small
"""


def insertion_sort(the_array):
    l = len(the_array)
    for index in range(1, l):
        value = the_array[index]
        pos = binary_search(the_array, value, 0, index - 1)
        the_array = the_array[:pos] + [value] + the_array[pos:index] + the_array[index+1:]
    return the_array


def merge(left, right):
    """Takes two sorted lists and returns a single sorted list by comparing the
    elements one at a time.
    [1, 2, 3, 4, 5, 6]
    """
    if not left:
        return right
    if not right:
        return left
    if left[0] < right[0]:
        return [left[0]] + merge(left[1:], right)
    return [right[0]] + merge(left, right[1:])


@decorator
def timsort(array):
    the_array = array.copy()
    runs, sorted_runs = [], []
    l = len(the_array)
    new_run = [the_array[0]]
    for i in range(1, l):
        if i == l-1:
            new_run.append(the_array[i])
            runs.append(new_run)
            break
        if the_array[i] < the_array[i-1]:
            if not new_run:
                runs.append([the_array[i-1]])
                new_run.append(the_array[i])
            else:
                runs.append(new_run)
                new_run = [the_array[i]]
        else:
            new_run.append(the_array[i])
    for each in runs:
        sorted_runs.append(insertion_sort(each))
    sorted_array = []
    for run in sorted_runs:
        sorted_array = merge(sorted_array, run)
    return str(sorted_array)


# Результаты работы функций

if __name__ == '__main__':
    print('Создаем массивы случафных цифр. В выводе не более 10 цифр.')
    print(num_lst_10)
    print(num_lst_100[0:10])
    print(num_lst_1000[0:10])

    print(f"{'-' * 20}")
    res, mem_result, time_result = timsort(num_lst_10)
    print(f"Выполнение timsort(num_lst_10) заняло {mem_result} Mib и {time_result} секунд.\n Результат работы: {res}")
    res, mem_result, time_result = timsort(num_lst_100)
    print(f"Выполнение timsort(num_lst_100) заняло {mem_result} Mib и {time_result} секунд.\n Результат работы: {res}")
    res, mem_result, time_result = timsort(num_lst_1000)
    print(f"Выполнение timsort(num_lst_1000) заняло {mem_result} Mib и {time_result} секунд.\n Результат работы: {res}")

"""
Исходные данные:
Создаем массивы случафных цифр. В выводе не более 10 цифр.
[6.069407845376518, 14.468567357663304, 20.634655164484883, 16.07866501048697, 25.895886604371455, 9.100088270707019, 
45.488643023183066, 13.096441999481645, 44.70104705958712, 13.484084553517782]
[48.39684064271198, 13.658756159579742, 23.441771668935736, 28.40877955765154, 8.945394627661967, 11.831254494810759, 
7.8539945705583065, 16.52769487255558, 2.8941929413644596, 10.21255677341739]........
[25.208221632656812, 11.658750787277153, 38.83092400837052, 11.675009137828713, 46.2480310577934, 36.24207143710703, 
30.59148619316661, 41.68557864715291, 22.972992346815364, 34.60329177594517]...........................

Выполнение timsort(num_lst_10) заняло 0.01171875 Mib и 0.21817549999999997 секунд.
[6.069407845376518, 9.100088270707019, 13.096441999481645, 13.484084553517782, 14.468567357663304, 16.07866501048697, 
20.634655164484883, 25.895886604371455, 44.70104705958712, 45.488643023183066]

Выполнение timsort(num_lst_100) заняло 0.07421875 Mib и 0.21628990000000003 секунд.
[0.1839007641624274, 0.31773367897080784, 0.48257229839826044, 0.5725965117573201, 1.0441464342197198, 
1.5004468977209047, 1.5859326310274109, 2.6162646213547003, 2.8941929413644596, 3.11238645245307.........

Выполнение timsort(num_lst_1000) заняло 2.33203125 Mib и 0.8044547000000001 секунд.
[0.07370560969997597, 0.07530775998699113, 0.1647833903606577, 0.16541572671739313, 0.18000387402000273, 
0.18863008963224248, 0.22667565144126045, 0.24318106087542335, 0.2992279556407791, 0.42516362517354644,.............


По существу - это вообще не простое задание.
"""
