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
from statistics import mean

firms = namedtuple('firms', 'name earning')
average_earning = {}

firms_num = int(input('Enter the num of firms'))
for el in range(firms_num):
    firm_name = input('Enter the name of the firm: ')
    firm_earning = list(map(int, input('Enter the firm`s earning by quarter: ').split()))
    firm = firms(firm_name, firm_earning)
    average_earning[firm.name] = round(mean(firm.earning))

total_average = sum(average_earning.values()) / firms_num

for key, val in average_earning.items():
    if val < total_average:
        print(f'{key} Less than average')
    else:
        print(f'{key} More than average')
