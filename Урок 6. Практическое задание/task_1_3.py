from timeit import default_timer
import memory_profiler


def decor(func):
    def wrapper(*args):
        start_time = default_timer()
        m1 = memory_profiler.memory_usage()
        res = func(*args)
        m2 = memory_profiler.memory_usage()
        memory_usage = m2[0] - m1[0]
        run_time = default_timer() - start_time
        return res, memory_usage, run_time

    return wrapper


"""
Задача № 3.
Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
"""


@decor
def func_1():
    def get_number(num=262519123214214312412412412, even_num=0, odd_num=0):
        return f'Количество четных и нечетных цифр в числе равно: {even_num, odd_num}' if num == 0 else \
            get_number(num // 10, even_num + 1, odd_num) \
            if num % 2 == 0 else get_number(num // 10, even_num, odd_num + 1)


@decor
def func_2(num=262519123214214312412412412):
    even_numb = 0
    odd_numb = 0
    num = str(num)
    for i in num:
        if int(i) % 2 == 0:
            even_numb += 1
        else:
            odd_numb += 1
    return f'Количество четных и нечетных цифр в числе равно: {even_numb, odd_numb}'


if __name__ == '__main__':
    result, m_usage, r_time = func_1()
    print(f"Выполнение функции func_1 по памяти {m_usage} Mib и {r_time} сек")
if __name__ == '__main__':
    result, m_usage, r_time = func_2()
    print(f"Выполнение функции func_2 по памяти {m_usage} Mib и {r_time} сек")

"""
Выполнение функции func_1 по памяти 0.0078125 Mib и 0.2003455999999999 сек
Выполнение функции func_2 по памяти 0.0 Mib и 0.20002489999999995 сек

Вывод: уход от рекурсий также является способом оптимизации памяти.
"""
