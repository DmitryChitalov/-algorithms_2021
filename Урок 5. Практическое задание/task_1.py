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

one_company_profit_lst = list()
company = list()
name_of_company = list()
all_companies_profit = 0
count_of_companies = int(input('Введите количество предприятий для расчета прибыли: '))
for i in range(count_of_companies):
    name_of_company.append(input('Введите название предприятия: '))
    companies = namedtuple("name_of_company", "one_company_profit")
    one_company_profit = sum(list(map(int, input('Через пробел введите прибыль данного предприятия '
                                 'за каждый квартал(Всего 4 квартала): ').split())))
    all_companies_profit += one_company_profit
    average_annual_profit = all_companies_profit / count_of_companies
    company.append(companies(one_company_profit))
    one_company_profit_lst.append(one_company_profit)
print('Средняя годовая прибыль всех предприятий: ', average_annual_profit)
for i in range(count_of_companies):
    if average_annual_profit < one_company_profit_lst[i]:
        print(f'Предприятия, с прибылью выше среднего значения: {name_of_company[i]}')
    else:
        print(f'Предприятия, с прибылью ниже среднего значения: {name_of_company[i]}')
