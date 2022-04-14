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
за каждый квартал(Всего 4 квартала): 4345 34 543 3
Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Фирма_1
Предприятия, с прибылью ниже среднего значения: Фирма_2
"""
from collections import namedtuple

num_company = int(input('Введите количество предприятий для расчета прибыли: '))
counter = num_company  # счётчик для цикла, num_company понадобится ниже, поэтому как счётчик не использую
companies = namedtuple('Companies', 'name_company prof_1 prof_2 prof_3 prof_4 prof_sum')  # кортеж данных по компании
companies_list = []  # список для хранения наименования компании и её годовой прибыли
total_profit = 0  # переменная для подсчёта прибыли по всем компаниям
while counter != 0:  # собираем данные обо всех компаниях
    name_company = input('Введите название предприятия: ')
    profit = list(map(int, input(
        'Через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): ').split()))
    company_n = companies(
        name_company=name_company,
        prof_1=profit[0],
        prof_2=profit[1],
        prof_3=profit[2],
        prof_4=profit[3],
        prof_sum=(sum(profit))
    )
    counter -= 1
    total_profit += company_n.prof_sum
    companies_list.append((company_n.name_company, company_n.prof_sum))

average_profit = total_profit / num_company
companies_low_profit = []  # список компаний с годовой прибылью меньше среднего
companies_high_profit = [] # список компаний с годовой прибылью выше среднего
print(f'Средняя годовая прибыль всех предприятий: {average_profit}')
for company in companies_list:
    if company[1] < average_profit:
        companies_low_profit.append(company[0])
    elif company[1] > average_profit:
        companies_high_profit.append(company[0])
print('Предприятия, с прибылью выше среднего значения:', ', '.join(companies_high_profit))
print(f'Предприятия, с прибылью ниже среднего значения:', ', '.join(companies_low_profit))
