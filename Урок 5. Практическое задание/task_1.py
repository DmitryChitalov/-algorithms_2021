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
RES = namedtuple('Company', 'name first_q second_q third_q fourth_q')
print(RES)
companies = {}
above_aver = []
below_aver = []
ent_num = int(input('Введите количество предприятий для расчета прибыли: '))
for i in range(ent_num):
    company_name = input('Введите название предприятия:')
    income_per_q = input('через пробел введите прибыль данного предприятия '
                         'за каждый квартал(Всего 4 квартала):')
    income_per_q = income_per_q.split(' ')
    RESUME_PARTS = RES(
        name=company_name,
        first_q=int(income_per_q[0]),
        second_q=int(income_per_q[1]),
        third_q=int(income_per_q[2]),
        fourth_q=int(income_per_q[3])
    )

    aver_income = (RESUME_PARTS.first_q + RESUME_PARTS.second_q + RESUME_PARTS.third_q + RESUME_PARTS.fourth_q) / 4
    companies[company_name]=aver_income

total_average = sum(companies.values()) / ent_num
for k, v in companies.items():
    if v > total_average:
        above_aver.append(k)
    elif v < total_average:
        below_aver.append(k)

print(f'Средняя годовая прибыль всех предприятий: {total_average}')
print(f'Предприятия, с прибылью выше среднего значения: {above_aver}')
print(f'Предприятия, с прибылью ниже среднего значения: {below_aver}')

