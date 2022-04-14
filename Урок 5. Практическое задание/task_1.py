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

def comp(name, qrtr_1, qrtr_2, qrtr_3, qrtr_4):
    companies = namedtuple('Companies', 'comp_name q_1 q_2 q_3 q_4 avg_income')
    comp_data = companies(comp_name = name, q_1 = int(qrtr_1), q_2 = int(qrtr_2),
                        q_3 = int(qrtr_3), q_4 = int(qrtr_4),
                        avg_income = (int(qrtr_1) + int(qrtr_2) + int(qrtr_3) + int(qrtr_4)) / 4)
    return comp_data


def calculations():
    comp_list = []
    avg_income_lst = []
    qty = int(input('Введите количество предприятий для расчета прибыли: '))
    for company in range(qty):
        comp_name = input('Введите название предприятия: ')
        income = (input('через пробел введите прибыль данного предприятия'
                        'за каждый квартал(Всего 4 квартала): ')).split(' ')
        company = comp(comp_name, *income)
        comp_list.append(company)
        avg_income_lst.append(company.avg_income)
    print(f'Средняя годовая прибыль всех предприятий: {sum(avg_income_lst) / qty}')
    print(
        f'Предприятия, с прибылью выше среднего значения: '
        f'{",".join([i.comp_name for i in comp_list if i.avg_income > sum(avg_income_lst) / qty])}')
    print(
        f'Предприятия, с прибылью ниже среднего значения: '
        f'{",".join([i.comp_name for i in comp_list if i.avg_income < sum(avg_income_lst) / qty])}')


calculations()