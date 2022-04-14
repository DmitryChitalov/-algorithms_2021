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

count_of_comp = int(input("Введите количество предприятий: "))
company = namedtuple("company", "company_name pf_1 pf_2 pf_3 pf_4")
count = count_of_comp
company_profit = {}
max_profit = []
min_profit = []
avg_profit = 0

while count_of_comp != 0:
    name_comp = input("Введите название предприятия: ")
    profits = input("через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): ")
    profits = profits.split(' ')
    profits = list(map(int, profits))
    company_tuple = company(company_name=name_comp, pf_1=profits[0], pf_2=profits[1], pf_3=profits[2], pf_4=profits[3])
    count_of_comp -= 1
    company_profit[company_tuple.company_name] = company_tuple.pf_1 + company_tuple.pf_2 + company_tuple.pf_3 + company_tuple.pf_1

for profit in company_profit.values():
    avg_profit += profit
avg_profit = avg_profit / count

for key, value in company_profit.items():
    if value > avg_profit:
        max_profit.append(key)
    elif value < avg_profit:
        min_profit.append(key)

print(f"Средняя прибыль для {count} компаний - {avg_profit}")
print(f"Компании с прибылью выше среднего: {' '.join(max_profit)}")
print(f"Компании с прибылью ниже среднего: {' '.join(min_profit)}")
