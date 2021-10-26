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

from collections import namedtuple, defaultdict


def adv_prof():
    number = int(input("Введите количество предприятий для расчета прибыли: "))
    companies_profit = defaultdict(tuple)
    all_profits = []
    for num in range(number):
        name = input("Введите название предприятия: ")
        profits = input("Через пробел введите прибыль данного предприятия за каждый квартал (всего 4 квартала): ")
        lst_profits = profits.split(' ')
        nt = namedtuple('company_4profits', 'q1 q2 q3 q4 avg')
        avg_year = (sum(map(int, lst_profits)))/4
        companies_profit[name] = nt(q1=int(lst_profits[0]), q2=int(lst_profits[1]),
                                    q3=int(lst_profits[2]), q4=int(lst_profits[3]),
                                    avg=avg_year)
        all_profits.extend([companies_profit[name].q1, companies_profit[name].q2,
                            companies_profit[name].q3, companies_profit[name].q4])
    all_avg = round(sum(all_profits)/len(all_profits), 2)
    print(f'Средняя годовая прибыль всех предприятий: {all_avg}')
    big_profit = []
    small_profit = []
    for company in companies_profit:
        if companies_profit[company].avg >= all_avg:
            big_profit.extend([company, round(companies_profit[company].avg, 2)])
        else:
            small_profit.extend([company, round(companies_profit[company].avg, 2)])
    print(f'Предприятия, с прибылью не ниже среднего значения: {big_profit}')
    print(f'Предприятия, с прибылью ниже среднего значения: {small_profit}')


adv_prof()

# Введите количество предприятий для расчета прибыли: 3
# Введите название предприятия: VAZ
# Через пробел введите прибыль данного предприятия за каждый квартал (всего 4 квартала): 2000 3000 4000 3000
# Введите название предприятия: GAZ
# Через пробел введите прибыль данного предприятия за каждый квартал (всего 4 квартала): 1000 1500 2000 1800
# Введите название предприятия: Audi
# Через пробел введите прибыль данного предприятия за каждый квартал (всего 4 квартала): 4000 6000 3000 1000
# Средняя годовая прибыль всех предприятий: 2691.67
# Предприятия, с прибылью не ниже среднего значения: ['VAZ', 3000.0, 'Audi', 3500.0]
# Предприятия, с прибылью ниже среднего значения: ['GAZ', 1575.0]
