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


def func():
    n = int(input('Введите количество предприятий для расчета прибыли: '))
    company = namedtuple('quarterly_profit', 'name_company quarter_1 quarter_2 quarter_3 quarter_4')
    company_dict = {}
    for i in range(n):
        name = input('Введите название предприятия: ')
        profit = list(map(float, input('Через пробел введите прибыль данного '
                                       'предприятия за каждый квартал(Всего 4 квартала): ').split()))
        company_profit = company(name_company=name,
                                 quarter_1=profit[0],
                                 quarter_2=profit[1],
                                 quarter_3=profit[2],
                                 quarter_4=profit[3])
        company_dict[company_profit.name_company] = (company_profit.quarter_1 + company_profit.quarter_2 +
                                                     company_profit.quarter_3 + company_profit.quarter_4)

    average_profit = sum(el for el in company_dict.values()) / n
    list_max = [el for el in company_dict.keys() if company_dict[el] >= average_profit]
    list_min = [el for el in company_dict.keys() if company_dict[el] < average_profit]
    print(f'Предприятия, с прибылью средней и выше среднего значения: {", ".join(list_max)}')
    print(f'Предприятия, с прибылью ниже среднего значения: {", ".join(list_min)}')


if __name__ == '__main__':
    func()
