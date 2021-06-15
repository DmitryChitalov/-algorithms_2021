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

def companies(n):
    average_profit = []
    company = {}
    for i in range(n):
        name_company = input('Введите название компании: ')
        profit = input('Введите прибыль за 4 квартала через пробел: ')
        profit = profit.split(' ')
        TAMPLATES = namedtuple(f'{name_company}', 'quarter_one quarter_two quarter_three quarter_four')
        name_company = TAMPLATES(
            quarter_one=int(profit[0]),
            quarter_two=int(profit[1]),
            quarter_three=int(profit[2]),
            quarter_four=int(profit[3]))
        sum_profit = name_company.quarter_one + name_company.quarter_two + \
                     name_company.quarter_three + name_company.quarter_four
        company[name_company] = sum_profit
        average_profit.append(sum_profit)
    return int(sum(average_profit) / len(average_profit)), company


def check_average_profit(average_profit, company_dict):
    below_the_average, above_average = {}, {}
    for key, value in company_dict.items():
        if value < average_profit:
            below_the_average[key] = value
        else:
            above_average[key] = value
    return f'Средняя годовая прибыль всех предприятий: {average_profit}\n'\
           f'Предприятия, с прибылью ниже среднего значения: {below_the_average}\n' \
           f'Предприятия, с прибылью выше среднего значения: {above_average}'

average_profit, company_dict = companies(int(input('Введите кол-во компаний: ')))
print(check_average_profit(average_profit, company_dict))