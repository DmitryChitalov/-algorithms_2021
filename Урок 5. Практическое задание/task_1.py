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


def main():
    company = namedtuple('Company', ('name', 'profit'))
    company_ls = []
    n = int(input('Введите количество предприятий для расчета прибыли: '))

    for _ in range(n):
        name = input('Введите название предприятия: ')
        profit = input('через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): ').split()
        company_ls.append(company(name=name, profit=sum(map(int, profit[:4]))))
    average = sum(c.profit for c in company_ls) / n
    print(f'Средняя годовая прибыль всех предприятий: {average}')
    print(
        f'Предприятия, с прибылью выше среднего значения: {"".join([company.name for company in company_ls if company.profit > average])}')
    print(
        f'Предприятия, с прибылью ниже среднего значения: {"".join([company.name for company in company_ls if company.profit < average])}')


main()
