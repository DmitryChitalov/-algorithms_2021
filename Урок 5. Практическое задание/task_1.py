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

number_of_companies = input('Введите количество предприятий для расчета прибыли: ')


def must_be_float(line):
    if len(line.split()) == 4:
        try:
            for i in line.split():
                float(i)
            return line
        except ValueError:
            return must_be_float(input('Квартальная прибыль должна быть числом. Повторите ввод: '))
    else:
        return must_be_float(input('Не верное количество аргументов. Введите ровно 4 числа. Повторите ввод: '))


while not number_of_companies.isdigit() or not int(number_of_companies):
    number_of_companies = input('Введены некорректные данные. Количество предприятий должно быть натуральным числом.\
    \nВведите количество предприятий для расчета прибыли: ')

template = namedtuple('company_profits', 'company_name first_quarter second_quarter third_quarter fourth_quarter')

about_companies = []
for i in range(int(number_of_companies)):
    name = input('Введите название предприятия: ')
    profit = must_be_float(input('Через пробел введите прибыль данного предприятия за каждый квартал \
(Всего 4 квартала): ')).split()
    our_tuple = template(
        company_name=name,
        first_quarter=profit[0],
        second_quarter=profit[1],
        third_quarter=profit[2],
        fourth_quarter=profit[3]
    )
    about_companies.append(our_tuple)


def annual_profit(nt):
    return float(nt.first_quarter) + float(nt.second_quarter) + float(nt.third_quarter) + float(nt.fourth_quarter)


average_profit = sum([annual_profit(i) for i in about_companies]) / len(about_companies)

print('Средняя годовая прибыль всех предприятий: ', average_profit)

print('Предприятия, с прибылью выше среднего значения: ' + ' '.join(
    i.company_name for i in about_companies if annual_profit(i) > average_profit))

print('Предприятия, с прибылью ниже среднего значения: ' + ' '.join(
    i.company_name for i in about_companies if annual_profit(i) < average_profit))


