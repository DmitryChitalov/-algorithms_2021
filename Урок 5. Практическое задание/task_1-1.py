"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""

# Решение с использованием defaultdict
from collections import defaultdict

firm_dict = defaultdict(list)

# Запрашиваем количество фирм
while True:
    try:
        count = int(input('Введите количество предприятий: '))
        break
    except ValueError:
        pass

# вводим данные о фирмах
average_profit = 0
i = 1
while i <= count:
    name = input(f'Введите название фирмы {i}: ')
    if name in firm_dict:
        print('Такая фирма уже существует. Повторите ввод.')
        continue

    income = input('Введите прибыль предприятия за 4 квартала, через пробел: ').split()
    if len(income) != 4:
        print('Неверный ввод. Нужно ввести прибыль за 4 квартала.')
        continue

    try:
        firm_dict[name] = list(map(float, income))
    except ValueError:
        print('Неверные данные о доходе. Повторите попытку.')
        continue

    average_profit += sum(firm_dict[name])
    i += 1

# Средняя годова прибыль
average_profit = round(average_profit / count, 2)

# разделяем фирмы на два списка, относительно годовой прибыли и выводим на экран
more = [name for name in firm_dict if sum(firm_dict[name]) > average_profit]
less = [name for name in firm_dict if sum(firm_dict[name]) < average_profit]

print(f'Средняя годовая прибыль предприятий {average_profit}\n'
      f'Фирмы с прибылью выше среднего: {", ".join(more)}\n'
      f'Фирмы с прибылью ниже среднего: {", ".join(less)}')
