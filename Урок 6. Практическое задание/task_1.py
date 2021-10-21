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

from memory_profiler import memory_usage
from timeit import default_timer


def memory_and_time_print(func):
    def wrapper(*args):
        m1 = memory_usage()
        t1 = default_timer()
        res = func(*args)
        t2 = default_timer()
        m2 = memory_usage()
        time_diff = t2 - t1
        mem_diff = m2[0] - m1[0]

        print(f'Memory used: {round(mem_diff, 3)} MiB, wasted time: {round(time_diff, 3)} sec')
        return res
    return wrapper


@memory_and_time_print
def simple(i):
    """Без использования «Решета Эратосфена»"""
    count = 1
    n = 2
    while count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            count += 1
        n += 1
    return n


@memory_and_time_print
def sieve_eratosthenes(find):
    number = find * 10
    numbers = list(range(number + 1))
    numbers[1] = 0
    i = 2
    while i <= number:
        if numbers[i] != 0:
            j = i + i
            while j <= number:
                numbers[j] = 0
                j += i
        i += 1
    a = set(numbers)
    a.remove(0)
    a = sorted(list(a))
    return a[find - 1]


my_numbers = [10, 100, 1000, 5000]

for num in my_numbers:
    print(f'{num}-е число, полученное от функции simple: {simple(num)}', end='\n\n')

print('Решето Эратосфена:')

for num in my_numbers:
    print(f'{num}-е число, полученное от функции sieve_eratosthenes: {sieve_eratosthenes(num)}', end='\n\n')


# Алгоритм через перебор делителей                       # Алгоритм с использованием решета Эратосфена:

# Memory used: 0.0 MiB, wasted time: 0.0 sec             # Memory used: 0.0 MiB, wasted time: 0.0 sec
# 10-е число, полученное от функции simple: 29           # 10-е число, полученное от функции sieve_eratosthenes: 29
#                                                        #
# Memory used: 0.0 MiB, wasted time: 0.027 sec           # Memory used: 0.0 MiB, wasted time: 0.002 sec
# 100-е число, полученное от функции simple: 541         # 100-е число, полученное от функции sieve_eratosthenes: 541
#                                                        #
# Memory used: 0.0 MiB, wasted time: 1.346 sec           # Memory used: 0.574 MiB, wasted time: 0.027 sec
# 1000-е число, полученное от функции simple: 7919       # 1000-е число, полученное от функции sieve_eratosthenes: 7919
#                                                        #
# Memory used: 0.0 MiB, wasted time: 41.561 sec          # Memory used: 0.105 MiB, wasted time: 0.076 sec
# 5000-е число, полученное от функции simple: 48611      # 5000-е число, полученное от функции sieve_eratosthenes: 48611

# Из результатов тестирования этих двух алгоритмов можно отметить, что
# первый алгоритм практически не потребляет ресурсы памяти и довольно быстро находит небольшие простые числа.
# Однако для поиска больших по счёту простых чисел требуется всё больше и больше времени,
# хотя потребляемая память при этом практически не расходуется.

# Алгоритм с ипользованием решета Эратосфена позволяет создать массив простых чисел,
# что будет потреблять ресурсы памяти, но позволит значительно ускорить поиск больших по счёту простых чисел.
# Причём в данном алгоритме размер решета зависит от аргумента, что положительно влияет на потребляемые ресурсы памяти.
# Однако для поиска 10000-го простого числа, такой алгоритм не сработает, т.к. будет недостаточно размера решета.
