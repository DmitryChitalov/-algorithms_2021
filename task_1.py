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

firms_amount = int(input("Введите количество предприятий: "))
firms = namedtuple("firm", "firm_name qv_1 qv_2 qv_3 qv_4")
counter = 0
firm_profit = {}
while firms_amount > counter:
    firms_tuple = firms(firm_name=input("Введите название предприятия: "), qv_1=int(
                input("Введите прибыль за 1-ый квартал: ")), qv_2=int(
                input("За 2-ой квартал: ")), qv_3=int(
                input("За 3-ий квартал: ")), qv_4=int(
                    input("За 4-ый квартал: ")))
    counter += 1

    firm_profit[firms_tuple.firm_name] = firms_tuple.qv_1 + firms_tuple.qv_2 + firms_tuple.qv_3 + firms_tuple.qv_1

average_profit = 0
for profit in firm_profit.values():
    average_profit += profit
average_profit = average_profit / firms_amount
high_profit = []
low_profit = []
for key, value in firm_profit.items():
        if value > average_profit:
            high_profit.append(key)
        elif value < average_profit:
            low_profit.append(key)

print(f"Средняя прибыль для {firms_amount} компаний - {average_profit}")
print(f"Компании с прибылью выше среднего: {' '.join(high_profit)}")
print(f"Компании с прибылью ниже среднего: {' '.join(low_profit)}")
