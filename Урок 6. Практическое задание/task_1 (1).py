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
размер списка компаний namedtuple: 100520
размер списка компаний recordclass: 37048
Так же уменьшилось количество используемой памяти с 0.28125 MiB(namedtuple) до 0.0078125 MiB(recordclass).
Время выполнения функций сравнимо на при однократном запуске:
Функция original_calculation выполнялась 0.12688890000000003 сек
Функция improved_calculation выполнялась 0.12017449999999996 сек
Использование recordclass более предпочтительно по сравнению с namedtuple.
"""