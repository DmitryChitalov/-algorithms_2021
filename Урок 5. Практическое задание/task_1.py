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
from statistics import mean
from collections import namedtuple

# Вариант 1. Использование именованного кортежа namedtuple

comp_desc = namedtuple('Company', 'comp_name profit_4q profit_y')  # именованный кортеж с данными по компании
comp_all = []

while True:
    company = namedtuple('Company', 'comp_name profit_4q profit_y')
    company.comp_name = input('Введите наименование предприятия или 0 для завершения ввода: ')
    if company.comp_name == '0':
        break
    while True:
        try:
            company.profit_4q = list(map(float, input('Прибыль по кварталам через пробел: ').split()))
            company.profit_y = sum(company.profit_4q)
            break
        except ValueError:
            print('Необходимо ввести значения! Повторите ввод!')
    # Сохраняем данные в нашу БД (список)
    comp_all.append(company)
    print(f'Данные по {company.comp_name} успешно добалены в БД!\n')

# Выводим результаты:
print('\n---- Результаты ----')
mean_y = mean(list(map(lambda x: x.profit_y, comp_all)))
print(f'Средняя годовая прибыль всех предприятий: {mean_y}')
above_average = list(filter(lambda x: x.profit_y >= mean_y, comp_all))
name_above = [i.comp_name for i in above_average]
# Один из вариантов получения прочих компаний с помощью set()
name_less = set.difference(set([i.comp_name for i in comp_all]), name_above)
print(f'Предприятия, с прибылью выше среднего значения: {" ".join(name_above)}')
print(f'Предприятия, с прибылью ниже среднего значения: {" ".join(name_less)}')
