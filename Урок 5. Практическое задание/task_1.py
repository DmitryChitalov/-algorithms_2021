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

from collections import Counter


def profit_average():
    count_company = int(input('Please enter number of companies: '))
    company = Counter()
    counter = 0
    for _ in range(count_company):
        count_profit = 0
        com = input('Please enter name company: ')
        val = input('Please enter the profit this enterprise after space for each quarter: ')
        for el in val.split():
            count_profit += int(el)
        company[com] = count_profit
        counter += count_profit
    counter /= count_company
    companies_profit = []
    companies_unprofit = []
    for el in company.keys():
        if company[el] >= counter:
            companies_profit.append(el)
        else:
            companies_unprofit.append(el)
    return "Average annual profit of all enterprises: %d \nEnterprises with above average profit: %s \n" \
           "Enterprises with below average profit %s "\
           % (counter, ', '.join(companies_profit), ', '.join(companies_unprofit))


if __name__ == '__main__':
    print(profit_average())
