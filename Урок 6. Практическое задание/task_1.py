"""
Задание 1.

Выполните профилирование памяти в скриптах.
Проанализируйте результат и определите программы с
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
from memory_profiler import memory_usage


def memory_profile(func):
    def wrapper(*args):
        start_time = default_timer()
        start_memory = memory_usage()
        func(*args)
        end_time = default_timer()
        end_memory = memory_usage()
        print(f'затраты времени: {end_time - start_time}\nзатраты памяти: {end_memory[0] - start_memory[0]}')

    return wrapper


# Первый скрипт

@memory_profile
def even_odd_count_recur(usr_num):
    def recur_wrap(num, even=0, odd=0):
        if num == 0:
            return f'Количество четных и нечетных цифр в числе равно: ({even}, {odd})'
        else:
            operand = num % 10
            if operand % 2 == 0:
                even += 1
            else:
                odd += 1
            recur_wrap(num // 10, even, odd)

    return recur_wrap(usr_num)


@memory_profile
def even_odd_count_cycle(usr_num, even=0, odd=0):
    while usr_num != 0:
        operand = usr_num % 10
        if operand % 2 == 0:
            even += 1
        else:
            odd += 1
        usr_num = usr_num // 10
    return f'Количество четных и нечетных цифр в числе равно: ({even}, {odd})'


testing_num = 123456789987654321
even_odd_count_recur(testing_num)
even_odd_count_cycle(testing_num)

'''
затраты времени: 0.09956509600000002
затраты памяти: 0.00390625
затраты времени: 0.09992120000000004
затраты памяти: 0.0

первая функция требует большего объема памяти из-за рекурсии,
вторая функция реализована при помощи цикла и требуемый объем памяти меньше.
'''


# Второй скрипт


@memory_profile
def lc_creating(quantity):
    return [i for i in range(quantity)]


@memory_profile
def gener_creating(quantity):
    numbers_list = list(range(quantity))
    for i in numbers_list:
        yield i


print('')
lc_creating(1000000)
gener_creating(1000000)

'''
затраты времени: 0.188461011
затраты памяти: 0.09765625
затраты времени: 0.09994687899999999
затраты памяти: 0.0

в данном примере наглядно видна эффективность ленивых вычислений, 
генератор экономнее расходует память, чем списковое включение 
'''


# Третий скрипт


@memory_profile
def iter_foo(lst):
    for i in range(len(lst)):
        lst[i] = str(lst[i])
    return lst


@memory_profile
def map_foo(lst):
    return list(map(str, lst))


print('')
nums_list = [x*2 for x in range(10000)]
iter_foo(nums_list)
map_foo(nums_list)

'''
затраты времени: 0.10506041200000005
затраты памяти: 0.3203125
затраты времени: 0.10208349800000005
затраты памяти: 0.109375

вторая функция оптимизирована при помощи встроенной функции map и требует меньше памяти и меньше времени
'''
