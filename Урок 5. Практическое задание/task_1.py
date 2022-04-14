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
from statistics import mean

Companies = namedtuple('Companies', 'name income')
income_average = {}
companies_less_average_income = []
companies_above_average_income = []

companies_count = int(input('Введите количество предприятий для расчета прибыли: '))

for i in range(companies_count):
    company_name = input('Введите название предприятия: ')

    company_income = list(map(int, input(
        'Через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): ').split()))
    company = Companies(company_name, company_income)
    income_average[company.name] = round(mean(company.income))

income_average_total = sum(income_average.values()) / companies_count

for key, value in income_average.items():
    if value < income_average_total:
        companies_less_average_income.append(key)
    elif value > income_average_total:
        companies_above_average_income.append(key)

print()
print(f'Средняя годовая прибыль всех предприятий: {income_average_total}')
print(f'Предприятия, с прибылью выше среднего значения: {companies_above_average_income}')
print(f'Предприятия, с прибылью ниже среднего значения: {companies_less_average_income}')
