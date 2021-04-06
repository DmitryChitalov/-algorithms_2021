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
from functools import reduce

test_dict = {
    "apple":[100.7,110.2,120.9,101.1],
    "samsung":[90.35,110.3,95.15,130.2],
    "huawey":[98.7,80.95,99.35,100.5],
    "midea":[90.1,100.3,90.6,130.55],
}

# name: название фирмы
# q1-q4:поквартальные доходы
# avg: средняя прибыль за год
firms = namedtuple("firm","name q1 q2 q3 q4 avg") 

def get_firm()->list:
    '''
    Ввод данных фирм
    '''
    firm_list = list()
    for k,v in test_dict.items():
        avg = sum(v)/len(v)
        firm_list.append(firms(name=k,q1=v[0],q2=v[1],q3=v[2],q4=v[3],avg=avg))    
    return firm_list

def all_avg(all_firms:list)->int:
    '''
    Расчет среднегодового дохода всех фирм
    '''
    avg = 0
    for f in all_firms:
        avg += f.avg    
    return avg/len(all_firms) 



firm_list = get_firm()
avg = all_avg(firm_list)
up_firm = [[f.name,f.avg] for f in firm_list if f.avg > avg ]
dwn_firm = [[f.name,f.avg] for f in firm_list if f.avg <= avg ]

print(f"Средняя годовая прибыль всех предприятий: {avg:0.3f}")
print(f"Предприятия, с прибылью выше среднего значения: {up_firm}")
print(f"Предприятия, с прибылью ниже среднего значения: {dwn_firm}")
