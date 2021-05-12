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
from collections import deque


def average_profit():
    try:
        n = int(input('Введите количество предприятий для расчета прибыли: '))
        i = 1
        firms = namedtuple('firm', 'name profit')
        base_firms = {}
        summa = 0
        above_average = deque()
        below_average = deque()
        while i <= n:
            firma = input('Введите название предприятия: ')
            profit = input('через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): ')
            # sumprofit = sum(list(map(int, profit.split())))
            sumprofit = sum([int(n) for n in profit.split()])
            base_firm = firms(
                name=firma,
                profit=sumprofit
            )
            base_firms[firma] = base_firm
            i += 1
        for el in base_firms.values():
            summa += el.profit
        average = summa/n
        print(f'Средняя годовая прибыль всех предприятий: {average}')
        for el in base_firms.values():
            if average > el.profit:
                below_average.append(el.name)
            else:
                above_average.append(el.name)
        above_average = ', '.join(above_average)
        below_average = ', '.join(below_average)
        print(f'Предприятия, с прибылью выше среднего значения: {above_average}')
        print(f'Предприятия, с прибылью ниже среднего значения: {below_average}')
    except ValueError:
        print('Формат ввода прибыли 123 123 123 123')
        return average_profit()
    return base_firms


print(average_profit())