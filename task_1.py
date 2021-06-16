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
from memory_profiler import memory_usage
from timeit import default_timer
import numpy as np


def memory_time_profiler(func):
    def wrapper(*args, **kwargs):
        time1 = default_timer()
        mem1 = memory_usage()
        res = func(*args, **kwargs)
        diff_mem = memory_usage()[0] - mem1[0]
        diff_time = default_timer() - time1
        print(f'Функция {func.__name__}')
        return res, diff_mem, diff_time

    return wrapper


# Скрипт 1
# Оптимизация - ленивые вычисления
@memory_time_profiler
# for, append
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


@memory_time_profiler
# lambda
def func_2(nums):
    return [lambda i: nums[i] % 2 == 0, range(len(nums))]


if __name__ == '__main__':
    res, mem_diff, time_diff = func_1(list(range(100000)))
    print(f'Время выполнения функции: {time_diff}\nИспользуемая память: {mem_diff} MiB')
    print('\n')
    res, mem_diff, time_diff = func_2(list(range(100000)))
    print(f'Время выполнения функции: {time_diff}\nИспользуемая память: {mem_diff} MiB')
    print('_' * 50)
'''
Функция func_1
Время выполнения функции: 0.22402160000000004
Используемая память: 2.12890625 MiB

Функция func_2
Время выполнения функции: 0.21940800000000005
Используемая память: 0.0 MiB

lambda  функция выполнилась быстрее и не расходует память и упрощает код
'''


# Скрипт 2
# Оптимизация - слоты в ООП
class Worker():
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_position(self):
        return self.position


class WorkerNew():
    __slots__ = ('name', 'surname', 'position')

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_position(self):
        return self.position


@memory_time_profiler
def main():
    print('без slots')
    w = Worker('Ivan', 'Ivanov', 'middle')
    print(f'Полное имя {w.get_full_name()}, позиция {w.get_position()}')
    return w


@memory_time_profiler
def main_new():
    print('slots')
    w_new = WorkerNew('Ivan', 'Ivanov', 'middle')
    print(f'Полное имя {w_new.get_full_name()}, позиция {w_new.get_position()}')
    return w_new


if __name__ == '__main__':
    main()
    print(f'Время выполнения функции: {time_diff}\nИспользуемая память: {mem_diff} MiB')
    print('\n')
    main_new()
    print(f'Время выполнения функции: {time_diff}\nИспользуемая память: {mem_diff} MiB')
    print('_' * 50)

'''
без slots
Полное имя Ivan Ivanov, позиция middle
Функция main
Время выполнения функции: 0.21546949999999998
Используемая память: 0.00166665 MiB


slots
Полное имя Ivan Ivanov, позиция middle
Функция main_new
Время выполнения функции: 0.2249543999999994
Используемая память: 0.0 MiB

использование __slots__ несколько оптимизирует по использованию памяти, но при этом увеличило время рабрты скрипта
'''

# Скрипт 2
# Оптимизация - NumPy
array = [1, 3, 1, 3, 4, 5, 1]


@memory_time_profiler
def func_cycle():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


@memory_time_profiler
def func_np():
    counts = np.bincount(array)
    elem = np.argmax(counts)
    max_2 = max(counts)
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'

if __name__ == '__main__':
    res, mem_diff, time_diff = func_cycle()
    print(f'Время выполнения функции: {time_diff}\nИспользуемая память: {mem_diff} MiB')
    print('\n')
    res, mem_diff, time_diff = func_np()
    print(f'Время выполнения функции: {time_diff}\nИспользуемая память: {mem_diff} MiB')
    print('_' * 50)

'''
Функция func_cycle
Время выполнения функции: 0.22077659999999977
Используемая память: 0.0 MiB


Функция func_np
Время выполнения функции: 0.22284939999999986
Используемая память: 0.0234375 MiB  

Использование библиотеки numpy не дало ожидаемой оптимизации
неисключено, сто эффект будет на больших объемах данных
'''