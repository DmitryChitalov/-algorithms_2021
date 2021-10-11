from memory_profiler import memory_usage
from timeit import default_timer
from numpy import array


def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        start_time = default_timer()
        res = func(args[0])
        time_diff = default_timer() - start_time
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff, time_diff

    return wrapper

# Курс основ.


cubes_list = []


# solution
@decor
def func1(lst):
    for i in lst:
        if i % 2 != 0:
            cubes_list.append(i ** 3)
    return cubes_list


# first optimization (numpy array)
@decor
def func2(arr):
    lst_obj = array([i ** 3 for i in arr if i % 2 != 0])
    return lst_obj


# second optimization (generator)
@decor
def func3(numbers):
    for num in numbers:
        if num % 2 != 0:
            yield num ** 3


if __name__ == '__main__':
    test1, m_diff, t_diff = func1(list(range(10000)))

    print(f"Использование памяти func1: {m_diff} Mib")
    print(f'Время выполнения func1: {t_diff}')

    test2, m_diff2, t_diff2 = func2(list(range(10000)))

    print(f"Использование памяти func2: {m_diff2} Mib")
    print(f'Время выполнения func2: {t_diff2}')

    test3, m_diff3, t_diff3 = func3(list(range(10000)))

    print(f"Использование памяти func3 {m_diff3} Mib")
    print(f'Время выполнения func3: {t_diff3}')

    """
    Выполнение func1 заняло 0.24609375 Mib
    Время выполнения func1: 0.01087586300127441
    Выполнение func2 заняло 0.2421875 Mib
    Время выполнения func2: 0.013716818000830244
    Выполнение func3 заняло 0.0 Mib
    Время выполнения func3: 1.2520999007392675e-05
    
   
    1) Использование объекта array из библиотеки numpy чуть меньше занимает памяти 
    2) Использование генератора и выполнение функции заняло 0.0 Mib
    
    В данном примере наиболее эффективным оказалось использование генератора с помощью него
     расход памяти удалось минимизировать.
    
    """