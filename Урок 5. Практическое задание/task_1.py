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
my_var = "Company"
n = int(input('введите количество компаний: '))
companies = namedtuple(my_var, "name quarter1 quarter2 quarter3 quarter4")
profit_aver = {}

for i in range(n):
    my_var = input("name")
    company = companies(my_var, quarter1=int(input("quarter1 ")),
                        quarter2=int(input("quarter2 ")),
                        quarter3=int(input("quarter3 ")),
                        quarter4=int(input("quarter4 ")))
    print(company)
    profit_aver[company.name] = (company.quarter1 + company.quarter2 + company.quarter3 + company.quarter4) / 4
    print(profit_aver)

print(company)
total_aver = 0
for value in profit_aver.values():
    total_aver += value
total_aver = total_aver / n

for key, value in profit_aver.items():
    if value > total_aver:
        print(key, "прибыль выше среднего")
    elif value < total_aver:
        print(key, "прибыль ниже среднего")
    elif value == total_aver:
        print(key, "прибыль средняя")
