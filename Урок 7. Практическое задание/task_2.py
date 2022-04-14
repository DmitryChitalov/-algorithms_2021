"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Хотя в примерах к уроку уже есть вариант реализации слияния,
попробуйте предложить другой (придумать или найти).

И попытаться сделать замеры на массивах разной длины: 10, 100, 1000, ...

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806,
8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644,
41.62921998361278, 46.11436617832828]
"""
from timeit import default_timer
from random import uniform

"""
Я выбрала вариант реализации прямого слияния, известного, как алгоритм Боуза-Нельсона.
Замеры показывают, что при увеличении числа на 1 порядок, скорость выполнения операции сортировки
падает примерно в 35-38 раз.
"""


def decor(func):
    """ Decorator for measuring time"""
    def wrapper(*args):
        start_time = default_timer()
        res = func(args[0])
        print(f"Время выполнения функции при {len(args[0])} заданных элементах: "
              f"{(default_timer() - start_time):.5f}")
        return res
    return wrapper


def merge_processing(c, d, e, some_data):
    """ Basic sorting actions"""
    if c + d < len(some_data):
        if e == 1:
            if some_data[c] > some_data[c + d]:
                some_data[c], some_data[c + d] = some_data[c + d], some_data[c]
        else:
            e = e // 2
            merge_processing(c, d, e, some_data)
            if c + d + e < len(some_data):
                merge_processing(c + e, d, e, some_data)
            merge_processing(c + e, d - e, e, some_data)
    return some_data


@decor
def main_merge_b_n(data):
    """Initial stage of sorting"""
    b = 1
    while b < len(data):
        a = 0
        while a + b < len(data):
            merge_processing(a, b, b, data)
            a = a + b + b
        b = b + b
    return data


def start():
    """Starting function"""
    while True:
        try:
            my_lenght = int(input("Введите число элементов, число должно быть не меньше 2: "))
            if my_lenght < 2:
                raise ValueError
            break
        except ValueError:
            print('Требуется положительное целое число больше 2. Попробуйте еще раз')
    my_rand_list = [uniform(0, 50) for i in range(my_lenght)]
    print(f"Исходный массив - {my_rand_list}")
    res = main_merge_b_n(my_rand_list)
    print(f"Отсортированный массив - {res}")


start()
