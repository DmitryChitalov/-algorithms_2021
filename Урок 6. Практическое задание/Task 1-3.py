# Задание №1 из Lesson-4 по алгоритмам.

"""
Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива
"""

from memory_profiler import memory_usage
from timeit import default_timer
from numpy import array


# Функция-декоратор для профилирования (память и время0
def info_memory(func):
    def wrapper(*args, **kwargs):
        start_time = default_timer()
        m1 = memory_usage()
        res_f = func(*args)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        time_diff = default_timer() - start_time
        return round(mem_diff, 4), round(time_diff, 4)
    return wrapper


# 1. Вариант с циклом - базовое условие


@info_memory
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


# 2. Вариант с list comprehension

@info_memory
def func_lc(nums):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


# 3. Генератор в список

@info_memory
def func_gen_list(nums):
    gen_index = (i for i in range(len(nums)) if nums[i] % 2 == 0)
    new_arr = [i for i in gen_index]  # можно было просто extend()
    return new_arr


# 4. Только генератор (если нет необходимости в массиве)

@info_memory
def func_only_gen(nums):
    new_arr_gen = (i for i in range(len(nums)) if nums[i] % 2 == 0)
    return new_arr_gen

# 5. Array из NumPy


@info_memory
def func_numpy(nums):
    new_arr = array([i for i in range(len(nums)) if nums[i] % 2 == 0])
    return new_arr


# Проверяем созданные функции.
n = list(range(1000000))

print("Цикл     - Время: {0}   Память: {1}".format(*func_1(n)))
print("LC       - Время: {0}   Память: {1}".format(*func_lc(n)))
print('Ген - LC - Время: {0}   Память: {1}'.format(*func_gen_list(n)))
print('Ген.     - Время: {0}   Память: {1}'.format(*func_only_gen(n)))
print('NumPy    - Время: {0}   Память: {1}'.format(*func_numpy(n)))

"""
Вывод:
В данном примере по памяти выигрывает генератор и NumPy. 
По скорости выигрывает NumPy, если нужен массив с готовыми данными, а если не нужен, то генератор. 


Результат замеров при n = 10 000 000:
Цикл     - Время: 20.0195   Память: 0.2964
LC       - Время: 18.4648   Память: 0.2782
Ген - LC - Время: 20.7617   Память: 0.3076
Ген.     - Время: 0.0   Память: 0.2132
NumPy    - Время: 1.9102   Память: 0.3254 
"""
