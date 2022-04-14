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
import collections

organizations = []
org = collections.namedtuple('organization', 'org_name revenue_1 revenue_2 revenue_3 revenue_4 total_revenue')
n = int(input('Введите количество организаций: '))
for i in range(n):
    org_name = input('Введите наименование организации: ')
    revenue_1 = float(input('Введите выручку за 1-й квартал: '))
    revenue_2 = float(input('Введите выручку за 2-й квартал: '))
    revenue_3 = float(input('Введите выручку за 3-й квартал: '))
    revenue_4 = float(input('Введите выручку за 4-й квартал: '))
    total_revenue = revenue_1 + revenue_2 + revenue_3 + revenue_4
    organizations.append(org(
        org_name=org_name,
        revenue_1=revenue_1,
        revenue_2=revenue_2,
        revenue_3=revenue_3,
        revenue_4=revenue_4,
        total_revenue=total_revenue
    ))

global_revenue = 0
for i in organizations:
    global_revenue += i.total_revenue
average_revenue = global_revenue / len(organizations)

above_average = []
below_average = []
for i in organizations:
    above_average.append(i.org_name) if i.total_revenue >= average_revenue else below_average.append(i.org_name)

print(f'Средняя годовая прибыль всех предприятий: {average_revenue}')
print(f'Организации получившие прибыль выше среднего: {", ".join(above_average)}')
print(f'Организации получившие прибыль ниже среднего: {", ".join(below_average)}')
