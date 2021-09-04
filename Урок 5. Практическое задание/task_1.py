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


def avg_profit(lst):
    """Возвращает средний годовой доход списка фирм"""
    sum_profit = 0
    for el in lst:
        sum_profit += sum(el[1:])
    return sum_profit / len(lst)


COMPANY = namedtuple('Company', 'name profit_q_1 profit_q_2 profit_q_3 profit_q_4')
companies = []

try:
    cnt = int(input('Введите количество предприятий для расчета прибыли: '))
except ValueError:
    print('Вводить следует число.')
else:
    for idx in range(cnt):
        comp_name = input('Введите название предприятия: ')
        print('Через пробел введите прибыль данного предприятия за каждый квартал (Всего 4 квартала): ', end='')
        try:
            profit_q_1, profit_q_2, profit_q_3, profit_q_4 = map(int, input().split())
        except ValueError:
            print('Следует ввести 4 числа через пробел')
        else:
            companies.append(
                COMPANY(name=comp_name, profit_q_1=profit_q_1, profit_q_2=profit_q_2, profit_q_3=profit_q_3,
                        profit_q_4=profit_q_4))

avg_profit_per_year = avg_profit(companies)
print(f'Средняя годовая прибыль всех предприятий: {avg_profit_per_year:.2f}')

print(
    'Предприятия, с прибылью выше среднего значения: {}'.format(
        ', '.join([el.name for el in companies if sum(el[1:]) >= avg_profit_per_year])))

print(
    'Предприятия, с прибылью ниже среднего значения: {}'.format(
        ', '.join([el.name for el in companies if sum(el[1:]) < avg_profit_per_year])))
