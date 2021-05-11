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


def get_user_data():
    number_of_firms = int(input('Введите количество предприятий для расчета прибыли: '))
    Salaries = namedtuple('Salaries', ['quarter1', 'quarter2', 'quarter3', 'quarter4'])
    firms_and_salaries = {}

    for number in range(1, number_of_firms + 1):
        firm_name = input(f'Введите название предприятия №{number}: ')
        values_salary = input(f'Через пробел введите прибыль предприятия "{firm_name}" за каждый квартал (всего 4): ')
        firms_and_salaries[firm_name] = Salaries._make([int(value) for value in values_salary.split(' ')])

    return firms_and_salaries


def get_average_salaries(data: dict):
    return {key: sum(value)/len(value) for key, value in data.items()}


def get_general_average_salary(data: dict):
    content = data.values()
    return sum(content)/len(content)


def describe_firms():
    data = get_average_salaries(get_user_data())
    average_salary = round(get_general_average_salary(data), 2)

    print(f'\nСредняя годовая прибыль всех предприятий: {average_salary}')

    below_average = [key for key, value in data.items() if value < average_salary]
    above_average = [key for key, value in data.items() if value > average_salary]
    is_average = [key for key, value in data.items() if value == average_salary]

    print(f"Предприятия, с прибылью ниже среднего значения: {', '.join(below_average)}")
    print(f"Предприятия, с прибылью выше среднего значения: {', '.join(above_average)}")
    if is_average:
        print(f"Предприятия, с прибылью равному среднему значению: {', '.join(is_average)}")


describe_firms()
# Для этого спектра задач namedtuple ничем не помогает,
# однако если бы стояла задача посчитать поквартально, то этот инструмент был бы полезен
