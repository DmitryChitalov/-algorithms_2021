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

import memory_profiler
import collections
import timeit
from pympler import asizeof
import recordclass


def profiler(func):
    def wrapper(*args):
        start_time = timeit.default_timer()
        mem_start = memory_profiler.memory_usage()[0]
        func_result = func(*args)
        time_taken = timeit.default_timer() - start_time
        mem_used = memory_profiler.memory_usage()[0] - mem_start
        print("*" * 150)
        print(f"Функция {func.__name__} выполнялась {time_taken} сек и занимала в памяти {mem_used} MiB")
        print("*" * 150)
        return func_result

    return wrapper


def collect_companies_data():
    companies = []
    try:
        companies_number = int(input("Введите количество предприятий для расчета прибыли: "))
        for i in range(companies_number):
            comp_name = input("Введите название предприятия: ")
            profits = input("через пробел введите прибыль данного предприятия "
                            "за каждый квартал(Всего 4 квартала): ")

            company_profit = collections.namedtuple("company",
                                                    "company_name q_1_profit q_2_profit q_3_profit q_4_profit")
            companies.append(company_profit(comp_name, *[int(elem) for elem in profits.split(' ')]))

    except (ValueError, TypeError):
        print("Неверный ввод!!!")

    return companies


def avg_company_profit(company_profit):
    return (company_profit.q_1_profit + company_profit.q_2_profit
            + company_profit.q_3_profit + company_profit.q_4_profit) / 4


def all_companies_avg_profit(companies):
    total_profit = 0
    for company in companies:
        total_profit += avg_company_profit(company)
    return total_profit / len(companies) if len(companies) > 0 else "Не было введено ни одной компании"


def collect_companies_data_recordclass():
    companies = []
    try:
        companies_number = int(input("Введите количество предприятий для расчета прибыли: "))
        for i in range(companies_number):
            comp_name = input("Введите название предприятия: ")
            profits = input("через пробел введите прибыль данного предприятия "
                            "за каждый квартал(Всего 4 квартала): ")

            company_profit = recordclass.recordclass("company",
                                                     "company_name q_1_profit q_2_profit q_3_profit q_4_profit")
            companies.append(company_profit(comp_name, *map(int, profits.split(' '))))

    except (ValueError, TypeError):
        print("Неверный ввод!!!")

    return companies


def collect_companies_data_1():
    companies = []
    try:
        companies_number = int(input("Введите количество предприятий для расчета прибыли: "))
        for i in range(companies_number):
            comp_name = input("Введите название предприятия: ")
            profits = input("через пробел введите прибыль данного предприятия "
                            "за каждый квартал(Всего 4 квартала): ")

            company_profit = collections.namedtuple("company",
                                                    "company_name q_1_profit q_2_profit q_3_profit q_4_profit")
            companies.append(company_profit(comp_name, *map(int, profits.split(' '))))

    except (ValueError, TypeError):
        print("Неверный ввод!!!")

    return companies


def collect_companies_data_recordclass_2():
    companies = []
    try:
        companies_number = int(input("Введите количество предприятий для расчета прибыли: "))
        for i in range(companies_number):
            comp_name = input("Введите название предприятия: ")
            profits = input("через пробел введите прибыль данного предприятия "
                            "за каждый квартал(Всего 4 квартала): ")

            company_profit = recordclass.recordclass("company",
                                                     "company_name q_1_profit q_2_profit q_3_profit q_4_profit")
            companies.append(company_profit(comp_name, *[int(elem) for elem in profits.split(' ')]))

    except (ValueError, TypeError):
        print("Неверный ввод!!!")

    return companies


@profiler
def original_calculation():
    data = collect_companies_data()
    print(f"размер списка компаний namedtuple: {asizeof.asizeof(data)}")
    total_avg_prof = all_companies_avg_profit(data)
    print(f"Средняя прибыль компаний: {total_avg_prof}")
    print("Компании с прибылью выше среднего:")
    print(*[data[i].company_name for i in range(len(data)) if avg_company_profit(data[i]) > total_avg_prof], sep=', ')
    print("Компании со средней прибылью или ниже среднего:")
    print(*[data[i].company_name for i in range(len(data)) if avg_company_profit(data[i]) <= total_avg_prof], sep=', ')


@profiler
def improved_calculation():
    data = collect_companies_data_recordclass()
    print(f"размер списка компаний recordclass: {asizeof.asizeof(data)}")
    total_avg_prof = all_companies_avg_profit(data)
    print(f"Средняя прибыль компаний: {total_avg_prof}")
    print("Компании с прибылью выше среднего:")
    print(*[data[i].company_name for i in range(len(data)) if avg_company_profit(data[i]) > total_avg_prof], sep=', ')
    print("Компании со средней прибылью или ниже среднего:")
    print(*[data[i].company_name for i in range(len(data)) if avg_company_profit(data[i]) <= total_avg_prof], sep=', ')


@profiler
def improved_calculation_2():
    data = collect_companies_data_recordclass_2()
    print(f"размер списка компаний recordclass: {asizeof.asizeof(data)}")
    total_avg_prof = all_companies_avg_profit(data)
    print(f"Средняя прибыль компаний: {total_avg_prof}")
    print("Компании с прибылью выше среднего:")
    print(*[data[i].company_name for i in range(len(data)) if avg_company_profit(data[i]) > total_avg_prof], sep=', ')
    print("Компании со средней прибылью или ниже среднего:")
    print(*[data[i].company_name for i in range(len(data)) if avg_company_profit(data[i]) <= total_avg_prof], sep=', ')


@profiler
def original_calculation_map():
    data = collect_companies_data_1()
    print(f"размер списка компаний recordclass: {asizeof.asizeof(data)}")
    total_avg_prof = all_companies_avg_profit(data)
    print(f"Средняя прибыль компаний: {total_avg_prof}")
    print("Компании с прибылью выше среднего:")
    print(*[data[i].company_name for i in range(len(data)) if avg_company_profit(data[i]) > total_avg_prof], sep=', ')
    print("Компании со средней прибылью или ниже среднего:")
    print(*[data[i].company_name for i in range(len(data)) if avg_company_profit(data[i]) <= total_avg_prof], sep=', ')


original_calculation()
print("-" * 150)
original_calculation_map()
print("-" * 150)
improved_calculation()
print("-" * 150)
improved_calculation_2()
"""
Вывод:
В функции improved_calculation() структура данных namedtuple заменена на recordclass,
из-за чего ее размер увеличился(для одинаковых входных данных):
размер списка компаний namedtuple: 480
размер списка компаний recordclass: 1168
Так же увеличилось количество используемой памяти с 0.0 MiB до 0.29296875 MiB
"""
