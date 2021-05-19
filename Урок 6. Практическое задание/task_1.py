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
from random import randint
from memory_profiler import memory_usage
from timeit import default_timer


# Создадим декоратор для замера затрат времени и памяти.

def time_memory_profile(func):
    def wrapper(*args):
        start_time = default_timer()
        start_memory = memory_usage()
        res = func(*args)
        end_time = default_timer()
        end_memory = memory_usage()
        print(f'Затрачено на вызов функции {func.__name__}:'
              f'\nЗатраты времени: {end_time - start_time} сек.'
              f'\nЗатраты памяти: {end_memory[0] - start_memory[0]} MiB')
        return res

    return wrapper


# 1 Сравним затраты при обращении к списку через цикл и через генератор.

@time_memory_profile
def some_loop(num):
    numbers_list = list(range(num))
    for i in numbers_list:
        return i


@time_memory_profile
def some_gen(num):
    numbers_list = list(range(num))
    for i in numbers_list:
        yield i


some_loop(1000000)
some_gen(1000000)

'''
По результатам видно, что генератор не занимает место в памяти, а также выиграывает по скорости.
Затрачено на вызов функции some_loop:
Затраты времени: 0.1411718 сек.
Затраты памяти: 0.26171875 MiB
Затрачено на вызов функции some_gen:
Затраты времени: 0.10907920000000004 сек.
Затраты памяти: 0.0 MiB
'''


# 2 Сравним преобразование списка чисел int to str через цикл и встроенную функию map.

test_lst = [i for i in range(10000000)]


@time_memory_profile
def some_loop2(lst):
    for i in range(len(lst)):
        lst[i] = str(lst[i])
    return lst


@time_memory_profile
def some_bif(num):
    return list(map(str, num))


some_loop2(test_lst)
some_bif(test_lst)

'''
По результатам видно, что фунция с применением map оптимизирована и требует меньше памяти и времени.
Затрачено на вызов функции some_loop2:
Затраты времени: 3.0810065 сек.
Затраты памяти: 310.15625 MiB
Затрачено на вызов функции some_bif:
Затраты времени: 1.3347718999999998 сек.
Затраты памяти: 76.7734375 MiB
'''

# 3 Сравним переворачивание числа через рекурсию и через срез списка.

reverse_num = randint(10**10, 10**100)


@time_memory_profile
def reverse_num_rec(num_to_rev):
    def rev_num(number, reverse_digits_list=None):
        if reverse_digits_list is None:
            reverse_digits_list = []

        digit = number % 10
        new_number = number // 10

        reverse_digits_list.append(digit)

        if new_number == 0:
            result = ''
            for number in reverse_digits_list:
                result += str(number)

            return result

        rev_num(new_number, reverse_digits_list)

    return rev_num(num_to_rev)


@time_memory_profile
def reverse_num_slice(number):
    return str(number)[::-1]


reverse_num_rec(reverse_num)

reverse_num_slice(reverse_num)

'''
По результатам видно, что фунция с применением срезов выигрывает в памяти у рекурсии,
т.к. нет необходимости хранить в памяти промежуточные результаты.
Затрачено на вызов функции reverse_num_rec:
Затраты времени: 0.10804889999999999 сек.
Затраты памяти: 0.1328125 MiB
Затрачено на вызов функции reverse_num_slice:
Затраты времени: 0.10850369999999998 сек.
Затраты памяти: 0.0 MiB
'''
