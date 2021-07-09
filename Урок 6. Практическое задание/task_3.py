"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение
"""
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


@decor
def get_number(num, even_num=0, odd_num=0):
    return f'Количество четных и нечетных цифр в числе равно: {even_num, odd_num}' if num == 0 else \
        get_number(num // 10, even_num + 1, odd_num) \
        if num % 2 == 0 else get_number(num // 10, even_num, odd_num + 1)


@decor
def func_1():
    def get_number_1(num, even_num=0, odd_num=0):
        return f'Количество четных и нечетных цифр в числе равно: {even_num, odd_num}' if num == 0 else \
            get_number_1(num // 10, even_num + 1, odd_num) \
            if num % 2 == 0 else get_number_1(num // 10, even_num, odd_num + 1)


if __name__ == '__main__':
    res, m_usage, r_time = get_number(21421421421321)
    print(f"Выполнение функции func_1 по памяти {m_usage} Mib и {r_time} сек")
if __name__ == '__main__':
    res, m_usage, r_time = func_1()
    print(f"Выполнение функции func_1 по памяти {m_usage} Mib и {r_time} сек")

"""
Вывод:скрипты с рекусрсией профилировать можно, но перед этим необходимо обернуть функцию
с рекурсией в другую функцию, иначе, мы получим недостоверные данные
"""