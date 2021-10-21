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


def create_info(num):
    RES = namedtuple('Resume', 'id company_name quarterly_profit')
    resume_parts = RES(
        id=num,
        company_name=input('Введите название предприятия: : '),
        quarterly_profit=list(map(int, input(f'через пробел введите прибыль данного предприятия \n'
                                             f'за каждый квартал(Всего 4 квартала): ').split()))
        )
    return resume_parts


def average_profit(obj):
    lower_average = []
    above_average = []
    total = 0
    for i in obj:
        for j in i.quarterly_profit:
            total += j
    average = total / len(obj)
    for i in obj:
        if average < sum(i.quarterly_profit):
            lower_average.append(i.company_name)
        else:
            above_average.append(i.company_name)
    return average, lower_average, above_average


def create_list_company(num):
    lst_company = []
    for i in range(num):
        lst_company.append(create_info(i+1))
    return lst_company


some_list = create_list_company(int(input('Введите данные о количестве предприятий: ')))
result = average_profit(some_list)
print(f'Средняя годовая прибыль всех предприятий: {result[0]}')
print(f'Предприятия, с прибылью выше среднего значения: {", ".join(result[1])}\n')
print(f'Предприятия, с прибылью ниже среднего значения: {", ".join(result[2])}')
