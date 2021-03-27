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

number_of_enterprises = int(input('Введите количество предприятий для расчета прибыли: '))

FIRMS = namedtuple('Firm', 'name first_quarter second_quarter third_quarter fourth_quarter year_profit')

objects_list = []
for i in range(number_of_enterprises):
    name = input('Введите название предприятия: ')
    profits = [int(i) for i in input('Через пробел введите прибыль данного предприятия\n'
                                     'за каждый квартал(Всего 4 квартала): ').split()]
    objects_list.append(FIRMS(
        name=name,
        first_quarter=profits[0],
        second_quarter=profits[1],
        third_quarter=profits[2],
        fourth_quarter=profits[3],
        year_profit=sum(profits)
    ))

sum_all_profits = 0
for i in range(number_of_enterprises):
    sum_all_profits += objects_list[i].year_profit
average_profit = sum_all_profits / number_of_enterprises

print(f'\nСредняя годовая прибыль всех предприятий: {average_profit}')

above_average = []
below_average = []
for i in range(number_of_enterprises):
    if objects_list[i].year_profit > average_profit:
        above_average.append(objects_list[i].name)
    else:
        below_average.append(objects_list[i].name)

print('Предприятия, с прибылью выше среднего значения: ', *above_average)
print('Предприятия, с прибылью ниже среднего значения: ', *below_average)
