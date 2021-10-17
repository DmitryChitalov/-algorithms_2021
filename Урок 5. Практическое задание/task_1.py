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


def company_income(num_comp):

    n_t = namedtuple('Income',
                     'name fst_quarter snd_quarter trd_quarter fth_quarter')
    average_profit = {}
    for i in range(1, num_comp + 1):
        name = input(f'Введите название предприятия № {i}: ')
        a, b, c, d = input(
            'Через пробел введите прибыль данного предприятия за каждый '
            'квартал(Всего 4 квартала): ').split()

        income = n_t(
            name=name,
            fst_quarter=int(a),
            snd_quarter=int(b),
            trd_quarter=int(c),
            fth_quarter=int(d))
        average_profit[
            income.name] = (
                                   income.fst_quarter + income.snd_quarter +
                                   income.trd_quarter + income.fth_quarter) / 4
    all_average_profit = 0
    for key, values in average_profit.items():
        all_average_profit += values
    print('Средняя годовая прибыль предприятий: ',
          all_average_profit / num_comp)

    for key, values in average_profit.items():
        if values > all_average_profit:
            print('Предприятия, с прибылью выше среднего значения: ', key)
        else:
            print('Предприятия, с прибылью ниже среднего значения: ', key)


number = int(input('Введите количество предприятий для расчета прибыли: '))
company_income(number)
