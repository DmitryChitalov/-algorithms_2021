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

def func_max(comp_dict, aver_forsyst):
    comp_lst = []
    for i in range(len(comp_dict)):
        amt_ofquats = int(comp_dict[i+1].profit_q1) + int(comp_dict[i+1].profit_q2) +\
                      int(comp_dict[i+1].profit_q3) + int(comp_dict[i+1].profit_q4)
        if amt_ofquats > aver_forsyst:
            comp_lst.append(comp_dict[i+1].company)
    return comp_lst

def func_min(comp_dict, aver_forsyst):
    comp_lst = []
    for i in range(len(comp_dict)):
        amt_ofquats = int(comp_dict[i+1].profit_q1) + int(comp_dict[i+1].profit_q2) +\
                      int(comp_dict[i+1].profit_q3) + int(comp_dict[i+1].profit_q4)
        if amt_ofquats < aver_forsyst:
            comp_lst.append(comp_dict[i+1].company)
    return comp_lst

def firm_func():
    n = int(input("Введите количество компаний: "))
    i = 1
    comp_dict = {}
    comp_avprofit = 0
    while i != n + 1:
        company_tmplate = namedtuple(f"Company_{i}", "company profit_q1 profit_q2 profit_q3 profit_q4")
        user_cmpname = input(f"Введите название предприятия №{i}: ")
        user_cmpprofit = input(f"Через пробел введите прибыль предприятия №{i} "
                               f"за каждый квартал (всего 4 квартала): ").split()
        company_tpl = company_tmplate(
            company=user_cmpname,
            profit_q1=user_cmpprofit[0],
            profit_q2=user_cmpprofit[1],
            profit_q3=user_cmpprofit[2],
            profit_q4=user_cmpprofit[3]
        )
        comp_dict[i] = company_tpl
        i += 1
        comp_avprofit += int(company_tpl.profit_q1) + int(company_tpl.profit_q2) \
                         + int(company_tpl.profit_q3) + int(company_tpl.profit_q4)
    aver_forsyst = comp_avprofit / (i-1)
    print(f'Средняя годовая прибыль всех предприятий: {aver_forsyst}')
    print(f"Предприятия, с прибылью выше среднего значения: {', '.join(func_max(comp_dict, aver_forsyst))}")
    print(f"Предприятия, с прибылью ниже среднего значения: {', '.join(func_min(comp_dict, aver_forsyst))}")

firm_func()
