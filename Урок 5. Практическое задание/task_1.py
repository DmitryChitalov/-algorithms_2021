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

name_company = namedtuple("company", "name profit")
company_dct = {}

while True:
    try:
        company_number = int(input("Введите количество предприятий для расчета прибыли: "))
        if company_number <= 1:
            raise ValueError
        break
    except ValueError:
        print("Введите целое число, больше 1.")

for i in range(1, company_number + 1):
    name = input("Введите название предприятия:")
    while True:
        try:
            quarterly_profit = input(
                "Через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала):").split()
            if len(quarterly_profit) != 4:
                raise ValueError
            profit = sum(int(i) for i in quarterly_profit)
            break
        except ValueError:
            print("Введите 4 целых числа через пробел.")
    company = name_company(name=name, profit=profit)
    company_dct[company.name] = profit / 4

average_profit = sum(company_dct.values()) / company_number
more_average = [k for k in company_dct if company_dct[k] >= average_profit]
les_average = [k for k in company_dct if company_dct[k] < average_profit]
print(f"Средняя годовая прибыль всех предприятий: {average_profit:.2f}\n"
      f"Предприятия, с прибылью выше среднего значения: {', '.join(more_average)}\n"
      f"Предприятия, с прибылью ниже среднего значения: {', '.join(les_average)}")
