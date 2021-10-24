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


def company_profit():
    info = {}
    best_comp = []
    loosers_comp = []
    quantity_companies = int(input("Введите количество предприятий для расчета прибыли: "))
    company = namedtuple('Company', ['comp_name', 'inc_1', 'inc_2', 'inc_3', 'inc_4'])
    for i in range(quantity_companies):
        company_name = input("Введите название предприятия: ")
        profit = input("Через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): ")
        profit_1, profit_2, profit_3, profit_4 = profit.split(' ')
        comp = company(company_name, int(profit_1), int(profit_2), int(profit_3), int(profit_4))
        info[comp.comp_name] = (comp.inc_1 + comp.inc_2 + comp.inc_3 + comp.inc_4)

    common_summ = 0
    for j in info.values():
        common_summ += j

    print(f'Средняя годовая прибыль всех предприятий: {round(common_summ/quantity_companies)}')

    for company_name, profit in info.items():
        if profit > common_summ/quantity_companies:
            best_comp.append(company_name)
        else:
            loosers_comp.append(company_name)
    print(f'Предприятия, с прибылью выше среднего значения: {" ".join(map(str, best_comp))}')
    print(f'Предприятия, с прибылью ниже среднего значения: {" ".join(map(str, loosers_comp))}')

company_profit()