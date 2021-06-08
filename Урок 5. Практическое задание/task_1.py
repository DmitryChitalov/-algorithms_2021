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
above_average = []
below_average = []
enter_num = int(input('Enter the number of companies to calculate the profit\n'
                      'Введите количество предприятий для расчета прибыли: \n'))
for i in range(enter_num):
    company_name = input('Enter the name of the company.\n'
                         'Введите название предприятия: \n')
    income_per_q = input('Enter the profit of this company through a gap for 4 quarters.\n'
                         'Введите прибыль данного предприятия через пробел за 4 квартала: \n')

    income_per_q = income_per_q.split(' ')
    RESUME_PARTS = RES(
        name=company_name,
        first_q=int(income_per_q[0]),
        second_q=int(income_per_q[1]),
        third_q=int(income_per_q[2]),
        fourth_q=int(income_per_q[3])
    )

    aver_income = (RESUME_PARTS.first_q + RESUME_PARTS.second_q + RESUME_PARTS.third_q + RESUME_PARTS.fourth_q) / 4
    companies[company_name] = aver_income

total_average = sum(companies.values()) / enter_num
for k, v in companies.items():
    if v > total_average:
        above_average.append(k)
    elif v < total_average:
        below_average.append(k)

print(f'Average annual profit of all companies.\n'
      f'Средняя годовая прибыль всех предприятий:\n {total_average}')
print(f'Companies with above average profit.\n'
      f'Предприятия, с прибылью выше среднего значения:\n {above_average}')
print(f'Companies with below average profit.\n'
      f'Предприятия, с прибылью ниже среднего значения:\n {below_average}')
'''
C:\Users\79115\AppData\Local\Programs\Python\Python39\python.exe "C:/Users/79115/Desktop/2 Урок Алгоритмы/Урок 2. Коды примеров/Algorithm5.1.py"
<class '__main__.Company'>
Enter the number of companies to calculate the profit
Введите количество предприятий для расчета прибыли: 
4
Enter the name of the company.
Введите название предприятия: 
a
Enter the profit of this company through a gap for 4 quarters.
Введите прибыль данного предприятия через пробел за 4 квартала: 
1 2 3 4
Enter the name of the company.
Введите название предприятия: 
b
Enter the profit of this company through a gap for 4 quarters.
Введите прибыль данного предприятия через пробел за 4 квартала: 
2 3 4 5
Enter the name of the company.
Введите название предприятия: 
c
Enter the profit of this company through a gap for 4 quarters.
Введите прибыль данного предприятия через пробел за 4 квартала: 
3 4 5 2
Enter the name of the company.
Введите название предприятия: 
d
Enter the profit of this company through a gap for 4 quarters.
Введите прибыль данного предприятия через пробел за 4 квартала: 
4 5 6 7
Average annual profit of all companies.
Средняя годовая прибыль всех предприятий:
 3.75
Companies with above average profit.
Предприятия, с прибылью выше среднего значения:
 ['d']
Companies with below average profit.
Предприятия, с прибылью ниже среднего значения:
 ['a', 'b', 'c']

Process finished with exit code 0


'''
