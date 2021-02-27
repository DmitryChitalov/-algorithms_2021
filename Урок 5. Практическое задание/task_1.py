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


firm_amount = int(input('Введите количество предприятий для расчета прибыли: '))
firm_list = []
firm = namedtuple('firm', 'name profit')

for i in range(firm_amount):
    firm_list.append(firm(
        name=input('Введите название фирмы: '),
        profit=list(map(int, input('Через пробел введите прибыль предприятия (За 4 квартала): ').split()))
    ))

mid_profit = 0
for i in firm_list:
    mid_profit += sum(i.profit)/len(firm_list)


def higher_lower(firms, mid, higher_list=[], lower_list=[]):
    if len(firms) <= 0:
        return higher_list, lower_list
    else:
        add_firm, profit = firms.pop()
        higher_list.append(add_firm) if sum(profit) > mid else lower_list.append(add_firm)
        return higher_lower(firms, mid, higher_list, lower_list)


higher_firms, lower_firms = higher_lower(firm_list, mid_profit)

print(f'Средняя годовая прибыль фирм: {mid_profit}')

print('Предприятия, с прибылью выше среднего значения:')
for i in higher_firms:
    print(i)

print('Предприятия, с прибылью ниже среднего значения:')
for i in lower_firms:
    print(i)
