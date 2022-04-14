"""
Задание 2.*
Предложить еще какие-либо варианты (механизмы, подходы, библиотеки, идеи)
для оптимизации памяти и
доказать!!! (наглядно, кодом) их эффективность (на примере профилировщика).
С урока ничего не дублир-ть. только новые способы
"""


# Функция- декоратор для замера времени и памяти.
from timeit import default_timer

from memory_profiler import memory_usage




def decorator(func):
    def wrapper(*args, **kwargs):
        start_time = default_timer()
        m1 = memory_usage()
        res = func()
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        time_diff = default_timer() - start_time
        return res[0:20], mem_diff, time_diff
    return wrapper


"""
Гипотеза: одним из способов оптимизации работы скриптов с точки зрения использования памяти 
 является преобразование типов. Одним из наиболее экономичных способов является преобразование к string
"""


# Создадим список
@decorator
def get_lst():
    return list(el for el in range(10000000))


# Создадим tuple
@decorator
def get_tuple():
    return tuple(el for el in range(10000000))


# Создадим строку string
@decorator
def get_str():
    return f'{[el for el in range(10000000)]}'


if __name__ == '__main__':

    res, mem_diff, time_diff = get_lst()
    print(f"Выполнение get_lst() заняло {mem_diff} Mib и {time_diff} секунд. Результат работы: {res}")

    res, mem_diff, time_diff = get_tuple()
    print(f"Выполнение get_tuple() заняло {mem_diff} Mib и {time_diff} секунд. Результат работы: {res}")

    res, mem_diff, time_diff = get_str()
    print(f"Выполнение get_str() заняло {mem_diff} Mib и {time_diff} секунд. Результат работы: {res}")

"""
Получены результаты:

Выполнение get_lst() заняло 386.41796875 Mib и 0.6742064 секунд. 
Результат работы: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
Выполнение get_tuple() заняло 386.54296875 Mib и 0.6158059000000001 секунд. 
Результат работы: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19)
Выполнение get_str() заняло 85.7734375 Mib и 1.2316447 секунд. 
Результат работы: [0, 1, 2, 3, 4, 5, 6

Гипотеза подтвердилась. 
Из нюансов: необходимо обратить внимание, что строка экономнее по объему памяти и по сравнению со списком и по сравнению
с кортежем, однако ресурсов времени затрачивается на создание строки чуть больше. Возможно в связи с тем, что происходит 
преобразование в f строку.

Вывод: преобразование данных в строку совершенно определенно может использоваться для экономии ресурсов памяти.
"""