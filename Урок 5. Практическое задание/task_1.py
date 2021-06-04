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
from collections import defaultdict

companies = namedtuple('firms', 'comp_name revenue')
companies_list = []
number_of_comp = int(input('Enter the number of companies: '))

for i in range(number_of_comp):
    company_name = input('Enter the name of the company: ')
    income = input('Enter the profit of this enterprise for each quarter, separated by a space: ')
    companies_list.append(companies(company_name, sum(list(map(int, income.split())))))

average_profit = sum(int(c.revenue) for c in companies_list) / number_of_comp
print(f'{"*" * 40}')
print(f'Average annual profit of all companies: {average_profit}')
for i in companies_list:
    if i.revenue >= average_profit:
        print(f'Enterprises with above average profit: {i.comp_name}\n')
    else:
        print(f'Enterprises with below average profit: {i.comp_name}')
