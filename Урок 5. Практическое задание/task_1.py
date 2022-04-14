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

from collections import defaultdict


dict_of_comp_income = defaultdict(list)
amount_company = int(input('Enter amount of companies: '))

for i in range(amount_company):
    company_name = input('Enter company name: ')
    income_4q = map(int, input('Enter income for every quater separated by space: ').split())
    dict_of_comp_income[company_name] = sum(income_4q)

avrg_inc = sum(dict_of_comp_income.values()) / amount_company
more_avrg = []
less_avrg = []

for name, inc in dict_of_comp_income.items():
    if inc > avrg_inc:
        more_avrg.append(name)
    else:
        less_avrg.append(name)


print(f'Average income of all companies: {avrg_inc}.\nCompanies that have income more average: {more_avrg}\n'
      f'Companies that have income less average: {less_avrg} ')

