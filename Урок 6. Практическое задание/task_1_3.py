from task_1_1 import memory_time_profiler
from collections import namedtuple
from recordclass import recordclass

company_info = (('1', '200 300 400 500'), ('2', '100 200 300 400'))


def add_to_companies_list(com_ls, ls, *args):
    company = ls(*args)
    com_ls.append(company)
    return None


def get_avg_profit(ls):
    return round(sum([company.revenue for company in ls]) / len(ls), 2)


def systematize_companies(ls, av_pr):
    height, low = [], []
    for company in ls:
        if company.revenue >= av_pr:
            height.append(company.name)
        else:
            low.append(company.name)
    return height, low


@memory_time_profiler
def main():
    companies = namedtuple('company', ['name', 'revenue'])
    companies_ls = []
    for i in range(2):
        company_name, revenue = company_info[i]
        add_to_companies_list(companies_ls, companies, company_name, sum(map(int, revenue.split())))
    avg_profit = get_avg_profit(companies_ls)
    height, low = systematize_companies(companies_ls, avg_profit)
    return avg_profit, height, low


@memory_time_profiler
def main_new():
    companies = recordclass('company', ['name', 'revenue'])
    companies_ls = []
    for i in range(2):
        company_name, revenue = company_info[i]
        add_to_companies_list(companies_ls, companies, company_name, sum(map(int, revenue.split())))
    avg_profit = get_avg_profit(companies_ls)
    height, low = systematize_companies(companies_ls, avg_profit)
    return avg_profit, height, low


if __name__ == '__main__':
    main()
    main_new()

"""
Namedtuple
Время выполнения: 0.21870130000000002
Используемая память: 0.0546875 MiB

Recordclass
Время выполнения: 0.20244720000000005
Используемая память: 0.02734375 MiB

Recordclass работает не только быстрее namedtuple, но и требует меньше памяти. Учитывая, что recordclass
обладает возможностью к изменению на месте, это делает его более привлекательным иснтрументом для использования
(если нам не надо жестко запретить изменяемость объектов)
"""
