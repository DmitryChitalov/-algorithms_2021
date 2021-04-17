"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка: namedtuple (но не обязательно)
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


amount_of_firms = int(input('Введите количество компаний для расчета прибыли: '))
firms_list = []
firm = namedtuple('firm', 'name profit')

for i in range(amount_of_firms):
    firms_list.append(firm(
        name=input('Введите название компании: '),
        profit=list(map(int, input('Через пробел введите прибыль компании за каждый квартал '
                                   '(Всего 4 квартала): ').split()))
    ))


average_profit = 0
for i in firms_list:
    average_profit += sum(i.profit)/len(firms_list)


def func(companies, average, top_firms = [], low_firms = []):
    if len(companies) <= 0:
        return top_firms, low_firms
    else:
        add_firm, profit = companies.pop()
        if sum(profit) > average:
            top_firms.append(add_firm)
        else:
            low_firms.append(add_firm)
        return func(companies, average, top_firms, low_firms)


higher_company, lower_company = func(firms_list, average_profit)

print(f'Средняя годовая прибыль всех предприятий: {average_profit}')
print(f'Предприятия, с прибылью выше среднего значения: {", ".join(higher_company)}')
print(f'Предприятия, с прибылью ниже среднего значения: {", ".join(lower_company)}')
