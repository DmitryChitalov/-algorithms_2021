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


CompanyParams = namedtuple('CompanyParams', 'id name income1 income2 income3 income4')
companies_quantity = int(input('Введите кол-во компаний: '))
company_list = []
param_list = []
for company in range(companies_quantity):
    str_income = input('Введите через пробел название и прибыль за каждый из 4-х кварталов: ')
    param_list.append(company+1)
    param_list.extend(str_income.split())
    company_info = CompanyParams._make(param_list)
    company_list.append(company_info)
    param_list = []
companies_income = {}
i = 1
for company in company_list:
    companies_income[i] = int(company.income1) + int(company.income2) + int(company.income3) + int(company.income4)
    i += 1
print(f'Годовые доходы {companies_income}')
avg_income = sum(companies_income.values())/companies_quantity
print(f'Среднее {avg_income}')
print(f'компании с доходом меньше среднего '
      f'{[el.name for el in company_list if el.id in [id for id in companies_income.keys() if companies_income[id] < avg_income]]}')
print(f'компании с доходом больше среднего '
      f'{[el.name for el in company_list if el.id in [id for id in companies_income.keys() if companies_income[id] > avg_income]]}')
