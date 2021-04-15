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
from collections import defaultdict

# Вариант 1

numb_of_firm = int(input('Введите количество предприятий для расчета прибыли: '))

data_firm = defaultdict(int)
for i in range(numb_of_firm):
    name_firm = input('Введите название предприятия: ')
    income = sum(list(map(int, input('через пробел введите прибыль данного предприятия\n'
                                     'за каждый квартал(Всего 4 квартала): ').split())))
    data_firm[name_firm] = income
    data_firm['aver_prof'] += data_firm[name_firm] / numb_of_firm


def firm_info(data):
    result = defaultdict(str)
    for firm in data:
        if data[firm] < data['aver_prof']:
            result['less'] = firm
        if data[firm] > data['aver_prof']:
            result['more'] = firm
    return f'Средняя годовая прибыль всех предприятий: {data["aver_prof"]}\n' \
           f'Предприятия, с прибылью выше среднего значения: {result["more"]}\n\n' \
           f'Предприятия, с прибылью ниже среднего значения: {result["less"]}'


print(firm_info(data_firm))

# ********************************************************************************

# Вариант 2

all_firms = namedtuple('firms', 'comp_name revenue')
all_firms_list = []
numb_of_firm = int(input('Введите количество предприятий для расчета прибыли: '))

for i in range(numb_of_firm):
    name_firm = input('Введите название предприятия: ')
    income = input('через пробел введите прибыль данного предприятия\n'
                   'за каждый квартал(Всего 4 квартала): ')
    all_firms_list.append(all_firms(name_firm, sum(list(map(int, income.split())))))

middle_profit = sum(int(c.revenue) for c in all_firms_list) / numb_of_firm
print(f'{"*" * 40}')
print(f'Средняя годовая прибыль всех предприятий: {middle_profit}')
for i in all_firms_list:
    if i.revenue >= middle_profit:
        print(f'Предприятия, с прибылью выше среднего значения: {i.comp_name}\n')
    else:
        print(f'Предприятия, с прибылью ниже среднего значения: {i.comp_name}')
