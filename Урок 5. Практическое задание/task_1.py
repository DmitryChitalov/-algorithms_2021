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
from collections import namedtuple


company_amount = int(input('Введите количество компаний для расчета прибыли: '))
company_list = []
company = namedtuple('company', 'name profit')

for i in range(company_amount):
    company_list.append(company(
        name=input('Введите название компании: '),
        profit=list(map(int, input('Через пробел введите прибыль компании за каждый квартал (Всего 4 квартала): ').split()))
    ))

mid_profit = 0
for i in company_list:
    mid_profit += sum(i.profit)/len(company_list)


def higher_lower(companies, mid, higher_list=[], lower_list=[]):
    if len(companies) <= 0:
        return higher_list, lower_list
    else:
        add_firm, profit = companies.pop()
        higher_list.append(add_firm) if sum(profit) > mid else lower_list.append(add_firm)
        return higher_lower(companies, mid, higher_list, lower_list)


higher_company, lower_company = higher_lower(company_list, mid_profit)

print(f'Средняя годовая прибыль компании: {mid_profit}')

print('Компания, с прибылью выше среднего значения:')
for i in higher_company:
    print(i)

print('Компания, с прибылью ниже среднего значения:')
for i in lower_company:
    print(i)