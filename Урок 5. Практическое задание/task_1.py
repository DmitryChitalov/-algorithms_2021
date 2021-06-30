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

n = int(input('Введите колличество предприятий:'))
nam_tup = namedtuple('Firms', 'name qr1 qr2 qr3 qr4')
firms = []

for i in range(n):
    fir = nam_tup(input('Введите название фирмы:'),
                  int(input('Введите прибыль за 1 квартал:')),
                  int(input('Введите прибыль за 2 квартал:')),
                  int(input('Введите прибыль за 3 квартал:')),
                  int(input('Введите прибыль за 4 квартал:')))
    firms.append(fir)


def avg_profit(firms):
    sum = 0
    for i in range(len(firms)):
        sum += firms[i].qr1 + firms[i].qr2 + firms[i].qr3 + firms[i].qr4
    return sum / n


def above_below_avg_profit(firms, avg_prof):
    above = []
    below = []
    for i in range(len(firms)):
        sum = firms[i].qr1 + firms[i].qr2 + firms[i].qr3 + firms[i].qr4
        if sum > avg_prof:
            above.append(firms[i].name)
        else:
            below.append(firms[i].name)

    return above, below


print(firms[0].qr1 + firms[0].qr2 + firms[0].qr3 + firms[0].qr4)
avarage_profit = avg_profit(firms)
above_average, below_average = above_below_avg_profit(firms, avarage_profit)
print(f'Средняя годовая прибыль: {avarage_profit}')
print(f'Предприятия, с прибылью выше среднего значения: {above_average}')
print(f'Предприятия, с прибылью ниже среднего значения: {below_average}')
