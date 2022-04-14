  
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
dic_profit_comp_year = defaultdict(int)

number_company = int(input('Введите число предприятий для рассчета: '))
for i in range(number_company):
    name_company = input('Введите имя фирмы: ')
    profit_comp_year = input('Введите через пробел прибыль данного предприятияза каждый квартал: ')
    lst_profit_comp_year = [int(el) for el in profit_comp_year.split(' ')] # Без int в int(el) получим список строк, а не список чисел
    dic_profit_comp_year[name_company] = sum(lst_profit_comp_year) / len(lst_profit_comp_year)
    #print(dic_profit_comp_year)
for items in dic_profit_comp_year.items():
    print(f'Перечень фирм - Фирма: ср. прибыль', items)
average_profit_all = sum(dic_profit_comp_year.values()) / number_company # Средняя годовая прибыль всех предприятий
print(f'Средняя годовая прибыль всех предприятий: ', average_profit_all)


# Вывести наименования предприятий, чья прибыль выше среднего
for key in dic_profit_comp_year.keys():
    #print(f'Названия всех фирм: ', key)
    if dic_profit_comp_year[key] > average_profit_all:
        print(f'Предприятие, чья прибыль выше среднего: ', key)

# Вывести наименования предприятий, чья прибыль ниже среднего
for key in dic_profit_comp_year.keys():
    #print(key)
    if dic_profit_comp_year[key] < average_profit_all:
        print(f'Предприятие, чья прибыль ниже среднего: ', key)














