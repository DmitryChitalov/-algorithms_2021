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

company = namedtuple('firm', ['name', 'q1', 'q2', 'q3', 'q4'])


def average(avg):
    return avg.q1 + avg.q2 + avg.q3 + avg.q4


def company_profit():
    company_list = []
    less = []
    more = []
    number_firm = int(input('Введите количество предприятий для расчета прибыли: '))

    for i in range(number_firm):
        firm = input('Введите название предприятия: ')
        profits = input('Через пробел введите прибыль предприятия за каждый квартал(Всего 4 квартала): ')
        company_list.append(company(firm, *map(int, profits.split())))

    avg_profit = sum(map(average, company_list)) / len(company_list)
    print(f'Средняя годовая прибыль всех предприятий: {avg_profit}')

    for elem in company_list:
        if average(elem) < avg_profit:
            less.append(elem.name)
        elif average(elem) > avg_profit:
            more.append(elem.name)

    print(f'Предприятия, с прибылью выше среднего значения: {", ".join(more)}')
    print(f'Предприятия, с прибылью ниже среднего значения: {", ".join(less)}')


company_profit()
