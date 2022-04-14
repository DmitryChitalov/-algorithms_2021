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

n = int(input('Введите количество предприятий для расчета прибыли: '))
COMPANY = namedtuple('Company', 'company_name first_quarter_profit second_quarter_profit third_quarter_profit fourth_quarter_profit year_profit')
companies_list = []

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
# print(companies_list)
total_year_profit = 0
for c in companies_list:
    total_year_profit += c.year_profit
aver_year_profit = total_year_profit / n
top_profit_companies = [c.company_name for c in companies_list if c.year_profit > aver_year_profit]
low_profit_companies = [c.company_name for c in companies_list if c.year_profit < aver_year_profit]

print(f'Средняя годовая прибыль всех предприятий: {aver_year_profit}')
print('Предприятия, с прибылью выше среднего значения:')
print(*top_profit_companies, sep=', ')
print('Предприятия, с прибылью ниже среднего значения:')
print(*low_profit_companies, sep=', ')

