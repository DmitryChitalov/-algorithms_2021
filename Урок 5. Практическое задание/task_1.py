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

company_statistic = {}
company = namedtuple('company', 'firm_name quarter_1 quarter_2 quarter_3 quarter_4')

company_count = int(input('Введите количество предприятий для расчета прибыли: '))

for i in range(company_count):
    firm = company(firm_name=input('Введите название фирмы: '),
                   quarter_1=int(input('1-й квартал: ')),
                   quarter_2=int(input('2-й квартал: ')),
                   quarter_3=int(input('3-й квартал: ')),
                   quarter_4=int(input('4-й квартал: ')))

    avg_quarter = (firm.quarter_1 + firm.quarter_2 + firm.quarter_3 + firm.quarter_4) / 4
    company_statistic[firm.firm_name] = avg_quarter

avg_profit_company = 0
for val in company_statistic.values():
    avg_profit_company += val
avg_profit_company = round((avg_profit_company / company_count), 2)

big_company, avg_company, little_company = [], [], []
for key, val in company_statistic.items():
    if val < avg_profit_company:
        little_company.append(key)
    elif val == avg_profit_company:
        avg_company.append(key)
    elif val > avg_profit_company:
        big_company.append(key)

print(f'Средняя годовая прибыль всех предприятий: {avg_profit_company}\n'
      f'Предприятия, с прибылью ниже среднего значения: {little_company}\n'
      f'Предприятия, с прибылью равной среднему значению: {avg_company}\n'
      f'Предприятия, с прибылью выше среднего значения: {big_company}')