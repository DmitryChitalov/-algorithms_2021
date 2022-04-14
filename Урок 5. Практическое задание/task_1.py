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
from collections import namedtuple

average_profit = {}
quantity_of_company = int(input('Введите количество предприятий для расчета прибыли:'))

for el in range(quantity_of_company):
    enterprise = namedtuple('сompany', 'name profit_1 profit_2 profit_3 profit_4')
    data_parts = enterprise(
        name=input('Введите название предприятия:'),
        profit_1=int(input('Введите прибыль за 1 квартал: ')),
        profit_2=int(input('Введите прибыль за 2 квартал: ')),
        profit_3=int(input('Введите прибыль за 3 квартал: ')),
        profit_4=int(input('Введите прибыль за 4 квартал: ')))

    average_profit[data_parts.name] = (data_parts.profit_1 + data_parts.profit_2 + data_parts.profit_3 +
                                       data_parts.profit_4) / quantity_of_company

total = 0

for el in average_profit.values():
    total += el
total = total / quantity_of_company
print(f'Средняя годовая прибыль всех предприятий: {total}')

for k, v in average_profit.items():
    if v > total:
        print(f'Предприятия, с прибылью выше среднего значения: {k}')
    else:
        print(f'Предприятия, с прибылью ниже среднего значения: {k}')
