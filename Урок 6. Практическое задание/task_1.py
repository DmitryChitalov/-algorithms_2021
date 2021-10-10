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

from memory_profiler import memory_usage, profile
from timeit import default_timer


"""
Декораторы для замеров
"""


def my_profiling_decorator(func):
    def wrapper(*args, **kwargs):
        before = memory_usage()
        start = default_timer()
        result = func(*args, **kwargs)
        stop = default_timer()
        after = memory_usage()
        print(f"Function {func.__name__} used {(after[0] - before[0])} MiBs")
        print(f"Function {func.__name__} execution took {stop - start} s")
        return result
    return wrapper


"""
Попытки оптимизации
"""

# Урок 2. task_2


@my_profiling_decorator
def hide_recursion_num_counter(num: int) -> dict:
    def num_counter_recursion(number: int) -> dict:
        counter = {"odd": 0, "even": 0}
        if number == 0:
            return counter
        if (number % 10) % 2 == 0:
            counter['even'] += 1
        else:
            counter['odd'] += 1
        next_dig = num_counter_recursion(number//10)
        counter['even'] += next_dig['even']
        counter['odd'] += next_dig['odd']
        return counter
    return num_counter_recursion(num)


@my_profiling_decorator
def num_counter_recursion_optimised(number: int) -> list:
    counter = [0, 0]
    while number > 0:
        if (number % 10) % 2 == 0:
            counter[1] += 1
        else:
            counter[0] += 1
        number = number//10
    return counter


@my_profiling_decorator
def num_counter_recursion_optimised2(number: int) -> tuple:
    even = 0
    odd = 0

    def number_generator(n):
        while n > 0:
            yield n % 10
            n //= 10

    for i in number_generator(number):
        if (number % 10) % 2 == 0:
            even += 1
        else:
            odd += 1
        number = number//10
    return odd, even


# Урок 2. task_3
@my_profiling_decorator
def hide_recursion_range_sum(num: int) -> float:
    def range_sum(num: int, cur_num: float = 1.0) -> float:
        if num == 1:
            return cur_num
        return cur_num + range_sum(num - 1, cur_num / (-2))

    return range_sum(num)


@my_profiling_decorator
def range_sum(num: int) -> float:
    # генератор
    def range_generator(count):
        num = 1.0
        while count > 0:
            yield num
            num /= -2
            count -= 1

    sum = 0

    for i in range_generator(num):
        sum += i
    return sum


@my_profiling_decorator
def range_sum2(num: int) -> float:
    # генератор
    def range_generator(count):
        num = 1.0
        while count > 0:
            yield num
            num /= -2
            count -= 1

    return sum(range_generator(num))


# Урок 3. task_3
@my_profiling_decorator
def count_subs_v1(string: str) -> int:
    l = len(string)
    counter = set()
    for i in range(l):
        for j in range(i+1, l+1):
            counter.add(hash(string[i:j]))

    # counter.remove(hash(string))
    return len(counter) - 1


@my_profiling_decorator
def count_subs_v2(string: str) -> int:
    l = len(string)
    counter = []
    for i in range(l):
        for j in range(i + 1, l + 1):
            new_hash = hash(string[i:j])
            if new_hash not in counter:
                counter.append(new_hash)

    # counter.remove(hash(string))
    return len(counter) - 1


@my_profiling_decorator
def count_subs_v3(string: str) -> int:
    # counter = set()

    def generator(s):
        l = len(s)
        for i in range(l):
            for j in range(i + 1, l + 1):
                yield hash(s[i:j])

    counter = set(generator(string))

    return len(counter) - 1


if __name__ == '__main__':
    print(hide_recursion_num_counter(4567687))

    print(num_counter_recursion_optimised(4567687))

    print(num_counter_recursion_optimised2(4567687))
    # Function hide_recursion_num_counter used 0.06640625 MiBs
    # Function hide_recursion_num_counter execution took 7.819999999997274e-05 s
    # {'odd': 3, 'even': 4}
    # Function num_counter_recursion_optimised used 0.0 MiBs
    # Function num_counter_recursion_optimised execution took 1.56000000000045e-05 s
    # [3, 4]
    # Function num_counter_recursion_optimised2 used 0.0 MiBs
    # Function num_counter_recursion_optimised2 execution took 2.4700000000099642e-05 s
    # (3, 4)
    # По времени реального прироста или ухудшения не получилось по нескольким проведённым замерам. Хотя и видим,
    # что второй вариант алгоритма всё же быстрее, почти в 2 раза, первого, порядок этих цифр довольно мал.
    # По памяти оба улучшения получились одинаковыми (в пределах точности измерения).
    print('=' * 70)
    hide_recursion_range_sum(990)

    range_sum(990)

    range_sum2(990)
    # Function hide_recursion_range_sum used 1.33203125 MiBs
    # Function hide_recursion_range_sum execution took 0.00256590000000001 s
    # Function range_sum used 0.0 MiBs
    # Function range_sum execution took 0.001555799999999996 s
    # Function range_sum2 used 0.0 MiBs
    # Function range_sum2 execution took 0.0004045999999999772 s
    # Function range_sum2 execution took 0.0003309999999999702 s
    # Получили вполне ожидаемый эффект - встроенная функция оказалась быстрее всех. Генератор вновь позволил сэкономить
    # память.
    print('=' * 70)
    word = 'Lopadotemachoselachogaleokranioleipsanodrimhypotrimmatosilphiokarabomelitokatakechymenokichlepikossyphoph' \
           'attoperisteralektryonoptekephalliokigklopeleiolagoiosiraiobaphetraganopterygon'
    print(count_subs_v1('Lopadotemachoselachogaleokranioleipsanodrimhypot'))
    print(count_subs_v2('Lopadotemachoselachogaleokranioleipsanodrimhypot'))
    print(count_subs_v3('Lopadotemachoselachogaleokranioleipsanodrimhypot'))
    # Function count_subs_v1 used -0.03515625 MiBs
    # Function count_subs_v1 execution took 0.009982099999999994 s
    # 16569
    # Function count_subs_v2 used 0.37109375 MiBs
    # Function count_subs_v2 execution took 1.5415401 s
    # 16569
    # Function count_subs_v3 used -0.25 MiBs
    # Function count_subs_v3 execution took 0.00903770000000037 s
    # 16569
    #
    # Что-то не так (((
    # *************************************************************************************************************
    # Line #    Mem usage    Increment  Occurences   Line Contents
    # ============================================================
    #    146     19.5 MiB     19.5 MiB           1   @profile
    #    147                                         def count_subs_v1(string: str) -> int:
    #    148     19.5 MiB      0.0 MiB           1       l = len(string)
    #    149     19.5 MiB      0.0 MiB           1       counter = set()
    #    150     20.8 MiB      0.0 MiB         184       for i in range(l):
    #    151     20.8 MiB      0.2 MiB       17019           for j in range(i+1, l+1):
    #    152     20.8 MiB      1.1 MiB       16836               counter.add(hash(string[i:j]))
    #    153
    #    154     20.8 MiB      0.0 MiB           1       counter.remove(hash(string))
    #    155     20.8 MiB      0.0 MiB           1       return len(counter)
    #
    #
    # 16569
    # ***********************************************************************************************************
    #
    # Line #    Mem usage    Increment  Occurences   Line Contents
    # ============================================================
    #    158     20.1 MiB     20.1 MiB           1   @profile
    #    159                                         def count_subs_v2(string: str) -> int:
    #    160     20.1 MiB      0.0 MiB           1       l = len(string)
    #    161     20.1 MiB      0.0 MiB           1       counter = []
    #    162     20.5 MiB      0.0 MiB         184       for i in range(l):
    #    163     20.5 MiB      0.0 MiB       17019           for j in range(i + 1, l + 1):
    #    164     20.5 MiB      0.0 MiB       16836               new_hash = hash(string[i:j])
    #    165     20.5 MiB      0.0 MiB       16836               if new_hash not in counter:
    #    166     20.5 MiB      0.4 MiB       16570                   counter.append(new_hash)
    #    167
    #    168     20.5 MiB      0.0 MiB           1       counter.remove(hash(string))
    #    169     20.5 MiB      0.0 MiB           1       return len(counter)
    #
    #
    # 16569
    # ***********************************************************************************************************
    #
    # Line #    Mem usage    Increment  Occurences   Line Contents
    # ============================================================
    #    172     20.5 MiB     20.5 MiB           1   @profile
    #    173                                         def count_subs_v3(string: str) -> int:
    #    174                                             # counter = set()
    #    175
    #    176     20.5 MiB      0.0 MiB           2       def generator(s):
    #    177     20.5 MiB      0.0 MiB           1           l = len(s)
    #    178     21.0 MiB      0.0 MiB         184           for i in range(l):
    #    179     21.0 MiB      0.0 MiB       17019               for j in range(i + 1, l + 1):
    #    180     21.0 MiB      0.5 MiB       33672                   yield hash(s[i:j])
    #    181
    #    182     21.0 MiB      0.0 MiB           1       counter = set(generator(string))
    #    183
    #    184     21.0 MiB      0.0 MiB           1       return len(counter) - 1
    #
    #
    # 16569
    # ***********************************************************************************************************
    #
    # Для оценки использования памяти в этой функции использовал не самодельный декоратор, потому что не смог понять,
    # почему самодельный выдаёт отрицательный объём использования памяти, причём такой результат только для этой
    # функции. Единственное предположение - сборщик мусора успевает в процессе выполнения функции выполнить свою работу,
    # что приводит к тому, что функция memory_usage() после выполнения функции возвращает меньшее значение. К этому  же
    # выводу я прихожу выполнив запуск скрипта не менее 10 раз (обязательно вручную) - результат почти всегда разный,
    # вплоть до того, что отношение результатов меняется в разную сторону.
    # Анализ же по полученным данным показал, что лучший вариант по памяти - это использование списка, хотя и
    # генератор не сильно больше, всего на 0,1 MiB. При это по времени это, наоборот, худший из 3-х вариантов.
