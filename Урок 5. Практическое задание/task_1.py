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

devs = []
numb_of_devs = int(input('Enter the number of developments: '))
for i in range(numb_of_devs):
    dev = namedtuple('report', 'name income1 income2 income3 income4 full_income')
    name_of_dev = input('Enter the name of development: ')
    income_of_dev = input('Enter the profit of this development for each quarter, separated by a space (Total 4 quarters): ')
    devel = dev(name_of_dev, *income_of_dev.split(), sum(map(int, income_of_dev.split())))
    devs.append(devel)

income_middle = sum(Company.full_income for Company in devs) / len(devs)
print(f"Average annual profit of all enterprises: {income_middle}")
print("Developments with above average profit: ")
print(*(Company.name for Company in devs if Company.full_income >= income_middle))
print("Developments with below average profit: ")
print(*(Company.name for Company in devs if Company.full_income < income_middle))