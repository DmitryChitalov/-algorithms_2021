"""
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль
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


ProfitEnterprise = namedtuple('profit_enterprise', 'first second third fourth')


enterprise = {}


def enter_info_enterprise(i):
    info_enterprise = input(f'Введите название предприятия {i} \n'
                            f'и через пробел прибыль данного предприятия\n'
                            f'за каждый квартал(Всего 4 квартала):').split()
    return info_enterprise


def number_enterprise():
    return int(input('Введите количество предприятий: '))


def average_profit():
    total_profit = []
    for profit in enterprise.values():
        for i in profit:
            total_profit.append(int(i))
    average = sum(total_profit) / len(total_profit)

    above_average = ''
    below_average = ''
    for title, profit in enterprise.items():
        if sum(map(int, profit)) > average:
            above_average += f'"{title}" '
        else:
            below_average += f'"{title}" '

    return f'Средняя годовая прибыль всех предприятий: {average}\n' \
           f'Предприятия, с прибылью выше среднего значения: {above_average}\n' \
           f'Предприятия, с прибылью ниже среднего значения: {below_average}'


for i in range(1, number_enterprise() + 1):
    temp = enter_info_enterprise(i)
    enterprise[temp[0]] = ProfitEnterprise._make(temp[1:])


print(average_profit())

'''
Выполнил задания до разбора, в задании указанно ввести через пробел название фирмы и прибыль, именованный кортеж
теряет смысл, а в разборе все вводится отдельно, и сразу ясно для чего использовать namedtuple.
'''