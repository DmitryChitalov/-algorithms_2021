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


def my_program():
    information = namedtuple('information', 'company_name average_profit')
    companies = {}
    profits = 0
    n = int(input('Please insert the number of companies: '))
    for i in range(n):
        company_name_1 = input('Please enter the name of the company: ')
        profit_1 = input(' Please insert the profit like this "32 66 899 554" :').split()
        profit = [int(i) for i in profit_1]
        new_inf = information(
            company_name=company_name_1,
            average_profit=sum(profit) / len(profit)

        )
        companies[company_name_1] = new_inf.average_profit
        profits = profits + new_inf.average_profit
    average_profits = profits / n
    print(f'Minimal average profit for each company is: {average_profits}')
    result = companies.items()
    for company, profit in result:
        if profit < average_profits:
            print(f'The company "{company}" has the average profit of {profit} ')


my_program()
