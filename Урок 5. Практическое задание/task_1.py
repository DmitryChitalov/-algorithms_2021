"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
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

count = 0
quanity = int(input('Введите кол-во компаний: '))
profit = 0
company_dict = dict()
while quanity > 0:
    company_name = input('Введит название компании: ')
    company_att = input('Введите прибыль данного предприятия за каждый квартал через пробел: ').split(' ')
    COMPANY = namedtuple(f'Company', 'name first_quarter second_quarter third_quarter fourth_quarter '
                                     'average_profit')
    company = COMPANY(
        name=company_name,
        first_quarter=int(company_att[0]),
        second_quarter=int(company_att[1]),
        third_quarter=int(company_att[2]),
        fourth_quarter=int(company_att[3]),
        average_profit=(int(company_att[0]) + int(company_att[1]) + int(company_att[2]) + int(company_att[3])) / 4
    )
    profit += company.average_profit
    company_dict[company.name] = company.average_profit
    count += 1
    quanity -= 1
all_average = profit / count
for key, value in company_dict.items():
    if value < all_average:
        print(f'Компания {key} ниже среднего уровня прибыли')
    elif value > profit / count:
        print(f'Компания {key} выше среднего уровня прибыли')
    else:
        print(f'Компания {key}  равна среднему уровню прибыли')
print(f'Средняя общая прибыль {all_average}')
