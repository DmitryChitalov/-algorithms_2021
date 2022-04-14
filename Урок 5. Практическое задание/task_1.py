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

Companies = namedtuple('Companies', 'name first_quarter second_quarter third_quarter fourth_quarter')
profit_avr = {}
num_of_comp = int(input('Введите количество компаний'))

for i in range(num_of_comp):
    companies = Companies(
        name=input('название'),
        first_quarter=int(input('Введите значение прибыли для 1 квартала ')),
        second_quarter=int(input('Введите значение прибыли для 2 квартала ')),
        third_quarter=int(input('Введите значение прибыли для 3 квартала ')),
        fourth_quarter=int(input('Введите значение прибыли для 4 квартала ')))

    profit_avr[companies.name] = round((companies.first_quarter +
                                        companies.second_quarter +
                                        companies.third_quarter +
                                        companies.fourth_quarter) / 4, 2)

total_profit_avr = round(sum(profit_avr.values()) / num_of_comp)

for key, values in profit_avr.items():
    if values > total_profit_avr:
        print(f'У компании {key} прибыль выше среднего')
    elif values < total_profit_avr:
        print(f'У компании {key} прибыль ниже среднего')
