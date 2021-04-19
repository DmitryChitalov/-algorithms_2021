"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections

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

from collections import ChainMap

is_mock = True


def get_companies_mock():
    return [
        {
            'name': 'Yandex',
            'profits': [20, 30, 40, 50],
        },
        {
            'name': 'Google',
            'profits': [50, 90, 70, 90],
        },
        {
            'name': 'Apple',
            'profits': [10, 10, 20, 90],
        },
    ]


def get_companies():
    companies_count = input('Введите количество предприятий для расчета прибыли: ')
    companies = []
    for _ in range(int(companies_count)):
        name = input('Введите название предприятия: ')
        profits_raw = input('через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): ')
        profits = list(map(int, profits_raw.split(' ')))
        companies.append({
            'name': name,
            'profits': profits,
        })
    return companies


def get_average(array):
    return sum(array) / len(array)


def add_average_annual_profit(company):
    company['average_annual_profit'] = get_average(company['profits'])
    return company


companies = []

if is_mock:
    companies = get_companies_mock()
else:
    companies = get_companies()

average_profits = list(map(lambda company: get_average(company['profits']), companies))

company_views = []
for i in range(len(companies)):
    company = companies[i]
    average_profit = average_profits[i]
    company_views.append(ChainMap(
        company,
        {
            'average_annual_profit': average_profit,
        }
    ))

total_average_annual_profit = get_average(average_profits)

names_with_more_than_average_annual_profit = list(map(
    lambda company: company['name'],
    filter(
        lambda company: company['average_annual_profit'] > total_average_annual_profit,
        company_views
    )
))
names_with_less_than_average_annual_profit = list(map(
    lambda company: company['name'],
    filter(
        lambda company: company['average_annual_profit'] < total_average_annual_profit,
        company_views
    )
))

print(f'Средняя годовая прибыль всех предприятий: {total_average_annual_profit}')
print(f'Предприятия, с прибылью выше среднего значения: {names_with_more_than_average_annual_profit}')
print(f'Предприятия, с прибылью ниже среднего значения: {names_with_less_than_average_annual_profit}')
