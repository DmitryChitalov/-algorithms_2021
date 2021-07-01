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

def lst_int(cmp):
    return int(cmp.quarterly_profit.split(' ')[0]) + int(cmp.quarterly_profit.split(' ')[1]) + int(cmp.quarterly_profit.split(' ')[2]) + int(cmp.quarterly_profit.split(' ')[3])

def more_profit(profit, cmp):
    if lst_int(cmp) >= profit:
        return cmp.name
    return ''

def less_profit(profit, cmp):
    if lst_int(cmp) < profit:
        return cmp.name
    return ''


quantity = int(input('Введите количество предприятий для расчета прибыли: '))

REZ = namedtuple('Company', 'name quarterly_profit')

company = []
all_profit = 0
for i in range(1, quantity+1):
    company.append(REZ(name=input(f'Введите название {i} предприятия: '), quarterly_profit=input(f'Введите прибыль данного предприятия за каждый квартал через пробел: ')))
    all_profit += lst_int(company[i-1])

print(f'Средняя годовая прибыль всех предприятий: {all_profit/4}')

print('Предприятия, с прибылью выше среднего значения: ', end=' ')
for el in company:
    print(more_profit(all_profit / 4, el), end=' ')

print()

print('Предприятия, с прибылью ниже среднего значения: ', end=' ')
for el in company:
    print(less_profit(all_profit / 4, el), end=' ')
