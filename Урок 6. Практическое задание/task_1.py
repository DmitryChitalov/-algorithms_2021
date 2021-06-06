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
from collections import Counter


def memory_and_time(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        t1 = default_timer()
        res = func(args[0])
        t2 = default_timer()
        m2 = memory_usage()
        time_diff = t2 - t1
        mem_diff = m2[0] - m1[0]

        print(f'Memory used: {round(mem_diff, 3)} MiB, wasted time: {round(time_diff, 3)} sec')
        return res

    return wrapper


# 1 Задача до
@memory_and_time
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


func_1(range(100000))


# 1 Задача после
@memory_and_time
def optimized_func_1(nums):
    return [i for i, num in enumerate(nums) if not num % 2]


optimized_func_1(range(100000))


# Выводы по 1 задаче. За счет генератора 2 функция работает намного быстрее и потребляет меньше памяти.
# В первой функции создается пустой список и в него добавляются четные элементы и поэтому он занимет больше памяти.

# Memory used: 2.074 MiB, wasted time: 0.121 sec - РЕЗУЛЬТАТЫ 1 ФУНКЦИИ
# Memory used: 1.285 MiB, wasted time: 0.078 sec - РЕЗУЛЬТАТЫ 2 ФУНКЦИИ


# 2 Задача до

@memory_and_time
def inverted_number(n, my_lst=[]):
    if n == 0:
        my_lst = ''.join(str(x) for x in my_lst)
        return my_lst
    else:
        c = n % 10
        my_lst.append(c)
        n = n // 10
        return inverted_number(n)


number = 683874834903
my_lst = inverted_number(number)


# 2 задача после

@memory_and_time
def inverted_number_2(nn):
    lst = []
    while nn > 0:
        c = nn % 10
        lst.append(c)
        nn = nn // 10
    lst = ''.join(str(x) for x in lst)
    return lst


nn = 683874834903
inverted_number_2(nn)

# Вывод по 2 задаче: Рекурсия требует больше памяти, так как при ее работе хранится стек вызовов.
# В то время как во втором решении мы используемся цикл.

# Memory used: 0.023 MiB, wasted time: 2.511 sec  - РЕЗУЛЬТАТЫ 1 ФУНКЦИИ
# Memory used: 0.0 MiB, wasted time: 0.0 sec  - РЕЗУЛЬТАТЫ 2 ФУНКЦИИ


lst = [100, 100]

for el in range(1, 10000):
    lst.append(el)


# 3 задача до

@memory_and_time
def most_common_2(n):
    n = Counter(n).most_common(2)
    return n


most_common_2(lst)


# 3 задача после

@memory_and_time
def most_common(array):
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


most_common(lst)

# Выводы по 3 задаче: Как оказалось, вторая функция работает дольше, но памяти расходует меньше.
# Было ощущение, что благодаря каунтеру код будет меньше весить, до сих пор не понимаю с чем это связано.

# Memory used: 0.445 MiB, wasted time: 0.004 sec - РЕЗУЛЬТАТЫ 1 ФУНКЦИИ
# Memory used: 0.008 MiB, wasted time: 1.826 sec - РЕЗУЛЬТАТЫ 2 ФУНКЦИИ
