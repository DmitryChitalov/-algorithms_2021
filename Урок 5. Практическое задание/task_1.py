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

companies_ls = []
companies = namedtuple('company', ['name', 'revenue'])


def add_to_companies_list(*args):
    company = companies(*args)
    companies_ls.append(company)
    return None


def read_companies_info():
    company_name = input('Введите название предприятия: ')
    revenue = sum(list(map(int, input(
        'через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): ').split())))
    return company_name, revenue


def get_avg_profit():
    return round(sum([company.revenue for company in companies_ls]) / len(companies_ls), 2)


def systematize_companies(ls, av_pr):
    height, low = [], []
    for company in ls:
        if company.revenue >= av_pr:
            height.append(company.name)
        else:
            low.append(company.name)
    return height, low


def main():
    count_of_companies = int(input('Введите количество предприятий для расчета прибыли: '))
    for i in range(count_of_companies):
        company_name, revenue = read_companies_info()
        add_to_companies_list(company_name, revenue)
    avg_profit = get_avg_profit()
    height, low = systematize_companies(companies_ls, avg_profit)
    print(
        f"Средняя годовая прибыль всех предприятий: {avg_profit}\nПредприятия, "
        f"с прибылью выше среднего значения: {', '.join(height)}\nПредприятия, "
        f"с прибылью ниже среднего значения: {', '.join(low)}")


if __name__ == '__main__':
    main()
