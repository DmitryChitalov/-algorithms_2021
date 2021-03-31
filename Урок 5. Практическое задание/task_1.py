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


company_template = namedtuple('Company', 'q1 q2 q3 q4')
number_of_companies = int(input("Введите количество предприятий для расчета прибыли: "))

total_companies = {}
income_collector = 0
for i in range(number_of_companies):
    current_company_name = input("Введите название предприятия: ")
    current_company_stats = input("через пробел введите прибыль данного предприятия: ")
    current_company_stats_lst = list(map(int, current_company_stats.split()))
    current_company = company_template._make(current_company_stats_lst)
    income_collector += sum(current_company)
    total_companies[current_company_name] = current_company

average_income = income_collector / number_of_companies
print(f"Средняя годовая прибыль всех предприятий: {average_income}")
print("Предприятия, с прибылью выше среднего значения: ", end="")
for company, stats in total_companies.items():
    if sum(stats) > average_income:
        print(company, end=" ")
print()
print("Предприятия, с прибылью ниже среднего значения: ", end="")
for company, stats in total_companies.items():
    if sum(stats) < average_income:
        print(company, end=" ")
print()
