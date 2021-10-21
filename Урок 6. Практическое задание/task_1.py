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
import memory_profiler


def mem_tm(func):
    def wrapper(*args, **kwargs):
        m1 = memory_profiler.memory_usage()
        t1 = default_timer()
        res = func(*args, **kwargs)
        time_diff = default_timer() - t1
        m2 = memory_profiler.memory_usage()
        mem_diff = m2[0] - m1[0]
        return f'Заняло памяти: {mem_diff} MiB\n Заняло времени: {time_diff}, {res}'
    return wrapper



@mem_tm
def calc_while(num):
    even = 0
    odd = 0
    while num >= 1:
        check = num % 10
        if check % 2 == 0:
            even += 1
        elif check % 2 == 1:
            odd += 1
        num //= 10
    return even, odd



@mem_tm
def calc_rec():
    return rec(12321)


def rec(num, even=0, odd=0):
    if num < 1:
        return even, odd
    check = num % 10
    if check % 2 == 0:
        even += 1
    elif check % 2 == 1:
        odd += 1
    num //= 10
    return rec(num, even, odd)


print(f'Рекурсия\n {calc_rec()}')  # 0.00390625 MiB, 4.940000000003275e-05
print(f'Цикл\n {calc_while(12321)}')    # 0.0 MiB, 3.2999999999949736e-05

"""
Были произведены замеры на выполнении рекусии и с применением циклов
Рекурсия заняло больше памяти и времени, так как во время работы хранит в памяти результаты
каждого вызова функции.
"""