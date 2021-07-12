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

from collections import defaultdict


def check(v):
    temp = (v.split(" "))
    for i in temp:
        if not i.isdigit() or len(temp) != 4:
            print("Ошибка ввода данных. Введены не 4 числа.")
            exit()
        else:
            continue
    return [int(item) for item in temp]


comp_year = defaultdict(int)

number = (input('Введите число компаний: '))
while not number.isdigit():
    number = (input('Введите число компаний: '))

for i in range(int(number)):
    name_company = input('Введите имя Компании: ')
    profit_company = input('Введите через пробел прибыль данной организации за каждый квартал: ')
    s = check(profit_company)
    comp_year[name_company] = sum(s) / len(s)

average_profit_all = sum(comp_year.values()) / int(number)
print(f'Средняя годовая прибыль всех организаций: ', average_profit_all)

for items, value in comp_year.items():
    print(f'Средняя прибыль {items} {value} рублей')
    if comp_year[items] > average_profit_all:
        print(f'Организация, чья прибыль выше средней: ', items)
    else:
        print(f'Организация, чья прибыль ниже средней: ', items)