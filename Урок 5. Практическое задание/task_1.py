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


def add_firm(count_firm):
    all_company = []
    for el in range(count_firm):
        name = input('Введите название фирмы')
        profits_srt = input('Введите через пробел прибыль данного предприятия за каждый квартал: ')
        profits = profits_srt.split()
        if len(profits) != 4:
                print('Вы ввели либо мало, либо много значений')
                continue
        try:
            average_profit = (int(profits[0]) + int(profits[1]) + int(profits[2]) + int(profits[3])) / 4
            firm_tuple = Firm_template(name_firm=name,
                                       average_profit_firm=average_profit)
            all_company.append(firm_tuple)
        except ValueError:
            print('Вы ввели не правильное значение прибыли!!!')
            continue
    return all_company


def aver_profit(all_company):
    average_profit_all_firm = 0
    average_profit_less = []
    average_profit_more = []
    for el in all_company:
        average_profit_all_firm = average_profit_all_firm + el.average_profit_firm
    average_profit_all_firm = average_profit_all_firm / len(all_company)
    print(f'Средняя годовая прибыль всех предприятий: {average_profit_all_firm}')
    for el in all_company:
        if el.average_profit_firm >= average_profit_all_firm:
            average_profit_more.append(el.name_firm)
        else:
            average_profit_less.append(el.name_firm)
    print(f'Предприятия, с прибылью выше среднего значения: {average_profit_more}')
    print(f'Предприятия, с прибылью ниже среднего значения: {average_profit_less}')


Firm_template = namedtuple('Firm_Profit', 'name_firm average_profit_firm')
try:
    count_firm = int(input('Введите количество предприятий для расчета прибыли: '))
    aver_profit(add_firm(count_firm))
except ValueError:
    print('Вы ввели не число!!!')

