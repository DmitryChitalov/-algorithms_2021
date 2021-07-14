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

from collections import defaultdict


def reporter():
    report = defaultdict(int)
    for i in range(int(input('Введите количество предприятий для расчета прибыли: '))):
        name = input(f'Введите названия предприятия №{i+1}: ')
        k_profit = [int(num) for num in input(f'через пробел введите прибыль данного предприятия\n'
                                              f'за каждый квартал(Всего 4 квартала): ').split(' ')]

        report[name] = sum(k_profit)
        report['all_profit'] += report[name]
        report['all_count'] += 1

    print(f'Средняя годовая прибыль всех предприятий: {report["all_profit"]/report["all_count"]}')
    upper = []
    lower = []
    for key, item in report.items():
        if key in ('all_profit', 'all_count'):
            continue
        if item > report["all_profit"]/report["all_count"]:
            upper.append(key)
        else:
            lower.append(key)
    print(f'Предприятия, с прибылью выше среднего значения: {", ".join(map(str,upper))}')
    print(f'Предприятия, с прибылью ниже среднего значения: {",  ".join(map(str,lower))}')


reporter()
