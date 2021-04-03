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


def main():
    companies_count = int(input('Введите количество предприятий для расчета прибыли: '))
    companies_data = {}

    def data_collect(companies_count, companies_data):
        if companies_count == 1:
            companies_info = input('Заполните шаблон анкеты: Фирма квартал квартал квартал квартал: ').strip().split(
                ' ')
            companies = namedtuple("Company", "name profit")
            companies.name = companies_info[0]
            companies.profit = (int(companies_info[1]) + int(companies_info[2]) + int(companies_info[3]) + int(
                companies_info[4])) / 4
            companies_data[companies.name] = companies.profit

            return companies_data

        companies_info = input('Заполните шаблон анкеты: Фирма квартал квартал квартал квартал: ').strip().split(' ')
        companies = namedtuple("Company", "name profit")
        companies.name = companies_info[0]
        companies.profit = (int(companies_info[1]) + int(companies_info[2]) + int(companies_info[3]) + int(
            companies_info[4])) / 4
        companies_data[companies.name] = companies.profit

        return data_collect(companies_count - 1, companies_data)

    data_collect(companies_count, companies_data)

    average_profit = sum(companies_data.values()) / len(companies_data.values())
    print(f'Средняя годовая прибыль всех фирм {average_profit}')

    for key, value in companies_data.items():
        if value > average_profit:
            print(key, " - фирма с повышенной прибылью")
        elif value < average_profit:
            print(key, " - фирма с пониженной прибылью")
        else:
            print(key, " - фирма со сбалансированной прибылью")


main()
