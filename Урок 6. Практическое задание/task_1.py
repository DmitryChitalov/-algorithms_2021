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
    company_profit = collections.namedtuple("company",
                                            "company_name q_1_profit q_2_profit q_3_profit q_4_profit")
    for i in range(1000):
        companies.append(company_profit(str(i * 10), i, i, i, i))
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
    company_profit = recordclass.recordclass("company",
                                             "company_name q_1_profit q_2_profit q_3_profit q_4_profit")
    for i in range(1000):
        companies.append(company_profit(str(i * 10), i, i, i, i))
    return companies


@profiler
def original_calculation():
    data = collect_companies_data()
    print(f"размер списка компаний namedtuple: {asizeof.asizeof(data)}")
    total_avg_prof = all_companies_avg_profit(data)
    print(f"Средняя прибыль компаний: {total_avg_prof}")


@profiler
def improved_calculation():
    data = collect_companies_data_recordclass()
    print(f"размер списка компаний recordclass: {asizeof.asizeof(data)}")
    total_avg_prof = all_companies_avg_profit(data)
    print(f"Средняя прибыль компаний: {total_avg_prof}")


original_calculation()
print("-" * 150)
improved_calculation()

"""
Вывод:
В функции improved_calculation() структура данных namedtuple заменена на recordclass,
из-за чего ее размер уменьшился(для одинаковых входных данных):
размер списка компаний namedtuple: 176848
размер списка компаний recordclass: 73776
Так же уменьшилось количество используемой памяти с 0.6796875 MiB до 0.02734375 MiB
Время выполнения функций сравнимо на при однократном запуске:
Функция original_calculation выполнялась 0.11952869999999999 сек
Функция improved_calculation выполнялась 0.12076930000000002 сек
Использование recordclass более предпочтительно по сравнению с namedtuple.
"""
