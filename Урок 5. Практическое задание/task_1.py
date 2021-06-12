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


def counter_firm():
    n = int(input('Введите количество предприятий для расчета прибыли: '))
    firm = namedtuple('Firm', 'firm_name first_quarter second_quarter third_quarter forth_quarter avg_profit')
    lst = []
    for _ in range(n):
        firm_name = input('Введите название предприятия: ')
        quarter = list(map(int, input('через пробел введите прибыль данного предприятия за каждый'
                                      'квартал(Всего 4 квартала): ').split(' ')))
        lst.append(firm(
            firm_name=firm_name,
            first_quarter=quarter[0],
            second_quarter=quarter[1],
            third_quarter=quarter[2],
            forth_quarter=quarter[3],
            avg_profit=(sum(quarter) / 4)
        ))
    avg_all = 0
    for company in range(n):
        avg_all += lst[company].avg_profit
    avg_all = round(avg_all / n, 2)
    max_firm, min_firm = '', ''

    for company in range(n):
        if lst[company].avg_profit > avg_all:
            max_firm = max_firm + (' ,' if max_firm != '' else '') + (lst[company].firm_name)
        else:
            min_firm = min_firm + (' ,' if min_firm != '' else '') + (lst[company].firm_name)

    return f'Средняя годовая прибыль всех предприятий:{avg_all}\n' \
           f'Предприятия, с прибылью выше среднего значения: {max_firm}\n' \
           f'Предприятия, с прибылью ниже среднего значения или равным ему: {min_firm}'


print(counter_firm())
