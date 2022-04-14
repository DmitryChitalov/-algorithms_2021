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

import collections

companies = {}
profitable_companies = collections.deque()
unprofitable_companies = collections.deque()
total_profit = 0
number_of_quarters = 4

number_of_companies = int(input('Введите количество предприятий для '
                                        'расчёта среднегодовой прибыли: '))

for i in range(number_of_companies):
    name_of_company = input(f'Введите название {i+1}-го предприятия: ')
    quarter = 1
    profit = 0
    while quarter <= number_of_quarters:
        try:
            profit += float(input(f'Введите прибыль предприятия за {quarter}-й квартал: '))
        except ValueError:
            print('Вы ввели недопустимое значение.')
            continue
        quarter += 1
        companies[name_of_company] = profit
        total_profit += profit

average_profit_per_year = total_profit / number_of_companies
for i, item in companies.items():
    if item >= average_profit_per_year:
        profitable_companies.append(i)
    else:
        unprofitable_companies.append(i)
print(f'Среднегодовая прибыль для всех предприятий: {average_profit_per_year}.')
print(f'Количество предприятий с прибылью выше среднегодововой: '
      f'{len(profitable_companies)}.')
for name_of_company in profitable_companies:
    print(name_of_company)
print(f'Количество предприятий с прибылью ниже среднегодовой: '
      f'{len(unprofitable_companies)}.')
for name in unprofitable_companies:
    print(name_of_company)

