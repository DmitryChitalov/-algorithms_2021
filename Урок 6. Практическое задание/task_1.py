"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять задачи с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""

"""Для списка реализовать обмен значений соседних элементов. Значениями обмениваются
элементы с индексами 0 и 1, 2 и 3 и т. д."""
from memory_profiler import profile, memory_usage
from functools import reduce
from random import randint
from numpy import array
from timeit import default_timer


def my_decorator(func):
    def wrapper(*args, **kwargs):
        start = default_timer()
        m1 = memory_usage()
        m2 = memory_usage()
        end = default_timer()
        my_time = end - start
        mem_diff = m2[0] - m1[0]
        print(f"Потраченная память {mem_diff}, Потраченое время {my_time}")
        return my_time, mem_diff
    return wrapper


@my_decorator
@profile
def first_func(my_list):
    y = 0                                                           # Mem usage 34.2 MiB Increment 0.0 MiB
    for el in range(int(len(my_list)) // 2):                        # Mem usage 34.2 MiB Increment 0.0 MiB
        my_list[y], my_list[y + 1] = my_list[y + 1], my_list[y]     # Mem usage 34.2 MiB Increment 0.0 MiB
        y += 2                                                      # Mem usage 34.2 MiB Increment 0.0 MiB
    return my_list                                                  # Mem usage 34.2 MiB Increment 0.0 MiB


first_func(list(range(100000)))



@my_decorator
@profile
def rework_first_func(my_list):
    y = 0                                                        # Mem usage 31.2 MiB Increment 0.0 MiB
    for el in range(int(len(my_list)) // 2):                     # Mem usage 31.2 MiB Increment 0.0 MiB
        my_list[y], my_list[y + 1] = my_list[y + 1], my_list[y]  # Mem usage 31.2 MiB Increment 0.0 MiB
        y += 2                                                   # Mem usage 31.2 MiB Increment 0.0 MiB
    return my_list


rework_first_func(array(list(range(100000))))
"""В данной задаче было реализована замена элементов списков рядо стоящих, к примеру 1 с 2, 3 с 4.
В изначальном варианте в функцию передавал просто генератор списка что после профилирования показало Mem usage 34.2 MiB.
Было решено оптимизировать память c помошью numpy и его функцию array которая сократила задействуную память до 31.2 MiB.
который сжимает массив достигая экономии. По замерам моего декоратора 1_функция Потраченная память 0.00390625, 
Потраченое время 0.2229214, Вторая функция Потраченная память 0.0, Потраченое время 0.22279589999999994. Если брать 
во внимание скорость выполнения, то все доработанные версии работают не много быстрее.
"""



@my_decorator
@profile
def second_func(old_list):
    gen_list = [old_list[el + 1] for el in range(len(old_list) - 1)
                if old_list[el] < old_list[el + 1]]                      # Mem usage 34.1 MiB Increment 1.0 MiB
    return gen_list


second_func([randint(100, 1000) for _ in range(100000)])


@my_decorator
@profile
def rework_second_func(my_list):
    new_list = array([my_list[el + 1] for el in range(len(my_list) - 1)
                      if my_list[el] < my_list[el + 1]])                  # Mem usage 33.0 MiB Increment 0.8 MiB
    return new_list                                                       # Mem usage 32.2 MiB Increment -0.8 MiB


rework_second_func(array([randint(100, 1000) for _ in range(100000)]))

"""Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента. 
Изменения в исходной функции были проведены такие же как и в первой функции, 
numpy все так же хорошо отработал, тут же можно заметить что появились цифры в энкримент, поскольку 
внутри списка есть лист комперхеншен который так же был ускорен при помощи numpy, в первом варианте инкремент равен 1.0,
в доработаном варианте 0.8."""

@my_decorator
@profile
def third_func(my_list):
    for el in range(len(my_list)- 1):
        if my_list[el] > my_list[el + 1]:
            my_list[el], my_list[el + 1] = my_list[el + 1], my_list[el]          # Mem usage 32.5 Increment 0.0 MiB
        return my_list[-1]


print(third_func([randint(1, 100) for _ in range(100000)]))


@my_decorator
@profile
def rework_third_func(my_list):
    for el in range(len(my_list) - 1):
        if my_list[el] > my_list[el + 1]:
            my_list[el], my_list[el + 1] = my_list[el + 1], my_list[el]           # Mem usage 30.8 Increment 0.0 MiB
        return my_list[-1]


print(rework_third_func(array([randint(1, 100) for _ in range(100000)])))

"""Необходимо вывести наибольший элемент списка. 
Изменения в исходной функции были проведены такие же как и в первой функции добавление array из numpy, 
numpy все так же хорошо отработал."""