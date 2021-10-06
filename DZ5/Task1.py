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

testdata = [
    ['Фирма_1', '1 2 3 4'],
    ['Фирма_2', '5 6 7 8'],
    ['Фирма_3', '9 10 11 12']
]


def preds(test, n):
    result = []
    factory = namedtuple('Enterprise', ['name', 'income', 'summary'])
    for i in range(n):
        # name = input('Введите название предприятия: ')
        name = test[i][0]
        income_str = test[i][1]
        income = [int(quater) for quater in income_str.split(' ')]
        # income_str = input('Через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): ')
        result.append(factory(
            name,
            income,
            sum(income)
        ))
    return result


def average(data, n):
    return sum(factory.summary for factory in data) / n


# n = input('Введите количество предприятий для расчета прибыли: ')
n = 3
data = preds(testdata, n)
av = average(data, n)
list1 = [factory.name for factory in data if factory.summary > av]
list2 = [factory.name for factory in data if factory.summary < av]
print('Средняя годовая прибыль всех предприятий: ', av)
print('Предприятия, с прибылью выше среднего значения: ', list1)
print('Предприятия, с прибылью ниже среднего значения: ', list2)