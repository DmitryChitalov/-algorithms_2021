"""
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль
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


def enterprises_info(number, quarter=4):
    enterprises = collections.defaultdict(int)
    total_profit = 0
    more_avg = collections.deque()
    less_avg = collections.deque()
    for el in range(number):
        enterprise_profit = 0
        q = 1
        enterprise_name = input(f'Введите имя предприятия № {el + 1}: ')
        while q <= quarter:
            try:
                enterprise_profit += float(input(f'Введите прибыль {enterprise_name} ' \
                                          f'за {q} квартал: '))
            except ValueError:
                print('Вы ввели не число! Исправьтесь.')
            q += 1
        enterprises[enterprise_name] = enterprise_profit
        total_profit += enterprise_profit

    avg_annual_profit = total_profit / number
    for key, val in enterprises.items():
        if val >= avg_annual_profit:
            more_avg.append(key)
        else:
            less_avg.append(key)

    return avg_annual_profit, more_avg, less_avg


if __name__ == '__main__':
    number_of_enterprises = input('Введите количество предприятий: ')
    try:
        number_of_enterprises = int(number_of_enterprises)
    except ValueError:
        print('Вы ввели не число! Исправьтесь.')
    #info = enterprises_info(number_of_enterprises)
    avg_profit, more_avg_list, less_avg_list = enterprises_info(number_of_enterprises)
    print(f'Средняя годовая прибль всех предприятий: {avg_profit}')
    print(f'Предприятия с прибылью выше среднего: {", ".join(more_avg_list)}')
    print(f'Предприятия с прибылью ниже среднего: {", ".join(less_avg_list)}')

