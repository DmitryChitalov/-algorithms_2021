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

from collections import defaultdict as defdict


def calc_profit():
    company = defdict(int)
    try:
        for i in range(int(input('Введите количество предприятий для расчета прибыли: '))):
            one_name = input('Введите название предприятия: ')
            company[one_name] = sum(map(int, input().split()))
        av_profit = sum(company.values()) / len(company)
    except ValueError:
        return 'Вместо числа вы ввели что-то другое.'
    except ZeroDivisionError:
        return 'Количество предприятий не может быть равно 0.'
    else:
        print(f'Средняя годовая прибыль всех предприятий:  {av_profit}')
        above = [i for i in company if company[i] >= av_profit]
        below = [i for i in company if company[i] < av_profit]
        return f'Предприятия, с прибылью выше среднего значения: {", ".join(above)}.\n' \
               f'Предприятия, с прибылью ниже среднего значения: {", ".join(below)}.'


print(calc_profit())
