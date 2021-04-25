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


def get_sum_comp(company):
    return (company.first_quar + company.second_quar + company.third_quar + company.fourth_quar) / 4


def get_max_comp(company_1, company_2, avg_comp):
    str = ""
    sum_1 = get_sum_comp(company_1)
    sum_2 = get_sum_comp(company_2)
    if avg_comp < sum_1:
        str = company_1.name_company
    if avg_comp < sum_2:
        if str == " ":
            str += ", "
        str += company_2.name_company
    return str


def get_min_comp(company_1, company_2, avg_comp):
    str = ""
    sum_1 = get_sum_comp(company_1)
    sum_2 = get_sum_comp(company_2)
    if avg_comp > sum_1:
        str = company_1.name_company
    if avg_comp > sum_2:
        if str == " ":
            str += ", "
        str += company_2.name_company
    return str


Company = namedtuple('Company', 'name_company first_quar second_quar third_quar fourth_quar')

name_comp = input("Введите название предприятия: ")
profit = input("Через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала):").split(" ")
profit = [int(item) for item in profit]
comp_1 = Company(name_comp, profit[0], profit[1], profit[2], profit[3])

name_comp = input("Введите название предприятия: ")
profit = input("Через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала):").split(" ")
profit = [int(item) for item in profit]
comp_2 = Company(name_comp, profit[0], profit[1], profit[2], profit[3])

avg_1 = get_sum_comp(comp_1) / 4
avg_2 = get_sum_comp(comp_2) / 4

print(f"Средняя годовая прибыль всех предприятий: {avg_1 + avg_2}")
print(f"Предприятия, с прибылью выше среднего значения: {get_max_comp(comp_1, comp_2, (avg_1 + avg_2))}")
print(f"Предприятия, с прибылью ниже среднего значения: {get_min_comp(comp_1, comp_2, (avg_1 + avg_2))}")
