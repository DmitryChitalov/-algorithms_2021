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


def create_namedtuple():
    company_profit = namedtuple('Profit', 'name, first_quarter, second_quarter, third_quarter, fourth_quarter')
    name = input('Введите название предприятия: ')
    first_quarter, second_quarter, third_quarter, fourth_quarter = map(int, input(
        "Введите через пробел прибыль данного предприятия\n"
        "за каждый квартал(Всего 4 квартала): ").split())
    result = company_profit(name, first_quarter, second_quarter, third_quarter, fourth_quarter)
    return result


more_below_average = {'more': [], 'below': []}
company_number = int(input('Введите колличество предприятий: '))
result_company_tuple = [create_namedtuple() for i in range(company_number)]
full_profit_company = [int(i.first_quarter) + int(i.second_quarter) + int(i.third_quarter) + int(i.fourth_quarter)
                       for i in result_company_tuple]
average_profit = sum(full_profit_company) / company_number

for el in range(len(result_company_tuple)):
    if full_profit_company[el] > average_profit:
        more_below_average['more'].append(result_company_tuple[el].name)
    else:
        more_below_average['below'].append(result_company_tuple[el].name)

print(f'Предприятия, с прибылью выше среднего значения: {more_below_average["more"]}')
print(f'Предприятия, с прибылью ниже среднего значения: {more_below_average["below"]}')
