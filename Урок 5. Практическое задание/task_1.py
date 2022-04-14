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

number_company = int(input('Введите количество предприятий для расчета прибыли: '))
company = namedtuple('Company', 'one two tree four')
firms = {}
for i in range(number_company):
    name_company = input('Введите название предприятия: ')
    profit = list(
        map(int, input('через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала):').split())
    )
    firms[name_company] = (company(*profit))

annual_profit = 0
for i in firms:
    annual_profit += sum(firms[i])

total_midl = annual_profit / len(firms)

for k, v in firms.items():
    if total_midl < sum(v):
        print(f'Предприятия, с прибылью выше среднего значения: {k}')
    elif total_midl > sum(v):
        print(f'Предприятия, с прибылью ниже среднего значения: {k}')

print(f'Средняя годовая прибыль всех предприятий {total_midl}')
