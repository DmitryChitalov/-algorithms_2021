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


def year_profit(comp_name, profit_lst):
    """
    Возвращает namedtuple с названием компании и годовым доходом
    :param comp_name: Название компании
    :param profit_lst: список из четырех сумм доходов за каждый квартал
    :return: Company(name, average_profit)
    """
    Company = namedtuple('Company', 'name year_profit')
    return Company(name=comp_name, year_profit=sum(profit_lst))


QUANTITY = int(input('Введите количество предприятий для расчета прибыли: '))
all_companies = {}
total_sum = 0

for _ in range(QUANTITY):
    company_name = input('Введите название предприятия: ')
    profits = list(map(int, input('через пробел введите прибыль данного предприятия '
                                  'за каждый квартал(Всего 4 квартала): ').split(' ')))
    company = year_profit(company_name, profits)
    all_companies[company.name] = company.year_profit
    total_sum += company.year_profit

average_for_all_companies = total_sum / QUANTITY
lt_average = []
gt_average = []

for name, avg in all_companies.items():
    if avg > average_for_all_companies:
        gt_average.append(name)
    else:
        lt_average.append(name)

print(f'Средняя годовая прибыль всех предприятий: {average_for_all_companies}')
print(f'Предприятия, с прибылью выше среднего значения: {", ".join(gt_average)}')
print(f'Предприятия, с прибылью ниже среднего значения: {", ".join(lt_average)}')
