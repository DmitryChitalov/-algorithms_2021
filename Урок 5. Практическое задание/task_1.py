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

import collections
import random


def sum_tuple(numbers):

    total_sum = 0
    for sum_q in numbers:
        total_sum += sum_q
        return total_sum


Company = collections.namedtuple('Company', ['q1', 'q2', 'q3', 'q4'])

base_Company = {}

n = int(input("Количество предприятий: "))

for i in range(n):
    name = input(str(i+1) + '-е предприятие: ')
    profit_q1 = int(input('Прибыль за 1-й квартал: '))
    profit_q2 = int(input('Прибыль за 2-й квартал: '))
    profit_q3 = int(input('Прибыль за 3-й квартал: '))
    profit_q4 = int(input('Прибыль за 4-й квартал: '))
    base_Company[name] = Company(
        q1=profit_q1,
        q2=profit_q2,
        q3=profit_q3,
        q4=profit_q4
    )

base_Company['Name1'] = Company(
    q1=random.randint(100, 500),
    q2=random.randint(100, 500),
    q3=random.randint(100, 500),
    q4=random.randint(100, 500)
)

base_Company['Name2'] = Company(
    q1=random.randint(100, 500),
    q2=random.randint(100, 500),
    q3=random.randint(100, 500),
    q4=random.randint(100, 500)
)

total_profit = ()

for name, profit in base_Company.items():
    print(f'Предприятие: {name} прибыль за год - {sum(profit)}')
    total_profit += profit

avg_profit_total = sum(total_profit) / len(base_Company)
print(f'Средняя прибыль за год для всех предприятий {avg_profit_total}')

print('Предприятия, у которых прибыль выше среднего:')

for name, profit in base_Company.items():
    if sum(profit) > avg_profit_total:
        print(f'{name} - {sum(profit)}')

for name, profit in base_Company.items():
    if sum(profit) < avg_profit_total:
        print(f'{name} - {sum(profit)}')
