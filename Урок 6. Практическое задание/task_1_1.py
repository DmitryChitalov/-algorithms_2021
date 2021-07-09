"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять только домашние задания с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""
from timeit import default_timer
import memory_profiler


def decor(func):
    def wrapper(*args):
        start_time = default_timer()
        m1 = memory_profiler.memory_usage()
        res = func(args[0])
        m2 = memory_profiler.memory_usage()
        memory_usage = m2[0] - m1[0]
        run_time = default_timer() - start_time
        return res, memory_usage, run_time
    return wrapper


"""
Задача № 1
Получение списка чётных чисел
"""
numbers = [i for i in range(10000)]


# Реализация без оптимизации
@decor
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


# Реализация без оптимизации
@decor
def func_2(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


# Реализация с наиболее эффективным использованием памяти
@decor
def func_3(nums):
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            yield i


if __name__ == '__main__':
    result, m_usage, r_time = func_1(numbers)
    print(f"Выполнение функции func_1 по памяти {m_usage} Mib и {r_time} сек")
if __name__ == '__main__':
    result, m_usage, r_time = func_2(numbers)
    print(f"Выполнение функции func_2 по памяти {m_usage} Mib и {r_time} сек")
if __name__ == '__main__':
    result, m_usage, r_time = func_3(numbers)
    print(f"Выполнение функции func_3 по памяти {m_usage} Mib и {r_time} сек")

"""
Выполнение функции func_1 по памяти 0.2109375 Mib и 0.20199579999999995 сек
Выполнение функции func_2 по памяти 0.18359375 Mib и 0.20111630000000003 сек
Выполнение функции func_1 по памяти 0.0 Mib и 0.20078050000000014 сек

Вывод: реализация решения через функцию-генератор с ключевым словом yield позволила
значительно сократить объем используемой памяти, поэтому, func_3 мы используем, если необходимо
скоратить объем используемой памяти
"""
