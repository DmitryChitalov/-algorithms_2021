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
Класс collections.namedtuple()"""
from collections import namedtuple


def companies_average(obj):
    sum_all_average = sum(company.average for company in obj)
    return sum_all_average / len(obj)


def companies_up(obj, average):
    up_list = []
    for company in obj:
        if company.average > average:
            up_list.append(company.name)
    return up_list


def companies_down(obj, average):
    down_list = []
    for company in obj:
        if company.average < average:
            down_list.append(company.name)
    return down_list


RES = namedtuple('Company_profit', 'name profit_1 profit_2 profit_3 profit_4 average')
companies_number = int(input('Введите количество предприятий для расчета прибыли: '))
companies_list = []
for i in range(companies_number):
    temp_name = input('Введите название предприятия: ')
    temp_profit = [int(x) for x in input('через пробел введите прибыль данного предприятия\
за каждый квартал(Всего 4 квартала): ').split()]
    companies_list.append(RES(
        name=temp_name,
        profit_1=temp_profit[0],
        profit_2=temp_profit[1],
        profit_3=temp_profit[2],
        profit_4=temp_profit[3],
        average=sum(temp_profit) / len(temp_profit)
    ))
    print(f'{companies_list[i].name, companies_list[i].average}')

companies__average = companies_average(companies_list)
print(f'\nСредняя годовая прибыль всех предприятий: {companies__average}')
print(f'Предприятия, с прибылью выше среднего значения: {companies_up(companies_list, companies__average)}')
print(f'Предприятия, с прибылью ниже среднего значения: {companies_down(companies_list, companies__average)}')
