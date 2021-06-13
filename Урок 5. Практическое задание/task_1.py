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

financials = []
higher_revenue = []
lower_revenue = []

revenue = namedtuple("Companies", " name quarter1 quarter2 quarter3 quarter4")
average_revenue = {}

n = int(input("Введите количество предприятий для расчета прибыли: "))
for i in range(n):
    company = input("Введите название предприятия: ")
    financials = input(
        "Через пробел введите прибыль данного предприятия за каждый квартал (всего 4 квартала): ").split()
    revenue_dataset = revenue(name=company, quarter1=int(financials[0]), quarter2=int(financials[1]),
                              quarter3=int(financials[2]), quarter4=int(financials[3]))
    average_revenue[revenue_dataset.name] = (
            revenue_dataset.quarter1 + revenue_dataset.quarter2 + revenue_dataset.quarter3 + revenue_dataset.quarter4)

total_average = sum(average_revenue.values()) / n

print("Средняя годовая прибыль всех предприятий: ", total_average)

for company, value in average_revenue.items():
    if value >= total_average:
        higher_revenue.append(company)
    else:
        lower_revenue.append(company)

print("Предприятия, с прибылью выше среднего значения: ", higher_revenue)
print("Предприятия, с прибылью ниже среднего значения: ", lower_revenue)

