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
from functools import reduce
from collections import namedtuple

companies = []
COM = namedtuple('Company', 'name profit_1 profit_2 profit_3 profit_4 profit_year')
company_count = 0

while True:
    try:
        company_count = int(input('Введите количество предприятий для расчета прибыли: '))
        if company_count < 1:
            raise ValueError
    except ValueError:
        continue
    break

for _ in range(company_count):
    while True:
        try:
            company_name = input('Введите название предприятия: ')
            if len(company_name) < 2:
                raise ValueError
            if company_name in [company.name for company in companies]:
                print(f'Компания {company_name} уже в списке!')
                continue
            q_profits_str = input('Через пробел введите прибыль данного предприятия'
                                  'за каждый квартал(Всего 4 квартала): ')
            q_profits = [float(i) for i in q_profits_str.split()]
            if len(q_profits) != 4:
                raise ValueError

            company = COM(
                name=company_name,
                profit_1=q_profits[0],
                profit_2=q_profits[1],
                profit_3=q_profits[2],
                profit_4=q_profits[3],
                profit_year=reduce(lambda a, b: a + b, q_profits) / 4
            )
            companies.append(company)
        except ValueError:
            print('Некорректные данные!')
            continue
        break

total_average_profit = reduce(lambda a, b: a + b, cp := [company.profit_year for company in companies])/len(cp)
below_avg_profit = [company.name for company in companies if company.profit_year < total_average_profit]
above_avg_profit = [company.name for company in companies if company.profit_year >= total_average_profit]

print(f'Средняя годовая прибыль всех предприятий: {total_average_profit}')
print('Предприятия, с прибылью выше среднего значения: ', end='')
print(*above_avg_profit, sep=', ')
print('Предприятия, с прибылью ниже среднего значения: ', end='')
print(*below_avg_profit, sep=', ')
