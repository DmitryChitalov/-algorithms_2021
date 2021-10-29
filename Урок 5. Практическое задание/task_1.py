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

enterprises = namedtuple('firm', ['name', 'q1', 'q2', 'q3', 'q4'])
enterprises_list = []
less_profit = []
more_profit = []

def average(avg):
    return avg.q1 + avg.q2 + avg.q3 + avg.q4

def company_profit():
    while True:
        try:
            n = int(input('Введите количество предприятий: '))
        except ValueError:
            print('Вы ввели недопустимое значение!')
            continue
        break

    for i in range(n):
        company = input('Введите название предприятия: ')
        profits = input('Через пробел введите прибыль данного предприятия за каждый квартал(всего 4 квартала): ')
        enterprises_list.append(enterprises(company, *map(int, profits.split())))

    avg_profit = sum(map(average, enterprises_list)) / len(enterprises_list)
    print(f'Средняя годовая прибыль всех предприятий: {avg_profit}')

    for el in enterprises_list:
        if average(el) < avg_profit:
            less_profit.append(el.name)
        elif average(el) > avg_profit:
            more_profit.append(el.name)

    print(f'Предприятия, с прибылью выше среднего значения: {", ".join(more)}')
    print(f'Предприятия, с прибылью ниже среднего значения: {", ".join(less)}')

company_profit()