"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections.

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Фирма_1
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Фирма_2
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Фирма_1

Предприятия, с прибылью ниже среднего значения: Фирма_2
"""
from collections import namedtuple
from recordclass import recordclass
import memory_profiler
from memory_profiler import profile
import sys

# вариант без профилирования памяти (исходный):

n = int(input('Введите количество предприятий для расчета прибыли: '))


def decor(func):
    def wrapper(x, c):
        m1 = memory_profiler.memory_usage()
        res = func(x, c)
        m2 = memory_profiler.memory_usage()
        mem_diff = m2[0] - m1[0]
        print(f'Выполнение заняло {mem_diff} Mib')
        return res

    return wrapper


def decor_1(func):
    def wrapper(n):
        m1 = memory_profiler.memory_usage()
        companies_list, company = func(n)
        m2 = memory_profiler.memory_usage()
        mem_diff = m2[0] - m1[0]
        print(print(f'Выполнение заняло {mem_diff} Mib'))
        return companies_list, company

    return wrapper


@decor_1
@profile
def get_companies_list(n):
    COMPANY = namedtuple('Company',
                         'company_name first_quarter_profit second_quarter_profit third_quarter_profit fourth_quarter_profit year_profit')
    companies_list = []
    global company
    for _ in range(n):
        name = input('Введите название предприятия: ')
        profit_row = input('Через пробел введите прибыль данного предприятия за каждый квартал(всего 4 квартала): ')
        profit_list = [int(el) for el in profit_row.split()]
        company = COMPANY(
            company_name=name,
            first_quarter_profit=profit_list[0],
            second_quarter_profit=profit_list[1],
            third_quarter_profit=profit_list[2],
            fourth_quarter_profit=profit_list[3],
            year_profit=sum(profit_list)
        )
        companies_list.append(company)
    print(f'Объём занимаемой объектом list (через списковое включение) памяти: {sys.getsizeof(profit_list)} байт(а)')
    return companies_list, company


companies_list, company = get_companies_list(n)
print(f'Объём занимаемой объектом namedtuple памяти: {sys.getsizeof(companies_list)} байт(а)')


@decor
@profile
def get_top_prifit_companies(companies_list, company):
    total_year_profit = 0
    for c in companies_list:
        total_year_profit += c.year_profit
    aver_year_profit = total_year_profit / len(companies_list)
    top_profit_companies = [c.company_name for c in companies_list if c.year_profit > aver_year_profit]
    return f'Предприятия, с прибылью выше среднего значения: {top_profit_companies}'


@decor
@profile
def get_low_prifit_companies(companies_list, company):
    total_year_profit = 0
    for c in companies_list:
        total_year_profit += c.year_profit
    aver_year_profit = total_year_profit / len(companies_list)
    low_profit_companies = [c.company_name for c in companies_list if c.year_profit < aver_year_profit]
    return f'Предприятия, с прибылью ниже среднего значения: {low_profit_companies}'


print(get_top_prifit_companies(companies_list, company))
print(get_low_prifit_companies(companies_list, company))

######## Вариант с использованием  минимизации расходования памяти (в одном была возможность применить
# сразу несколько способов: использование генератора вместо спискового включения,
# map вместо спискового включения (не получилось), recordclass вместо namedtuple,
# а также удаление ненужных переменных (объектов)


n1 = int(input('Введите количество предприятий для расчета прибыли: '))


# использование модуля recordclass вместо namedtuple:
@decor_1
@profile
def get_companies_list_1(n1):
    COMPANY = recordclass('Company',
                          'company_name first_quarter_profit second_quarter_profit third_quarter_profit fourth_quarter_profit year_profit')
    companies_list = []  # здесь необходим именно список, его значения используются, должны храниться
    for _ in range(n1):
        name = input('Введите название предприятия: ')
        profit_row = input('Через пробел введите прибыль данного предприятия за каждый квартал(всего 4 квартала): ')
        profit_list = [int(el) for el in profit_row.split()]
        # применила map вместо спискового включения list(map(int, profit_row.split())) - пришлось
        # преобразовать в обычный list, иначе при обращении через индексы была ошибка:
        # 'map' object is not subscriptable,  -  как показали измерения, памяти такой
        # объект занимает почти в 1,5 раз больше, чем list comprehension: 112 байт против 88.
        # поэтому вернулась к списковому включению
        company = COMPANY(
            company_name=name,
            first_quarter_profit=profit_list[0],
            second_quarter_profit=profit_list[1],
            third_quarter_profit=profit_list[2],
            fourth_quarter_profit=profit_list[3],
            year_profit=sum(profit_list)
        )
        companies_list.append(company)
    print(f'Объём занимаемой объектом list памяти: {sys.getsizeof(profit_list)} байт(а)')
    print(sys.getrefcount(profit_row))  # 2
    del profit_row  # удаляю объект
    print(sys.getrefcount(n1))  # 671!!!!!!
    del n1  # удаляю объект
    print(sys.getrefcount(profit_list))  # 2
    del profit_list  # удаляю объект
    print(sys.getrefcount(name))  # 8
    del name  # удаляю объект
    return companies_list, company


companies_list_1, company_1 = get_companies_list_1(n1)
print(f'Объём занимаемой объектом recordclass памяти: {sys.getsizeof(companies_list_1)} байт(а)')


@decor
@profile
def get_top_profit_companies_1(companies_list, company):
    total_year_profit = 0
    for c in companies_list:
        total_year_profit += c.year_profit
    global aver_year_profit_1
    aver_year_profit_1 = total_year_profit / len(companies_list)
    for c in companies_list:
        if c.year_profit > aver_year_profit_1:
            yield c.company_name  # Ленивые вычисления  через функции-генераторы и  yield


@decor
@profile
def get_low_profit_companies_1(companies_list, company):
    year_total_profit = 0
    for c in companies_list:
        year_total_profit += c.year_profit
    aver_year_profit_1 = year_total_profit / len(companies_list)
    for c in companies_list:
        if c.year_profit < aver_year_profit_1:
            yield c.company_name  # Ленивые вычисления  через функции-генераторы и  yield


my_generator_top = get_top_profit_companies_1(companies_list_1, company_1)
print('Предприятия, с прибылью выше среднего значения:')
for i in my_generator_top:
    print(i, sep=', ', end='')
print()

my_generator_low = get_low_profit_companies_1(companies_list_1, company_1)
print('Предприятия, с прибылью ниже среднего значения:')
for i in my_generator_low:
    print(i, sep=', ', end='')
print()

# удаляю объекты
del my_generator_low  #  удаляю ссылку на значение
try:
    print(sys.getrefcount(my_generator_low))
except NameError:
    print('Нет ссылок на my_generator_low')

del my_generator_top #  удаляю ссылку на значение
try:
    print(sys.getrefcount(my_generator_top))
except NameError:
    print('Нет ссылок на my_generator_top')

del companies_list_1 #  удаляю ссылку на значение
try:
    print(sys.getrefcount(companies_list_1))
except NameError:
    print('Нет ссылок на companies_list_1')

del company_1 #  удаляю ссылку на значение
try:
    print(sys.getrefcount(company_1))
except NameError:
    print('Нет ссылок на company_1')


# Оба варианта кода отработаны при n=7, n1=7:

# Введите количество предприятий для расчета прибыли: 7
# Введите название предприятия: r
# Через пробел введите прибыль данного предприятия за каждый квартал(всего 4 квартала): 111 111 111 111
# Введите название предприятия: y
# Через пробел введите прибыль данного предприятия за каждый квартал(всего 4 квартала): 888 8888 88888 88888
# Введите название предприятия: g
# Через пробел введите прибыль данного предприятия за каждый квартал(всего 4 квартала): 999 9999 999 999999
# Введите название предприятия: f
# Через пробел введите прибыль данного предприятия за каждый квартал(всего 4 квартала): 0 8888 9999 666
# Введите название предприятия: o
# Через пробел введите прибыль данного предприятия за каждый квартал(всего 4 квартала): 6666 6666666 77777 7
# Введите название предприятия: g
# Через пробел введите прибыль данного предприятия за каждый квартал(всего 4 квартала): 77777 77777 77777 77777
# Введите название предприятия: f
# Через пробел введите прибыль данного предприятия за каждый квартал(всего 4 квартала): 99999 9999 999 9999
# Объём занимаемой объектом list (через списковое включение) памяти: 88 байт(а)
# Filename: C:/Users/momot/Desktop/PROGRAMMING/Geekbrains/Algorythms_Python/DZ/ДЗ с репо/урок 6. дз/1.2_lesson-6.py
#
# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     61     19.3 MiB     19.3 MiB           1   @decor_1
#     62                                         @profile
#     63                                         def get_companies_list(n):
#     64     19.4 MiB      0.0 MiB           2       COMPANY = namedtuple('Company',
#     65     19.3 MiB      0.0 MiB           1                            'company_name first_quarter_profit second_quarter_profit third_quarter_profit fourth_quarter_profit year_profit')
#     66     19.4 MiB      0.0 MiB           1       companies_list = []
#     67                                             global company
#     68     19.4 MiB     -0.2 MiB           8       for _ in range(n):
#     69     19.4 MiB     -0.1 MiB           7           name = input('Введите название предприятия: ')
#     70     19.4 MiB     -0.1 MiB           7           profit_row = input('Через пробел введите прибыль данного предприятия за каждый квартал(всего 4 квартала): ')
#     71     19.4 MiB     -1.1 MiB          49           profit_list = [int(el) for el in profit_row.split()]
#     72     19.4 MiB     -0.3 MiB          14           company = COMPANY(
#     73     19.4 MiB     -0.2 MiB           7               company_name=name,
#     74     19.4 MiB     -0.2 MiB           7               first_quarter_profit=profit_list[0],
#     75     19.4 MiB     -0.2 MiB           7               second_quarter_profit=profit_list[1],
#     76     19.4 MiB     -0.2 MiB           7               third_quarter_profit=profit_list[2],
#     77     19.4 MiB     -0.2 MiB           7               fourth_quarter_profit=profit_list[3],
#     78     19.4 MiB     -0.2 MiB           7               year_profit=sum(profit_list)
#     79                                                 )
#     80     19.4 MiB     -0.2 MiB           7           companies_list.append(company)
#     81     19.3 MiB     -0.0 MiB           1       print(f'Объём занимаемой объектом list (через списковое включение) памяти: {sys.getsizeof(profit_list)} байт(а)')
#     82     19.3 MiB      0.0 MiB           1       return companies_list, company
#
#
# Выполнение заняло 0.30078125 Mib
# None
# Объём занимаемой объектом namedtuple памяти: 120 байт(а)
# Filename: C:/Users/momot/Desktop/PROGRAMMING/Geekbrains/Algorythms_Python/DZ/ДЗ с репо/урок 6. дз/1.2_lesson-6.py
#
# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#     89     19.4 MiB     19.4 MiB           1   @decor
#     90                                         @profile
#     91                                         def get_top_prifit_companies(companies_list, company):
#     92     19.4 MiB      0.0 MiB           1       total_year_profit = 0
#     93     19.4 MiB      0.0 MiB           8       for c in companies_list:
#     94     19.4 MiB      0.0 MiB           7           total_year_profit += c.year_profit
#     95     19.4 MiB      0.0 MiB           1       aver_year_profit = total_year_profit / len(companies_list)
#     96     19.4 MiB      0.0 MiB          10       top_profit_companies = [c.company_name for c in companies_list if c.year_profit > aver_year_profit]
#     97     19.4 MiB      0.0 MiB           1       return f'Предприятия, с прибылью выше среднего значения: {top_profit_companies}'
#
#
# Выполнение заняло 0.0 Mib
# Предприятия, с прибылью выше среднего значения: ['o']
# Filename: C:/Users/momot/Desktop/PROGRAMMING/Geekbrains/Algorythms_Python/DZ/ДЗ с репо/урок 6. дз/1.2_lesson-6.py
#
# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#    100     19.4 MiB     19.4 MiB           1   @decor
#    101                                         @profile
#    102                                         def get_low_prifit_companies(companies_list, company):
#    103     19.4 MiB      0.0 MiB           1       total_year_profit = 0
#    104     19.4 MiB      0.0 MiB           8       for c in companies_list:
#    105     19.4 MiB      0.0 MiB           7           total_year_profit += c.year_profit
#    106     19.4 MiB      0.0 MiB           1       aver_year_profit = total_year_profit / len(companies_list)
#    107     19.4 MiB      0.0 MiB          10       low_profit_companies = [c.company_name for c in companies_list if c.year_profit < aver_year_profit]
#    108     19.4 MiB      0.0 MiB           1       return f'Предприятия, с прибылью ниже среднего значения: {low_profit_companies}'
#
#
# Выполнение заняло 0.0 Mib
# Предприятия, с прибылью ниже среднего значения: ['r', 'y', 'g', 'f', 'g', 'f']
# Введите количество предприятий для расчета прибыли: 7
# Введите название предприятия: r
# Через пробел введите прибыль данного предприятия за каждый квартал(всего 4 квартала): 7777 77777 7777 7777
# Введите название предприятия: y
# Через пробел введите прибыль данного предприятия за каждый квартал(всего 4 квартала): 9999 9999 999 9999
# Введите название предприятия: f
# Через пробел введите прибыль данного предприятия за каждый квартал(всего 4 квартала): 1111 1111 1111 1111
# Введите название предприятия: d
# Через пробел введите прибыль данного предприятия за каждый квартал(всего 4 квартала): 9999 6666 9999 9999
# Введите название предприятия: d
# Через пробел введите прибыль данного предприятия за каждый квартал(всего 4 квартала): 7 4 7777 7777
# Введите название предприятия: s
# Через пробел введите прибыль данного предприятия за каждый квартал(всего 4 квартала): 1111 7777 8888 9999
# Введите название предприятия: i
# Через пробел введите прибыль данного предприятия за каждый квартал(всего 4 квартала): 7777 8888 9999 4444
# Объём занимаемой объектом list(map()) памяти: 88 байт(а)
# 3
# 70
# 3
# 106
# Filename: C:/Users/momot/Desktop/PROGRAMMING/Geekbrains/Algorythms_Python/DZ/ДЗ с репо/урок 6. дз/1.2_lesson-6.py
#
# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#    124     19.4 MiB     19.4 MiB           1   @decor_1
#    125                                         @profile
#    126                                         def get_companies_list_1(n1):
#    127     19.7 MiB      0.3 MiB           2       COMPANY = recordclass('Company',
#    128     19.4 MiB      0.0 MiB           1                             'company_name first_quarter_profit second_quarter_profit third_quarter_profit fourth_quarter_profit year_profit')
#    129     19.7 MiB      0.0 MiB           1       companies_list = []  # здесь необходим именно список, его значения используются, должны храниться
#    130     19.7 MiB     -0.1 MiB           8       for _ in range(n1):
#    131     19.7 MiB     -0.1 MiB           7           name = input('Введите название предприятия: ')
#    132     19.7 MiB     -0.1 MiB           7           profit_row = input('Через пробел введите прибыль данного предприятия за каждый квартал(всего 4 квартала): ')
#    133     19.7 MiB     -0.5 MiB          49           profit_list = [int(el) for el in profit_row.split()]
#    134                                                 # применила map вместо спискового включения list(map(int, profit_row.split())) - пришлось
#    135                                                 # преобразовать в обычный list, иначе при обращении через индексы была ошибка:
#    136                                                 # 'map' object is not subscriptable,  -  как показали измерения, памяти такой
#    137                                                 # объект занимает почти в 1,5 раз больше, чем list comprehension: 112 байт против 88.
#    138                                                 # поэтому вернулась к списковому включению
#    139     19.7 MiB     -0.2 MiB          14           company = COMPANY(
#    140     19.7 MiB     -0.1 MiB           7               company_name=name,
#    141     19.7 MiB     -0.1 MiB           7               first_quarter_profit=profit_list[0],
#    142     19.7 MiB     -0.1 MiB           7               second_quarter_profit=profit_list[1],
#    143     19.7 MiB     -0.1 MiB           7               third_quarter_profit=profit_list[2],
#    144     19.7 MiB     -0.1 MiB           7               fourth_quarter_profit=profit_list[3],
#    145     19.7 MiB     -0.1 MiB           7               year_profit=sum(profit_list)
#    146                                                 )
#    147     19.7 MiB     -0.1 MiB           7           companies_list.append(company)
#    148     19.6 MiB     -0.0 MiB           1       print(f'Объём занимаемой объектом list(map()) памяти: {sys.getsizeof(profit_list)} байт(а)')
#    149     19.6 MiB      0.0 MiB           1       print(sys.getrefcount(profit_row))  # 2
#    150     19.6 MiB      0.0 MiB           1       del profit_row  # удаляю объект
#    151     19.6 MiB      0.0 MiB           1       print(sys.getrefcount(n1))  # 671!!!!!!
#    152     19.6 MiB      0.0 MiB           1       del n1  # удаляю объект
#    153     19.6 MiB      0.0 MiB           1       print(sys.getrefcount(profit_list))  # 2
#    154     19.6 MiB      0.0 MiB           1       del profit_list  # удаляю объект
#    155     19.6 MiB      0.0 MiB           1       print(sys.getrefcount(name))  # 8
#    156     19.6 MiB      0.0 MiB           1       del name  # удаляю объект
#    157     19.6 MiB      0.0 MiB           1       return companies_list, company
#
#
# Выполнение заняло 0.27734375 Mib
# None
# Объём занимаемой объектом recordclass памяти: 120 байт(а)
# Выполнение заняло 0.0 Mib
# Предприятия, с прибылью выше среднего значения:
# rd
# Выполнение заняло 0.0 Mib
# Предприятия, с прибылью ниже среднего значения:
# yfdsi
# Нет ссылок на my_generator_low
# Нет ссылок на my_generator_top
# Нет ссылок на companies_list_1
# Нет ссылок на company_1

# Выводы:
# Выполнение get_companies_list(n) заняло  0.30078125 Mib
# # Объём занимаемой объектом namedtuple памяти: 120 байт(а)
# выполнение через namedtuple заняло меньше Mib:
#  Выполнение get_companies_list_1(n1) заняло 0.27734375 Mib -
# # Объём занимаемой объектом recordclass памяти: 120 байт(а) - равноценны,
# экономия будет на больших n.
# Результаты через @profile обратны:
# Memory usage get_companies_list(n) - 19.3, доп память не использована.
# Memory usage get_companies_list_1(n1) - 19.6, увеличение на 0.3 на 0.3 MiB  на
# операции создания объекта recordclass, хотя именно его я использую для экономнии
# в её потреблении (не смогла найти в чем нюанс).
# Функции get_low_profit_companies, get_top_profit_companies,
# get_low_profit_companies_1, get_top_profit_companies_1 отработаны без проблем
# с использованием памяти.
# Удаление ссылок на значения во втором варианте  освобождают память после выполнения кода
