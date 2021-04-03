"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections

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

import sys
from collections import namedtuple

is_input_from_file = False      # Ввод данных с консоли
is_input_from_file = True       # флаг перенаправления консольного чтения ввода информации в файл (закомментировать)

# создаем шаблон кортежа
company_n_tup = namedtuple('Company', 'name profit')
company_list = []               # Список для коллекций фирм

if is_input_from_file:
    sys.stdin = open('task_1.txt', "r")     # Redirect sys.stdin to the file
    stdout_fileno = sys.stdout              # Remember file handler for sys.stdout
    sys.stdout = open('Output.txt', 'w')    # Redirect sys.stdout to the file

print('Введите количество предприятий для расчета прибыли:')
amount_company = int(sys.stdin.readline())

for i in range(amount_company):
    print('Введите название предприятия:')
    company_name = sys.stdin.readline().rstrip()
    print('через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала):')
    profit = [float(el) for el in sys.stdin.readline().rstrip().split(' ')]
    company_list.append(company_n_tup(company_name, profit))

if is_input_from_file:
    sys.stdout.close()
    sys.stdout = stdout_fileno              # Restore sys.stdout to our old saved file handler

profit_average = round(sum(sum(el.profit) for el in company_list) / len(company_list),2)
company_upper = [el.name for el in company_list if sum(el.profit) > profit_average]
company_lower = [el.name for el in company_list if sum(el.profit) < profit_average]

print('Средняя годовая прибыль всех предприятий: ', profit_average)
print('Предприятия, с прибылью выше среднего значения: ', ', '.join(company_upper))
print('Предприятия, с прибылью ниже среднего значения: ', ', '.join(company_lower))
print('Общий реестр предприятий:\n', '\n'.join([el.name + ' ' + str(el.profit) for el in company_list]))
