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
Введите название предприятиприятияя: Фирма_2
через пробел введите прибыль данного пред
за каждый квартал(Всего 4 квартала): 345 34 543 34
Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Фирма_1
Предприятия, с прибылью ниже среднего значения: Фирма_2
"""

from collections import namedtuple

def AVG_company():
    count_com = int(input('Введите количество предприятий для расчета прибыли: '))
    company = namedtuple("companies", "name profit")
    company_dict = {}
    for i in range(count_com):
        name_company = input('Введите название предприятия: ')
        profit_company = input('Через пробел введите прибыль данного'
                                   ' предприятия за каждый квартал(Всего 4 квартала): ')
        avg_profit = 0
        for i in profit_company.split(' '):
            avg_profit += int(i)
        avg_profit = avg_profit / 4
        companies = company(name=name_company, profit=avg_profit)
        company_dict[companies.name] = (companies.profit)
        print(companies)
    avg_profit_com = 0
    for value in company_dict.values():
        avg_profit_com += value
    avg_profit_com = avg_profit_com / count_com
    print(f'Cредняя прибыль (за год для всех предприятий): {avg_profit_com}')
    stonks = []
    no_stonks = []
    for key, value in company_dict.items():
        if value > avg_profit_com:
            stonks.append(key)
        if value <= avg_profit_com:
            no_stonks.append(key)
    print(f'Предприяти, с прибылью выше среднего значения: {stonks}')
    print(f'Предприятия, с прибылью ниже или равной среднему значению: {no_stonks}')
AVG_company()
