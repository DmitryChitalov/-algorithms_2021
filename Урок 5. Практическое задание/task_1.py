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
import re


def annual_profit():
    list_of_companies = {}
    sum_of_profit = 0
    above_profit = []
    below_profit = []
    equal_profit = []
    while True:
        try:
            n = int(input('Введите количество предприятий: '))
        except ValueError:
            print('Введите число')
        else:
            break
    COMPANY = namedtuple('Company', 'name profit')
    while n >= 1:
        company = input('Введите название предприятия: ')
        while True:
            profit = input('Через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): ')
            if re.match('[0-9 ]+$', profit):
                break
            else:
                print('Неправильный ввод, необходимо вводить суммы цифрами через пробел')
        profit = sum(list(map(int, profit.split())))
        company_parts = COMPANY(
            name=company,
            profit=profit
        )
        list_of_companies[company] = company_parts
        n -= 1
    for part in list_of_companies.values():
        sum_of_profit += part.profit
    average_profit = sum_of_profit/len(list_of_companies)
    for part in list_of_companies.values():
        if part.profit > average_profit:
            above_profit.append(part.name)
        elif part.profit == average_profit:
            equal_profit.append(part.name)
        else:
            below_profit.append(part.name)
    print(f'Средняя годовая прибыль всех предприятий: {average_profit}')
    print(f'Предприятия, с прибылью выше среднего значения: {above_profit}')
    print(f'Предприятия, с прибылью равной среднему значению: {equal_profit}')
    print(f'Предприятия, с прибылью ниже среднего значения: {below_profit}')
    return list_of_companies


print(annual_profit())
