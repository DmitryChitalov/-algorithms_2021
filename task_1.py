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


def create_list_of_company():
    num_of_company = int(input('Введите количество предприятий для расчета прибыли: '))
    company = []
    for num in range(num_of_company):
        name_of_company = input('Введите название предприятия: ')
        inf_for_company = collections.namedtuple(f'{name_of_company}',
                                                 'first_quarter second_quarter third_quarter fourth_quarter')
        revenue = list(map(int, input('Через пробел введите прибыль данного '
                                      'предприятия за каждый квартал (IV квартала): ').split(' ')))
        some_company = inf_for_company(
            first_quarter=revenue[0],
            second_quarter=revenue[1],
            fourth_quarter=revenue[3],
            third_quarter=revenue[2]
        )
        company.append(some_company)
    return company


def inf_of_revenue(list_of_company):
    average_for_company = {type(company).__name__:sum(company) / 4 for company in list_of_company}
    all_average = sum(average_for_company.values()) / len(list_of_company)
    more_than_average, less_than_average = [], []
    for name, average in average_for_company.items():
        more_than_average.append(name) if average > all_average else less_than_average.append(name)
    print(
        f'Средняя годовая прибыль всех предприятий: {all_average}\n'
        f'Предприятия, с прибылью выше среднего значения: {", ".join(more_than_average)}\n\n'
        f'Предприятия, с прибылью ниже среднего значения: {", ".join(less_than_average)}'
    )


if __name__ == '__main__':
    inf_of_revenue(create_list_of_company())
