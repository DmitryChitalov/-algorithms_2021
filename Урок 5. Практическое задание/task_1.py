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


def average_annual_profit(company_list):
    profit = 0
    up_average = []
    down_average = []
    for comp in company_list:
        profit += sum(comp[1:])
    for comp in company_list:
        up_average.append(comp.company_name) \
            if sum(comp[1:]) >= profit / len(company_list) \
            else down_average.append(comp.company_name)
    return f'Средняя годовая прибыль всех предприятий: {profit / len(company_list)}\n' \
           f'Предприятия, с прибылью выше среднего значения: {", ".join(up_average)}\n' \
           f'Предприятия, с прибылью ниже среднего значения: {", ".join(down_average)}'


company_quantity = int(input('Введите общее количество компаний: '))
company_data = []
company = namedtuple('Company_data', 'company_name kv_1 kv_2 kv_3 kv_4')
for i in range(company_quantity):
    comp_name = input(f'Введите название {i + 1}ой компании: ')
    comp_profit = input('Через пробел введите прибыль данного предприятия за каждый квартал: ').split(' ')
    company_data.append(company(comp_name,
                                int(comp_profit[0]),
                                int(comp_profit[1]),
                                int(comp_profit[2]),
                                int(comp_profit[3])))

print(average_annual_profit(company_data))




