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


def memory_time_profiler(func):
    def wrapper(*args, **kwargs):
        time1 = default_timer()
        mem1 = memory_usage()
        res = func(*args, **kwargs)
        mem2 = memory_usage()
        time2 = default_timer()
        print(f'Время выполнения: {time2 - time1}')
        print(f'Используемая память: {mem2[0] - mem1[0]} MiB')
        return res
    return wrapper

# Скрипт 1
@memory_time_profiler
def req_even_odd(num):
    print('Рекурсия')

    def check_numbers(num, count_even, count_odd):
        base = 10
        if num >= base:
            tail = num % base
            if tail % 2 > 0:
                count_odd += 1
            else:
                count_even += 1
            check_numbers(num // base, count_even, count_odd)
        else:
            if num % 2 > 0:
                count_odd += 1
            else:
                count_even += 1
            # print(f'Количество четных и нечетных цифр в числе равно: {count_even}, {count_odd}')

    check_numbers(num, 0, 0)

@memory_time_profiler
def loop_even_odd(num):
    print('Цикл')
    even, odd = 0, 0
    while num != 0:
        last = num % 10
        if last % 2:
            odd += 1
        else:
            even += 1
        num = num // 10
    # print(f'Количество четных и нечетных цифр в числе равно: {even}, {odd}')


# Скрипт 2
@memory_time_profiler
def cube_numbers(num):

    cube_list = []
    for i in list(range(num)):
        cube_list.append(i**3)
    return cube_list


@memory_time_profiler
def cube_numbers_yield(num):

    for i in list(range(num)):
        yield(i**3)

#  Скрипт 3
@memory_time_profiler
def org_tuple():
    from collections import namedtuple
    org_list = []
    org = namedtuple('org', 'name_org year_sum')

    for i in range(10000):
        name_org = 'Org_' + str(i)
        profits = '5000 6000 7000 8000'.split()

        year_sum = sum(list(map(int, profits)))
        org_list.append(org(name_org, year_sum))

        average_year_sum = sum([x.year_sum for x in org_list]) / len(org_list)

        orgs_less = [x.name_org for x in org_list if x.year_sum < average_year_sum]
        orgs_great = [x.name_org for x in org_list if x.year_sum > average_year_sum]
    return average_year_sum, orgs_less, orgs_great


@memory_time_profiler
def org_record():
    from recordclass import recordclass
    org = recordclass('org', ['name_org', 'year_sum'])
    org_list = []
    for i in range(10000):
        name_org = 'Org_' + str(i)
        profits = '5000 6000 7000 8000'.split()

        year_sum = sum(list(map(int, profits)))
        org_list.append(org(name_org, year_sum))

        average_year_sum = sum([x.year_sum for x in org_list]) / len(org_list)

        orgs_less = [x.name_org for x in org_list if x.year_sum < average_year_sum]
        orgs_great = [x.name_org for x in org_list if x.year_sum > average_year_sum]
    return average_year_sum, orgs_less, orgs_great

print('Пример 1')
req_even_odd(1324354657687980)
loop_even_odd(1324354657687980)

print('Пример 2')
print('Список из кубов чисел')
res_2_1 = cube_numbers(1324354)
print('Генератор кубов чисел')
res_2_2 = cube_numbers_yield(1324354)

print('Пример 3')
print('NamedTuple')
res_3_1_1, res_3_2_1, res_3_3_1 = org_tuple()
print('RecordClass')
res_3_1_2, res_3_2_2, res_3_3_2 = org_record()



# Пример 1
# Рекурсия
# Время выполнения: 0.2179138
# Используемая память: 0.0078125 MiB
# Цикл
# Время выполнения: 0.2214815
# Используемая память: 0.0 MiB
# Ожидал, что цикл будет быстрее рекурсии. Но замеры показывают, что они примерно равны по времени.
# При этом цикл требует меньших затрат в памяти. Рекурсия требует хранения стека вызова, поэтому расход памяти больше
#
# Пример 2
# Список из кубов чисел
# Время выполнения: 0.660082
# Используемая память: 72.3203125 MiB
# Генератор кубов чисел
# Время выполнения: 0.21813519999999986
# Используемая память: 0.0 MiB
# При использовании генератора память расходуется сильно меньше,
# Если массив хранить не нужно, то лучше использовать генератор.
# Генератор так же требует меньше времени в данном примере
#
# Пример 3
# NamedTuple
# Время выполнения: 8.4028827
# Используемая память: 0.890625 MiB
# RecordClass
# Время выполнения: 8.148904400000001
# Используемая память: 0.76953125 MiB
# Recordclass работает быстрее namedtuple и требует меньше памяти.