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

companies = namedtuple('corp', 'name year_profit')

count_of_companies = int(input('Введите предприятий для расчета прибыли: '))

companies_list = []
total_profit = 0

for i in range(count_of_companies):
    name = input('Введите название предприятия: ')
    profit = input('Через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): ')

    profit_str = profit.split()
    year_profit = 0
    for j in profit_str:
        year_profit += int(j)

    companies_metrics = companies(
        name=name,
        year_profit=year_profit
    )

    companies_list.append(companies_metrics)
    total_profit += companies_metrics.year_profit

average_profit = total_profit / count_of_companies

below_average = []
above_average = []
for n in companies_list:
    if n.year_profit >= average_profit:
        above_average.append(n.name)
    else:
        below_average.append(n.name)

print(f'Средняя прибыль всех предприятий {average_profit}')
print(f'Предприятия, с прибылью выше среднего значения: {above_average}')
print(f'Предприятия, с прибылью ниже среднего значения: {below_average}')
