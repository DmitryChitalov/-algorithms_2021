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

corp = namedtuple('corp', 'name year_revenue')

num_of_companies = int(input('Введите количество компаний для заполнения '))

companies_list = []
total_revenue = 0

for i in range(num_of_companies):
    name = input('Введите название компании ')
    rev = input('Введите выручку за последние 4 квартала через пробел ')

    rev_str = rev.split()
    year_revenue = 0
    for n in rev_str:
        year_revenue += int(n)

    comp_metrics = corp(
        name=name,
        year_revenue=year_revenue
    )

    companies_list.append(comp_metrics)
    total_revenue += comp_metrics.year_revenue

average_revenue = total_revenue / num_of_companies

below_list = []
above_list = []
for k in companies_list:
    if k.year_revenue >= average_revenue:
        above_list.append(k.name)
    else:
        below_list.append(k.name)

print(f'Средняя прибыль всех предприятий {average_revenue}')
print(f'Предприятия, с прибылью выше среднего значения: {above_list}')
print(f'Предприятия, с прибылью ниже среднего значения: {below_list}')
