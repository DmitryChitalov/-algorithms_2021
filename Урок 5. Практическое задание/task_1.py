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


annual_prof = {}
com_num = int(input('Введите количество предприятий: '))
for i in range(com_num):
    prof = namedtuple('companies', 'company quarter_1 quarter_2 quarter_3 quarter_4')
    company_data = prof(
        company=input('Введите название предприятия: '),
        quarter_1=int(input('Прибыль за первый квартал: ')),
        quarter_2=int(input('Прибыль за второй квартал: ')),
        quarter_3=int(input('Прибыль за третий квартал: ')),
        quarter_4=int(input('Прибыль за четвертый квартал: '))
    )
    annual_prof[company_data.company] =\
        company_data.quarter_1+company_data.quarter_2+company_data.quarter_3+company_data.quarter_4


average_prof = sum(annual_prof.values()) / len(annual_prof)
print(f'Средняя годовая прибыль всех предприятий: {average_prof}')
upper_prof = [key for key,value in annual_prof.items() if value > average_prof]
print(f'Предприятия с прибылью выше среднего: {" ".join(upper_prof)}')
lower_prof = [key for key,value in annual_prof.items() if value < average_prof]
print(f'Предприятия с прибылью ниже среднего: {" ".join(lower_prof)}')
