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


def input_company(i):
    sample_tuple = namedtuple('company_info', 'company first second third fourth')
    res_list = []
    for cnt in range(i):
        company_name = input(f'Введите название предприятия: ')
        company_input = input('Через пробел введите прибыль данного предприятия '
                              'за каждый квартал(Всего 4 квартала): ')
        company_income_list = company_input.split(' ')
        res_list.append(sample_tuple(
            company=company_name,
            first=int(company_income_list[0]),
            second=int(company_income_list[1]),
            third=int(company_income_list[2]),
            fourth=int(company_income_list[3])
        )
        )
    return res_list


i = int(input('Введите колличество предприятий: '))

company_list = input_company(i)
company_income = []
for num in range(i):
    year_income = company_list[num].first + company_list[num].second + \
                  company_list[num].third + company_list[num].fourth
    company_income.append(year_income)


avg_income = sum(company_income) / i
more_avg = []
less_avg = []

for el in range(i):
    if company_income[el] > avg_income:
        more_avg.append(company_list[el].company)
    elif company_income[el] < avg_income:
        less_avg.append(company_list[el].company)

more_avg = ', '.join(more_avg)
less_avg = ', '.join(less_avg)

print()
print('Средняя годовая прибыль всех предприятий:', avg_income)
print()
print('Предприятия, с прибылью выше среднего значения:', more_avg)
print()
print('Предприятия, с прибылью ниже среднего значения:', less_avg)

# Результат работы программы:
#
# Введите колличество предприятий: 4
# Введите название предприятия: Фирма_1
# Через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): 456 789 123 654
# Введите название предприятия: Фирма_2
# Через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): 789456 123456 8888 456
# Введите название предприятия: Фирма_3
# Через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): 777 94621 8563 45
# Введите название предприятия: Фирма_4
# Через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): 84965 123598 524215 487
#
# Средняя годовая прибыль всех предприятий: 440387.25
#
# Предприятия, с прибылью выше среднего значения: Фирма_2, Фирма_4
#
# Предприятия, с прибылью ниже среднего значения: Фирма_1, Фирма_3


