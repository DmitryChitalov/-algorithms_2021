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


def firm_make():
    firm = namedtuple('firm', 'name quarter_1 quarter_2 quarter_3 quarter_4 profit_sum')
    name = input('Введите название предприятия: ').rstrip()
    while True:
        try:
            profit = list(map(int, input('через пробел введите прибыль данного '
                                         'предприятия за каждый квартал (Всего 4 квартала): ').split()))
        except ValueError:
            print('вы ввели не цифры!!!')
        else:
            if len(profit) != 4:
                print('Проверьте введённые данные о прибыли. Необходимо ввести 4 значения!')
            else:
                break
    return firm._make([name, *profit, sum(profit)])


def average_profit_count(firm_list: list):
    try:
        avg_profit = sum([getattr(company, 'profit_sum') for company in firm_list]) / len(firm_list)
        print(f'Средняя годовая прибыль всех предприятий: {avg_profit}')
        return avg_profit
    except ZeroDivisionError:
        print('Вы не внесли никаких данных!')
        return None


def firms_statistics(firm_list, profit):
    if profit is None:
        print('К сожалению нечего считать =(')
    else:
        less_then_average = []
        more_then_average = []
        for company in firm_list:
            if company.profit_sum >= profit:
                more_then_average.append(company.name)
            else:
                less_then_average.append(company.name)
        print(f'Предприятия, с прибылью выше среднего значения: {", ".join(more_then_average)}')
        print(f'Предприятия, с прибылью ниже среднего значения: {", ".join(less_then_average)}')


counter = int(input('Введите количество предприятий для расчета прибыли: '))
firms = [firm_make() for i in range(counter)]

average_profit = average_profit_count(firms)
firms_statistics(firms, average_profit)
